# Creating phishing email

import smtplib 
import ssl

#set up port number and server name
smtp_port = 587
smtp_server = "smtp.gmail.com"

email_from = "testerabcd602@gmail.com"
email_to = "jhur2397@gmail.com"

#password was generated randomly
pswd = "galhvxrijrwughle"

#Message that will be sent 
message = "You won a trip to Costa Rica!!"

#Creating a context
simple_email_context = ssl.create_default_context()

try:
    #connect to server
    print("Connecting to server...")
    TIE_server = smtplib.SMTP(smtp_server, smtp_port)
    TIE_server.starttls(context=simple_email_context)
    TIE_server.login(email_from, pswd)
    print("Connected to server : ")

    print()
    print(f"Sending email to - {email_to}")
    TIE_server.sendmail(email_from, email_to, message)
    print(f"Email was successful sent to - {email_to}")

#if email fails to send
except Exception as e:
    print(e)

#closing server
finally:
    TIE_server.quit()
    