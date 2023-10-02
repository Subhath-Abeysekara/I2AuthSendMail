sender_email = "icodeinnovahostingservice@gmail.com"
sender_password = "hnykgvqgyvorghrb"

def set_sender(email , password):
    if email == "" or password == "":
        return
    global sender_email , sender_password
    sender_email = email
    sender_password = password
    return

def get_sender():
    global sender_email, sender_password
    sender  = {
        "email":sender_email,
        "password":sender_password
    }
    sender_email = "icodeinnovahostingservice@gmail.com"
    sender_password = "hnykgvqgyvorghrb"
    return sender

def set_sender_by_user(obj_body):
    try:
        set_sender(email=obj_body['sender_email'], password=obj_body['sender_password'])
    except:
        print("default email")
    return