alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encript(plain_text, shift_number):
    cipher_text = ""
    for letter in plain_text:
        
        position = alphabet.index(letter)    
        new_position = position +shift_number
        new_letter= alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded message is {cipher_text}")
    
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encript(plain_text=text,shift_number=shift)