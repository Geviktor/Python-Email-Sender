#Import
import smtplib, ssl
from time import sleep
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

msg = MIMEMultipart("")

def textMsg(sender,receiver,text):
    global msg
    msg["Subject"] = ""
    msg["From"] = sender
    msg["To"] = receiver
    part1 = MIMEText(text, "plain")
    msg.attach(part1)

def attachMsg(filepath,filename):
    global msg
    part2 = MIMEBase("application", "octet-stream")
    part2.set_payload(open(filepath, "rb").read())
    encoders.encode_base64(part2)

    part2.add_header("Content-Disposition", f"attachment; filename= {filename}")
    msg.attach(part2)


def htmlMsg(html):
    global msg
    part3 = MIMEText(html, "html")
    msg.attach(part3)

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

def sendEmail(sender,receiver,password,msg,many):
    server = loginEmail(sender,password)
    for i in range(many):
        try:
            server.sendmail(sender,receiver,msg.as_string())
            if i != 0 and i % 30 == 0:
                server.quit()
                print("Wait 1 minute...")
                sleep(60)
                server = loginEmail(sender,password)
            print(f"{i}. Email sent successfully.")
        except:
            print("Error.")
    
    server.quit()

def main():
    global msg
    sender = "{SENDER}"
    password = "{PASSWORD}"
    receiver = "{RECEIVER}"
    many = {HOW_MANY}

    text = """
    {ENTER_MESSAGE}
    """
    html = """
    <html>
        <body>
            {ENTER_TAGS}
        </body>
    </html>
    """
    filepath = "{FILE/PATH}"
    filename = "{FILENAME}"

    textMsg(sender,receiver,text)
    htmlMsg(html)
    attachMsg(filepath,filename)
    sendEmail(sender,receiver,password,msg,many)
