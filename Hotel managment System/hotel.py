from tkinter import*
import tkinter as tk
from customer import Cust_win
from developer import developer1
from room import Roombooking
from Deatails import DeatailsRoom

class HotelManagmentSystem:
	def __init__(self,root):
		self.root=root
		self.root.title("Hotel Managment System")
		self.root.geometry("1550x800+0+0")
	
		# =================Title===============#
		lb1_tilte=Label(self.root,text="MOON  LUXURY  HOTEL  MANAGMENT  SYSTEM", font=("times new roman",40,"bold"),
			bg="gray",fg="blue",bd=4,relief=RIDGE)
		lb1_tilte.place(x=0, y=20, width=1550, height=50)

		#=================Main Frame===========#
		main_frame=Frame(self.root,bd=4,relief=RIDGE)
		main_frame.place(x=0, y=190, width=1550, height=620)

		#=================menu==================#
		lb1_menu=Label(main_frame,text="MENU" , font=("times new roman",20,"bold"),
			bg="orange",fg="black",bd=4,relief=RIDGE)
		lb1_menu.place(x=0, y=0, width=230)

		#=================button Frame=================#
		btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
		btn_frame.place(x=0, y=35, width=228, height=190)


		#cust Button
		cust_btu=Button(btn_frame, text="CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),
			bg="gray",fg="black",bd=0)
		cust_btu.grid(row=0, column=0, pady=1)


		#Room Button
		room_btu=Button(btn_frame, text="ROOM",command=self.Roombooking,width=22,font=("times new roman",14,"bold"),
			bg="gray",fg="black",bd=0)
		room_btu.grid(row=1, column=0, pady=1)


		#details_Button
		details_btu=Button(btn_frame, text="BILL INFO",command=self.DeatailsRoom,width=22,font=("times new roman",14,"bold"),
			bg="gray",fg="black",bd=0)
		details_btu.grid(row=2, column=0, pady=1)

		#Rport Button
		report_btu=Button(btn_frame, text="DEVELOPER INFO",command=self.developer1,width=22,font=("times new roman",14,"bold"),
			bg="gray",fg="black",bd=0)
		report_btu.grid(row=3, column=0, pady=1)


		#logout Button
		logout_btu=Button(btn_frame, text="LOGOUT",command=self.logout,width=22,font=("times new roman",14,"bold"),
			bg="gray",fg="black",bd=0)
		logout_btu.grid(row=4, column=0, pady=1)


	def cust_details(self):
		self.new_window=Toplevel(self.root)    

		self.app=Cust_win(self.new_window)


	def Roombooking(self):
		self.new_window=Toplevel(self.root)    

		self.app=Roombooking(self.new_window)

	def DeatailsRoom(self):
		self.new_window=Toplevel(self.root)    

		self.app=DeatailsRoom(self.new_window)

	def logout(self):
		self.root.destroy()

	def developer1(self):

		self.new_window=Toplevel(self.root)    
		self.app=developer1(self.new_window)


	

		#lb = tk.Label(developer, text = "home page\n\nPage1:", font = ("Bold", 30))
		



	


if __name__ == "__main__":
	root=Tk()
	obj=HotelManagmentSystem(root)
	root.mainloop()
