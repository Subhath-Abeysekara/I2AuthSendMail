import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_verification_email(receiver_email, verification_code , userCode , type):
    sender_email = 'icodeinnovahostingservice@gmail.com'  # Replace with your email address
    sender_password = 'hnykgvqgyvorghrb'  # Replace with your email password
    subject = 'Account Verification'
    link = "https://zr2wffw0tl.execute-api.ap-south-1.amazonaws.com/dev/"+type+"/verifyEmail/"+userCode+"/"+verification_code
    html_content = '''
        <html>
            <head></head>
            <body>
                <h1>I2Auth</h1>
                <h2>Hello!</h2>
                <p>Please Use The Folowing Link To Verify Your Email.</p>
                <p><a href="'''+f'{link}'+'''">VERIFY</a></p>
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