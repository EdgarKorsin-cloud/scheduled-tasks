##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas as pd
import smtplib
import os

now = dt.datetime.now()
year = now.year
current_month = now.month
current_day = now.day

birthdays = pd.read_csv("birthdays.csv")
for index, row in birthdays.iterrows():
    if row["month"] == current_month and row["day"]==current_day:
        with open("letter_templates/letter_1.txt") as f:
            letter_1 = f.read()
            personalized_letter = letter_1.replace("[NAME]", row['name'])
            filename = f"letter_for_{row['name']}.txt"
            with open(filename, "w") as file:
                file.write(personalized_letter)
        my_email = email
        password = password
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="pepepotamopython@yahoo.com",
                msg=f"Subject: Happy Birthday\n\n{personalized_letter}")
