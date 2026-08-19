#!/usr/bin/env python3
# targets.py - 122 Target OTP WhatsApp/SMS
# SCRIPETEREN OTP - scripeterenotp
# Updated: Agustus 2026

import uuid
import random
from utils import fmt_08, fmt_nocode, fmt_plus, fmt_phone_only

TARGETS = [
    # ===== BAGIAN 1: INDONESIA E-COMMERCE (10) =====
    {'name': 'Tokopedia', 'post_type': 'tokopedia', 'number_fmt': fmt_08},
    {'name': 'Shopee', 'post_type': 'shopee', 'number_fmt': fmt_plus},
    {'name': 'Bukalapak', 'post_type': 'bukalapak', 'number_fmt': fmt_08},
    {'name': 'Lazada', 'post_type': 'lazada', 'number_fmt': fmt_plus},
    {'name': 'Blibli', 'post_type': 'blibli', 'number_fmt': fmt_08},
    {'name': 'JD.ID', 'post_type': 'jdid', 'number_fmt': fmt_08},
    {'name': 'Zalora', 'post_type': 'zalora', 'number_fmt': fmt_plus},
    {'name': 'Sociolla', 'post_type': 'sociolla', 'number_fmt': fmt_08},
    {'name': 'Traveloka', 'post_type': 'traveloka', 'number_fmt': fmt_plus},
    {'name': 'Tiket.com', 'post_type': 'tiketcom', 'number_fmt': fmt_08},

    # ===== BAGIAN 2: INDONESIA FINTECH (10) =====
    {'name': 'OVO', 'post_type': 'ovo', 'number_fmt': fmt_plus},
    {'name': 'DANA', 'post_type': 'dana', 'number_fmt': fmt_plus},
    {'name': 'LinkAja', 'post_type': 'linkaja', 'number_fmt': fmt_08},
    {'name': 'GoPay', 'post_type': 'gopay', 'number_fmt': fmt_plus},
    {'name': 'GrabPay', 'post_type': 'grabpay', 'number_fmt': fmt_plus},
    {'name': 'ShopeePay', 'post_type': 'shopeepay', 'number_fmt': fmt_plus},
    {'name': 'Jenius', 'post_type': 'jenius', 'number_fmt': fmt_08},
    {'name': 'MyBCA', 'post_type': 'mybca', 'number_fmt': fmt_08},
    {'name': 'Flip', 'post_type': 'flip', 'number_fmt': fmt_08},
    {'name': 'Kredivo', 'post_type': 'kredivo', 'number_fmt': fmt_08},

    # ===== BAGIAN 3: INDONESIA BANK (10) =====
    {'name': 'BCA', 'post_type': 'bca', 'number_fmt': fmt_08},
    {'name': 'Mandiri', 'post_type': 'mandiri', 'number_fmt': fmt_08},
    {'name': 'BNI', 'post_type': 'bni', 'number_fmt': fmt_08},
    {'name': 'BRI', 'post_type': 'bri', 'number_fmt': fmt_08},
    {'name': 'BTN', 'post_type': 'btn', 'number_fmt': fmt_08},
    {'name': 'CIMB Niaga', 'post_type': 'cimb', 'number_fmt': fmt_08},
    {'name': 'Danamon', 'post_type': 'danamon', 'number_fmt': fmt_08},
    {'name': 'Permata', 'post_type': 'permata', 'number_fmt': fmt_08},
    {'name': 'Maybank', 'post_type': 'maybank', 'number_fmt': fmt_08},
    {'name': 'OCBC NISP', 'post_type': 'ocbc', 'number_fmt': fmt_08},

    # ===== BAGIAN 4: INDONESIA RIDE HAILING (8) =====
    {'name': 'Gojek', 'post_type': 'gojek', 'number_fmt': fmt_plus},
    {'name': 'Grab', 'post_type': 'grab', 'number_fmt': fmt_plus},
    {'name': 'Maxim', 'post_type': 'maxim', 'number_fmt': fmt_08},
    {'name': 'inDrive', 'post_type': 'indrive', 'number_fmt': fmt_plus},
    {'name': 'GoFood', 'post_type': 'gofood', 'number_fmt': fmt_plus},
    {'name': 'GrabFood', 'post_type': 'grabfood', 'number_fmt': fmt_plus},
    {'name': 'ShopeeFood', 'post_type': 'shopeefood', 'number_fmt': fmt_plus},
    {'name': 'Bluebird', 'post_type': 'bluebird', 'number_fmt': fmt_08},

    # ===== BAGIAN 5: INDONESIA FOOD (8) =====
    {'name': 'KFC', 'post_type': 'kfc', 'number_fmt': fmt_08},
    {'name': 'McDonald\'s', 'post_type': 'mcd', 'number_fmt': fmt_plus},
    {'name': 'Burger King', 'post_type': 'burgerking', 'number_fmt': fmt_plus},
    {'name': 'Pizza Hut', 'post_type': 'pizzahut', 'number_fmt': fmt_08},
    {'name': 'Domino\'s', 'post_type': 'dominos', 'number_fmt': fmt_08},
    {'name': 'Starbucks', 'post_type': 'starbucks', 'number_fmt': fmt_plus},
    {'name': 'Kopi Kenangan', 'post_type': 'kopikenangan', 'number_fmt': fmt_08},
    {'name': 'Fore Coffee', 'post_type': 'forecoffee', 'number_fmt': fmt_08},

    # ===== BAGIAN 6: INDONESIA TELCO (6) =====
    {'name': 'MyTelkomsel', 'post_type': 'mytelkomsel', 'number_fmt': fmt_08},
    {'name': 'Indosat', 'post_type': 'indosat', 'number_fmt': fmt_08},
    {'name': 'XL Axiata', 'post_type': 'xl', 'number_fmt': fmt_08},
    {'name': 'Tri', 'post_type': 'tri', 'number_fmt': fmt_08},
    {'name': 'Smartfren', 'post_type': 'smartfren', 'number_fmt': fmt_08},
    {'name': 'By.U', 'post_type': 'byu', 'number_fmt': fmt_08},

    # ===== BAGIAN 7: INDONESIA E-GOV (6) =====
    {'name': 'PLN Mobile', 'post_type': 'pln', 'number_fmt': fmt_08},
    {'name': 'BPJS Kesehatan', 'post_type': 'bpjs', 'number_fmt': fmt_08},
    {'name': 'PeduliLindungi', 'post_type': 'pedulilindungi', 'number_fmt': fmt_08},
    {'name': 'MyPertamina', 'post_type': 'mypertamina', 'number_fmt': fmt_08},
    {'name': 'DJP Online', 'post_type': 'djp', 'number_fmt': fmt_08},
    {'name': 'eHAC', 'post_type': 'ehac', 'number_fmt': fmt_08},

    # ===== BAGIAN 8: INDONESIA COURIER (6) =====
    {'name': 'J&T Express', 'post_type': 'jnt', 'number_fmt': fmt_08},
    {'name': 'SiCepat', 'post_type': 'sicepat', 'number_fmt': fmt_08},
    {'name': 'Anteraja', 'post_type': 'anteraja', 'number_fmt': fmt_08},
    {'name': 'POS Indonesia', 'post_type': 'posindonesia', 'number_fmt': fmt_08},
    {'name': 'Ninja Xpress', 'post_type': 'ninjaxpress', 'number_fmt': fmt_08},
    {'name': 'Lion Parcel', 'post_type': 'lionparcel', 'number_fmt': fmt_08},

    # ===== BAGIAN 9: INDONESIA AIRLINES (6) =====
    {'name': 'Lion Air', 'post_type': 'lionair', 'number_fmt': fmt_plus},
    {'name': 'Garuda Indonesia', 'post_type': 'garuda', 'number_fmt': fmt_plus},
    {'name': 'Citilink', 'post_type': 'citilink', 'number_fmt': fmt_plus},
    {'name': 'Batik Air', 'post_type': 'batikair', 'number_fmt': fmt_plus},
    {'name': 'Sriwijaya Air', 'post_type': 'sriwijayaair', 'number_fmt': fmt_plus},
    {'name': 'AirAsia Indonesia', 'post_type': 'airasia', 'number_fmt': fmt_plus},

    # ===== BAGIAN 10: INDONESIA RETAIL (6) =====
    {'name': 'Super Indo', 'post_type': 'superindo', 'number_fmt': fmt_08},
    {'name': 'Hypermart', 'post_type': 'hypermart', 'number_fmt': fmt_08},
    {'name': 'Transmart', 'post_type': 'transmart', 'number_fmt': fmt_08},
    {'name': 'Alfamart', 'post_type': 'alfamart', 'number_fmt': fmt_08},
    {'name': 'Indomaret', 'post_type': 'indomaret', 'number_fmt': fmt_08},
    {'name': 'Guardian', 'post_type': 'guardian', 'number_fmt': fmt_08},

    # ===== BAGIAN 11: INTERNASIONAL E-COMMERCE (8) =====
    {'name': 'Amazon', 'post_type': 'amazon', 'number_fmt': fmt_plus},
    {'name': 'eBay', 'post_type': 'ebay', 'number_fmt': fmt_plus},
    {'name': 'AliExpress', 'post_type': 'aliexpress', 'number_fmt': fmt_plus},
    {'name': 'Temu', 'post_type': 'temu', 'number_fmt': fmt_plus},
    {'name': 'Shein', 'post_type': 'shein', 'number_fmt': fmt_plus},
    {'name': 'Wish', 'post_type': 'wish', 'number_fmt': fmt_plus},
    {'name': 'Etsy', 'post_type': 'etsy', 'number_fmt': fmt_plus},
    {'name': 'Rakuten', 'post_type': 'rakuten', 'number_fmt': fmt_plus},

    # ===== BAGIAN 12: INTERNASIONAL SOCIAL MEDIA (8) =====
    {'name': 'WhatsApp Business', 'post_type': 'whatsapp_business', 'number_fmt': fmt_plus},
    {'name': 'Telegram', 'post_type': 'telegram', 'number_fmt': fmt_plus},
    {'name': 'Discord', 'post_type': 'discord', 'number_fmt': fmt_plus},
    {'name': 'Twitter/X', 'post_type': 'twitter', 'number_fmt': fmt_plus},
    {'name': 'Instagram', 'post_type': 'instagram', 'number_fmt': fmt_plus},
    {'name': 'Facebook', 'post_type': 'facebook', 'number_fmt': fmt_plus},
    {'name': 'TikTok', 'post_type': 'tiktok', 'number_fmt': fmt_plus},
    {'name': 'Snapchat', 'post_type': 'snapchat', 'number_fmt': fmt_plus},

    # ===== BAGIAN 13: INTERNASIONAL STREAMING (8) =====
    {'name': 'Netflix', 'post_type': 'netflix', 'number_fmt': fmt_plus},
    {'name': 'Spotify', 'post_type': 'spotify', 'number_fmt': fmt_plus},
    {'name': 'YouTube', 'post_type': 'youtube', 'number_fmt': fmt_plus},
    {'name': 'Disney+', 'post_type': 'disney', 'number_fmt': fmt_plus},
    {'name': 'HBO Max', 'post_type': 'hbomax', 'number_fmt': fmt_plus},
    {'name': 'Prime Video', 'post_type': 'primevideo', 'number_fmt': fmt_plus},
    {'name': 'Apple Music', 'post_type': 'apple', 'number_fmt': fmt_plus},
    {'name': 'TikTok Music', 'post_type': 'tiktokmusic', 'number_fmt': fmt_plus},

    # ===== BAGIAN 14: INTERNASIONAL GAMING (8) =====
    {'name': 'Steam', 'post_type': 'steam', 'number_fmt': fmt_plus},
    {'name': 'Epic Games', 'post_type': 'epic', 'number_fmt': fmt_plus},
    {'name': 'PlayStation', 'post_type': 'playstation', 'number_fmt': fmt_plus},
    {'name': 'Xbox', 'post_type': 'xbox', 'number_fmt': fmt_plus},
    {'name': 'Nintendo', 'post_type': 'nintendo', 'number_fmt': fmt_plus},
    {'name': 'Roblox', 'post_type': 'roblox', 'number_fmt': fmt_plus},
    {'name': 'Minecraft', 'post_type': 'minecraft', 'number_fmt': fmt_plus},
    {'name': 'Valorant', 'post_type': 'valorant', 'number_fmt': fmt_plus},

    # ===== BAGIAN 15: INTERNASIONAL PAYMENT (8) =====
    {'name': 'PayPal', 'post_type': 'paypal', 'number_fmt': fmt_plus},
    {'name': 'Stripe', 'post_type': 'stripe', 'number_fmt': fmt_plus},
    {'name': 'Square', 'post_type': 'square', 'number_fmt': fmt_plus},
    {'name': 'Klarna', 'post_type': 'klarna', 'number_fmt': fmt_plus},
    {'name': 'Revolut', 'post_type': 'revolut', 'number_fmt': fmt_plus},
    {'name': 'Wise', 'post_type': 'wise', 'number_fmt': fmt_plus},
    {'name': 'N26', 'post_type': 'n26', 'number_fmt': fmt_plus},
    {'name': 'Monzo', 'post_type': 'monzo', 'number_fmt': fmt_plus},

    # ===== BAGIAN 16: INTERNASIONAL DELIVERY (6) =====
    {'name': 'Uber', 'post_type': 'uber', 'number_fmt': fmt_plus},
    {'name': 'Lyft', 'post_type': 'lyft', 'number_fmt': fmt_plus},
    {'name': 'DoorDash', 'post_type': 'doordash', 'number_fmt': fmt_plus},
    {'name': 'UberEats', 'post_type': 'ubereats', 'number_fmt': fmt_plus},
    {'name': 'Bolt', 'post_type': 'bolt', 'number_fmt': fmt_plus},
    {'name': 'Didi', 'post_type': 'didi', 'number_fmt': fmt_plus},
]