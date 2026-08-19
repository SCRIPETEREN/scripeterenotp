# Di dalam process_target, setelah handler_map = {...}
# Tambahkan semua post_type baru ke handler_map:
handler_map.update({
    # ===== INDONESIA E-COMMERCE =====
    'tokopedia': (send_tokopedia_otp, [api['number_fmt'](target62)]),
    'shopee': (send_shopee_otp, [api['number_fmt'](target62)]),
    'bukalapak': (send_bukalapak_otp, [api['number_fmt'](target62)]),
    'lazada': (send_lazada_otp, [api['number_fmt'](target62)]),
    'blibli': (send_blibli_otp, [api['number_fmt'](target62)]),
    'jdid': (send_jdid_otp, [api['number_fmt'](target62)]),
    'zalora': (send_zalora_otp, [api['number_fmt'](target62)]),
    'sociolla': (send_sociolla_otp, [api['number_fmt'](target62)]),
    'traveloka': (send_traveloka_otp, [api['number_fmt'](target62)]),
    'tiketcom': (send_tiketcom_otp, [api['number_fmt'](target62)]),
    
    # ===== FINTECH =====
    'ovo': (send_ovo_otp, [api['number_fmt'](target62)]),
    'dana': (send_dana_otp, [api['number_fmt'](target62)]),
    'linkaja': (send_linkaja_otp, [api['number_fmt'](target62)]),
    'gopay': (send_gopay_otp, [api['number_fmt'](target62)]),
    'grabpay': (send_grabpay_otp, [api['number_fmt'](target62)]),
    'shopeepay': (send_shopeepay_otp, [api['number_fmt'](target62)]),
    'jenius': (send_jenius_otp, [api['number_fmt'](target62)]),
    'mybca': (send_mybca_otp, [api['number_fmt'](target62)]),
    'flip': (send_flip_otp, [api['number_fmt'](target62)]),
    'kredivo': (send_kredivo_otp, [api['number_fmt'](target62)]),
    
    # ===== BANK =====
    'bca': (send_bca_otp, [api['number_fmt'](target62)]),
    'mandiri': (send_mandiri_otp, [api['number_fmt'](target62)]),
    'bni': (send_bni_otp, [api['number_fmt'](target62)]),
    'bri': (send_bri_otp, [api['number_fmt'](target62)]),
    'btn': (send_btn_otp, [api['number_fmt'](target62)]),
    'cimb': (send_cimb_otp, [api['number_fmt'](target62)]),
    'danamon': (send_danamon_otp, [api['number_fmt'](target62)]),
    'permata': (send_permata_otp, [api['number_fmt'](target62)]),
    'maybank': (send_maybank_otp, [api['number_fmt'](target62)]),
    'ocbc': (send_ocbc_otp, [api['number_fmt'](target62)]),
    
    # ===== RIDE HAILING =====
    'gojek': (send_gojek_otp, [api['number_fmt'](target62)]),
    'grab': (send_grab_otp, [api['number_fmt'](target62)]),
    'maxim': (send_maxim_otp, [api['number_fmt'](target62)]),
    'indrive': (send_indrive_otp, [api['number_fmt'](target62)]),
    'gofood': (send_gofood_otp, [api['number_fmt'](target62)]),
    'grabfood': (send_grabfood_otp, [api['number_fmt'](target62)]),
    'shopeefood': (send_shopeefood_otp, [api['number_fmt'](target62)]),
    'bluebird': (send_bluebird_otp, [api['number_fmt'](target62)]),
    
    # ===== FOOD =====
    'kfc': (send_kfc_otp, [api['number_fmt'](target62)]),
    'mcd': (send_mcd_otp, [api['number_fmt'](target62)]),
    'burgerking': (send_burgerking_otp, [api['number_fmt'](target62)]),
    'pizzahut': (send_pizzahut_otp, [api['number_fmt'](target62)]),
    'dominos': (send_dominos_otp, [api['number_fmt'](target62)]),
    'starbucks': (send_starbucks_otp, [api['number_fmt'](target62)]),
    'kopikenangan': (send_kopikenangan_otp, [api['number_fmt'](target62)]),
    'forecoffee': (send_forecoffee_otp, [api['number_fmt'](target62)]),
    
    # ===== TELCO =====
    'mytelkomsel': (send_mytelkomsel_otp, [api['number_fmt'](target62)]),
    'indosat': (send_indosat_otp, [api['number_fmt'](target62)]),
    'xl': (send_xl_otp, [api['number_fmt'](target62)]),
    'tri': (send_tri_otp, [api['number_fmt'](target62)]),
    'smartfren': (send_smartfren_otp, [api['number_fmt'](target62)]),
    'byu': (send_byu_otp, [api['number_fmt'](target62)]),
    
    # ===== E-GOV =====
    'pln': (send_pln_otp, [api['number_fmt'](target62)]),
    'bpjs': (send_bpjs_otp, [api['number_fmt'](target62)]),
    'pedulilindungi': (send_pedulilindungi_otp, [api['number_fmt'](target62)]),
    'mypertamina': (send_mypertamina_otp, [api['number_fmt'](target62)]),
    'djp': (send_djp_otp, [api['number_fmt'](target62)]),
    'ehac': (send_ehac_otp, [api['number_fmt'](target62)]),
    
    # ===== COURIER =====
    'jnt': (send_jnt_otp, [api['number_fmt'](target62)]),
    'sicepat': (send_sicepat_otp, [api['number_fmt'](target62)]),
    'anteraja': (send_anteraja_otp, [api['number_fmt'](target62)]),
    'posindonesia': (send_posindonesia_otp, [api['number_fmt'](target62)]),
    'ninjaxpress': (send_ninjaxpress_otp, [api['number_fmt'](target62)]),
    'lionparcel': (send_lionparcel_otp, [api['number_fmt'](target62)]),
    
    # ===== AIRLINES =====
    'lionair': (send_lionair_otp, [api['number_fmt'](target62)]),
    'garuda': (send_garuda_otp, [api['number_fmt'](target62)]),
    'citilink': (send_citilink_otp, [api['number_fmt'](target62)]),
    'batikair': (send_batikair_otp, [api['number_fmt'](target62)]),
    'sriwijayaair': (send_sriwijayaair_otp, [api['number_fmt'](target62)]),
    'airasia': (send_airasia_otp, [api['number_fmt'](target62)]),
    
    # ===== RETAIL =====
    'superindo': (send_superindo_otp, [api['number_fmt'](target62)]),
    'hypermart': (send_hypermart_otp, [api['number_fmt'](target62)]),
    'transmart': (send_transmart_otp, [api['number_fmt'](target62)]),
    'alfamart': (send_alfamart_otp, [api['number_fmt'](target62)]),
    'indomaret': (send_indomaret_otp, [api['number_fmt'](target62)]),
    'guardian': (send_guardian_otp, [api['number_fmt'](target62)]),
    
    # ===== INTERNASIONAL E-COMMERCE =====
    'amazon': (send_amazon_otp, [api['number_fmt'](target62)]),
    'ebay': (send_ebay_otp, [api['number_fmt'](target62)]),
    'aliexpress': (send_aliexpress_otp, [api['number_fmt'](target62)]),
    'temu': (send_temu_otp, [api['number_fmt'](target62)]),
    'shein': (send_shein_otp, [api['number_fmt'](target62)]),
    'wish': (send_wish_otp, [api['number_fmt'](target62)]),
    'etsy': (send_etsy_otp, [api['number_fmt'](target62)]),
    'rakuten': (send_rakuten_otp, [api['number_fmt'](target62)]),
    
    # ===== INTERNASIONAL SOCIAL MEDIA =====
    'whatsapp_business': (send_whatsapp_business_otp, [api['number_fmt'](target62)]),
    'telegram': (send_telegram_otp, [api['number_fmt'](target62)]),
    'discord': (send_discord_otp, [api['number_fmt'](target62)]),
    'twitter': (send_twitter_otp, [api['number_fmt'](target62)]),
    'instagram': (send_instagram_otp, [api['number_fmt'](target62)]),
    'facebook': (send_facebook_otp, [api['number_fmt'](target62)]),
    'tiktok': (send_tiktok_otp, [api['number_fmt'](target62)]),
    'snapchat': (send_snapchat_otp, [api['number_fmt'](target62)]),
    
    # ===== INTERNASIONAL STREAMING =====
    'netflix': (send_netflix_otp, [api['number_fmt'](target62)]),
    'spotify': (send_spotify_otp, [api['number_fmt'](target62)]),
    'youtube': (send_youtube_otp, [api['number_fmt'](target62)]),
    'disney': (send_disney_otp, [api['number_fmt'](target62)]),
    'hbomax': (send_hbomax_otp, [api['number_fmt'](target62)]),
    'primevideo': (send_primevideo_otp, [api['number_fmt'](target62)]),
    'apple': (send_apple_otp, [api['number_fmt'](target62)]),
    'tiktokmusic': (send_tiktokmusic_otp, [api['number_fmt'](target62)]),
    
    # ===== INTERNASIONAL GAMING =====
    'steam': (send_steam_otp, [api['number_fmt'](target62)]),
    'epic': (send_epic_otp, [api['number_fmt'](target62)]),
    'playstation': (send_playstation_otp, [api['number_fmt'](target62)]),
    'xbox': (send_xbox_otp, [api['number_fmt'](target62)]),
    'nintendo': (send_nintendo_otp, [api['number_fmt'](target62)]),
    'roblox': (send_roblox_otp, [api['number_fmt'](target62)]),
    'minecraft': (send_minecraft_otp, [api['number_fmt'](target62)]),
    'valorant': (send_valorant_otp, [api['number_fmt'](target62)]),
    
    # ===== INTERNASIONAL PAYMENT =====
    'paypal': (send_paypal_otp, [api['number_fmt'](target62)]),
    'stripe': (send_stripe_otp, [api['number_fmt'](target62)]),
    'square': (send_square_otp, [api['number_fmt'](target62)]),
    'klarna': (send_klarna_otp, [api['number_fmt'](target62)]),
    'revolut': (send_revolut_otp, [api['number_fmt'](target62)]),
    'wise': (send_wise_otp, [api['number_fmt'](target62)]),
    'n26': (send_n26_otp, [api['number_fmt'](target62)]),
    'monzo': (send_monzo_otp, [api['number_fmt'](target62)]),
    
    # ===== INTERNASIONAL DELIVERY =====
    'uber': (send_uber_otp, [api['number_fmt'](target62)]),
    'lyft': (send_lyft_otp, [api['number_fmt'](target62)]),
    'doordash': (send_doordash_otp, [api['number_fmt'](target62)]),
    'ubereats': (send_ubereats_otp, [api['number_fmt'](target62)]),
    'bolt': (send_bolt_otp, [api['number_fmt'](target62)]),
    'didi': (send_didi_otp, [api['number_fmt'](target62)]),
})