import random
key_table = {'A':'D9', 'B':'X', 'C':'S', 'D':'F', 'E':'Z721', 'F':'E', 'G':'H', 'H':'C', 'I':'V3',
	'J':'I', 'K':'T', 'L':'P', 'M':'G', 'N':'A5', 'O':'Q0', 'P':'L', 'Q':'K', 'R':'J', 'S':'R4', 'T':'6U', 
	'U':'O', 'V':'W', 'W':'M', 'X':'Y', 'Y':'B', 'Z':'N', 'a':'d(', 'b':'x', 'c': 's', 'd':'f', 'e':'z&@!', 
	'f':'e', 'g':'h', 'h':'c', 'i':'v#', 'j':'i', 'k':'t', 'l':'p', 'm':'g', 'n':'a%', 'o':'q)', 'p':'l', 
	'q':'k', 'r':'j','s':'r$', 't':'^u', 'u':'o', 'v':'w', 'w':'m', 'x':'y', 'y':'b', 'z':'n'}

def encryption(txt):
    enc_text = ""
    for item in txt:
        if item in key_table:
            enc_text += random.choice(key_table[item])
        else:
            enc_text += item
    return enc_text
    
def decryption(txt):
    dec_text = ""		
    flag = 1
    words = txt.split(" ")

    lst = []
    for item in words:
        lst += item + " "

    for letter in lst:
        if letter == " ":
            dec_text += " "
        else:
            for item in key_table:
                flag = 1
                if letter in key_table[item]:
                    dec_text += item
                    flag = 0
                    break
            if flag == 1:
                dec_text += letter
    return dec_text