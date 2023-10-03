sender_email = "icodeinnovahostingservice@gmail.com"
sender_password = "hnykgvqgyvorghrb"
cc_email = ""
def set_sender(email , password):
    if email == "" or password == "":
        return
    global sender_email , sender_password
    sender_email = email
    sender_password = password
    return

def set_cc(cc_email_):
    if cc_email_ == "":
        return
    global cc_email
    cc_email = cc_email_
    return

def get_sender():
    global sender_email, sender_password , cc_email
    sender  = {
        "email":sender_email,
        "password":sender_password,
        "cc_email":cc_email
    }
    sender_email = "icodeinnovahostingservice@gmail.com"
    sender_password = "hnykgvqgyvorghrb"
    cc_email = ""
    return sender

def set_sender_by_user(obj_body):
    try:
        set_sender(email=obj_body['sender_email'], password=obj_body['sender_password'])
    except:
        print("default email")
    return

def set_cc_by_user(obj_body):
    try:
        set_cc(cc_email_=obj_body['cc_email'])
    except:
        print("default cc email")
    return