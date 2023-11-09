from tkinter import*
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox

class Cust_win:
	
	def __init__(self,root):
		self.root=root
		self.root.title("Hotel Managment System")
		self.root.geometry("1295x550+230+220")


		#==================variable===============#

		self.var_ref=StringVar()
		x=random.randint(1000,9999)
		self.var_ref.set(str(x))

		self.var_cust_name=StringVar()
		self.var_father=StringVar()
		self.var_gender=StringVar()
		self.var_post=StringVar()
		self.var_mobile=StringVar()
		self.var_email=StringVar()
		self.var_nationality=StringVar()
		self.var_address=StringVar()
		self.var_id_proof=StringVar()
		self.var_id_number=StringVar()
		
		
	


		#==================Titel===================#

		lb1_tilte=Label(self.root,text="ADD CUSTOMER DETAILS", font=("times new roman",18,"bold"),
			bg="gray",fg="blue",bd=4,relief=RIDGE)
		lb1_tilte.place(x=0, y=20, width=1295, height=50)


		#=================LableFrame================#

		lableframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details",
		 font=("times new roman", 12, "bold"), padx=2)
		lableframeleft.place(x=5, y=70, width=425, height=490)


		#==================Lables and Entrys=========#

		# custref

		lb1_cust_ref=Label(lableframeleft,text="Customer Ref", font=("arial",12,"bold"),
			padx=2, pady=6)
		lb1_cust_ref.grid(row=0, column=0,sticky=W)

		enty_ref=ttk.Entry(lableframeleft,textvariable=self.var_ref,width=29,font=("arial",13,"bold"),state="readonly")
		enty_ref.grid(row=0, column=1)


		# cust name

		cname=Label(lableframeleft,text="Customer Name:", font=("arial",12,"bold"),
			padx=2, pady=6)
		cname.grid(row=1, column=0,sticky=W)

		txtcname=ttk.Entry(lableframeleft,textvariable=self.var_cust_name,width=29,font=("arial",13,"bold"))
		txtcname.grid(row=1, column=1)


		# father name

		lb1fname=Label(lableframeleft,text="Father Name:", font=("arial",12,"bold"),
			padx=2, pady=6)
		lb1fname.grid(row=2, column=0,sticky=W)

		txtfname=ttk.Entry(lableframeleft,textvariable=self.var_father,width=29,font=("arial",13,"bold"))
		txtfname.grid(row=2, column=1)



		# gender combobox

		Label_gender=Label(lableframeleft,font=("arial",12,"bold"),text="Gender:", padx=2, pady=6)
		Label_gender.grid(row=3, column=0, sticky=W)

		combo_gender=ttk.Combobox(lableframeleft,textvariable=self.var_gender, font=("arial",12,"bold"), width=27,
		 state="readonly")
		combo_gender["value"]=("Male","Female","Other")
		combo_gender.current(0)
		combo_gender.grid(row =3, column=1)


		#postcode

		lb1postcode=Label(lableframeleft,text="PostCode:", font=("arial",12,"bold"),
			padx=2, pady=6)
		lb1postcode.grid(row=4, column=0,sticky=W)

		txtpostcode=ttk.Entry(lableframeleft,textvariable=self.var_post,width=29,font=("arial",13,"bold"))
		txtpostcode.grid(row=4, column=1)


		#mobile number

		lb1mobilenumber=Label(lableframeleft,text="Mobile No:", font=("arial",12,"bold"),
			padx=2, pady=6)
		lb1mobilenumber.grid(row=5, column=0,sticky=W)

		txtmobilenumber=ttk.Entry(lableframeleft,textvariable=self.var_mobile,width=29,font=("arial",13,"bold"))
		txtmobilenumber.grid(row=5, column=1)

		#email

		lb1email=Label(lableframeleft,text="Email:", font=("arial",12,"bold"),
			padx=2, pady=6)
		lb1email.grid(row=6, column=0,sticky=W)

		txtemail=ttk.Entry(lableframeleft,textvariable=self.var_email,width=29,font=("arial",13,"bold"))
		txtemail.grid(row=6, column=1)


		# nationality

		lb1nationality=Label(lableframeleft,font=("arial",12,"bold"), text="Nationality:", 
			padx=2, pady=6)
		lb1nationality.grid(row=7, column=0,sticky=W)

		combo_nationality=ttk.Combobox(lableframeleft,textvariable=self.var_nationality, font=("arial",12,"bold"), width=27, 
			state="readonly")
		combo_nationality["value"]=("Sri lanka","India","American","Britist")
		combo_nationality.current(0)
		combo_nationality.grid(row =7, column=1)


		# idproof type combobox

		lb1idproof=Label(lableframeleft,text="Id Proof Type:", font=("arial",12,"bold"),
			padx=2, pady=6)
		lb1idproof.grid(row=8, column=0,sticky=W)

		combo_idproof=ttk.Combobox(lableframeleft,textvariable=self.var_id_proof, font=("arial",12,"bold"), width=27, 
			state="readonly")
		combo_idproof["value"]=("NICCard","DrivingLicence","Passport")
		combo_idproof.current(0)
		combo_idproof.grid(row =8, column=1)


		#id number

		lb1idnumber=Label(lableframeleft,text="Id Number:", font=("arial",12,"bold"),
			padx=2, pady=6)
		lb1idnumber.grid(row=9, column=0,sticky=W)

		txtidnumber=ttk.Entry(lableframeleft,textvariable=self.var_id_number,width=29,font=("arial",13,"bold"))
		txtidnumber.grid(row=9, column=1)


		#address

		lb1address=Label(lableframeleft,text="Address:", font=("arial",12,"bold"),
			padx=2, pady=6)
		lb1address.grid(row=10, column=0,sticky=W)

		txtaddress=ttk.Entry(lableframeleft,textvariable=self.var_address,width=29,font=("arial",13,"bold"))
		txtaddress.grid(row=10, column=1)


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
		Table_frame.place(x=435, y=70, width=860, height=490)

		lb1search=Label(Table_frame ,text="search By:", font=("arial",12,"bold"),
			bg="red",fg="white")
		lb1search.grid(row=0, column=0,sticky=W, padx=2)


		self.search_var=StringVar()
		combo_search=ttk.Combobox(Table_frame,textvariable=self.search_var, font=("arial",12,"bold"), width=27, 
			state="readonly")
		combo_search["value"]=("Mobile","Ref")
		combo_search.current(0)
		combo_search.grid(row =0, column=1, padx=2)

		self.txt_search=StringVar()
		txtsearch=ttk.Entry(Table_frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
		txtsearch.grid(row=0, column=2, padx=2)


		btnsearch=Button(Table_frame,text="Search",font=("arial",12,"bold"),bg="gray",fg="black",width=9)
		btnsearch.grid(row=0,column=3,padx=1)

		btnshowall=Button(Table_frame,text="Show All",font=("arial",12,"bold"),bg="gray",fg="black",width=9)
		btnshowall.grid(row=0,column=4,padx=1)



		#===========================Show Data Table========================#

		Details_table=Frame(Table_frame, bd=2, relief=RIDGE)
		Details_table.place(x=0, y=50, width=860, height=350)

		scroll_x=ttk.Scrollbar(Details_table,orient=HORIZONTAL)
		scroll_y=ttk.Scrollbar(Details_table,orient=VERTICAL)

		self.cust_details_table=ttk.Treeview(Details_table,column=("ref","name","father","gender",
			"post","mobile","email","nationality","idproof","idnumber", "address"),
			xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT,fill=Y)

		scroll_x.config(command=self.cust_details_table.xview)
		scroll_y.config(command=self.cust_details_table.yview)

		self.cust_details_table.heading("ref", text="Refer No")
		self.cust_details_table.heading("name", text="Name")
		self.cust_details_table.heading("father", text="Father Name")
		self.cust_details_table.heading("gender", text="Gender")
		self.cust_details_table.heading("post", text="PostCode")
		self.cust_details_table.heading("mobile", text="Mobile")
		self.cust_details_table.heading("email", text="Email")
		self.cust_details_table.heading("nationality", text="Nationality")
		self.cust_details_table.heading("idproof", text="Id Proof")
		self.cust_details_table.heading("idnumber", text="Id Name")
		self.cust_details_table.heading("address", text="Address")


		self.cust_details_table["show"]="headings"

		self.cust_details_table.column("ref",width=100)
		self.cust_details_table.column("name",width=100)
		self.cust_details_table.column("father",width=100)
		self.cust_details_table.column("gender",width=100)
		self.cust_details_table.column("post",width=100)
		self.cust_details_table.column("mobile",width=100)
		self.cust_details_table.column("email",width=100)
		self.cust_details_table.column("nationality",width=100)
		self.cust_details_table.column("idproof",width=100)
		self.cust_details_table.column("idnumber",width=100)
		self.cust_details_table.column("address",width=100)

		self.cust_details_table.pack(fill=BOTH,expand=1)
		self.cust_details_table.bind("<ButtonRelease-1>", self.get_cuersor)
		self.fetch_data()


	def add_data(self):
		if self.var_mobile.get()=="" or self.var_father.get()=="":
			messagebox.showerror("Error","All fields are requaired", parent=self.root)
		else:
			try:
				conn=mysql.connector.connect(host="localhost",username="root",password="insimam@1234" ,database="moon luxury")
				my_cursor=conn.cursor()
				my_cursor.execute("insert into customer value(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
																						self.var_ref.get(), 
																						self.var_cust_name.get(),
																						self.var_father.get(),
																						self.var_gender.get(),
						 																self.var_post.get(),
						 																self.var_mobile.get(),
						 																self.var_email.get(), 
																						self.var_nationality.get(),
																						self.var_id_proof.get(), 
																						self.var_id_number.get(),
																						self.var_address.get()
																					))


				conn.commit()
				self.fetch_data()
				conn.close()


			except Exception as es:
				messagebox.showwarning("Warning",f"Some thing went wrong:{str(es)}",parent=self.root)

	def fetch_data(self):
		conn=mysql.connector.connect(host="localhost",username="root",password="insimam@1234" ,database="moon luxury")
		my_cursor=conn.cursor()
		my_cursor.execute("select * from customer")
		rows=my_cursor.fetchall()
		if len(rows)!=0:
			self.cust_details_table.delete(*self.cust_details_table.get_children())
			for i in rows:
				self.cust_details_table.insert("",END, values=i)
			conn.commit()
		conn.close()


	def get_cuersor(self,event=""):
		cusrsor_row=self.cust_details_table.focus()
		conntent=self.cust_details_table.item(cusrsor_row)
		row=conntent["values"]

		self.var_ref.set(row[0]),
		self.var_cust_name.set(row[1]),
		self.var_father.set(row[2]),
		self.var_gender.set(row[3]),
		self.var_post.set(row[4]),
		self.var_mobile.set(row[5]),
		self.var_email.set(row[6]),
		self.var_nationality.set(row[7]),
		self.var_id_proof.set(row[8]),
		self.var_id_number.set(row[9]),
		self.var_address.set(row[10]),

	def update(self):
		if self.var_mobile.get()=="":
			messagebox.showerror("Error","Plaece enter the mobile number", parent=self.root)

		else:
			conn=mysql.connector.connect(host="localhost",username="root",password="insimam@1234" ,database="moon luxury")
			my_cursor=conn.cursor()
			my_cursor.execute("update customer set Name=%s,Father=%s,Gender=%s,PostCode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber=%s,Address=%s where Ref=%s",(



																					
																						self.var_cust_name.get(),
																						self.var_father.get(),
																						self.var_gender.get(),
						 																self.var_post.get(),
						 																self.var_mobile.get(),
						 																self.var_email.get(), 
																						self.var_nationality.get(),
																						self.var_id_proof.get(), 
																						self.var_id_number.get(),
																						self.var_address.get(),
																						self.var_ref.get() 
																						))

			conn.commit()
			self.fetch_data()
			conn.close()

	def mDelete(self):
		mDelete=messagebox.askyesno("Moon luxury System","Do you want delete this customer",parent=self.root)
		if mDelete>0:
			conn=mysql.connector.connect(host="localhost",username="root",password="insimam@1234" ,database="moon luxury")
			my_cursor=conn.cursor()
			query="delete from customer where Ref=%s"
			value=(self.var_ref.get(),)
			my_cursor.execute(query,value)

		else:
			if not mDelete:
				return

		conn.commit()
		self.fetch_data()
		conn.close()

	def reset(self):


		#==self.var_ref.set(""),
		self.var_cust_name.set(""),
		self.var_father.set(""),
		#==self.var_gender.set(""),
		self.var_post.set(""),
		self.var_mobile.set(""),
		self.var_email.set(""),
		#==self.var_nationality.set(""),
		#==self.var_id_proof.set(""),
		self.var_id_number.set(""),
		self.var_address.set("")
		 
		x=random.randint(1000,9999)
		self.var_ref.set(str(x))



	















if __name__ == "__main__":
	root=Tk()
	obj=Cust_win(root) 
	root.mainloop()