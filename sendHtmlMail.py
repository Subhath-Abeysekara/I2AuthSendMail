import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from sender_details import get_sender


def sendMail(receiver_email, html_content , subject ):
    sender = get_sender()
    print(sender)
    sender_email = sender['email']  # Replace with your email address
    sender_password = sender['password']  # Replace with your email password
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