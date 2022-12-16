import smtplib
from email.mime.text import MIMEText

SERVER = 'smtp.***'
PORT = ***
LOGIN = 'your login'
PASSWORD = 'your password '
FROM_EMAIL = 'from which email'
TEXT_TYPE = 'plain'  # html


def send_email(to, subject, message):
    msg = MIMEText(message, TEXT_TYPE, 'utf-8')
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = to

    smtp = smtplib.SMTP(SERVER, PORT)
    smtp.starttls()
    smtp.login(LOGIN, PASSWORD)
    smtp.send_message(msg)
    smtp.quit()


if __name__ == '__main__':
    send_email('FROM_EMAIL', 'THEME OF THE LETTER', 'TEXT OF THE LETTER')
