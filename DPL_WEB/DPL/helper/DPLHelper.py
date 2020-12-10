import qrcode
from benefactors import mail, app
from flask_mail import Message

def generateSendQRCode(passcode: str):
    qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=5)
    qr.add_data(passcode)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    print('about to save the image')
    rgb = img.convert('RGB')
    rgb.save(f'benefactors/static/QR/{passcode}.png')
    return True

def sendQr(passcode: str, user_email:str, tracking_number: str, Couries_passcode: str):
    #@todo: update the msg content
    msg = Message(f"Delivery:{passcode} QR Code", sender = "parcelsolution440", recipients=[user_email])
    path = f"static/QR/{passcode}.png"
    msg.body = f"""
    \nUse this QR code to access your package once it's been dropped off.\n
    Package Tracking Number = {tracking_number}
    Package User Passcode = {passcode}
    Package Courier Passcode = {Couries_passcode}
    """
    try:
        with app.open_resource(path) as fp:
            msg.attach(path, "{passcode}/png", fp.read() )
    except:
        return False
    print('sent the mail')
    mail.send(msg)
    return True

def NotificationEmail(status_code: str, passcode:str, user_email:str):
    print('inside emailing functions')
    status_code= str(status_code)
    if status_code == "1":
        msg_body = "Your package has been delivered and it is ready for pick up!"
    elif status_code == "2":
        msg_body = "Your package has been picked up! Please refer to the website for further information."
    else:
        return False

    msg = Message(f"Updates for {passcode} package", sender = "parcelsolution440", recipients=[user_email])
    msg.body = msg_body
    mail.send(msg)
    print('sent update email')
    return True
