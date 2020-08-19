def encrypt(string, key):

    a = [[None for i in range(len(string))] for j in range(key)]

    curr = 0
    findex = 0
    sindex = 0
    enc_text = ""

    while curr < len(string):
        if findex < key:
            while findex < key and curr < len(string):
                a[findex][sindex] = string[curr]
                curr += 1
                findex += 1
                sindex += 1
        if findex == key:
            findex -= 1
            while findex > 0 and curr < len(string):
                findex -= 1
                a[findex][sindex] = string[curr]
                curr += 1
                sindex += 1
            findex += 1

    for i in a:
        l = [x for x in i if x is not None]
        enc_text += "".join(l)
    return enc_text

def decrypt(string, key):

    a = [[None for i in range(len(string))] for j in range(key)]

    curr = 0
    findex = 0
    sindex = 0
    dec_text = ""

    while curr < len(string):
        if findex < key:
            while findex < key and curr < len(string):
                a[findex][sindex] = "0"
                curr += 1
                findex += 1
                sindex += 1

        if findex == key:
            findex -= 1
            while findex > 0 and curr < len(string):
                findex -= 1
                a[findex][sindex] = "0"
                curr += 1
                sindex += 1
            findex += 1

    curr = 0

    for i in a:
        for j in range(len(i)):
            if i[j] == "0":
                i[j] = string[curr]
                curr += 1

    curr = 0
    findex = 0
    sindex = 0

    while curr < len(string):
        if findex < key:
            while findex < key and curr < len(string):
                dec_text += a[findex][sindex]
                curr += 1
                findex += 1
                sindex += 1

        if findex == key:
            findex -= 1
            while findex > 0 and curr < len(string):
                findex -= 1
                dec_text += a[findex][sindex]
                curr += 1
                sindex += 1
            findex += 1
    return dec_text