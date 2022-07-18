from email import message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime
import pandas as pd
import requests

from constants import SENDER_EMAIL, RECEIVER_EMAIL, RESULT_PATH
from secret import EMAIL_PASSWORD, APP_PASSWORD


PASSWORD = EMAIL_PASSWORD
sender_email = SENDER_EMAIL
receiver_email = RECEIVER_EMAIL
today = datetime.datetime.now().day


def get_SNC_url():
    '''
    return the url for StartUp Nation Central, recently updated, current year,
    with pre-seed, seed or bootstreped funding stage
    '''
    current_year = get_current_year()
    url = "https://finder.startupnationcentral.org/startups/search?tab=recently_updated&list_1_action=and&list_2_action=and&list_3_action=and&list_4_action=and&list_5_action=and&list_6_action=and&list_7_action=and&list_8_action=and&list_9_action=and&list_10_action=and&list_11_action=and&list_12_action=and&list_13_action=and&list_14_action=and&list_15_action=and&list_16_action=and&list_17_action=and&list_18_action=and&list_19_action=and&list_20_action=and&funding_stage=Bootstrapped&funding_stage=Pre-Seed&funding_stage=Seed&founded_from_year=" + \
        str(current_year-1) + "&founded_to_year=" + str(current_year) + \
        "&status=Active&academia_based=0&time_range_code=2&time_range_from_date=2020-02-27"
    return url


def get_current_year():
    '''
    return the current year as an int
    '''
    return int(datetime.datetime.now().year)


def create_basic_html_table():
    '''
    convert excel file to a basic HTML table file
    '''
    df = pd.read_excel('result.xlsx')
    with open('pandas_table.html', 'w') as f:
        f.write(df.to_html())


def create_pretty_html_table():
    '''
    convert excel file to a 'pretty' HTML table file
    '''
    from pretty_html_table import build_table

    df = pd.read_excel('result.xlsx')
    html_table_blue_light = build_table(df, 'blue_light')

    # save to html file
    with open('pretty_table.html', 'w') as f:
        f.write(html_table_blue_light)


def send_email(sender_email, receiver_email, message):
    '''
    send email with subject, body, attached file
    '''

    import smtplib

    smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    # smtpserver.login(sender_email, PASSWORD)
    smtpserver.login(sender_email, APP_PASSWORD)

    subject = "Startup Nation Central Scraping"
    body = "Attached is the Startup Nation Central Scraping from " + str(today)

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = RESULT_PATH

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
    '''
    easy to use send_email() fucntion with preloaded params
    '''
    send_email(sender_email=sender_email,
               receiver_email=receiver_email, message=message)


def get_company_name_from_page_url(page_url):
    '''
    given page url of format: 
    /company_page/company-name

    return the company name
    '''
    if page_url == None:
        return None
    return page_url.split('/')[-1]


def summarize_description(page_url, description):
    from secret import AI21_API_KEY

    name = get_company_name_from_page_url(page_url)

    prompt = f"Company: {name} \nReview: {description}\nSummary:"

    res = requests.post(
        "https://api.ai21.com/studio/v1/j1-jumbo/complete",
        headers={"Authorization": f"Bearer {AI21_API_KEY}"},
        json={
            "prompt": prompt,
            "numResults": 1,
            "maxTokens": 20,
            "stopSequences": ["."],
            "topKReturn": 0,
            "temperature": 0.3,
            "topP": 0.98
        }
    )

    data = res.json()
    return data['completions'][0]['data']['text'].strip()
