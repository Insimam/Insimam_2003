from tkinter import*
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox


class Roombooking:
	def __init__(self,root):
		self.root=root
		self.root.title("Hotel Managment System")
		self.root.geometry("1295x550+230+220")

		#================varibales==================#

		self.var_conntct=StringVar()
		self.var_checkin=StringVar()
		self.var_checkout=StringVar()
		self.var_roomtype=StringVar()
		self.var_roomavailable=StringVar()
		self.var_meal=StringVar()
		self.var_noofdays=StringVar()
		self.var_paidtax=StringVar()
		self.var_actualtotal=StringVar()
		self.var_total=StringVar()
	




		#==================Titel===================#

		lb1_tilte=Label(self.root,text="ADD RoomBooking DETAILS", font=("times new roman",18,"bold"),
			bg="gray",fg="blue",bd=4,relief=RIDGE)
		lb1_tilte.place(x=0, y=20, width=1295, height=50)

		#=================LableFrame================#

		lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="RoomBooking Deatils",
			font=("times new roman", 12, "bold"), padx=2)
		lableframeleft.place(x=5, y=70, width=425, height=490)

			#==================Lables and Entrys=========#

			# customer contact

		lb1_cust_contact=Label(lableframeleft,text="Customer contact", font=("arial",12,"bold"),
			padx=2, pady=6)
		lb1_cust_contact.grid(row=0, column=0,sticky=W)

		enty_contact=ttk.Entry(lableframeleft,textvariable=self.var_conntct,width=20,font=("arial",13,"bold"))
		enty_contact.grid(row=0, column=1,sticky=W)

			#Featch data button

		btnFeatchData=Button(lableframeleft,command=self.Fetch_contact,text="Featch",font=("arial",12,"bold"),bg="gray",fg="black",width=8)
		btnFeatchData.place(x=330, y=1)

			# check_in Date

		check_in_date=Label(lableframeleft,text="Check in Date:", font=("arial",12,"bold"),
			padx=2, pady=6)
		check_in_date.grid(row=1, column=0,sticky=W)

		txtcheck_in_date=ttk.Entry(lableframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
		txtcheck_in_date.grid(row=1, column=1)


			# check_out Date

		lb1_check_out=Label(lableframeleft,text="Check out Date:", font=("arial",12,"bold"),
			padx=2, pady=6)
		lb1_check_out.grid(row=2, column=0,sticky=W)

		txtcheck_out=ttk.Entry(lableframeleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
		txtcheck_out.grid(row=2, column=1)

			# Room Type

		Label_RoomType=Label(lableframeleft,font=("arial",12,"bold"),text="Room Type:", padx=2, pady=6)
		Label_RoomType.grid(row=3, column=0, sticky=W)

		combo_RoomType=ttk.Combobox(lableframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"), width=27,
			state="readonly")
		combo_RoomType["value"]=("Single","Double","laxary")
		combo_RoomType.current(0)
		combo_RoomType.grid(row =3, column=1)

			#Room Available

		lb1RoomAvailable=Label(lableframeleft,text="Room Available:", font=("arial",12,"bold"),
			padx=2, pady=6)
		lb1RoomAvailable.grid(row=4, column=0,sticky=W)

		#txtRoomAvailable=ttk.Entry(lableframeleft,textvariable=self.var_roomavailable,width=29,font=("arial",13,"bold"))
		#txtRoomAvailable.grid(row=4, column=1)

		combo_roomNo=ttk.Combobox(lableframeleft,textvariable=self.var_roomavailable,font=("arial",12,"bold"), width=27,
			state="readonly")
		combo_roomNo["value"]=("1001","1002","4002","1003","4001","1004","1005","4003","1006","4004","1007","1008","5001","5002",
			"4005","1009","4006","2001","2002","2003","4007","2004","4008","2005","2006","4009","2007","2008","2009","3001","3002",
			"3003","3004","3005","3006","3007","3008","3009","5003","5004","5005","5006","5007","5008","5009")
		combo_roomNo.current(0)
		combo_roomNo.grid(row =4, column=1)


		
		


			#Meal

		lb1Meal=Label(lableframeleft,text="Services:", font=("arial",12,"bold"),
			padx=2, pady=6)
		lb1Meal.grid(row=5, column=0,sticky=W)

		combo_Meal=ttk.Combobox(lableframeleft,textvariable=self.var_meal,font=("arial",12,"bold"), width=27,
			state="readonly")
		combo_Meal["value"]=("Pool","Spa","Meal")
		combo_Meal.current(0)
		combo_Meal.grid(row =5, column=1)


		#No of Days

		lb1NoOfDays=Label(lableframeleft,text="No Of Days:", font=("arial",12,"bold"),
		padx=2, pady=6)
		lb1NoOfDays.grid(row=6, column=0,sticky=W)

		txtNoOfDays=ttk.Entry(lableframeleft,textvariable=self.var_noofdays,width=29,font=("arial",13,"bold"))
		txtNoOfDays.grid(row=6, column=1)




		# Paid Tax

		lb1NoOfDays=Label(lableframeleft,font=("arial",12,"bold"), text="Paid Tax:", 
		padx=2, pady=6)
		lb1NoOfDays.grid(row=7, column=0,sticky=W)

		txtNoOfDays=ttk.Entry(lableframeleft,textvariable=self.var_paidtax,width=29,font=("arial",13,"bold"))
		txtNoOfDays.grid(row=7, column=1)


		# Sub Total

		lb1NoOfDays=Label(lableframeleft,font=("arial",12,"bold"), text="Sub Total:", 
		padx=2, pady=6)
		lb1NoOfDays.grid(row=8, column=0,sticky=W)

		txtNoOfDays=ttk.Entry(lableframeleft,textvariable=self.var_actualtotal,width=29,font=("arial",13,"bold"))
		txtNoOfDays.grid(row=8, column=1)


		# Total Cost

		lb1IdNumber=Label(lableframeleft,font=("arial",12,"bold"), text="Total Cost:", 
		padx=2, pady=6)
		lb1IdNumber.grid(row=9, column=0,sticky=W)

		txtIdNumber=ttk.Entry(lableframeleft,textvariable=self.var_total,width=29,font=("arial",13,"bold"))
		txtIdNumber.grid(row=9, column=1)

		#====================Bill Buttons=============#

		btnBill=Button(lableframeleft,text="Bill",command=self.totel,font=("arial",12,"bold"),bg="gray",fg="black",width=9)
		btnBill.grid(row=10,column=0,padx=1,sticky=W)


		#====================Buttons==================#

		btn_frame=Frame(lableframeleft, bd=2, relief=RIDGE)
		btn_frame.place(x=0, y=400, width=412, height=40)

		btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="gray",fg="black",width=9)
		btnAdd.grid(row=0,column=0,padx=1)


		btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="gray",fg="black",width=9)
		btnUpdate.grid(row=0,column=1,padx=1)


		btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="gray",fg="black",width=9)
		btnDelete.grid(row=0,column=2,padx=1)


		btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="gray",fg="black",width=9)
		btnReset.grid(row=0,column=3,padx=1)


		#=====================lable frame search system==================#

		Table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And search System",
		font=("times new roman", 12, "bold"), padx=2)
		Table_frame.place(x=435, y=280, width=860, height=260)



		#===========================Show Data Table========================#

		Details_table=Frame(Table_frame, bd=2, relief=RIDGE)
		Details_table.place(x=0, y=50, width=860, height=350)

		scroll_x=ttk.Scrollbar(Details_table,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(Details_table,orient=VERTICAL)

		self.room_table=ttk.Treeview(Details_table,column=("contact","checkin","checkout","roomtype",
		"roomavailable","meal","noOfdays"),
		xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)

		scroll_x.config(command=self.room_table.xview)
		scroll_y.config(command=self.room_table.yview)

		self.room_table.heading("contact", text="Contact")
		self.room_table.heading("checkin", text="Check-in")
		self.room_table.heading("checkout", text="Check-out")
		self.room_table.heading("roomtype", text="Room Type")
		self.room_table.heading("roomavailable", text="Room No")
		self.room_table.heading("meal", text="Services")
		self.room_table.heading("noOfdays", text="NoOfDays")
		


		self.room_table["show"]="headings"

		self.room_table.column("contact",width=100)
		self.room_table.column("checkin",width=100)
		self.room_table.column("checkout",width=100)
		self.room_table.column("roomtype",width=100)
		self.room_table.column("roomavailable",width=100)
		self.room_table.column("meal",width=100)
		self.room_table.column("noOfdays",width=100)


		self.room_table.pack(fill=BOTH,expand=1)
		self.room_table.bind("<ButtonRelease-1>", self.get_cuersor)
		self.fetch_data()



	#=============================add data=====================================#
		


	def add_data(self):
		if self.var_conntct.get()=="" or self.var_checkin .get()=="":
			messagebox.showerror("Error","All fields are requaired", parent=self.root)
		else:
			try:
				conn=mysql.connector.connect(host="localhost",username="root",password="insimam@1234" ,database="moon luxury")
				my_cursor=conn.cursor()
				my_cursor.execute("insert into room value(%s,%s,%s,%s,%s,%s,%s)",(
																						self.var_conntct.get(),
																						self.var_checkin.get(),
																						self.var_checkout.get(),
																						self.var_roomtype.get(),
																						self.var_roomavailable.get(),
																						self.var_meal.get(),
																						self.var_noofdays.get()
																						
																					))




				conn.commit()
				self.fetch_data()
				conn.close()


			except Exception as es:
				messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)





			#=========================fetch data==================================#

	def fetch_data(self):
		conn=mysql.connector.connect(host="localhost",username="root",password="insimam@1234" ,database="moon luxury")
		my_cursor=conn.cursor()
		my_cursor.execute("select * from room")
		rows=my_cursor.fetchall()
		if len(rows)!=0:
			self.room_table.delete(*self.room_table.get_children())
			for i in rows:
				self.room_table.insert("",END, values=i)
			conn.commit()
		conn.close()


	#================getcuersor===========================#




	def get_cuersor(self,event=""):
		cusrsor_row=self.room_table.focus()
		conntent=self.room_table.item(cusrsor_row)
		row=conntent["values"]

		self.var_conntct.set(row[0])
		self.var_checkin.set(row[1])
		self.var_checkout.set(row[2])
		self.var_roomtype.set(row[3])
		self.var_roomavailable.set(row[4])
		self.var_meal.set(row[5])
		self.var_noofdays.set(row[6])

			#update fun


	def update(self):
		if self.var_conntct.get()=="":
			messagebox.showerror("Error","Plaece enter the mobile number", parent=self.root)

		else:
			conn=mysql.connector.connect(host="localhost",username="root",password="insimam@1234" ,database="moon luxury")
			my_cursor=conn.cursor()
			my_cursor.execute("update room set check_in=%s,check_out=%s,roomtype=%s,roomavailable=%s,meal=%s,noOfdays=%s where Contact=%s",(
																						self.var_checkin.get(),
																						self.var_checkout.get(),
																						self.var_roomtype.get(),
						 																self.var_roomavailable.get(),
						 																self.var_meal.get(),
						 																self.var_noofdays.get(), 
																						self.var_conntct.get()
																						 
																						))

			conn.commit()
		
			conn.close()	

			self.fetch_data()

#delite

	
	def mDelete(self):
		mDelete=messagebox.askyesno("Moon luxury System","Do you want delete this customer",parent=self.root)
		if mDelete>0:
			conn=mysql.connector.connect(host="localhost",username="root",password="insimam@1234" ,database="moon luxury")
			my_cursor=conn.cursor()
			query="delete from room where Contact=%s"
			value=(self.var_conntct.get(),)
			my_cursor.execute(query,value)

		else:
			if not mDelete:
				return

		conn.commit()
		self.fetch_data()
		conn.close()


#reset


	def reset(self):
		self.var_conntct.set("")
		self.var_checkin.set("")
		self.var_checkout.set("")
		#self.var_roomtype.set("")
		#self.var_roomavailable.set("")
		#self.var_meal.set("")
		self.var_noofdays.set("")
		self.var_paidtax.set("")
		self.var_actualtotal.set("")
		self.var_total.set("")
	





		#===============Alldata Fetch=============#
			
	def Fetch_contact(self):
		if self.var_conntct.get()=="":
			messagebox.showerror("Error","Plaese enter contact No",parent=self.root)
		else:
			conn=mysql.connector.connect(host="localhost",username="root",password="insimam@1234" ,database="moon luxury")
			my_cursor=conn.cursor()
			query=("select Name from customer where Mobile=%s")
			value=(self.var_conntct.get(),)
			my_cursor.execute(query,value)
			row=my_cursor.fetchone()

		if row==None:
			messagebox.showerror("Error","This No Not Found",parent=self.root)
		else:
			
		

			showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
			showDataframe.place(x=455,y=77,width=300,height=180)


			lb1Name=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
			lb1Name.place(x=0,y=0)

			lb1=Label(showDataframe,text=row,font=("arial",12,"bold"))
			lb1.place(x=90,y=0)

			#======================Gender==============================#

			conn=mysql.connector.connect(host="localhost",username="root",password="insimam@1234" ,database="moon luxury")
			my_cursor=conn.cursor()
			query=("select Gender from customer where Mobile=%s")
			value=(self.var_conntct.get(),)
			my_cursor.execute(query,value)
			row=my_cursor.fetchone()


			lb1Gender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
			lb1Gender.place(x=0,y=30)

			lb2=Label(showDataframe,text=row,font=("arial",12,"bold"))
			lb2.place(x=90,y=30)

			#=============================Email=======================#


			conn=mysql.connector.connect(host="localhost",username="root",password="insimam@1234" ,database="moon luxury")
			my_cursor=conn.cursor()
			query=("select Email from customer where Mobile=%s")
			value=(self.var_conntct.get(),)
			my_cursor.execute(query,value)
			row=my_cursor.fetchone()


			lb1Email=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
			lb1Email.place(x=0,y=60)

			lb3=Label(showDataframe,text=row,font=("arial",12,"bold"))
			lb3.place(x=90,y=60)

			#===============================Nationality==========================#



			conn=mysql.connector.connect(host="localhost",username="root",password="insimam@1234" ,database="moon luxury")
			my_cursor=conn.cursor()
			query=("select Nationality from customer where Mobile=%s")
			value=(self.var_conntct.get(),)
			my_cursor.execute(query,value)
			row=my_cursor.fetchone()


			lb1Nationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
			lb1Nationality.place(x=0,y=90)

			lb4=Label(showDataframe,text=row,font=("arial",12,"bold"))
			lb4.place(x=90,y=90)


			#===========================Address==============================#



			conn=mysql.connector.connect(host="localhost",username="root",password="insimam@1234" ,database="moon luxury")
			my_cursor=conn.cursor()
			query=("select Address from customer where Mobile=%s")
			value=(self.var_conntct.get(),)
			my_cursor.execute(query,value)
			row=my_cursor.fetchone()


			lb1Address=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
			lb1Address.place(x=0,y=120)

			lb5=Label(showDataframe,text=row,font=("arial",12,"bold"))
			lb5.place(x=90,y=120)


			conn.commit()
			conn.close()

	def totel(self):
		inDate=self.var_checkin.get()
		outDate=self.var_checkout.get()
		inDate=datetime.strptime(inDate,"%d/%m/%Y")
		outDate=datetime.strptime(outDate,"%d/%m/%Y")

		self.var_noofdays.set(abs(outDate-inDate).days)


		if(self.var_meal.get()=="Pool" and self.var_roomtype.get()=="laxary"):
			q1=float(3000)
			q2=float(8000)
			q3=float(self.var_noofdays.get())
			q4=float(q1+q2)
			q5=float(q3+q4)
			Tax="Rs."+str("%.2f"%((q5)*0.3))
			ST="Rs."+str("%.2f"%((q5)))
			TT="Rs."+str("%.2f"%(q5+((q5)*0.3)))
			self.var_paidtax.set(Tax)
			self.var_actualtotal.set(ST)
			self.var_total.set(TT)


		elif(self.var_meal.get()=="Spa" and self.var_roomtype.get()=="laxary"):
			q1=float(3000)
			q2=float(8000)
			q3=float(self.var_noofdays.get())
			q4=float(q1+q2)
			q5=float(q3+q4)
			Tax="Rs."+str("%.2f"%((q5)*0.4))
			ST="Rs."+str("%.2f"%((q5)))
			TT="Rs."+str("%.2f"%(q5+((q5)*0.4)))
			self.var_paidtax.set(Tax)
			self.var_actualtotal.set(ST)
			self.var_total.set(TT)	


		elif(self.var_meal.get()=="Meal" and self.var_roomtype.get()=="laxary"):
			q1=float(3000)
			q2=float(8000)
			q3=float(self.var_noofdays.get())
			q4=float(q1+q2)
			q5=float(q3+q4)
			Tax="Rs."+str("%.2f"%((q5)*0.25))
			ST="Rs."+str("%.2f"%((q5)))
			TT="Rs."+str("%.2f"%(q5+((q5)*0.25)))
			self.var_paidtax.set(Tax)
			self.var_actualtotal.set(ST)
			self.var_total.set(TT)



		elif (self.var_meal.get()=="Pool" and self.var_roomtype.get()=="Double"):
			q1=float(3000)
			q2=float(7000)
			q3=float(self.var_noofdays.get())
			q4=float(q1+q2)
			q5=float(q3+q4)
			Tax="Rs."+str("%.2f"%((q5)*0.2))
			ST="Rs."+str("%.2f"%((q5)))
			TT="Rs."+str("%.2f"%(q5+((q5)*0.2)))
			self.var_paidtax.set(Tax)
			self.var_actualtotal.set(ST)
			self.var_total.set(TT)


		elif (self.var_meal.get()=="Spa" and self.var_roomtype.get()=="Double"):
			q1=float(3000)
			q2=float(7000)
			q3=float(self.var_noofdays.get())
			q4=float(q1+q2)
			q5=float(q3+q4)
			Tax="Rs."+str("%.2f"%((q5)*0.3))
			ST="Rs."+str("%.2f"%((q5)))
			TT="Rs."+str("%.2f"%(q5+((q5)*0.3)))
			self.var_paidtax.set(Tax)
			self.var_actualtotal.set(ST)
			self.var_total.set(TT)


		elif (self.var_meal.get()=="Meal" and self.var_roomtype.get()=="Double"):
			q1=float(3000)
			q2=float(7000)
			q3=float(self.var_noofdays.get())
			q4=float(q1+q2)
			q5=float(q3+q4)
			Tax="Rs."+str("%.2f"%((q5)*0.25))
			ST="Rs."+str("%.2f"%((q5)))
			TT="Rs."+str("%.2f"%(q5+((q5)*0.25)))
			self.var_paidtax.set(Tax)
			self.var_actualtotal.set(ST)
			self.var_total.set(TT)


		elif (self.var_meal.get()=="Pool" and self.var_roomtype.get()=="Single"):
			q1=float(3000)
			q2=float(6000)
			q3=float(self.var_noofdays.get())
			q4=float(q1+q2)
			q5=float(q3+q4)
			Tax="Rs."+str("%.2f"%((q5)*0.1))
			ST="Rs."+str("%.2f"%((q5)))
			TT="Rs."+str("%.2f"%(q5+((q5)*0.1)))
			self.var_paidtax.set(Tax)
			self.var_actualtotal.set(ST)
			self.var_total.set(TT)


		elif (self.var_meal.get()=="Spa" and self.var_roomtype.get()=="Single"):
			q1=float(3000)
			q2=float(6000)
			q3=float(self.var_noofdays.get())
			q4=float(q1+q2)
			q5=float(q3+q4)
			Tax="Rs."+str("%.2f"%((q5)*0.2))
			ST="Rs."+str("%.2f"%((q5)))
			TT="Rs."+str("%.2f"%(q5+((q5)*0.2)))
			self.var_paidtax.set(Tax)
			self.var_actualtotal.set(ST)
			self.var_total.set(TT)

		elif (self.var_meal.get()=="Meal" and self.var_roomtype.get()=="Single"):
			q1=float(3000)
			q2=float(6000)
			q3=float(self.var_noofdays.get())
			q4=float(q1+q2)
			q5=float(q3+q4)
			Tax="Rs."+str("%.2f"%((q5)*0.25))
			ST="Rs."+str("%.2f"%((q5)))
			TT="Rs."+str("%.2f"%(q5+((q5)*0.25)))
			self.var_paidtax.set(Tax)
			self.var_actualtotal.set(ST)
			self.var_total.set(TT)



			




if __name__ == "__main__":
		root=Tk()
		obj=Roombooking(root) 
		root.mainloop()