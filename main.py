##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import pandas
import smtplib

# email vars
my_email = ""
password = ""
# Date vars
now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
# File vars
file_path = "birthdays.csv"
data = pandas.read_csv(file_path)
birthdays_dict = data.to_dict(orient="records")
file_templates = ["letter_templates/letter_1.txt","letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

# Loop through birthday_dict
for entry in birthdays_dict:
    # Check if any birthdays match todays date
    if entry["year"] == year and entry["month"] == month and entry["day"] == day:
        # Store name and email address of persons birthday
        name = entry["name"]
        birthday_email_address = entry["email"]
        # Get a random letter template file path
        letter_template = random.choice(file_templates)
        # Open template
        with open(letter_template, "r") as letter:
            # Get raw message
            raw_message = letter.read()
            # Replace name in raw message
            customised_message = raw_message.replace("[NAME]", name)
            # Set up smtp connection
            with smtplib.SMTP("smtp.gmail.com") as connection:
                # Secure connection
                connection.starttls()
                # Login
                connection.login(user=my_email, password=password)
                # Send mail
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=birthday_email_address,
                    msg=f"Subject: Happy birthday \n\n {customised_message}")







