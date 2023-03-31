from email.message import EmailMessage
import smtplib
msg = EmailMessage()
def sendMail(doc_id,email):
    msg.set_content('Hello, Your UserID is '+str(doc_id))
    msg['Subject'] = 'Video Decryption UserID'
    msg['From'] = "sy4529630@gmail.com"
    msg['To'] = email
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("sy4529630@gmail.com", "spxclrzivmqjjbod")
    server.send_message(msg)
    server.quit()
print("Welcome to SendMail Service ")
doc_id = input("Enter the Firebase Document ID: ")
email = input("Enter the user email: ")
sendMail(doc_id, email)
