import boto3
from botocore.exceptions import ClientError
import consts as c
import yaml
from datetime import date, datetime, time

cfg_file = open(c.config_path, 'r')
cfg = yaml.load(cfg_file, Loader=yaml.FullLoader)

# define sender and recipients
SENDER = cfg['mailing']['sender']
TO_RECIPIENT = cfg['mailing']['recipients'][0:1]
BCC_RECIPIENTS = cfg['mailing']['recipients'][1:]

# aws region
AWS_REGION = cfg['aws']['region']


def send_mails(mail_html):

    # subject line for the email
    today = date.today()
    dt = today.strftime("%d/%m/%Y")
    if datetime.utcnow().time() < time(12,00):
        SUBJECT = "Stock Infos {} Morning".format(dt)
    else:
        SUBJECT = "Stock Infos {} Evening".format(dt)

    # email body for recipients with non-HTML email clients
    BODY_TEXT = ("Stock infos:\r\n"
             "You are reading this message without a html client."
             "Please use or activate a mail client that can render html content."
            )
            
    # HTML body of the email
    BODY_HTML = mail_html           

    # char encoding
    CHARSET = "UTF-8"

    # ses client
    client = boto3.client('ses',region_name=AWS_REGION)

    # Try to send the email.
    try:
        #Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': TO_RECIPIENT,
                'BccAddresses': BCC_RECIPIENTS
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    # error handling	
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])

    