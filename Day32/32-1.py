import smtplib

my_email = "ppaarrtthh1001@gmail.com"
my_password = "gmail@password"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="ppaarrtthh1001@yahoo.com",
                        msg="Subject:Python\n\nHello this mail is sent by python.")
