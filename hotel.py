from tkinter import *     # module for placing buttons etc
from tkinter import filedialog
from PIL import Image , ImageTk                   #module for importing images ( know as pillow module )
import os
from customer import Cust_Win
import random
import mysql.connector
from room import Roombooking
from  bus import busmanagement
import PySimpleGUI as psg
import os





class HotelManagementSystem :
    def __init__(self, root ) :
        self.root = root
        self.root.title("Hotel Magement System")
        self.root.geometry("1520x800+0+0")






        #  ========================================= 1st img =======================================
        img1 = Image.open(r"C:\Users\USER\COMPPUTER HOTEL MANEGMENT FOLDER\images\the-orchard-greens down image .png")  # space betwwen manli  and .png is a must or this does not work
        img1 = img1.resize((1520, 160), Image.ANTIALIAS)
        self.Photoimg1 = ImageTk.PhotoImage(img1)
        lblimg = Label(self.root, image=self.Photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1520, height=160)

        # ======================================== logo ==============================================

        img2 = Image.open(r"C:\Users\USER\COMPPUTER HOTEL MANEGMENT FOLDER\images\orchids manali logo .png")  # space betwwen manli  and .png is a must or this does not work
        img2 = img2.resize((230, 160), Image.ANTIALIAS)
        self.Photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.Photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=160)

        #======================================== title ==============================================

        lbl_title =  Label(self.root ,text = "MAKE MY JOURNEY ", font = ("times new roman",40,"bold"),bg = "black",fg ="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1530,height=50)

        #===================================== main frame ============================================

        main_frame =Frame(self.root,bd =4,relief = RIDGE )
        main_frame.place(x=0,y= 190,width=1530,height=620 )

        # ========================================== menue ============================================
        lbl_menue=Label(main_frame,text="MENU",font= ("times new roman" ,20 ,"bold"),bg ="black",fg="gold",relief=RIDGE)
        lbl_menue.place(x=0,y=0,width=230)

        # ======================================== btn Frame ==========================================
        btn_frame = Frame(main_frame,bd= 4 ,relief = RIDGE)
        btn_frame.place(x=0,y=35,width=228,height =190)

        cust_btn =Button(btn_frame,text ="CUSTOMER",command=self.cust_details,width=22, font = ("times new roman" ,14 ,"bold") ,bg ="black",fg="gold", bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn =Button(btn_frame,text ="ROOMS BOOKING",width=22,command=self.roombooking ,font = ("times new roman" ,14 ,"bold") ,bg ="black",fg="gold", bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)

        bus =Button(btn_frame,text ="BUS BOOKING",width=22,command=self.busbooking, font = ("times new roman" ,14 ,"bold") ,bg ="black",fg="gold", bd=0,cursor="hand1")
        bus.grid(row=2,column=0,pady=1)

        tourist_spots =Button(btn_frame,text ="WAITING LOBBY",command=self.OPEN_GAMES,width=22, font = ("times new roman" ,14 ,"bold") ,bg ="black",fg="gold", bd=0,cursor="hand1")
        tourist_spots.grid(row=4,column=0,pady=1)

        aeroplanebooking_system =Button(btn_frame,text ="FLIGHT BOOKING",width=22, command=self.aeroplanebooking,font = ("times new roman" ,14 ,"bold") ,bg ="black",fg="gold", bd=0,cursor="hand1")
        aeroplanebooking_system.grid(row=3,column=0,pady=1)




        # ======================================== right side image ==========================================
        img3 = Image.open(r"C:\Users\USER\COMPPUTER HOTEL MANEGMENT FOLDER\images\main background .png")  # space betwwen manli  and .png is a must or this does not work
        img3 = img3.resize((1310,590), Image.ANTIALIAS)
        self.Photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(main_frame, image=self.Photoimg3, bd=4, relief=RIDGE)
        lblimg.place(x=225, y=0, width=1310, height=590)

        # ======================================== side down image  ==========================================

        img4 = Image.open(r"C:\Users\USER\COMPPUTER HOTEL MANEGMENT FOLDER\images\orchids hotel .jpeg")  # space betwwen manli  and .png is a must or this does not work
        img4 = img4.resize((230,210), Image.ANTIALIAS)
        self.Photoimg4 = ImageTk.PhotoImage(img4)

        lblimg = Label(main_frame, image=self.Photoimg4, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=225, width=230, height=210)





        img5 = Image.open(r"C:\Users\USER\COMPPUTER HOTEL MANEGMENT FOLDER\images\manali food  3 .png ")  # space betwwen manli  and .png is a must or this does not work
        img5 = img5.resize((230,190), Image.ANTIALIAS)
        self.Photoimg5 = ImageTk.PhotoImage(img5)

        lblimg = Label(main_frame, image=self.Photoimg5, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=420 ,width=230, height=190)



    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Cust_Win(self.new_window)


    def roombooking (self):
        self.new_window = Toplevel(self.root)
        self.app = Roombooking(self.new_window)


    def busbooking (self):
        self.new_window = Toplevel(self.root)
        self.app = busmanagement(self.new_window)

    def aeroplanebooking (self):

        psg.theme('light blue')

        def payment_window():
            psg.theme('light blue')
            layout_p = [
                [psg.Text('Payment page', size=(20, 1), justification='left')],
                [psg.Text('Amount to be payed =Rs.' + price, size=(40, 1), justification='left', key='amount')],
                [psg.Button('Pay', key='pay'), psg.Cancel('Exit', key='pexit')]
            ]

            window = psg.Window("Payment", layout_p, size=(300, 200), auto_close=False, )

            events, values = window.read()

            while True:

                if events == psg.WIN_CLOSED:
                    break

                elif events == "pexit":
                    break

                elif events == "pay":
                    psg.popup("Your booking was successfull !",
                              '\nYou will Travel from :\n' + value['board'] + ' to ' + value[
                                  'dest'] + '\n\n Seats booked = ' + strx[0:len(strx)], button_type='POPUP_BUTTONS_OK',
                              button_color='orange', background_color='light blue', text_color='dark blue')
                    break

            window.close()

        layout1 = [[psg.Text('Departure City', size=(20, 1), font='Lucida', justification='left')],
                   [psg.Combo(['Bangalore', 'Chennai', 'Mumbai', 'Kolkata'], size=(40, 1), key='board')],
                   [psg.Text('Arrival City', size=(30, 1), font='Lucida', justification='left')],
                   [psg.Combo(['Delhi'], size=(40, 1), key='dest', default_value='Delhi')],
                   [psg.Text('Choose the number of seats: ', size=(30, 1), font='Lucida', justification='left')],
                   [
                       [psg.Radio("1", "RADIO1", key='1', default=True, circle_color='orange'),
                        psg.Radio("2", "RADIO1", key='2', circle_color='orange'),
                        psg.Radio("3", "RADIO1", key='3', circle_color='orange'),
                        psg.Radio("4", "RADIO1", key='4', circle_color='orange')
                        ]
                   ],
                   [psg.Button('Next', key='next', mouseover_colors=('orange', 'grey')),
                    psg.Cancel('Exit', key='exit')]]

        window = psg.Window('Booking Project', layout1, size=(400, 300))

        event, value = window.read()

        strx = ""

        for val in value:
            if window.FindElement(val).get() == True:
                strx = strx + " " + val

        departure = value['board']
        tic_price = 0
        seats = int(strx[0:len(strx)])

        if departure == 'Bangalore':

            tic_price = 2000 * seats

        elif departure == 'Chennai':

            tic_price = 3000 * seats

        elif departure == 'Mumbai':

            tic_price = 2500 * seats

        elif departure == 'Kolkata':

            tic_price = 2800 * seats

        price = str(tic_price)

        while True:

            if event == psg.WIN_CLOSED:

                break

            elif event == "exit":

                break

            elif event == "next":

                payment_window()

                break

            window.close()






    def OPEN_GAMES(self):
        root = Tk()
        root.title('waiting loby')
        root.iconbitmap(r"C:\Users\USER\COMPPUTER HOTEL MANEGMENT FOLDER")

        def openprogram():
            my_program = filedialog.askopenfilename()
            my_lable.config(text=my_program)
            os.system('"%s"' % my_program)

        my_button = Button(root, text="Open games window", command=openprogram)
        my_button.pack(pady=20)


        my_lable = Label(root, text="")
        my_lable.pack(pady=20)
        root.mainloop()








if __name__ == "__main__":
    root=Tk()
    obj=HotelManagementSystem(root)
    root.mainloop()


