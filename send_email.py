import smtplib
from email.mime.text import MIMEText
import myconfig #store secrets

def send_email(subject, message, from_addr=myconfig.sender, to_addr=myconfig.recipient):
    GMAIL_LOGIN = myconfig.sender
    GMAIL_PASSWORD = myconfig.password

    if not to_addr:
        print("Recipient not provided")
        return

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(GMAIL_LOGIN,GMAIL_PASSWORD)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.close()

# TEST FUNCTION
# if __name__ == '__main__':
#     send_email("Test 2", "Hi, \n I hope this email finds you well.")
