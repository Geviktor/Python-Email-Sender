#Import
import smtplib, ssl
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

#Sender and receiver emails.
sender = "{SENDER_EMAIL}"
receiver = "{RECEIVER_EMAIL}"

#Create email headers.
message = MIMEMultipart("")

message["Subject"] = "{SUBJECT}"
message["From"] = sender
message["To"] = receiver

#Send text message.
text = """
{MESSAGE}
"""
part1 = MIMEText(text, "plain")
message.attach(part1)

#Send attachment with message.
filepath = "{FILEPATH}"
part2 = MIMEBase("application", "octet-stream")
part2.set_payload(open(filepath, "rb").read())
encoders.encode_base64(part2)

part2.add_header("Content-Disposition", "attachment; filename= {FILENAME}")

message.attach(part2)

#Send message with html tags.
html = """
<html>
    <body>
       {ENTER_HTML}
    </body>
</html>
"""
part3 = MIMEText(html, "html")
message.attach(part3)


#Connect to server and send the email.
context = ssl.create_default_context()

    # mail   : smtp adress    |  port no
    # gmail  : smtp.gmail.com |  465,587
    # outlook: smtp.live.com  |  465,587
    # yahoo  : mail.yahoo.com |  465,587
server = smtplib.SMTP("{SMTP_ADRESS}",{PORT_NO}) #Connect smtp server.
server.starttls()
server.ehlo_or_helo_if_needed()

server.login(sender,"{PASSWORD}") #Login your account

try:
    server.sendmail(
                sender, receiver, message.as_string()
            )
    server.quit()
    print("Email sent successfully")
except:
    pass

