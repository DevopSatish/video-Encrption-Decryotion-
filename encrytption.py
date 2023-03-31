import random
from sanzan import Sanzan
from sanzan import  *
import smtplib
from email.message import EmailMessage
msg = EmailMessage()


with open("otp.txt", "r") as f:
    otp = f.read()

if __name__ == "__main__":
    s = Sanzan("devop.mp4")
    s.set_password(otp)
    s.encrypt("encrypted.mp4")
     

