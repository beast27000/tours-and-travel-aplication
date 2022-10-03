from tkinter import *
from PIL import Image , ImageTk
from tkinter import ttk
import random
from time import strftime
import mysql.connector
from datetime import datetime
from tkinter import messagebox

class busmanagement():
    def __init__(self, root ) :
        self.var_ = None
        self.root = root
        self.root.title("Hotel Magement System")
        self.root.geometry("1295x550+230+228")


        #======================variables====================

        self.var_contact=StringVar()
        self.var_boardingpoint = StringVar()
        self.var_daystarveled = StringVar()
        self.var_bustype = StringVar()
        self.var_arrivaltime= StringVar()
        self.var_departuretime = StringVar()
        self.var_seatno = StringVar()
        self.var_paidax= StringVar()
        self.var_subtotal = StringVar()
        self.var_total = StringVar()

        #======================================== title ==============================================

        lbl_title =  Label(self.root ,text = "BUS RESERVATION DETAILS", font = ("times new roman",18,"bold"),bg = "black",fg ="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # ======================================== logo ==============================================

        img2 = Image.open(r"C:\Users\USER\COMPPUTER HOTEL MANEGMENT FOLDER\images\orchids manali logo .png")  # space betwwen manli  and .png is a must or this does not work
        img2 = img2.resize((230, 160), Image.ANTIALIAS)
        self.Photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.Photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=160)

        # ======================== label Frame ===========================
        labelframeleft = LabelFrame(self.root  ,bd=2,relief = RIDGE,text = "BUS RESERVATION SYSTEM",font = ("times new roman",12,"bold" ),padx = 2)
        labelframeleft.place(x=5,y=50,width=425,height =490)

        #==========================fetch data==============================

        btnFetchData =  Button(labelframeleft,command=self.fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width = 8)
        btnFetchData.place(x=347,y=4)


        #=========================bill button==============================

        bill=  Button(labelframeleft,text="Bill",command =self.total,font=("arial",11,"bold"),bg="black",fg="gold",width = 10)
        bill.grid(row=10,column=0,padx=1,sticky=W)

        #==================payments==========================================

        #========================btns========================
        btns_frame = Frame(labelframeleft,bd = 2 ,relief = RIDGE)
        btns_frame.place(x=0,y=400,width =206, height =37)

        ADD =  Button(btns_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width = 10)
        ADD.grid(row=0,column=0,padx=1)

        bdelete = Button(btns_frame,text="Delete", command =self.mDelete,font=("arial",11,"bold"),bg="black",fg="gold",width = 10)
        bdelete.grid(row=0,column=1,padx=1)




        # ==========================labels and entrys=============================
        #custref

        lbl_cust_contact= Label(labelframeleft,text ="Contact",font=("arial",12,"bold"),padx= 2, pady=6)
        lbl_cust_contact.grid(row = 0,column=0,sticky=W )
        entry_contact = Entry(labelframeleft,textvariable=self.var_contact,width=20,font =("arial",12,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W )

        # Boarding Point

        bording_point= Label(labelframeleft,text="Boarding_Point", font=("arial", 12, "bold"), padx=2, pady=6)
        bording_point.grid(row=1, column=0,sticky = W )
        bording_point_comobobox = ttk.Combobox(labelframeleft,textvariable=self.var_boardingpoint,font=("arial", 12, "bold"),width =26)
        bording_point_comobobox ["values"]=("Indira Gandhi International Airport","New delhi bus stand","Old  Delhi bus stand")
        bording_point_comobobox .grid(row=1,column=1)
        bording_point_comobobox .current(0)




        #Bus Type
        bus_type= Label(labelframeleft,text="bus_type", font=("arial", 12, "bold"), padx=2, pady=6)
        bus_type.grid(row=2, column=0,sticky = W )
        bus_type_combobox = ttk.Combobox(labelframeleft, textvariable=self.var_bustype ,font=("arial", 12, "bold"),width =26)
        bus_type_combobox ["values"]=("AC","Non-AC")
        bus_type_combobox .grid(row=2,column=1)
        bus_type_combobox .current(0)


        #seat no

        seatno= Label(labelframeleft,text="seatno", font=("arial", 12, "bold"), padx=2, pady=6)
        seatno.grid(row=3, column=0,sticky = W )
        seatno_comobobox = ttk.Combobox(labelframeleft, textvariable=self.var_seatno ,font=("arial", 12, "bold"),width =26)
        seatno_comobobox ["values"]=("1","2","3","4","5","6","7","8","9","10","11","12")
        seatno_comobobox .grid(row=3,column=1)
        seatno_comobobox .current(0)


        #Departure Time
        lblDeparturetime = Label(labelframeleft, text="departure_time", font=("arial", 12, "bold"), padx=2, pady=6)
        lblDeparturetime.grid(row=4, column=0, sticky=W)
        totaltime=ttk.Entry(labelframeleft, width=26,textvariable=self.var_departuretime , font=("arial", 12, "bold"))
        totaltime.grid(row=4, column=1)


        #arrival time


        seattype = Label(labelframeleft, text="Arrival Time", font=("arial", 12, "bold"), padx=2, pady=6)
        seattype.grid(row=5, column=0, sticky=W)
        txt_avialble=ttk.Entry(labelframeleft, width=26,textvariable=self.var_arrivaltime, font=("arial", 12, "bold"))
        txt_avialble.grid(row=5, column=1)

        # total no of days of travel
        days_travelled = Label(labelframeleft, text="days_traveled", font=("arial", 12, "bold"), padx=2, pady=6)
        days_travelled.grid(row=6, column=0, sticky=W)
        txtdays_travelled = ttk.Entry(labelframeleft, textvariable=self.var_daystarveled, width=26,font=("arial", 12, "bold"),state = "readonly")
        txtdays_travelled.grid(row=6, column=1)

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

        img3 = Image.open(r"C:\Users\USER\COMPPUTER HOTEL MANEGMENT FOLDER\images\bus.jpg")  # space betwwen manli  and .png is a must or this does not work
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
        combo_search["values"] = ("contact", "room")
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


        self.bus_table=ttk.Treeview(details_table,column=("contact","Boarding_Point","Bus_Type","seat_no","Departure_Time","arrival_time","Daystravelled","paidtax","subtotal","total"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.bus_table.xview)
        scroll_y.config(command=self.bus_table.yview)


        self.bus_table.heading("contact",text="Contact")
        self.bus_table.heading("Boarding_Point", text="Boarding Point")
        self.bus_table.heading("Bus_Type", text="Bus Type")
        self.bus_table.heading("seat_no", text="Seat_No")
        self.bus_table.heading("Departure_Time", text="Departure Time")
        self.bus_table.heading("arrival_time", text="arrival time")
        self.bus_table.heading("Daystravelled", text="Days tavelled")
        self.bus_table.heading("paidtax", text="paid tax")
        self.bus_table.heading("subtotal", text="sub total")
        self.bus_table.heading("total", text="total")


        self.bus_table["show"]="headings"

        self.bus_table.column("contact",width=100)
        self.bus_table.column("Boarding_Point", width=100)
        self.bus_table.column("Bus_Type", width=100)
        self.bus_table.column("seat_no", width=100)
        self.bus_table.column("Departure_Time", width=100)
        self.bus_table.column("arrival_time", width=100)
        self.bus_table.column("Departure_Time", width=100)
        self.bus_table.column("paidtax", width=100)
        self.bus_table.column("subtotal", width=100)
        self.bus_table.column("total", width=100)

        self.bus_table.pack(fill=BOTH, expand=1)
        self.bus_table.bind("<ButtonRelease-1>", self.get_cuersor)
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
        if self.var_contact.get=="" or self.var_boardingpoint.get()=="" :
            messagebox.showerror("error","all feild are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username= "vishvvesh nagappan",password="Music*1234",database="hotel_management")
                my_courser =conn.cursor()
                my_courser.execute("insert into bus values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                        self.var_contact.get(),
                                                                                        self.var_boardingpoint.get(),
                                                                                        self.var_bustype.get(),
                                                                                        self.var_seatno.get(),
                                                                                        self.var_departuretime.get(),
                                                                                        self.var_arrivaltime.get(),
                                                                                        self.var_daystarveled.get(),
                                                                                        self.var_paidax.get(),
                                                                                        self.var_subtotal.get(),
                                                                                        self.var_total.get()


                                                                                        ))


                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Your bus has been booked", parent=self.root )
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root )

                # ===============================fetch data=================================

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username= "vishvvesh nagappan",password="Music*1234",database="hotel_management")
        my_courser=conn.cursor()
        my_courser.execute("select * from bus")
        rows=my_courser.fetchall()
        if len(rows)!=0:
            self.bus_table.delete(*self.bus_table.get_children())
            for i in rows:
                self.bus_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #===================gwt courser============================

    def get_cuersor(self,events=""):
        cursor_row=self.bus_table.focus()
        content=self.bus_table.item(cursor_row)
        row =content["values"]

        self.var_contact.set(row[0]),
        self.var_boardingpoint.set(row[1]),
        self.var_bustype.set(row[2]),
        self.var_seatno.set(row[3]),
        self.var_departuretime.set(row[4]),
        self.var_arrivaltime.set(row[5]),
        self.var_daystarveled.set(row[6]),
        self.var_paidax.set(row[7]),
        self.var_subtotal.set(row[8]),
        self.var_total.set(row[9])

    #==========================update function==============================


    def mupdate(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","please enter mobile number",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username= "vishvvesh nagappan",password="Music*1234",database="hotel_management")
                my_courser=conn.cursor()
                my_courser.execute("UPDATE room set Check In=%s,Check out=%s,Room Type=%s,Rooms Available=%s,Meal=%s,No of Days=%s where Contact=%s ",(

                                                                                                                                                            self.var_boardingpoint.get(),
                                                                                                                                                            self.var_daystarveled.get(),
                                                                                                                                                            self.var_bustype.get(),
                                                                                                                                                            self.var_arrivaltime.get(),
                                                                                                                                                            self.var_total.get(),
                                                                                                                                                            self.var_seatno.get(),
                                                                                                                                                            self.var_contact.get()
                                                                                                                                                            ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","bus has been updated ", parent=self.root )
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root )



    #=====================================delete============================

    def mDelete(self):
        mDelete=messagebox.askyesno("hotel management system ","do you want to DELETE ",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username= "vishvvesh nagappan",password="Music*1234",database="hotel_management")
            my_cursor=conn.cursor()
            query="delete from bus where Contact=%s"
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)

        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
#==========================================vishvvesh's game==========================

    def total(self):
        indate = self.var_departuretime.get()
        outdate = self.var_arrivaltime.get()
        indate = datetime.strptime(indate, "%d/%m/%y")
        outdate = datetime.strptime(outdate, "%d/%m/%y")
        self.var_daystarveled.set(abs(outdate - indate).days)

        if (self.var_boardingpoint.get() == "Indira Gandhi International Airport" and self.var_bustype.get() == "AC"):
            q1=float(50)
            q2=float(500)
            q3=float(self.var_daystarveled.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_boardingpoint.get() == "Indira Gandhi International Airport" and self.var_bustype.get() == "Non-AC"):
            q1=float(50)
            q2=float(400)
            q3=float(self.var_daystarveled.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_boardingpoint.get() == "New delhi bus stand" and self.var_bustype.get() == "AC"):
            q1=float(50)
            q2=float(400)
            q3=float(self.var_daystarveled.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_boardingpoint.get() == "New delhi bus stand" and self.var_bustype.get() == "NON-AC"):
            q1=float(50)
            q2=float(400)
            q3=float(self.var_daystarveled.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_boardingpoint.get() == "Old  Delhi bus stand" and self.var_bustype.get() == "AC"):
            q1=float(50)
            q2=float(400)
            q3=float(self.var_daystarveled.get())
            q4=float(q1+q2)
            q5=float(q3*q4)
            Tax="Rs."+str("%.2f"%((q5)*0.09))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*0.09)))
            self.var_paidax.set(Tax)
            self.var_subtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_boardingpoint.get() == "Old  Delhi bus stand" and self.var_bustype.get() == "NON-AC"):
            q1=float(50)
            q2=float(400)
            q3=float(self.var_daystarveled.get())
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
    obj = busmanagement(root)
    root.mainloop()