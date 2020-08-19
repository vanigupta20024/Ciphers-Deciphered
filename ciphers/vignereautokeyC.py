def encrypt(txt, key):
    if key == "":
        key = "a"
    enc_text = ""	

    if len(key) > len(txt):
        key = key[: len(txt)]
    elif len(key) < len(txt):
        key += txt
        key = key[:len(txt)]
        # key += txt[:len(key)]
    for i in range(len(txt)):
        if txt[i].isupper(): 
            v = 'A'
        elif txt[i].islower(): 
            v = 'a'
        else:
            enc_text += txt[i]
            continue

        enc_text += (chr(((ord(txt[i]) - 2 * ord(v) + ord(key[i])) % 26) + ord(v)))
    return enc_text

def decrypt(txt, key):
    if key == "":
        key = "a"
    dec_text = ""
    for i in range(len(txt)):
        if txt[i].isupper(): 
            v = 'A'
        elif txt[i].islower(): 
            v = 'a'
        else:
            dec_text += txt[i]
            continue

        s = ord(txt[i]) - ord(key[i])
        if s < 0: 
            s += 26
        v_k = chr(s + ord(v))
        key += v_k
        dec_text += v_k
    return dec_text
    