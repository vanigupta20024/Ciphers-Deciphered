def encryption(txt, key):
    enc_text = ""

    for index in range(len(txt)):

        if txt[index].isalpha():
            if txt[index].isupper():
                temp = (ord(txt[index]) - ord('A') + key) % 26 + ord('A')
                enc_text += chr(temp)

            elif txt[index].islower():
                temp = (ord(txt[index]) - ord('a') + key) % 26 + ord('a')
                enc_text += chr(temp)
        else:
            enc_text += txt[index]
    return enc_text


def decryption(txt, key):
    dec_text = ""
    for index in range(len(txt)):

        if txt[index].isalpha():
            if txt[index].isupper():
                temp = (ord(txt[index]) - ord('A') - key)
                if temp < 0:
                    temp += 26
                temp += ord('A')
                dec_text += chr(temp)

            elif txt[index].islower():
                temp = (ord(txt[index]) - ord('a') - key)
                if temp < 0:
                    temp += 26
                temp += ord('a')
                dec_text += chr(temp)

        else:
            dec_text += txt[index]
    return dec_text