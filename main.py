# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import pandas as pd
import smtplib
import datetime as dt
import random
import os

now_datetime = dt.datetime.now()
now_month = now_datetime.month
now_day = now_datetime.day
my_email = os.environ.get("my_email")
my_email_password = os.environ.get("my_email_password")
all_wish_letter = []

with open("letter_templates/letter_1.txt") as letter_1_file:
    letter1_data = letter_1_file.read().splitlines()
    all_wish_letter.append(letter1_data)

with open("letter_templates/letter_2.txt") as letter_2_file:
    letter2_data = letter_2_file.read().splitlines()
    all_wish_letter.append(letter2_data)

with open("letter_templates/letter_3.txt") as letter_3_file:
    letter3_data = letter_3_file.read().splitlines()
    all_wish_letter.append(letter3_data)


with open("birthdays.csv") as birthdays_file:
    data = pd.read_csv(birthdays_file) #data為DataFrame格式

    for (index, row) in data.iterrows():
        if row['month'] == now_month and row['day'] == now_day:
            receipt_email = row['email']
            receipt_name = row['name']
            wish_letter = random.choice(all_wish_letter)
            update_name = [text.replace("[NAME]", receipt_name) for text in wish_letter]
            final_wish_letter = "\n".join(update_name)
            print(final_wish_letter)

            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(user = my_email, password = my_email_password)
                connection.sendmail(
                    from_addr = my_email,
                    to_addrs = receipt_email,
                    msg = f'Subject: Happy Birthday {receipt_name}\n\n{final_wish_letter}\nDate at: {now_datetime.strftime("%Y/%m/%d %H:%M:%S")}'
                )


