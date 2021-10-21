# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId)
from datetime import datetime
import base64


def send_email():
    message = Mail(
        from_email='spendtrack671@gmail.com',
        to_emails='YOUR PERSONAL EMAIL ACCOUNT GOES HERE',
        subject="Purchase Habit Analytics - {}".format(str(datetime.now().strftime("%m/%d/%Y"))),
        html_content='<strong>Below is your daily update on your purchasing habits. The CSV file attached shows your total amount spent per category as of now.</strong>')
    with open('purchase_count_visual.png', 'rb') as f:
        img_data = f.read()
        f.close()
    message.attachment = __create_attachment(img_data, 'png', 'purchase_count_visual.png', '1')
    
    with open('total_amount_spent.png', 'rb') as f:
        img_data = f.read()
        f.close()
    message.attachment = __create_attachment(img_data, 'png', 'total_amount_spent.png', '2')
    
    with open("total_spent.csv", "rb") as f:
        csv_data = f.read()
        f.close()
    message.attachment = __create_attachment(csv_data, 'csv', 'total_spent.csv', '3')
    
    try:
        sg = SendGridAPIClient(api_key='YOUR SENDGRID API KEY GOES HERE')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

def __create_attachment(data, file_type, file_name, content_id):
    encoded = base64.b64encode(data).decode()
    attachment = Attachment()
    attachment.file_content = FileContent(encoded)
    attachment.file_type = FileType(f'application/{str(file_type)}')
    attachment.file_name = FileName(file_name)
    attachment.disposition = Disposition('attachment')
    attachment.content_id = ContentId(content_id)
    return attachment
