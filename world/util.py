import string
import random

from django.core.mail import EmailMessage

def otp_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def send_otp_email(email, otp):
    try:
        message = "Your otp is %s" %(otp)
        email = EmailMessage('OTP for panorbit login', message, to=[email])
        email.send()
    except Exception:
        return False
    
    return True
    
def validate_otp(otp, sent_otp, email, sent_email):
    if not sent_otp or not sent_email:
        result = {"success": False, "message": "session expired"}
        return result

    if not email or not otp:
        result = {"success": False, "message": "didnot recieve proper data"}
        return result

    if otp != sent_otp:
        result = {"success": False, "message": "wrong otp"}
        return result

    if email != sent_email:
        result = {"success": False, "message": "wrong email"}
        return result

    result = {"success": True, "message": "validated"}
    return result

