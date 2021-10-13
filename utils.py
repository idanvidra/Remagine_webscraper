from email import message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import date
import pandas as pd

PASSWORD = "remaginescraper1"
sender_email = "remaginewebscraper@gmail.com"
receiver_email = "eze@remagineventures.com"
today = date.today()

def create_basic_html_table():
    df = pd.read_excel('result.xlsx')

    with open('pandas_table.html', 'w') as f:
        f.write(df.to_html())

def create_pretty_html_table():
    from pretty_html_table import build_table

    df = pd.read_excel('result.xlsx')
    html_table_blue_light = build_table(df, 'blue_light')

    # save to html file
    with open ('pretty_table.html', 'w') as f:
        f.write(html_table_blue_light)

def send_email(sender_email, receiver_email, message):
    import smtplib

    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(sender_email, PASSWORD)

    subject = "Startup Nation Central Scraping"
    body = "Attached is the Startup Nation Central Scraping from " + str(today)

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "result.xlsx"

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    smtpserver.sendmail(sender_email, receiver_email, text)

def default_send_email():
    send_email(sender_email=sender_email, receiver_email=receiver_email, message=message)





