def encrypt(txt, key):
    if key == "":
        key = "A"
    enc_text = ""
    if len(key) < len(txt):
        key = (key + txt)[: len(txt)]
    elif len(key) > len(txt):
        key = key[: len(txt)]
    for i in range(len(txt)):
        if txt[i].isalpha():
            if txt[i].isupper():
                v = 'A'
            else:
                v = 'a'
            s = (ord(txt[i]) - ord(v) + ord(key[i]) - ord(v)) % 26
            enc_text += chr(s + ord(v))
        else:
            enc_text += txt[i]
    return enc_text

def decrypt(txt, key):
    if key == "":
        key = "A"
    dec_text = ""	
    for i in range(len(txt)):
        k = ""
        if txt[i].isalpha():
            if txt[i].isupper():
                v = 'A'
            else:
                v = 'a'
            s = ord(txt[i]) - ord(key[i])
            if s < 0:
                s += 26
            k += chr(s + ord(v))
            key += k
            dec_text += k
        else:
            dec_text += txt[i]
    return dec_text