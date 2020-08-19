Morse_dict = { 
		'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 
		'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 
		'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 
		'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..', 
		'1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', 
		'7':'--...', '8':'---..', '9':'----.', '0':'-----', ',':'--..--', '.':'.-.-.-', 
		'?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-', ' ':'`'}

Reverse_morse = {val : key for key, val in Morse_dict.items()}

def encrypt(txt):
    enc_text = ""

    for i in txt:
        if i.upper() in Morse_dict.keys():
            enc_text += Morse_dict[i.upper()] + " "
        else:
            enc_text += i + " "
    return enc_text

def decrypt(txt):
    dec_text = ""

    for i in txt.split():
        if i in Reverse_morse.keys():
            dec_text += Reverse_morse[i]
        else:
            dec_text += i
    return dec_text