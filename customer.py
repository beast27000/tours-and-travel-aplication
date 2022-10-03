from tkinter import *
from PIL import Image , ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

def self(args):
    pass


class Cust_Win:
    def __init__(self, root ) :
        self.var_ = None
        self.root = root
        self.root.title("Hotel Magement System")
        self.root.geometry("1295x550+230+228")


        #=================variables==================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_name= StringVar()
        self.var_mother = StringVar()
        self.var_gender= StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_idproof= StringVar()
        self.var_idnumber = StringVar()



        #======================================== title ==============================================

        lbl_title =  Label(self.root ,text = "ADD CUSTOMER DETAILS", font = ("times new roman",18,"bold"),bg = "black",fg ="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)

        # ======================================== logo ==============================================

        img2 = Image.open(r"C:\Users\USER\COMPPUTER HOTEL MANEGMENT FOLDER\images\orchids manali logo .png")  # space betwwen manli  and .png is a must or this does not work
        img2 = img2.resize((230, 50), Image.ANTIALIAS)
        self.Photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.Photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=50)

        # ======================== label Frame ===========================
        labelframeleft = LabelFrame(self.root  ,bd=2,relief = RIDGE,text = "coustomer details",font = ("times new roman",12,"bold" ),padx = 2)
        labelframeleft.place(x=5,y=50,width=425,height =490)

        # ==========================labels and entrys=============================
        #custref

        lbl_cust_ref= Label(labelframeleft,text ="customer Ref",font=("arial",12,"bold"),padx= 2, pady=6)
        lbl_cust_ref.grid(row = 0,column=0,sticky =W )
        entry_ref = Entry(labelframeleft,textvariable = self.var_ref,width=26,font =("arial",12,"bold"),state = "readonly")
        entry_ref.grid(row=0,column = 1)

        #custname
        cname = Label(labelframeleft,text ="customer Name",font=("arial",12,"bold"),padx= 2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname=ttk.Entry(labelframeleft, textvariable= self.var_name,width=26, font=("arial", 12, "bold"))
        txtcname.grid(row=1, column=1)

        #mothername
        mname = Label(labelframeleft,text ="Mother Name: ",font=("arial",12,"bold"),padx= 2, pady=6)
        mname.grid(row=2, column=0, sticky=W)
        txtmname=ttk.Entry(labelframeleft, textvariable= self.var_mother,width=26, font=("arial", 12, "bold"))
        txtmname.grid(row=2, column=1)

        #gender combobox
        gender= Label(labelframeleft,text="Gender: ", font=("arial", 12, "bold"), padx=2, pady=6)
        gender.grid(row=3, column=0,sticky = W )
        gender_comobobox = ttk.Combobox(labelframeleft, textvariable= self.var_gender, font=("arial", 12, "bold"),width =26)
        gender_comobobox["values"]=("Male","female","other")
        gender_comobobox.grid(row=3,column=1)
        gender_comobobox.current(0)


        #postcode
        postcode = Label(labelframeleft,text ="postcode: ",font=("arial",12,"bold"),padx= 2, pady=6)
        postcode.grid(row=4, column=0, sticky=W)
        txtpostcode=ttk.Entry(labelframeleft,textvariable= self.var_post, width=26, font=("arial", 12, "bold"))
        txtpostcode.grid(row=4, column=1)

        #mobile number
        mobilenumber = Label(labelframeleft,text ="mobile number: ",font=("arial",12,"bold"),padx= 2, pady=6)
        mobilenumber.grid(row=5, column=0, sticky=W)
        txtmobilenumber=ttk.Entry(labelframeleft, width=26, textvariable= self.var_mobile ,font=("arial", 12, "bold"))
        txtmobilenumber.grid(row=5, column=1)

        # email
        email = Label(labelframeleft,text ="email: ",font=("arial",12,"bold"),padx= 2, pady=6)
        email.grid(row=6, column=0, sticky=W)
        txtemail=ttk.Entry(labelframeleft,textvariable= self.var_email, width=26, font=("arial", 12, "bold"))
        txtemail.grid(row=6, column=1)

        #nationality
        nationality =Label(labelframeleft,text ="nationality: ",font=("arial",12,"bold"),padx= 2, pady=6)
        nationality.grid(row=7,column = 0 ,sticky =W)
        nationality_combobox= ttk.Combobox(labelframeleft,textvariable= self.var_nationality, font=("arial", 12, "bold"),width =26)
        nationality_combobox["values"]=("indian","american","australian","british","other")
        nationality_combobox.grid(row=7,column=1)
        nationality_combobox.current(0)


        #idproof type combobox
        idproof =Label(labelframeleft,text ="idproof: ",font=("arial",12,"bold"),padx= 2, pady=6)
        idproof.grid(row=8,column = 0 ,sticky =W)
        idproof_combobox= ttk.Combobox(labelframeleft, textvariable= self.var_idproof,font=("arial", 12, "bold"),width =26)
        idproof_combobox["values"]=("adharcard","deiving license","pasport")
        idproof_combobox.grid(row=8,column=1)
        idproof_combobox.current(0)



        #id number
        id = Label(labelframeleft,text ="idnumber:",font=("arial",12,"bold"),padx= 2, pady=6,)
        id.grid(row=9, column=0, sticky=W)
        txtid=ttk.Entry(labelframeleft, width=26,textvariable= self.var_idnumber, font=("arial", 12, "bold"))
        txtid.grid(row=9, column=1)

        #address
        address = Label(labelframeleft,text ="address: ",font=("arial",12,"bold"),padx= 2,pady=6)
        address.grid(row=10, column=0, sticky=W)
        txtaddress=ttk.Entry(labelframeleft, width=26,textvariable= self.var_address, font=("arial", 12, "bold"))
        txtaddress.grid(row=10, column=1)


        #========================btns========================
        btns_frame = Frame(labelframeleft,bd = 2 ,relief = RIDGE)
        btns_frame.place(x=0,y=400,width =206, height =37)

        ADD =  Button(btns_frame,text="Add",command=self.add_data,font=("arial",11,"bold"),bg="black",fg="gold",width = 10)
        ADD.grid(row=0,column=1,padx=1)



        bdelete = Button(btns_frame,text="Delete",command=self.mDelete, font=("arial",11,"bold"),bg="black",fg="gold",width = 10)
        bdelete.grid(row=0,column=2,padx=1)



        #table_frame
        table_frame =LabelFrame(self.root,relief = RIDGE,text = "Veiw details and search",font = ("arial",12,"bold"),padx =2 )
        table_frame.place(x=435,y=50,width=860,height=490)

        lbl_search = Label(table_frame,text="search by ",font=("arial",12,"bold"),bg="red",fg="white")
        lbl_search.grid(row=0,column=0,sticky=W,padx =2)


        self.search_var=StringVar()
        combo_search = ttk. Combobox(table_frame,textvariable=self.search_var,font=("arial",12,"bold"),width = 24,state ="read only")
        combo_search["values"]=("mobile","ref")
        combo_search.current(0)
        combo_search.grid(row = 0,column=1,padx=2)

        self.txt_search = StringVar()
        table_search =ttk.Entry(table_frame,textvariable=self.txt_search,font=("arial",11,"bold"),width = 24)
        table_search.grid(row=0,column=2,padx=2)

        btnsearch = Button(table_frame,text="Search",command =self.search, font = ("arial",12,"bold"),bg= "black",fg="gold",width=10)
        btnsearch.grid(row=0,column=3,padx=1)

        btnshowall = Button(table_frame,text="ShowAll",command =self.fetch_data, font = ("arial",12,"bold"),bg= "black",fg="gold",width=10)
        btnshowall.grid(row=0,column=4,padx=1)

        #==========================show data table==========================
        details_table=Frame(table_frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)


        self.cust_details_table=ttk.Treeview(details_table,column=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)


        self.cust_details_table.heading("ref",text="Ref")
        self.cust_details_table.heading("name", text="Name")
        self.cust_details_table.heading("mother", text="Mother")
        self.cust_details_table.heading("gender", text="Gender")
        self.cust_details_table.heading("post", text="Postcode")
        self.cust_details_table.heading("mobile", text="Mobile")
        self.cust_details_table.heading("email", text="Email")
        self.cust_details_table.heading("nationality",text="Nationality")
        self.cust_details_table.heading('idproof', text='Idproof')
        self.cust_details_table.heading('idnumber', text='Idnumber')
        self.cust_details_table.heading('address', text='Address')

        self.cust_details_table["show"]="headings"

        self.cust_details_table.column("ref",width=100)
        self.cust_details_table.column("name", width=100)
        self.cust_details_table.column("mother", width=100)
        self.cust_details_table.column("gender", width=100)
        self.cust_details_table.column("post", width=100)
        self.cust_details_table.column("mobile", width=100)
        self.cust_details_table.column("email", width=100)
        self.cust_details_table.column("nationality", width=100)
        self.cust_details_table.column("idproof", width=100)
        self.cust_details_table.column("idnumber", width=100)
        self.cust_details_table.column("address", width=100)
        self.cust_details_table.pack(fill=BOTH, expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>",self.get_cuersor)
        self.fetch_data()



    def add_data(self):
        if self.var_mobile.get=="" or self.var_mother.get()=="" :
            messagebox.showerror("error","all feild are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username= "vishvvesh nagappan",password="Music*1234",database="hotel_management")
                my_courser =conn.cursor()
                my_courser.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                            self.var_ref.get(),
                                                            self.var_name.get(),
                                                            self.var_mother.get(),
                                                            self.var_gender.get(),
                                                            self.var_post.get(),
                                                            self.var_mobile.get(),
                                                            self.var_email.get(),
                                                            self.var_nationality.get(),
                                                            self.var_idproof.get(),
                                                            self.var_idnumber.get(),
                                                            self.var_address.get()



                                                         ))


                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","customer has been added", parent=self.root )
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root )

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username= "vishvvesh nagappan",password="Music*1234",database="hotel_management")
        my_courser=conn.cursor()
        my_courser.execute("select * from customer")
        rows=my_courser.fetchall()
        if len(rows)!=0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cuersor(self,events=""):
        cursor_row=self.cust_details_table.focus()
        content=self.cust_details_table.item(cursor_row)
        row =content["values"]

        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_idproof.set(row[8]),
        self.var_idnumber.set(row[9]),
        self.var_address.set(row[10])

    def mupdate(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","please enter mobile number",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username= "vishvvesh nagappan",password="Music*1234",database="hotel_management")
                my_courser=conn.cursor()
                my_courser.execute("UPDATE customer set Name=%s,Mother=%s,Gender=%s,Postcode=%s,Mobile=%s,Email=%s,Nationality=%s,Idproof=%s,Idnumber= %s,Address=%s where Ref=%s",(

                                                                                                                                                            self.var_name.get(),
                                                                                                                                                            self.var_mother.get(),
                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                            self.var_post.get(),
                                                                                                                                                            self.var_mobile.get(),
                                                                                                                                                            self.var_email.get(),
                                                                                                                                                            self.var_nationality.get(),
                                                                                                                                                            self.var_idproof.get(),
                                                                                                                                                            self.var_idnumber.get(),
                                                                                                                                                            self.var_address.get(),
                                                                                                                                                            self.var_ref.get()

                                                                                                                                                            ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","customer has been updated ", parent=self.root )
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root )



    def mDelete(self):
        mDelete=messagebox.askyesno("hotel management system ","do you want to  delete this customer",parent=self.root)
        if mDelete>0:
            conn=mysql.connector.connect(host="localhost",username= "vishvvesh nagappan",password="Music*1234",database="hotel_management")
            my_cursor=conn.cursor()
            query="delete from customer where Ref =%s"
            value=(self.var_ref.get(),)
            my_cursor.execute(query,value)

        else:
            if not mDelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()




    def search(self):
        conn = mysql.connector.connect(host="localhost", username="vishvvesh nagappan", password="Music*1234",
                                           database="hotel_management")
        my_courser = conn.cursor()
        my_courser.execute("select * from customer where "+str(self.search_var.get())+"Like'%"+str(self.txt_search.get())+"%'")
        rows = my_courser.fetchall()
        if len(rows)!= 0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("",END,values=i)
            conn.commit()
        conn.close()



























if __name__ == '__main__':
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()

