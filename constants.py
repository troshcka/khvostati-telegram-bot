TOKEN = '5800166946:AAFRDBo1LjC4h-K0JRld3fMiBCDMlq-EfTk'

START_SCREEN_TEMPLATE = "Привіт, {first_name}!"

SERVICE_ACCOUNT = {
    "type": "service_account",
    "project_id": "khovstatyi-bot",
    "private_key_id": "a5c84f763ce3529f5f9d85ab3e925c3826c0b811",
    "private_key": "-----BEGIN PRIVATE KEY-----\
                \nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC8kIQ3fGpW7dKK\
                \ng5/5b5hfMv/gyW5KbL8t+ns3E5tvvElxCVnftEHi/ltG3BVGU0uuixQCVAre8b/i\
                \nuvSwuTsH4rkEIcPJIw52iYUuAr4lWFnoPt4OXxWp3873zEsSNwCct/16yk73WyuP\
                \n+tQo4n7YPS/goR4B26zPkyw7XSstSoMKv1ujS8raMu1AKnllLOn8wZl4yrY8j262\
                \n2S4gkT7Ub6sat1h7U5BKp9ty+vw2SyGsg0GEezwtON+2+w8akGnA+hb+hY3ePoF0\
                \nRK1lng3gvkoHceAX/6BYhC5pNKqQZR34DNT47gsvRHatC4KNqiQn460XMs+VLCdB\
                \nuwNZwo4DAgMBAAECggEAAKVcFpaSBK823+uYgjG8K2NQ1hPKkW2y7/TiNCuYhjb2\
                \nZ3E5QhdrfFwTsvfxCLcjVLs8O8/O47mfRycNzIct6RaBPL7i3U8F7ykEcEZpIVae\
                \npDmG6DSyLc1K97VW8n6GvYKx1xhXUeiZixo4XNV9yr7W6aWTpTz76BAggCmPCs4r\
                \niD3k3h7DxjGUn++437U8hr9RvG5/YpVKIR74OFOXHFTvpnYPNxvOgJaXm3BqrMfu\
                \nU1R6MEepQzOX3jV+f6Q09xVUNT5PjWDzsMtsjqc9lQyrVdCzGCO/QAyVlx4NJHtW\
                \nredsGhNy9HkLx1CY2+96WFdjHDUgDWJyxLh4TSeDYQKBgQDiB8a60ld+MJUK4Jnm\
                \nFjUayzMgR+JMEvWLzuojVCVvoilRbHKTstAxYIN8knqY4am1+lwJns93v0Xim6G4\
                \nWooTyCfFyxt0bi3XuXqipHs0RASMmfB2bhHfV/JRQYfxV6N+28qmShoqII3Bk4BO\
                \n/mf9R9rJ124NTryBGvcpdMfF4wKBgQDVkQYv6L/3L8TcpwJAty5G8eAGTbgpEpiA\
                \n8PGBDaKdroPymYEBBzSQEWADncQbQ/msZWgx5vuKbh0Z1xZk2XKLPFWw54/2cTNd\
                \nDDDWyDVlijGaqnj2rPXcmiFiV2gCKfQug1dFfbx3qu9vsw61hJx8msfx9xcins9C\
                \nwG9xagmRYQKBgHxyUZ18wAVPVFAX10QSSAzHgg+s5FCEQ8NFGi53XuE2xE77SZ4+\
                \nXlhBTkOhFnTkEh+Kh3AYixvgKOcaTxEEcG9xzUwehrA1FXJnwbiYnOjq5iJPg1CB\
                \nS7/PWTAZx3I+kVsAQnQJ6pv1Lnc88fEMK08NZ82nmgUjq6/dm+WsUW2HAoGBAMTQ\
                \nPY9xQ1edYiKmlmDlb3RZ+0ZT4V+Yj4pkgWuZET+XUGoGJOi5pysNmBo9DjjCUBkb\
                \n6wXyA+XyzEa//Rc7fV/rXl0FSZqnf9pEHc4R+4Nz83rBl3BcvMdsE0/5lRRJbYpf\
                \n59FWqpTtpnKd5PRLHZuHWLQYLe3txLuTdCBkxCSBAoGBAMNDQ4SgHOul+sdETwAv\
                \nN+NLvCfQXeOkukEcvdkqnXP9TtHb47L1m3uKHvxEfkgJ6hzZnd7GaZcS/ybYrqO6\
                \nSaZ10bNrVD00YUtcWJ4zJvyVm0Y4xuMrrs1Khs5ZClAnYkIMubO+SEgeTbxt/10f\
                \nxC+gYwzwTAr0SUhOF4tcNznO\n-----END PRIVATE KEY-----\n",
    "client_email":
    "khvostatyi-bot-service-acc@khovstatyi-bot.iam.gserviceaccount.com",
    "client_id": "117035210088017618259",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/\
                                    \noauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v\
                            \n1/metadata/x509/\
          khvostatyi-bot-service-acc%40khovstatyi-bot.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
}

POLL_SHEET_NAME = 'quest_answers'

QUESTIONNAIRE_CITY = """Заповніть, будь ласка, анкету, \
якщо хочете взяти собаку із притулку.\n\
\n\
Де ви проживаєте? (Київ, область, інше місто)"""
QUESTIONNAIRE_LIVE_PLACE = 'Квартира чи приватний будинок?'
QUESTIONNAIRE_DOG_PLACE = """Якщо приватний будинок, то як збираєтесь \
утримувати собаку (в будинку, вольєрі, \
в будці в дворі і тд?"""
QUESTIONNAIRE_CHILDREN = 'Чи є діти?'
QUESTIONNAIRE_OTHER_ANIMALS = 'Чи є інші тварини, якщо є, то які?'
QUESTIONNAIRE_DOG_EXPERIENCE = 'Чи є досвід із собаками?'
QUESTIONNAIRE_DOG_CHOICE = """Чи хочете взяти конкретну собаку \
(вказати ім'я, чи приїхати обрати)?"""
QUESTIONNAIRE_CONTACT_NUMBER = """Залиште свій номер телефону, \
щоб ми могли сконтактувати для детальнішого \
обговорення?"""
QUESTIONNAIRE_THANKS = 'Дякуємо! Найближчим часом ми Вас законтактуємо'

AVAILABLE_ROW_FOR_DICT = 2

MONOBANK_URL = 'https://send.monobank.ua/jar/5F27ncLLf3'
PRIVAT_BANK_URL = '''https://next.privat24.ua/money-transfer/\
form/%7B%22form%22:%7B%22receiver%22:%7B\
%22source%22:%22manual%22,%22number%22:%\
224149499117309763%22%7D,%22amount%22:%2\
2100%22,%22currency%22:%22UAH%22%7D%7D'''

GOOGLE_FORM_HAPPY_STORY_URL = '''https://docs.google.com/forms/d/e/\
1FAIpQLSdsHPYf6MoJ96wh7iSvWG81FGa\
lEWRoKHF5riNv3Wt1h4GfcA/viewform'''

CATALOG_URL = "https://t.me/khvostatyye"
