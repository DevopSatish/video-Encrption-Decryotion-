import random


def generate_otp():
    digits = "0123456789"
    OTP = ""
    for i in range(6):
        OTP += digits[random.randint(0, 9)]

    return OTP


otp=generate_otp()

with open("otp.txt", "w") as f:
    f.write(otp)
