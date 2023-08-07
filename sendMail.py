import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_verification_email(receiver_email, verification_code , userCode , type , image_url , name):
    sender_email = 'icodeinnovahostingservice@gmail.com'  # Replace with your email address
    sender_password = 'hnykgvqgyvorghrb'  # Replace with your email password
    subject = 'Account Verification'
    link = "https://zr2wffw0tl.execute-api.ap-south-1.amazonaws.com/dev/"+type+"/verifyEmail/"+userCode+"/"+verification_code
    html_content = '''
        <html>
    <head>
    </head>
    <body style="font-family: Verdana, Geneva, Tahoma, sans-serif;">
        <div style="display: flex; justify-content: center; align-items: center; margin-left: 25%;">
            <div 
                style="height: 510px; 
                    width: 520px; 
                    background-color: #fdfbf0; 
                    box-shadow: 3px 2px 3px rgba(129, 129, 129, 0.5);">
             
                <img src="'''+f'{image_url}'+'''" alt="Lunch Bucket Logo" style="height: 100px; width: 100px; margin-top: 10px; margin-left: 210px; ">
            
                <h3 style="color: #7E1F24 ; text-align: center;">Verify your email address</h3>
                <p style="text-align: center; font-size: 14px; font-weight: 500;">Thank you for signing up with '''+f'{name}'+'''.</p>
                <p style="text-align: center; font-size: 14px;">We're thrilled to have you on board!</p>
                <p style="text-align: center; font-size: 13px; color: grey;  margin-top: 70px;">To get started, please click the link below to verify your email address</p>
                <a  href="'''+f'{link}'+'''" 
                    ><button style="padding: 0.7rem;
                        width: 100%;
                        background-color: #037503; 
                        color: white; 
                        font-weight: 600;
                        border: none;
                        margin-top: 15px; 
                        font-size: 18px; 
                        cursor: pointer;">Verify My Email</button></a>
                <p 
                    style="margin-top:12vh; 
                    text-align: center;
                    font-size: 12px; 
                    color: rgb(110, 110, 110);">@2023 i2Auth</div>
            </p>
        </div>
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