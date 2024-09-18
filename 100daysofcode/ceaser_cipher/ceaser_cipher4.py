# List of alphabet letters repeated twice to handle wrapping when shifting
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# Function that performs Caesar cipher encoding/decoding
def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""  # String to store the final result
  if cipher_direction == "decode":  # If decoding, reverse the shift
    shift_amount *= -1
  for char in start_text:  # Loop through each character in the input text
    # If character is in the alphabet, apply the shift
    if char in alphabet:
        position = alphabet.index(char)  # Get current position of the letter
        new_position = position + shift_amount  # Calculate new position after shift
        end_text += alphabet[new_position]  # Add the shifted letter to the result
    else:
        # If the character is not in the alphabet (e.g. a space, number, or symbol), keep it unchanged
        end_text += char
    
  # Display the final encoded/decoded result
  print(f"Here's the {cipher_direction}d result: {end_text}")

# TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

# A flag to control when the program should stop
should_end = False

# Loop to keep the program running until the user chooses to stop
while not should_end:
    # Prompt the user for the action: encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    # Get the text to encode/decode
    text = input("Type your message:\n").lower()
    # Get the shift value from the user
    shift = int(input("Type the shift number:\n"))

    # TODO-2: Ensure shift number is within 0-25 by applying modulus 26
    shift = shift % 26
    
    # Call the Caesar cipher function with the user's inputs
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    # TODO-4: Ask the user if they want to restart the program
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == "no":  # If user types 'no', exit the loop and end the program
       should_end = True
       print("Goodbye!!")
