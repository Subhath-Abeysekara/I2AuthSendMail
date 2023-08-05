import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_verification_email(receiver_email, verification_code):
    sender_email = 'subath.abeysekara@gmail.com'  # Replace with your email address
    sender_password = 'ifbfbbzstpanyxmq'  # Replace with your email password
    subject = 'Account Verification'
    html_content = '''
        <html>
            <head></head>
            <body>
                <h1>Hello!</h1>
                <p>This is an example HTML email sent using Python.</p>
                <p><a href="'''+f'http://www.example.com/verify?code={verification_code}'+'''">VERIFY</a> to verify your email.</p>
            </body>
        </html>
        '''
    # Setup the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(html_content, 'html'))

    # Connect to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your SMTP server and port
    server.starttls()

    # Login to your email account
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    # Close the connection
    server.quit()

    return {
        "state": True,
        "message": "success"
    }

# Example usage:
# verification_code = "0102"
# receiver_email = 'dinikijayakody@gmail.com'  # Replace with the recipient's email address
# send_verification_email(receiver_email, verification_code)