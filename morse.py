"""*****************************************************************************
@title: An Utility to Encode And Decode Text Into Morse Code.
@author: vivekascode
@date: 11-4-2020
*****************************************************************************"""
class MorseCode():
    """Class Containing Feature To encode or decode text into morse code."""
    code = { 
        'A':'.-', 'B':'-...', 
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
        '0':'-----', ', ':'--..--', '.':'.-.-.-', 
        '?':'..--..', '/':'-..-.', '-':'-....-', 
        '(':'-.--.', ')':'-.--.-'
    } 
    def __init__(self, text):
        self.text = text
    def encode(self):
        temp_txt = ''
        list_of_words = self.text.split()
        for word in list_of_words:
            for char in word:
                capital_char = char.upper()
                if capital_char in self.code.keys():
                    temp_txt += self.code[capital_char]
                    temp_txt += " "
            temp_txt += "  "
        return temp_txt
            

    def decode(self):
        temp_txt = ''
        list_of_words = self.text.split("   ")
        for word in list_of_words:
            list_of_letter = word.split(' ')
            for char in list_of_letter:
                if char in self.code.values():
                    list_keys = list(self.code.keys())
                    list_values = list(self.code.values())
                    index = list_values.index(char)
                    required_char = list_keys[index]
                    temp_txt += required_char
            temp_txt += " "
        return temp_txt

print("########### MORSE CODE GENERATOR ##########")
text = input("Enter Text to Operate: ")
print("""
[1] Encode
[2] Decode
""")
choice = input(">>> ")
print("\n")
m = MorseCode(text)
if choice == "1":
    print("OUTPUT: ",  m.encode())
elif choice == "2":
    print("OUTPUT: ", m.decode())

else:
    print("NOT AN OPTION.")