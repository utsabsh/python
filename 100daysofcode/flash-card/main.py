from tkinter import *
import pandas
import random

# Constants
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# Load data from CSV file
try:
    # Attempt to read the words to learn if it exists
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # Fallback to original dataset if no progress file is found
    original_data = pandas.read_csv("data/french_words.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    # Convert the data to a dictionary of records
    to_learn = data.to_dict(orient="records")


# Function to display the next card
def next_card():
    global current_card, flip_timer
    # Cancel any existing timer to avoid overlap
    window.after_cancel(flip_timer)
    # Choose a random card from the list of words to learn
    current_card = random.choice(to_learn)
    # Update the canvas with the French word and reset the card appearance
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    # Set a timer to flip the card after 3 seconds
    flip_timer = window.after(3000, func=flip_card)


# Function to flip the card and show the English translation
def flip_card():
    # Update the card to show the English translation with new styles
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


# Function to handle known words
def is_known():
    # Remove the current word from the list of words to learn
    to_learn.remove(current_card)
    print(len(to_learn))  # Debug: Check remaining words
    # Save the updated list back to a CSV file
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    # Display the next card
    next_card()


# Initialize the main application window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Set an initial flip timer
flip_timer = window.after(3000, func=flip_card)

# Create a canvas to display the flashcards
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")  # Front card image
card_back_img = PhotoImage(file="images/card_back.png")  # Back card image
card_background = canvas.create_image(400, 263, image=card_front_img)  # Background image
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))  # Title text
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))  # Word text
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Create buttons for marking a word as unknown or known
cross_image = PhotoImage(file="images/wrong.png")  # Image for "unknown" button
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")  # Image for "known" button
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# Display the first card
next_card()

# Start the Tkinter event loop
window.mainloop()
