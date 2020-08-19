def convert(txt, key):
    spl = ['!','@','#','$','%','^','&','*','(',')','<','~',':',';','<','>','?','/']
    for i in key:
        if i in spl:
            key = key.replace(i,"")
    if key == "":
        key = "abc"
    converted_text = ""

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
            converted_text += txt[i]
            continue

        s = ord(key[i]) - ord(txt[i])
        if s < 0: 
            s += 26

        converted_text += chr(s + ord(v))
    return converted_text