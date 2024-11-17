from datetime import datetime  # Import the datetime module to get the current date
import pandas  # Import pandas to read the CSV file with birthday data
import random  # Import random to select a random birthday letter template
import smtplib  # Import smtplib for sending emails via SMTP

# 1. Replace these with your email credentials.
MY_EMAIL = "your_email@example.com"  # Your email address
MY_PASSWORD = "your_password"  # Your email password or app-specific password

# Get the current date (month and day) to check if it's someone's birthday today
today = datetime.now()  # Get the current date and time
today_tuple = (today.month, today.day)  # Store just the month and day as a tuple

# 2. Read the CSV file containing birthday data
data = pandas.read_csv("birthdays.csv")  # Read the CSV file with birthday info
# Create a dictionary where the key is a tuple (month, day) and the value is the corresponding row from the CSV
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Check if today's date is in the birthdays_dict
if today_tuple in birthdays_dict:  # If today matches any birthday
    birthday_person = birthdays_dict[today_tuple]  # Get the person's details

    # 3. Randomly choose one of the birthday letter templates
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"  # Randomly pick a letter template (1-3)
    with open(file_path) as letter_file:  # Open the selected letter template
        contents = letter_file.read()  # Read the contents of the letter template
        contents = contents.replace("[NAME]", birthday_person["name"])  # Replace the placeholder with the person's name

    # 4. Send the email
    # Set up the connection to your email provider's SMTP server
    with smtplib.SMTP("smtp.gmail.com") as connection:  # Replace with the SMTP server of your email provider
        connection.starttls()  # Start TLS encryption for secure communication
        connection.login(MY_EMAIL, MY_PASSWORD)  # Log in to the email account
        connection.sendmail(  # Send the email
            from_addr=MY_EMAIL,  # Your email address
            to_addrs=birthday_person["email"],  # Recipient's email address (from the CSV)
            msg=f"Subject: Happy Birthday!\n\n{contents}"  # Email subject and body (birthday message)
        )
