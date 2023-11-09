from tkinter import*
from tkinter import ttk
import tkinter as tk
import mysql.connector
import random
from tkinter import messagebox

class developer1:
	
	def __init__(self,root):
		self.root=root
		self.root.title("Hotel Managment System")
		self.root.geometry("1295x550+230+220")

	def home_page():
		home_frame = tk.Frame(main_frame)
		lb = tk.Label(home_frame, text = "home page\n\nPage1:", font = ("Bold", 30))
		lb.pack()
		home_frame.pack(pady = 20)

if __name__ == "__main__":
		root=Tk()
		obj= developer1(root) 
		root.mainloop()