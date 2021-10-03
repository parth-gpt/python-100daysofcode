import datetime as dt
import random
import smtplib

my_email = "ppaarrtthh1001@gmail.com"
my_password = "gmail@password"

with open("quotes.txt") as quotes:
    data = quotes.readlines()
    now = dt.datetime.now()
    day = now.weekday()
    if day == 5:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject: Monday Motivation\n\n{random.choice(data)}"
            )
