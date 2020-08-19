def encrypt(txt, key):
    spl = ['!','@','#','$','%','^','&','*','(',')','<','~',':',';','<','>','?','/']
    for i in key:
        if i in spl:
            key = key.replace(i,"")
    if key == "": key = "a"
    enc_text = ""	
    if len(key) > len(txt):
        key = key[: len(txt)]
    elif len(key) < len(txt):
        key = (key * ((len(txt) // len(key)) + 1))[:len(txt)]

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
    spl = ['!','@','#','$','%','^','&','*','(',')','<','~',':',';','<','>','?','/']
    for i in key:
        if i in spl:
            key = key.replace(i,"")
    dec_text = ""
    if key == "":
        key = "a"
    if len(key) > len(txt):
        key = key[: len(txt)]
    elif len(key) < len(txt):
        key = (key * ((len(txt) // len(key)) + 1))[:len(txt)]
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
        dec_text += chr(s + ord(v))
    return dec_text