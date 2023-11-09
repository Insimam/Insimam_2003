from authentication import *
user=input("enter your username:  ")
password=input("enter your password: ")
students ="userpassword.txt"

if signin(user,password,students)==True:
    file=open("student.txt","r")
    print("Book_ID","\t","Book_Title","\t\t\t\t","Book_Author","\t\t","Book_Genre","\t\t\t","Book_Year","\t","Checked_Out")
    for i in file:
        value=i.strip().split(":")
        print(value[0],"\t\t",value[1],"\t\t\t",value[2],"\t\t",value[3],"\t\t\t",value[4],"\t",value[5])

    
else:
    print("password incorrect")



