from flask import Flask,request
from flask_cors import CORS , cross_origin
from sendMail import send_verification_email

app = Flask(__name__)
CORS(app , resources={r"/":{"origins":"*"}})

@app.route("/")
def main():
    return "hello world"

@app.route("/sendMailUser", methods=["POST"])
@cross_origin()
def sendMailUser():
    try:
        if request.data:
            print(request.json)
            return send_verification_email(receiver_email=request.json['email'], verification_code=request.json['code'],userCode=request.json['userCode'] , type="user", image_url=request.json['image_url'], name=request.json['name'])
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
            return send_verification_email(receiver_email=request.json['email'], verification_code=request.json['code'],userCode=request.json['userCode'] , type="admin", image_url=request.json['image_url'], name=request.json['name'])
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
