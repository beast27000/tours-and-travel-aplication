from tkinter import *
from PIL import Image , ImageTk
from tkinter import ttk
import random
from time import strftime
import mysql.connector
from datetime import datetime
from tkinter import messagebox
import PySimpleGUI as psg

class Roombooking():
    def __init__(self, root ) :
        self.var_ = None
        self.root = root
        self.root.title("Hotel Magement System")
        self.root.geometry("1295x550+230+228")


        #======================variables====================

        self.var_contact=StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomsavailable= StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidax= StringVar()
        self.var_subtotal = StringVar()
        self.var_total = StringVar()

        #======================================== title ==============================================

        lbl_title =  Label(self.root ,text = "ROOMBOOKING DETAILS", font = ("times new roman",18,"bold"),bg = "black",fg ="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # ======================================== logo ==============================================

        img2 = Image.open(r"C:\Users\USER\COMPPUTER HOTEL MANEGMENT FOLDER\images\orchids manali logo .png")  # space betwwen manli  and .png is a must or this does not work
        img2 = img2.resize((230, 160), Image.ANTIALIAS)
        self.Photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.Photoimg2, bd=4, relief=RIDGE) 
        lblimg.place(x=0, y=0, width=230, height=160)

        # ======================== label Frame ===========================
        labelframeleft = LabelFrame(self.root  ,bd=2,relief = RIDGE,text = "ROOMBOOKING DETAILS",font = ("times new roman",12,"bold" ),padx = 2)
        labelframeleft.place(x=5,y=50,width=425,height =490)

        #==========================fetch data==============================

        btnFetchData =  Button(labelframeleft,command=self.fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width = 8)
        btnFetchData.place(x=347,y=4)


        #=========================bill button==============================

        bill=  Button(labelframeleft,text="Generate Bill",command=self.total,font=("arial",11,"bold"),bg="black",fg="gold",width = 10)
        bill.grid(row=10,column=0,padx=1,sticky=W)

        #=========================Payments==============================

        #========================btns========================
        btns_frame = Frame(labelframeleft,bd = 2 ,relief = RIDGE)
        btns_frame.place(x=0,y=400,width =206, height =37)

        ADD =  Button(btns_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width = 10)
        ADD.grid(row=0,column=0,padx=1)

        bdelete = Button(btns_frame,text="Delete", command =self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width = 10)
        bdelete.grid(row=0,column=1,padx=1)


        games = Button(btns_frame,text="games", font=("arial",11,"bold"),bg="black",fg="gold",width = 10)










        # ==========================labels and entrys=============================
        #custref

        lbl_cust_contact= Label(labelframeleft,text ="Contact",font=("arial",12,"bold"),padx= 2, pady=6)
        lbl_cust_contact.grid(row = 0,column=0,sticky=W )
        entry_contact = Entry(labelframeleft,textvariable=self.var_contact,width=20,font =("arial",12,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W )

        #Check in date

        check_in_date = Label(labelframeleft,text ="Check In",font=("arial",12,"bold"),padx= 2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheckin=ttk.Entry(labelframeleft,textvariable=self.var_checkin , width=26, font=("arial", 12, "bold"))
        txtcheckin.grid(row=1, column=1)


        #Check out date

        check_out_date = Label(labelframeleft,text ="Check out ",font=("arial",12,"bold"),padx= 2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)
        txtcheckout=ttk.Entry(labelframeleft,textvariable=self.var_checkout , width=26, font=("arial", 12, "bold"))
        txtcheckout.grid(row=2, column=1)

        #room type
        room_type= Label(labelframeleft,text="Room Type", font=("arial", 12, "bold"), padx=2, pady=6)
        room_type.grid(row=3, column=0,sticky = W )
        rooom_comobobox = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype ,font=("arial", 12, "bold"),width =26)
        rooom_comobobox ["values"]=("single","double","luxury")
        rooom_comobobox .grid(row=3,column=1)
        rooom_comobobox .current(0)


        #Available room

        roomsavilable= Label(labelframeleft, text="Rooms Available", font=("arial", 12, "bold"), padx=2, pady=6)
        roomsavilable.grid(row=4, column=0, sticky=W)
        available_combobox=ttk.Combobox(labelframeleft, width=26,textvariable=self.var_roomsavailable , font=("arial", 12, "bold"))
        available_combobox.grid(row=4, column=1)
        available_combobox ["values"]=("1001","1002","1003","1004","1005","1006","1007","1008","1009",)

        available_combobox .grid(row=4,column=1)
        available_combobox.current(0)





        #Meal
        lblMeal = Label(labelframeleft, text="Meal", font=("arial", 12, "bold"), padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        Meal=ttk.Combobox(labelframeleft, width=26,textvariable=self.var_meal , font=("arial", 12, "bold"))
        Meal.grid(row=5, column=1)
        Meal ["values"]=("Breakfast","Lunch","Dinner")
        Meal .grid(row=5,column=1)
        Meal.current(0)




        #no of Days
        lbl_no_of_days = Label(labelframeleft, text="No of Days", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_no_of_days.grid(row=6, column=0, sticky=W)
        txt_no_of_days=ttk.Entry(labelframeleft,textvariable=self.var_noofdays , width=26, font=("arial", 12, "bold"),state = "readonly")
        txt_no_of_days.grid(row=6, column=1)


        #paid tax
        lbl_paid_tax = Label(labelframeleft, text="Paid Tax", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_paid_tax.grid(row=7, column=0, sticky=W)
        txt_tax=ttk.Entry(labelframeleft, width=26, textvariable= self.var_paidax,font=("arial", 12, "bold"),state = "readonly")
        txt_tax.grid(row=7, column=1)

        #subtotal
        lbl_subtotal= Label(labelframeleft, text="Sub Total", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_subtotal.grid(row=8, column=0, sticky=W)
        txt_subtotal=ttk.Entry(labelframeleft, width=26,textvariable=self.var_subtotal , font=("arial", 12, "bold"),state = "readonly")
        txt_subtotal.grid(row=8, column=1)

        #total cost
        lbl_cost= Label(labelframeleft, text="Total Cost ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cost.grid(row=9, column=0, sticky=W)
        txt_cost=ttk.Entry(labelframeleft, width=26, textvariable=self.var_total , font=("arial", 12, "bold"),state = "readonly")
        txt_cost.grid(row=9, column=1)


        #==============================rightside image==============================

        img3 = Image.open(r"C:\Users\USER\COMPPUTER HOTEL MANEGMENT FOLDER\images\bed.jpg")  # space betwwen manli  and .png is a must or this does not work
        img3 = img3.resize((530,270), Image.ANTIALIAS)
        self.Photoimg3 = ImageTk.PhotoImage(img3)
        lblimg = Label(self.root, image=self.Photoimg3, bd=4, relief=RIDGE)
        lblimg.place(x=760, y=55, width=530, height=270)

        # =======================table_frame======================================
        table_frame = LabelFrame(self.root, relief=RIDGE, text="Veiw details and search", font=("arial", 12, "bold"),
                                 padx=2)
        table_frame.place(x=435, y=280, width=860, height=260)

        lbl_search = Label(table_frame, text="search by ", font=("arial", 12, "bold"), bg="red", fg="white")
        lbl_search.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=24,
                                    state="read only")
        combo_search["values"] = ("contact", "bus")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        table_search = ttk.Entry(table_frame, textvariable=self.txt_search, font=("arial", 11, "bold"), width=24)
        table_search.grid(row=0, column=2, padx=2)

        btnsearch = Button(table_frame, text="Search",  font=("arial", 12, "bold"), bg="black",
                           fg="gold", width=10)
        btnsearch.grid(row=0, column=3, padx=1)

        btnshowall = Button(table_frame, text="ShowAll",  font=("arial", 12, "bold"),
                            bg="black", fg="gold", width=10)
        btnshowall.grid(row=0, column=4, padx=1)

        #==========================show data table==========================
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=180)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)


        self.room_table=ttk.Treeview(details_table,column=("contact","Check_In","Check_out","Room_Type","Rooms_Available","Meal","No_of_Days"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)


        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("Check_In", text="Check In")
        self.room_table.heading("Check_out", text="Check out")
        self.room_table.heading("Room_Type", text="Room Type")
        self.room_table.heading("Rooms_Available", text="Rooms Available")
        self.room_table.heading("Meal", text="Meal")
        self.room_table.heading("No_of_Days", text="No of Days")


        self.room_table["show"]="headings"

        self.room_table.column("contact",width=100)
        self.room_table.column("Check_In", width=100)
        self.room_table.column("Check_out", width=100)
        self.room_table.column("Room_Type", width=100)
        self.room_table.column("Rooms_Available", width=100)
        self.room_table.column("Meal", width=100)
        self.room_table.column("No_of_Days", width=100)
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cuersor)
        self.fetch_data()






    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("error","please enter contact number",parent=self.root)
        else:

            conn = mysql.connector.connect(host="localhost", username="vishvvesh nagappan", password="Music*1234",database="hotel_management")
            my_courser = conn.cursor()
            query = ("select Name from customer where Mobile =%s")
            value = (self.var_contact.get(),)
            my_courser.execute(query, value)
            row = my_courser.fetchone()

            if row == None:
                messagebox.showerror("error", "this number is not found", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                showDataframe.place(x=450, y=55, width=300, height=180)

                lblName = Label(showDataframe, text="Name:", font=("arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl.place(x=90, y=0)

                #========================reference number========================


                conn = mysql.connector.connect(host="localhost", username="vishvvesh nagappan", password="Music*1234", database="hotel_management")
                my_courser = conn.cursor()
                query = ("select Ref from customer where Mobile =%s")
                value = (self.var_contact.get(),)
                my_courser.execute(query, value)
                row = my_courser.fetchone()


                lblref = Label(showDataframe, text="refrence no: ", font=("arial", 12, "bold"))
                lblref.place(x=0, y=30)

                lbl3 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl3.place(x=100, y=30)


                #=======gender=============
                conn = mysql.connector.connect(host="localhost", username="vishvvesh nagappan", password="Music*1234", database="hotel_management")
                my_courser = conn.cursor()
                query = ("select Gender from customer where Mobile =%s")
                value = (self.var_contact.get(),)
                my_courser.execute(query, value)
                row = my_courser.fetchone()


                lablgender = Label(showDataframe, text="gender:", font=("arial", 12, "bold"))
                lablgender.place(x=0, y=60)

                lbl2 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl2.place(x=90, y=60)


                #===============email====================

                conn = mysql.connector.connect(host="localhost", username="vishvvesh nagappan", password="Music*1234", database="hotel_management")
                my_courser = conn.cursor()
                query = ("select Email from customer where Mobile =%s")
                value = (self.var_contact.get(),)
                my_courser.execute(query, value)
                row = my_courser.fetchone()


                lablemail = Label(showDataframe, text="Email:", font=("arial", 12, "bold"))
                lablemail.place(x=0, y=90)

                lbl3 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl3.place(x=90, y=90)



                #=========================nationality============================

                conn = mysql.connector.connect(host="localhost", username="vishvvesh nagappan", password="Music*1234", database="hotel_management")
                my_courser = conn.cursor()
                query = ("select Nationality from customer where Mobile =%s")
                value = (self.var_contact.get(),)
                my_courser.execute(query, value)
                row = my_courser.fetchone()


                lblnationality = Label(showDataframe, text="Nationality:", font=("arial", 12, "bold"))
                lblnationality.place(x=0, y=120)

                lbl4 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl4.place(x=90, y=120)


                #========================address====================


                conn = mysql.connector.connect(host="localhost", username="vishvvesh nagappan", password="Music*1234", database="hotel_management")
                my_courser = conn.cursor()
                query = ("select Gender from customer where Mobile =%s")
                value = (self.var_contact.get(),)
                my_courser.execute(query, value)
                row = my_courser.fetchone()

                labladdress = Label(showDataframe, text="Address:", font=("arial", 12, "bold"))
                labladdress.place(x=0, y=150)

                lbl5 = Label(showDataframe, text=row, font=("arial", 12, "bold"))
                lbl5.place(x=90, y=150)




#===========================adding data===============================
    def add_data(self):
        if self.var_contact.get=="" or self.var_checkin.get()=="" :
            messagebox.showerror("error","all feild are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username= "vishvvesh nagappan",password="Music*1234",database="hotel_management")
                my_courser =conn.cursor()
                my_courser.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s)",(

                                                                                        self.var_contact.get(),
                                                                                        self.var_checkin.get(),
                                                                                        self.var_checkout.get(),
                                                                                        self.var_roomtype.get(),
                                                                                        self.var_roomsavailable.get(),
                                                                                        self.var_meal.get(),
                                                                                        self.var_noofdays.get()





                                                                                        ))


                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Your room has been booked", parent=self.root )
            except Exception as es:
                messagebox.showwarning("Warning",f"Sorry this room has alredy been booked:            {str(es)}",parent=self.root )
                #  messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root )
                # ===============================fetch data=================================

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username= "vishvvesh nagappan",password="Music*1234",database="hotel_management")
        my_courser=conn.cursor()
        my_courser.execute("select * from room")
        rows=my_courser.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #===================gwt courser============================

    def get_cuersor(self,events=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row =content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_roomsavailable.set(row[4]),
        self.var_meal.set(row[5]),
        self.var_noofdays.set(row[6])
    #==========================update function==============================


    def mupdate(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","please enter mobile number",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username= "vishvvesh nagappan",password="Music*1234",database="hotel_management")
                my_courser=conn.cursor()
                my_courser.execute("UPDATE room set Check In=%s,Check out=%s,Room Type=%s,Rooms Available=%s,Meal=%s,No of Days=%s where Contact=%s ",(

                                                                                                                                                            self.var_checkin.get(),
                                                                                                                                                            self.var_checkout.get(),
                                                                                                                                                            self.var_roomtype.get(),
                                                                                                                                                            self.var_roomsavailable.get(),
                                                                                                                                                            self.var_meal.get(),
                                                                                                                                                            self.var_noofdays.get(),
                                                                                                                                                            self.var_contact.get()
                                                                                                                                                            ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","room has been updated ", parent=self.root )
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root )



    #=====================================delete============================

    def mDelete(self):
        mDelete=messagebox.askyesno("hotel management system ","do you want to DELETE ",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username= "vishvvesh nagappan",password="Music*1234",database="hotel_management")
            my_cursor=conn.cursor()
            query="delete from room where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)

        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def total(self):
        indate = self.var_checkin.get()
        outdate = self.var_checkout.get()
        indate = datetime.strptime(indate, "%d/%m/%y")
        outdate = datetime.strptime(outdate, "%d/%m/%y")
        self.var_noofdays.set(abs(outdate - indate).days)

     #=====================luxary bedroom===============================
        if (self.var_meal.get()=="Breafast" and self.var_roomtype.get()=="luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)


        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="luxury"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        #===============================single bedroom========================
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="single"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

            #=========================================doublebedroom==========================================

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)



        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="double"):
            q1=float(300)
            q2=float(700)
            q3=float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)












if __name__ == '__main__':
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()