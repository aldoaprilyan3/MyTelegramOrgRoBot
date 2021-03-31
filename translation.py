class Translation(object):
    START_TEXT = """Hi!
Terima Kasih Telah Menggunakan Saya Silahkan Masukan Nomor Untuk Mendapatkan API HASH dan API ID Atau Bisa Hub Owner

 Creator : @coklintoud
 Support : @xthunderlol

/start at any stage to re-enter your details"""
    AFTER_RECVD_CODE_TEXT = """Aku Melihatnya!
Sekarang Tolong Berikan Kode Dari telegram
Kode ini hanya digunakan untuk tujuan mendapatkan APP ID dari my.telegram.org
Jika Anda tidak mempercayai dev bot ini, Bisa Anda Gunakan Account Tumbal.
        f" **[Support](t.me/xthunderlol)\n [ꜱʜᴀᴅᴏᴡ](t.me/coklintoud)\n")

/start at any stage to re-enter your details"""
    BEFORE_SUCC_LOGIN = "recieved code. Scarpping web page ..."
    ERRED_PAGE = "something wrongings. failed to get app id. \n\n@xthunderlol"
    CANCELLED_MESG = "Bye! Please re /start the bot conversation"
    IN_VALID_CODE_PVDED = "sorry, but the input does not seem to be a valid Telegram Web-Login code"
    IN_VALID_PHNO_PVDED = "sorry, but the input does not seem to be a valid phone number"
