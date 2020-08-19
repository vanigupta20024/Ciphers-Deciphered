def encrypt(txt, key):
    if key == "":
        key = "abc"
    converted_text = ""

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
            converted_text += txt[i]
            continue

        s = ord(key[i]) - ord(txt[i])
        if s < 0: 
            s += 26

        converted_text += chr(s + ord(v))
    return converted_text

def decrypt(txt, key):
    if key == "":
        key = "abc"
    converted_text = ""

    for i in range(len(txt)):
        b_k = ""
        if txt[i].isupper():
            v = 'A'
        elif txt[i].islower(): 
            v = 'a'
        else:
            converted_text += txt[i]
            continue

        s = ord(key[i]) - ord(txt[i])
        if s < 0: 
            s += 26
        b_k = chr(s + ord(v))
        key += b_k
        converted_text += b_k
    return converted_text