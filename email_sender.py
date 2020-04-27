#Import
import smtplib, ssl
from time import sleep
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

#Create email content.
msg = MIMEMultipart("")

#Add a text in email.
def textMsg(sender,receiver,subject,text):
    global msg
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = receiver
    part1 = MIMEText(text, "plain")
    msg.attach(part1)

#Add a file attachment in email.
def attachMsg(filepath,filename):
    global msg
    part2 = MIMEBase("application", "octet-stream")
    part2.set_payload(open(filepath, "rb").read())
    encoders.encode_base64(part2)

    part2.add_header("Content-Disposition", f"attachment; filename= {filename}")
    msg.attach(part2)

#Add html tag in email.
def htmlMsg(html):
    global msg
    part3 = MIMEText(html, "html")
    msg.attach(part3)

#Connect and login the sender email address.
def loginEmail(sender,password):
    context = ssl.create_default_context()
     # mail   : smtp adress    |  port no
     # gmail  : smtp.gmail.com |  465,587
     # outlook: smtp.live.com  |  465,587
     # yahoo  : mail.yahoo.com |  465,587
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.ehlo_or_helo_if_needed()
    server.login(sender,password)

    return server

#Send the email
def sendEmail(sender,receiver,password,msg,many):
    server = loginEmail(sender,password)
    for i in range(1,many+1):
        try:
            if i % 30 == 0:
                server.quit()
                print("Wait 1 minute...")
                sleep(60)
                server = loginEmail(sender,password)
            server.sendmail(sender,receiver,msg.as_string())
            print(f"{i}. Email sent successfully.")
        except:
            print("Error.")
    
    server.quit()

#Set parameters and send to function.
def main():
    global msg
    sender = "{SENDER}"
    password = "{PASSWORD}"
    receiver = "{RECEIVER}"
    many = {HOW_MANY}
    
    subject = "{ENTER_SUBJECT}"
    text = """
    {ENTER_MESSAGE}
    """
    textMsg(sender,receiver,subject,text)

    html = """
    <html>
        <body>
            {ENTER_TAGS}
        </body>
    </html>
    """
    htmlMsg(html)

    filepath = "{FILE/PATH}"
    filename = "{FILENAME}"
    attachMsg(filepath,filename)

    
    sendEmail(sender,receiver,password,msg,many)

if __name__ == '__main__':
    main()

