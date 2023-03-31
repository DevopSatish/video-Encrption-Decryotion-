from main import *
email=input("Enter the UserMailId correctly: ")
if(db.collection('users').add({'email':email}) ):
    print("User added succesfullyy!!")
else:
    print("Failed to added User check the User Details. ")