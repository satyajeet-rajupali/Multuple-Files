
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='satyajeetrajupali@gmail.com',
    to_emails='sahanisatyam42@gmail.com',
    subject='MY FIRST AUTOMATED EMAIL BY satyajeetrajupali@gmail.com!!',
    html_content='<strong>Twilio is amazing and the best part is that \
        I programmed it completely in Python!!! <br><br><br> \
        This is a daily challenge for the Major League Hacking 2021. <br> \
        Best regards, <br><br>\
        Satya Jeet Raj Upali</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print("ERROR:", e)