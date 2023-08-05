from flask import Flask,request
from flask_cors import CORS , cross_origin
import sendMail

app = Flask(__name__)
CORS(app , resources={r"/":{"origins":"*"}})

@app.route("/")
def main():
    return "hello world"

@app.route("/sendMail", methods=["POST"])
@cross_origin()
def sendMail():
    try:
        if request.data:
            print(request.json)
            return sendMail.send_verification_email(receiver_email=request.json['email'], verification_code=request.json['code'])
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
