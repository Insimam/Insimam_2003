from tkinter import*
from tkinter import ttk
import mysql.connector
import random
from time import strftime
from datetime import datetime
from tkinter import messagebox


class DeatailsRoom:
	def __init__(self,root):
		self.root=root
		self.root.title("Hotel Managment System")
		self.root.geometry("1295x550+230+220")


		#==================Titel===================#

		lb1_tilte=Label(self.root,text="MANAGMENT DETAILS", font=("times new roman",18,"bold"),
			bg="gray",fg="blue",bd=4,relief=RIDGE)
		lb1_tilte.place(x=0, y=20, width=1295, height=50)

		#=================LableFrame================#

		lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Deatils",
			font=("times new roman", 12, "bold"), padx=2)
		lableframeleft.place(x=5, y=70, width=540, height=350)

		# Billno

		self.var_bill=StringVar()
		x=random.randint(1000,9999)
		self.var_bill.set(str(x))

		ref=Label(lableframeleft,text="Bill No:", font=("arial",12,"bold"),
			padx=2, pady=6)
		ref.grid(row=1, column=0,sticky=W)

		

		txtref=ttk.Entry(lableframeleft,textvariable=self.var_bill,width=29,font=("arial",13,"bold"),state="readonly")
		txtref.grid(row=1, column=1)





		# Ref

		paid_tex=Label(lableframeleft,text="Ref:", font=("arial",12,"bold"),
			padx=2, pady=6)
		paid_tex.grid(row=2, column=0,sticky=W)

		self.var_ref=StringVar()

		txtpaid_tex=ttk.Entry(lableframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"))
		txtpaid_tex.grid(row=2, column=1)


			# Tex

		sub_total=Label(lableframeleft,text="Paid Tex:", font=("arial",12,"bold"),
			padx=2, pady=6)
		sub_total.grid(row=3, column=0,sticky=W)

		self.var_tex=StringVar()

		txtsub_total=ttk.Entry(lableframeleft,textvariable=self.var_tex,width=29,font=("arial",13,"bold"))
		txtsub_total.grid(row=3, column=1)

			# Sub total

		total_cost=Label(lableframeleft,font=("arial",12,"bold"),text="Sub Total:", padx=2, pady=6)
		total_cost.grid(row=4, column=0, sticky=W)

		self.var_sub=StringVar()


		txtsub_total=ttk.Entry(lableframeleft,textvariable=self.var_sub,width=29,font=("arial",13,"bold"))
		txtsub_total.grid(row=4, column=1)


		# Total Cost

		total_cost=Label(lableframeleft,font=("arial",12,"bold"),text="Total Cost:", padx=2, pady=6)
		total_cost.grid(row=5, column=0, sticky=W)

		self.var_total=StringVar()


		txtsub_total=ttk.Entry(lableframeleft,textvariable=self.var_total,width=29,font=("arial",13,"bold"))
		txtsub_total.grid(row=5, column=1)

		

		
		#====================Buttons==================#

		btn_frame=Frame(lableframeleft, bd=2, relief=RIDGE)
		btn_frame.place(x=0, y=200, width=412, height=40)

		
		#add Button

		btnAdd=Button(btn_frame,command=self.add_data,text="Add",font=("arial",12,"bold"),bg="gray",fg="black",width=9)
		btnAdd.grid(row=0,column=0,padx=1)

		
		#Update Button

		btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="gray",fg="black",width=9)
		btnUpdate.grid(row=0,column=1,padx=1)


		#Delete Button

		btnDelete=Button(btn_frame,text="Delete",command=self.mDelete,font=("arial",12,"bold"),bg="gray",fg="black",width=9)
		btnDelete.grid(row=0,column=2,padx=1)



		#Reset Button

		btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial",12,"bold"),bg="gray",fg="black",width=9)
		btnReset.grid(row=0,column=3,padx=1)


			#=====================lable frame search system==================#

		Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Bill Deatils",
		font=("times new roman", 12, "bold"), padx=2)
		Table_Frame.place(x=600, y=70, width=600, height=350)


		scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

		self.room_table=ttk.Treeview(Table_Frame,column=("billno","ref","paidtex","subtotal","totalcost"),
		xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)

		scroll_x.config(command=self.room_table.xview)
		scroll_y.config(command=self.room_table.yview)


		self.room_table.heading("billno", text="Bill Number")
		self.room_table.heading("ref", text="Ref")
		self.room_table.heading("paidtex", text="Paid Tex")
		self.room_table.heading("subtotal", text="Sub Total")
		self.room_table.heading("totalcost", text="Total Cost")
		


		self.room_table["show"]="headings"

		self.room_table.column("billno",width=100)
		self.room_table.column("ref",width=100)
		self.room_table.column("paidtex",width=100)
		self.room_table.column("subtotal",width=100)
		self.room_table.column("totalcost",width=100)
		

		self.room_table.pack(fill=BOTH,expand=1)

		self.room_table.bind("<ButtonRelease-1>", self.get_cuersor)

		self.fetch_data()




	def add_data(self):
		if self.var_ref.get()=="" or self.var_bill.get()=="":
			messagebox.showerror("Error","All fields are requaired", parent=self.root)
		else:
			try:
				conn=mysql.connector.connect(host="localhost",username="root",password="insimam@1234" ,database="moon luxury")
				my_cursor=conn.cursor()
				my_cursor.execute("insert into bill value(%s,%s,%s,%s,%s)",(
																						self.var_bill.get(),
																						self.var_ref.get(),
																						self.var_tex.get(),
																						self.var_sub.get(),
																						self.var_total.get(),
																				))




				conn.commit()
				self.fetch_data()
				conn.close()
				messagebox.showinfo("Success","New Bill Add",parent=self.root)
			except Exception as es:
				messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)





			#=========================fetch data==================================#

	def fetch_data(self):
		conn=mysql.connector.connect(host="localhost",username="root",password="insimam@1234" ,database="moon luxury")
		my_cursor=conn.cursor()
		my_cursor.execute("select * from bill ")
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

		self.var_bill.set(row[0]),
		self.var_ref.set(row[1]),
		self.var_tex.set(row[2]),
		self.var_sub.set(row[3]),
		self.var_total.set(row[4])

		#===========================update fun=============================#


	def update(self):
		if self.var_ref.get()=="":
			messagebox.showerror("Error","Plaece enter the mobile number", parent=self.root)

		else:
			conn=mysql.connector.connect(host="localhost",username="root",password="insimam@1234" ,database="moon luxury")
			my_cursor=conn.cursor()
			my_cursor.execute("update bill set ref=%s,paidtex=%s,subtotal=%s,totalcost=%swhere billno=%s",(
																						self.var_ref.get(),
																						self.var_tex.get(),
																						self.var_sub.get(),
						 																self.var_total.get(),
						 																self.var_bill.get(),
						 																
																						))

			conn.commit()
		
			conn.close()	

			self.fetch_data()


		


	#====================================delite==============================================#

	
	def mDelete(self):
		mDelete=messagebox.askyesno("Moon luxury System","Do you want delete this customer",parent=self.root)
		if mDelete>0:
			conn=mysql.connector.connect(host="localhost",username="root",password="insimam@1234" ,database="moon luxury")
			my_cursor=conn.cursor()
			query="delete from bill where ref=%s"
			value=(self.var_ref.get(),)
			my_cursor.execute(query,value)

		else:
			if not mDelete:
				return

		conn.commit()
		self.fetch_data()
		conn.close()
						
						

	#=====================reset==========================


	def reset(self):
		self.var_ref.set("")
		self.var_bill.set("")
		self.var_tex.set("")
		self.var_sub.set("")
		self.var_total.set("")

		x=random.randint(1000,9999)
		self.var_bill.set(str(x))
		
	













if __name__ == "__main__":
		root=Tk()
		obj= DeatailsRoom(root) 
		root.mainloop()




