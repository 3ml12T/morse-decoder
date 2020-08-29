def decrypt(message):
    MORSE_DICT = {'A':'.-', 'B':'-...', 
            'C':'-.-.', 'D':'-..', 'E':'.', 
            'F':'..-.', 'G':'--.', 'H':'....', 
            'I':'..', 'J':'.---', 'K':'-.-', 
            'L':'.-..', 'M':'--', 'N':'-.', 
            'O':'---', 'P':'.--.', 'Q':'--.-', 
            'R':'.-.', 'S':'...', 'T':'-', 
            'U':'..-', 'V':'...-', 'W':'.--', 
            'X':'-..-', 'Y':'-.--', 'Z':'--..', 
            '1':'.----', '2':'..---', '3':'...--', 
            '4':'....-', '5':'.....', '6':'-....', 
            '7':'--...', '8':'---..', '9':'----.', 
            '0':'-----'}
    morse = ''
    plaintext = ''

    for letter in message:
        if(letter == '.' or letter == '-' and letter != ' '):
            morse += letter
        else:
            plaintext += list(MORSE_DICT.keys())[list(MORSE_DICT.values()).index(morse)]
            morse = ''
    return plaintext

read_from = "output.txt"
write_to = "morse_decoded.txt"
encoded = open(read_from, "r")
decoded = open(write_to, "w+")
line = 1

for x in encoded:
  message = str.rstrip(x)
  if (line > 1):
    message = message[1:]
  decoded.write(decrypt(message))
  decoded.write("\n")
  line += 1

encoded.close()
decoded.close()

