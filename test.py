from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import os


root =  Tk()
root.geometry("500x300")
root.title("Student Record")


tab_con = ttk.Notebook(root)

tab1= ttk.Frame(tab_con)
tab_con.add(tab1, text="Add marks")
tab_con.pack(expand = 1 , fill= "both")

tab2 = ttk.Frame(tab_con)
tab_con.add(tab2, text="Show Marks")
tab_con.pack(expand = 1 , fill= "both")

tab3 = ttk.Frame(tab_con)
tab_con.add(tab3, text="Devp Info")
tab_con.pack(expand = 1 , fill= "both")



text_widget = tk.Text(root)

def open_file():
    file_path = os.path.abspath(os.getcwd()) + "user.txt"
    with open("user.txt" , "r") as f:
        text_widget.delete("1.0", tk.END)
        text_widget.insert("1.0",f.read())

root.title("Full Form")
heading = Label(tab2,text = "Full Form", font = ("calibri", 13))
heading.pack()


open_file_button = tk.Button(tab2, text="Open All File", command=open_file)
text_widget.pack()
open_file_button.pack()

def my_reset():
	for widget in tab1.winfo_children():
		if isinstance(widget,Entry):
			widget.delete(0, 'end')
user = []
def save_info():
	name_info = name.get()
	sid_info = sid.get()
	sid_info = str(sid_info)

	module_name_info = module_name.get()
	module_grade_info = module_grade.get()
	print(name_info, sid_info, module_name_info, module_grade_info)

	file = open("user.txt", "a")
	file.write(f"Name: {name_info}  ID: {sid_info}  Module Name: {module_name_info}  Module Grade: {module_grade_info}\n")
	print(" Dear ", name_info, " Your Successfully Submitted...............")


name_text = Label(tab1,text = "Student Name : ",)
sid_text = Label(tab1,text = "Student ID : ",)
module_name_text = Label(tab1,text = "Module Name: ",)
module_grade_text = Label(tab1,text = "Module Grade: ",)
	 
name_text.place(x = 10, y = 50)
sid_text.place(x = 10, y = 125)
module_name_text.place(x = 10, y = 200)
module_grade_text.place(x = 10, y = 275)

name = StringVar()
sid = IntVar()
module_name = StringVar()
module_grade = StringVar() 

name_entry = Entry(tab1,textvariable = name)
sid_entry = Entry(tab1,textvariable = sid)
module_name_entry = Entry(tab1,textvariable = module_name)
module_grade_entry = Entry(tab1,textvariable = module_grade)


name_entry.place(x = 10, y = 75)
sid_entry.place(x = 10, y = 150)
module_name_entry.place(x = 10, y = 225)
module_grade_entry.place(x = 10, y = 300)

enter = Button(tab1, text = "Submitt",command = save_info)
enter.place(x = 10, y = 350)
reset = Button(tab1, text = "Reset",command = lambda:my_reset())
reset.place(x = 95, y = 350)


about = Label(tab3, 
	text=" \n mminsimam@gmail.com \n Developer Info:Insimam. \n Bach: CSD-18 \n FOR PROGRAMMING ASSIGNMENT. ", 
	font = "arial 20 bold" , justify="center")
about.pack()



root.mainloop()