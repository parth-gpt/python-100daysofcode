##################### Normal Starting Project ######################

import datetime as dt
import random
import smtplib
import pandas

now = dt.datetime.now()
today = (now.month, now.day)


data = pandas.read_csv("birthdays.csv")
data_dict = {(row.month, row.day): row for (index, row) in data.iterrows()}

if today in data_dict:
    data_person = data_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        new_content = content.replace("[NAME]", data_person["name"])

    my_email = "ppaarrtthh1001@gmail.com"
    my_password = "gmail@password"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=data_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{new_content}")
