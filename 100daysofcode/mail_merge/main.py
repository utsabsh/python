#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
placeholer="[name]"
with open("Input/Names/invited_names.txt")as namesi:
    names=namesi.readlines()

    
with open("Input/Letters/starting_letter.txt") as start:
    start_letter=start.read()
    
    for name in names:
        stripped_name=name.strip()
        # with open(f"output/ReadyToSend/Letter_for_{name}",mode="w" ) as letters:
        new_letter=start_letter.replace(placeholer,stripped_name)
        with open(f"output/ReadyToSend/Letter_for_{stripped_name}",mode="w" ) as completed_letter:
            completed_letter.write(new_letter)