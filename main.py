from flask import Flask,request
from flask_cors import CORS , cross_origin

from sendOpenProjectEmail import send_open_mail, send_open_mail_prod, send_open_mail_sandBox
from sendVerificationMail import send_verification_email, send_verification_email_prod, send_verification_email_sandBox
from sendForgetPwMail import send_forgetPW_mail, send_forgetPW_mail_prod, send_forgetPW_mail_sandBox
from sender_details import set_sender, set_sender_by_user

app = Flask(__name__)
CORS(app , resources={r"/":{"origins":"*"}})

image_url = "https://firebasestorage.googleapis.com/v0/b/meetingdetecting.appspot.com/o/lunchbucket_special_meal%2Fi2AuthLogo.jpeg?alt=media&token=2cc0abf1-8069-47ad-863b-862be3afe2ed"
image_url_background = "https://firebasestorage.googleapis.com/v0/b/meetingdetecting.appspot.com/o/lunchbucket_special_meal%2Fbackground.jpeg?alt=media&token=94c39cf0-d097-4967-b261-1ac2b6f9e688"

@app.route("/")
def main():
    return '''<html>
    <head>
    </head>
    <body style="font-family: Verdana, Geneva, Tahoma, sans-serif; background-image: url(''' + f'{image_url_background}' + ''');">
        <div 
            style="height: 98%; 
                width: 100%;">
             
               <div style="margin-left: auto; margin-right: auto;height: 40%; width: 40%; min-width: 250px; min-height: 250px; max-width: 320px; max-height: 320px;"> <img src="''' + f'{image_url}' + '''" alt="Lunch Bucket Logo" style="height: 200px; width: 400px; "></div>
            
                <h3 style="color: #e7e7e7 ; text-align: center; font-size: 20px; margin: 0rem 10% 0% 10%;">Discover the power of our all-in-one authentication solution, where a comprehensive array of authentication services converges into a single, streamlined product.</h3>
                <h3 style="color: #e7dcdb ; text-align: center; font-size: 16px; margin: 2rem 10% 0% 10%;">Just leave the security worries to us while you focus on crafting exceptional software.</h3>
                <p style="text-align: center; font-size: 16px; font-weight: 500; color: #f7e5e8;">Here is how we assist you...</p>
     
                <table style="width: 100%; margin-top: 4rem;">
                    <tr>
                        <td style="width: 33.3%;"><div style="padding: 0.5rem; border-radius: 4px; background-color: #010033; color: white; text-align: center; margin: 0.5rem;">Customizable User Workflows</div> </td>
                        <td style="width: 33.3%;"><div style="padding: 0.5rem; border-radius: 4px; background-color: #010033; color: white; text-align: center; margin: 0.5rem;">Social Media and OAuth Integration</div> </td>
                        <td style="width: 33.3%;"><div style="padding: 0.5rem; border-radius: 4px; background-color: #010033; color: white; text-align: center; margin: 0.5rem;">Role-Based Access Control</div> </td>
                    </tr>
                    <tr>
                        <td style="width: 33.3%;"><div style="padding: 0.5rem; border-radius: 4px; background-color: #010033; color: white; text-align: center; margin: 0.5rem;">Customizable Login Themes</div> </td>
                        <td style="width: 33.3%;"><div style="padding: 0.5rem; border-radius: 4px; background-color: #010033; color: white; text-align: center; margin: 0.5rem;">Scalability and Performance</div> </td>
                        <td style="width: 33.3%;"><div style="padding: 0.5rem; border-radius: 4px; background-color: #010033; color: white; text-align: center; margin: 0.5rem;">Developer-Friendly SDKs</div> </td>
                    </tr>
                    <tr>
                        <td style="width: 33.3%;"><div style="padding: 0.5rem; border-radius: 4px; background-color: #010033; color: white; text-align: center; margin: 0.5rem;">Compliance and Regulations</div> </td>
                        <td style="width: 33.3%;"><div style="padding: 0.5rem; border-radius: 4px; background-color: #010033; color: white; text-align: center; margin: 0.5rem;">Support and Training</div> </td>
                        <td style="width: 33.3%;"><div style="padding: 0.5rem; border-radius: 4px; background-color: #010033; color: white; text-align: center; margin: 0.5rem;">ML Support</div> </td>
                    </tr>
                </table>
        </div>
    </body>
</html>'''

@app.route("/sendMailUser", methods=["POST"])
@cross_origin()
def sendMailUser():
    try:
        if request.data:
            print(request.json)
            set_sender_by_user(obj_body=request.json)
            return send_verification_email(receiver_email=request.json['email'], verification_code=request.json['code'],userCode=request.json['userCode'] , type="user", image_url=request.json['image_url'], name=request.json['name'],project_code=request.json['project_code'])
        else:
            return {
                "state": False,
                "message": "error no body"
            }
    except:
        return {
            "state": False,
            "message": "error"
        }

@app.route("/sendMailAdmin", methods=["POST"])
@cross_origin()
def sendMailAdmin():
    try:
        if request.data:
            print(request.json)
            set_sender_by_user(obj_body=request.json)
            return send_verification_email(receiver_email=request.json['email'], verification_code=request.json['code'],userCode=request.json['userCode'] , type="admin", image_url=request.json['image_url'], name=request.json['name'],project_code=request.json['project_code'])
        else:
            return {
                "state": False,
                "message": "error no body"
            }
    except:
        return {
            "state": False,
            "message": "error"
        }

@app.route("/sendMailForgetPw", methods=["POST"])
@cross_origin()
def sendMailForgetPw():
    try:
        if request.data:
            print(request.json)
            set_sender_by_user(obj_body=request.json)
            return send_forgetPW_mail(receiver_email=request.json['email'], token=request.json['token'], image_url=request.json['image_url'], name=request.json['name'],project_code=request.json['project_code'])
        else:
            return {
                "state": False,
                "message": "error no body"
            }
    except:
        return {
            "state": False,
            "message": "error"
        }

@app.route("/sendOpenMail", methods=["POST"])
@cross_origin()
def sendOpenMail_dev():
    try:
        if request.data:
            print(request.json)
            set_sender_by_user(obj_body=request.json)
            return send_open_mail(receiver_email=request.json['email'], token=request.json['token'], image_url=request.json['image_url'], name=request.json['name'],project_code=request.json['project_code'])
        else:
            return {
                "state": False,
                "message": "error no body"
            }
    except:
        return {
            "state": False,
            "message": "error"
        }


#         **********PROD************
@app.route("/prod/sendMailUser", methods=["POST"])
@cross_origin()
def sendMailUserProd():
    try:
        if request.data:
            print(request.json)
            set_sender_by_user(obj_body=request.json)
            return send_verification_email_prod(receiver_email=request.json['email'], verification_code=request.json['code'],userCode=request.json['userCode'] , type="user", image_url=request.json['image_url'], name=request.json['name'],project_code=request.json['project_code'])
        else:
            return {
                "state": False,
                "message": "error no body"
            }
    except:
        return {
            "state": False,
            "message": "error"
        }

@app.route("/prod/sendMailAdmin", methods=["POST"])
@cross_origin()
def sendMailAdminProd():
    try:
        if request.data:
            print(request.json)
            set_sender_by_user(obj_body=request.json)
            return send_verification_email_prod(receiver_email=request.json['email'], verification_code=request.json['code'],userCode=request.json['userCode'] , type="admin", image_url=request.json['image_url'], name=request.json['name'],project_code=request.json['project_code'])
        else:
            return {
                "state": False,
                "message": "error no body"
            }
    except:
        return {
            "state": False,
            "message": "error"
        }

@app.route("/prod/sendMailForgetPw", methods=["POST"])
@cross_origin()
def sendMailForgetPwProd():
    try:
        if request.data:
            print(request.json)
            set_sender_by_user(obj_body=request.json)
            return send_forgetPW_mail_prod(receiver_email=request.json['email'], token=request.json['token'], image_url=request.json['image_url'], name=request.json['name'],project_code=request.json['project_code'])
        else:
            return {
                "state": False,
                "message": "error no body"
            }
    except:
        return {
            "state": False,
            "message": "error"
        }

@app.route("/prod/sendOpenMail", methods=["POST"])
@cross_origin()
def sendOpenMail_prod():
    try:
        if request.data:
            print(request.json)
            set_sender_by_user(obj_body=request.json)
            return send_open_mail_prod(receiver_email=request.json['email'], token=request.json['token'], image_url=request.json['image_url'], name=request.json['name'],project_code=request.json['project_code'])
        else:
            return {
                "state": False,
                "message": "error no body"
            }
    except:
        return {
            "state": False,
            "message": "error"
        }


#      ********************SAND BOX***************

@app.route("/beta/sendMailUser", methods=["POST"])
@cross_origin()
def sendMailUserBeta():
    try:
        if request.data:
            print(request.json)
            set_sender_by_user(obj_body=request.json)
            return send_verification_email_sandBox(receiver_email=request.json['email'], verification_code=request.json['code'],userCode=request.json['userCode'] , type="user", image_url=request.json['image_url'], name=request.json['name'],project_code=request.json['project_code'])
        else:
            return {
                "state": False,
                "message": "error no body"
            }
    except:
        return {
            "state": False,
            "message": "error"
        }

@app.route("/beta/sendMailAdmin", methods=["POST"])
@cross_origin()
def sendMailAdminBeta():
    try:
        if request.data:
            print(request.json)
            set_sender_by_user(obj_body=request.json)
            return send_verification_email_sandBox(receiver_email=request.json['email'], verification_code=request.json['code'],userCode=request.json['userCode'] , type="admin", image_url=request.json['image_url'], name=request.json['name'],project_code=request.json['project_code'])
        else:
            return {
                "state": False,
                "message": "error no body"
            }
    except:
        return {
            "state": False,
            "message": "error"
        }

@app.route("/beta/sendMailForgetPw", methods=["POST"])
@cross_origin()
def sendMailForgetPwBeta():
    try:
        if request.data:
            print(request.json)
            set_sender_by_user(obj_body=request.json)
            return send_forgetPW_mail_sandBox(receiver_email=request.json['email'], token=request.json['token'], image_url=request.json['image_url'], name=request.json['name'],project_code=request.json['project_code'])
        else:
            return {
                "state": False,
                "message": "error no body"
            }
    except:
        return {
            "state": False,
            "message": "error"
        }

@app.route("/beta/sendOpenMail", methods=["POST"])
@cross_origin()
def sendOpenMail_beta():
    try:
        if request.data:
            print(request.json)
            set_sender_by_user(obj_body=request.json)
            return send_open_mail_sandBox(receiver_email=request.json['email'], token=request.json['token'], image_url=request.json['image_url'], name=request.json['name'],project_code=request.json['project_code'])
        else:
            return {
                "state": False,
                "message": "error no body"
            }
    except:
        return {
            "state": False,
            "message": "error"
        }

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost',port=5000)
