sender_email = "icodeinnovahostingservice@gmail.com"
sender_password = "hnykgvqgyvorghrb"

def set_sender(email , password):
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
    if hasattr(__obj=obj_body, __name='sender_email') and hasattr(__obj=obj_body , __name="sender_password"):
        if obj_body['sender_email'] != "" and obj_body['sender_password'] != "":
            set_sender(email=obj_body.json['sender_email'], password=obj_body.json['sender_password'])
    return