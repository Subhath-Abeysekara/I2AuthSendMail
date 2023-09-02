import sendHtmlMail


def send_forgetPW_mail(receiver_email, token, image_url, name , project_code):
    subject = 'Account Verification'
    link = "https://zr2wffw0tl.execute-api.ap-south-1.amazonaws.com/dev/user/updatePassword/" + token + "/" + project_code
    html_content = '''
        <html>
    <head>
    </head>
    <body style="font-family: Verdana, Geneva, Tahoma, sans-serif;">
<div 
            style="height: 510px; 
                width: 520px; 
                background-color: #fdfbf0; 
                margin-left: auto;
                margin-right: auto;
                box-shadow: 3px 2px 3px rgba(129, 129, 129, 0.5);">

                <img src="''' + f'{image_url}' + '''" alt="Lunch Bucket Logo" style="height: 100px; width: 100px; margin-top: 10px; margin-left: 40%; ">

                <h3 style="color: #7E1F24 ; text-align: center;">Verify your email address</h3>
                <p style="text-align: center; font-size: 14px; font-weight: 500;">Thank you for signing in with ''' + f'{name}' + '''.</p>
                <p style="text-align: center; font-size: 14px;">We're thrilled to have you on board!</p>
                <p style="text-align: center; font-size: 13px; color: grey;  margin-top: 70px;">To get started, please click the link below to verify change your password</p>
                <a  href="''' + f'{link}' + '''" 
                    ><button style="padding: 0.7rem;
                        width: 100%;
                        background-color: #037503; 
                        color: white; 
                        font-weight: 600;
                        border: none;
                        margin-top: 15px; 
                        font-size: 18px; 
                        cursor: pointer;">Verify My Email</button></a>
                <a href="http://43.205.96.222:5000"><p 
                                style="margin-top:12%; 
                                text-align: center;
                                font-size: 12px; 
                                color: rgb(110, 110, 110);">Click here @2023 i2Auth</p></a>
                </div>
    </body>
</html>
        '''
    # Setup the email
    return sendHtmlMail.sendMail(receiver_email=receiver_email, subject=subject, html_content=html_content)

# send_forgetPW_mail("subath.abeysekara@gmail.com",'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Im5waXVtYW50aGkzMUBnbWFpbC5jb20iLCJwYXNzd29yZCI6IjEyMzQ1Njc4OSIsImNvZGUiOiI2NGQ3YzQ4NDAxM2Q5OWNiOTgwYTY5ODMiLCJleHBpcmUiOjE2OTMzODM4MTV9.sCmLtJVIbTgZt6lS3UCz-5TkVgOSXxVOvzm1LBjeu-s','url','lunchbucket')