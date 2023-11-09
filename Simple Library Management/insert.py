from authentication import *
print("Library Management System Login Page".center(100))
file=open("student.txt","a")
user=input("Enter your username:  ")
password=input("Enter your password:  ")
student ="userpassword.txt"
if signin(user,password,student)==True:
    B_id = input("Enter The Book Id: ")
    Title = input("Enter The Title Of BooK: ")
    Author = input("Enter The Author: ")
    Genre = input("Enter The Book Genre: ")
    Year = input("Enter The Year Of Book: ")
    Cd_out = input("Checked Out: ")
    file.write(B_id+":"+Title+":"+Author+":"+Genre+":"+Year+":"+Cd_out+"\n")
    print(" Your Successfully Submitted...............")
else:
    print("password incorrect")
   