from googletrans import Translator

def translate_text():
    translator = Translator()

    result = translator.translate('안녕하세요.')
    print(result)  # <Translated src=ko dest=en text=Hello. pronunciation=Annyeonghaseyo.>

    result = translator.translate('안녕하세요.', dest='ja')
    print(result)  # <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>

    result = translator.translate('veritas lux mea', src='la')
    print(result)  # <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>

translate_text()