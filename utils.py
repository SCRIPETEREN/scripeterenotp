#!/usr/bin/env python3
# utils.py - Utility Functions

import re
import uuid
import random
import string
import urllib.parse
import requests
import json
from useragents import USER_AGENTS

def normalize(phone):
    """Normalisasi nomor telepon ke format 62"""
    n = phone.strip().replace(' ', '').replace('-', '').replace('+', '')
    if n.startswith('08'):
        return '62' + n[1:]
    if n.startswith('8'):
        return '62' + n
    if n.startswith('62'):
        return n
    return ''

def fmt_08(p):
    """Format ke 08xxx"""
    if p.startswith('62'):
        return '0' + p[2:]
    if p.startswith('0'):
        return p
    return '0' + p

def fmt_nocode(p):
    """Format tanpa kode negara (628xx -> 8xx)"""
    if p.startswith('62'):
        return p[2:]
    if p.startswith('0'):
        return p[1:]
    return p

def fmt_plus(p):
    """Format ke +62xxx"""
    if not p.startswith('+'):
        if p.startswith('62'):
            return '+' + p
        if p.startswith('0'):
            return '+62' + p[1:]
        return '+62' + p
    return p

def fmt_phone_only(p):
    """Format nomor saja tanpa kode dan tanpa +"""
    if p.startswith('+62'):
        return p[3:]
    if p.startswith('62'):
        return p[2:]
    if p.startswith('0'):
        return p[1:]
    return p

def get_public_ip():
    try:
        return requests.get('https://api.ipify.org', timeout=5).text.strip()
    except:
        return '127.0.0.1'

def extract_csrf(html):
    patterns = [
        r'<meta name="csrf-token" content="([^"]+)"',
        r'<meta name="csrf_token" content="([^"]+)"',
        r'<input type="hidden" name="_token" value="([^"]+)"',
        r'<input type="hidden" name="csrf_token" value="([^"]+)"',
        r'<input type="hidden" name="_csrf" value="([^"]+)"',
        r'csrf_token\s*=\s*"([^"]+)"',
    ]
    for p in patterns:
        m = re.search(p, html, re.I)
        if m:
            return m.group(1)
    return None

def generate_multipart(data, boundary):
    body = ""
    for key, val in data.items():
        body += f"--{boundary}\r\n"
        body += f'Content-Disposition: form-data; name="{key}"\r\n\r\n'
        body += f"{val}\r\n"
    body += f"--{boundary}--\r\n"
    return body

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def get_headers_with_random_ua(custom_headers=None):
    headers = {
        'User-Agent': get_random_user_agent(),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Connection': 'keep-alive',
    }
    if custom_headers:
        headers.update(custom_headers)
    return headers

def is_success_response(resp):
    """
    Cek apakah response benar-benar sukses.
    Status 2xx dianggap sukses, kecuali body JSON secara eksplisit menunjukkan error.
    """
    if resp is None:
        return False
    if resp.status_code < 200 or resp.status_code >= 300:
        return False

    try:
        data = resp.json()
        if isinstance(data, dict):
            if 'success' in data and data['success'] in (False, 'false', 0):
                return False
            if 'status' in data and data['status'] in ('error', 'failed', '0', 'FAIL', 'ERROR'):
                return False
            if 'error' in data and data['error'] and data['error'] != 'null':
                if data['error'] not in (None, '', 'null'):
                    return False
            if 'code' in data and data['code'] not in ('0', '200', '201', '00', 'success', 'OK'):
                return False
            msg = data.get('message') or data.get('msg') or ''
            if any(kata in msg.lower() for kata in ('gagal', 'failed', 'error', 'invalid', 'not found', 'tidak terdaftar', 'wrong')):
                return False
        return True
    except:
        return True