from my_package import Manager
from my_package import Deliverer
from my_package import Publication
from my_package import Subscription
from my_package import Customer
from my_package import Address

from tkinter import *
import tkinter as ttk
from tkinter import scrolledtext
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from PIL import ImageTk,Image
import random
import datetime
from datetime import date
import json

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login Page")
        self.master.geometry('1350x750+0+0')
        Grid.rowconfigure(self.master, 0, weight=1)
        Grid.columnconfigure(self.master, 0, weight=1)
        self.frame = Frame(self.master, width=1350, height=750)
        self.frame.pack()
        self.frame.grid_propagate(False)
        bg = ImageTk.PhotoImage(Image.open("./Data/Newspapers.jpg"))
        img_label = Label(self.frame, image=bg)
        img_label.place(x=0, y=0)


        self.labelTitle = Label(self.frame, text = "Newspaper Agency Automation Software", font=('arial', 30, 'bold'), fg="#222730", bg="#b6b2ad", bd=20)
        #self.labelTitle.grid(row=0, column=0, pady=(0,40),padx=(0,50))
        self.labelTitle.place(in_=self.frame, anchor="c", relx=.5, rely=.123)

        #====================             FRAMES             ===================================================================================

        self.frame1 = Frame(self.frame, width=542, height=90, bd=2, relief='solid',padx=12,pady=12,bg="#7D8CA3")
        self.frame1.place(in_=self.frame, anchor="c", relx=.5, rely=.25)
        #self.frame1.grid(row=1, column=0, sticky="")
        self.frame1.grid_propagate(False)

        self.frame2 = Frame(self.frame, width=542, height=180, bd=2, relief='solid',padx=12,bg="#7D8CA3")
        self.frame2.place(in_=self.frame, anchor="c", relx=.5, rely=.44)
        #self.frame2.grid(row=2, column=0)
        self.frame2.grid_propagate(False)

        self.frame3 = Frame(self.frame, width=542, height=70, bd=2, relief='solid',padx=12,bg="#7D8CA3")
        self.frame3.place(in_=self.frame, anchor="c", relx=.5, rely=.61)
        #self.frame3.grid(row=3, column=0)
        self.frame3.grid_propagate(False)

        # ====================             DROP DOWN MENU  (FRAME 1)         ===================================================================================

        self.labelUserType = Label(self.frame1, text = "USER TYPE   ", font = ('arial',12,'bold'),bg="#7D8CA3", padx=12)
        self.labelUserType.grid(row=0, column=0, padx=(50,10))

        self.clickedUser = StringVar()
        self.clickedUser.set("Select User Type")
        self.users = ["Manager", "Deliverer"]
        self.usersDrop =OptionMenu(self.frame1, self.clickedUser, *self.users)
        self.usersDrop.config(font = ('arial',10,'bold'))
        self.usersDrop.grid(row=0, column=1, padx=(50,50))

        self.labelSetDate = Label(self.frame1, text="SET DATE  ", font=('arial', 12, 'bold'),bg="#7D8CA3", padx=12)
        self.labelSetDate.grid(row=1, column=0, padx=(50, 0), pady=10)

        self.calSetDate = DateEntry(self.frame1, width=20, background="#b6b2ad",
                                 foreground='black', borderwidth=2)
        self.calSetDate.grid(row=1, column=1, pady=10)

        # ===========             USERNAME AND PASSWORD (FRAME 2)            ===================================================================================

        self.labelUser = Label(self.frame2, text = "USERNAME / USER ID   ", font = ('arial',12,'bold'),bg="#7D8CA3", bd=20)
        self.labelUser.grid(row=0, column=0, columnspan=2, pady=10)
        self.username = StringVar()
        self.eUsername = Entry(self.frame2, width=30,font=('arial', 12), bg="white", fg="black", relief="solid", borderwidth=1, textvariable=self.username)
        self.eUsername.grid(row=0, column=2, columnspan=2, pady=10)

        self.labelPass = Label(self.frame2, text="PASSWORD   ", font=('arial', 12, 'bold'),bg="#7D8CA3", bd=20)
        self.labelPass.grid(row=1, column=0, columnspan=2, pady=10)
        self.password = StringVar()
        self.ePass = Entry(self.frame2, show="*", width=30,font=('arial', 12), bg="white", fg="black", relief="solid", borderwidth=1, textvariable=self.password)
        self.ePass.grid(row=1, column=2, columnspan=2, pady=10)

        # ===========            LOGIN RESET EXIT (FRAME 3)            ===================================================================================

        self.btnLogin = Button(self.frame3, text="Login", command=lambda: self.decide(), font=('arial', 12, 'bold'), width=13)
        self.btnLogin.grid(row=0, column=0, padx=11, pady=11)

        self.btnReset = Button(self.frame3, text="Reset", command=lambda: self.reset(), font=('arial', 12, 'bold'), width=15)
        self.btnReset.grid(row=0, column=1, padx=11, pady=11)

        self.btnExit = Button(self.frame3, text="Exit", command=lambda: self.exitProgram(), font=('arial', 12, 'bold'), width=13)
        self.btnExit.grid(row=0, column=2, padx=11, pady=11)

        #self.b2 = Button(self.frame1, text="Deliverer", command=self.deliverer_window)
        #self.b2.grid(row=0, column=1)

        self.master.mainloop()

    def decide(self):
        if self.clickedUser.get()=="Select User Type":
            messagebox.showerror("Select User Type", "Select valid User Type")

        if self.clickedUser.get()=="Manager":
            if (self.eUsername.get() != manager.name and self.eUsername.get() != manager.ID) or self.ePass.get() != manager.password:
                messagebox.showwarning("Invalid Entries!", "The Username or Password entered is incorrect")
            elif (self.eUsername.get() == manager.ID or self.eUsername.get() == manager.name) and self.ePass.get() == manager.password:
                d = self.calSetDate.get().split("/")
                d = [int(i) for i in d]
                SetDate = date(2000+d[2],d[0],d[1])
                self.manager_window()
        elif self.clickedUser.get() == "Deliverer":
            flag = False
            for i in deliverers:
                if ((i.name == self.eUsername.get() or i.ID == self.eUsername.get()) and i.password == self.ePass.get()):
                    flag = True
                    break
            if flag:
                d = self.calSetDate.get().split("/")
                d = [int(i) for i in d]
                SetDate = date(2000 + d[2], d[0], d[1])
                self.deliverer_window(i)
            else:
                messagebox.showwarning("Invalid Entries!", "The Username or Password entered is incorrect")

        self.btnLogin.mainloop()

    def reset(self):
        self.master.destroy()
        MainWindow(Tk())

    def exitProgram(self):
        choice = messagebox.askquestion("Exit", "Are you sure?")
        if choice=='yes':
            exit()

    def manager_window(self):
        self.username.set("")
        self.password.set("")
        self.newWindow = Toplevel(self.master)
        self.app = ManagerWindow(self.newWindow)

    def deliverer_window(self, deliverer):
        self.newWindow = Toplevel(self.master)
        self.app = DelivererWindow(self.newWindow,deliverer)

class ManagerWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Manager Page")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        # ====================             FRAMES             ===================================================================================

        self.frame1 = Frame(self.frame, width=1000, height=100, bd=7, relief='ridge', bg = "SkyBlue2")
        self.frame1.grid(row=0, column=0, sticky="news")

        self.frame2 = Frame(self.frame, width=800, height=200, bd=7, relief='ridge', padx=12)
        self.frame2.grid(row=0, column=1)

        # ====================             BUTTONS IN FRAME1             ===================================================================================

        self.btnAddCustomers = Button(self.frame1, text="Add Customers",command=lambda: self.addCustomers(), font=('arial', 12, 'bold'),width=20)
        self.btnAddCustomers.grid(row=0, column=0, padx=40, pady=22)

        self.btnEditCustomers = Button(self.frame1, text="Edit Customers Details",command=lambda: self.editCustomer(), font=('arial', 12, 'bold'), width=20)
        self.btnEditCustomers.grid(row=1, column=0, padx=40, pady=22)

        self.btnAddPublication = Button(self.frame1, text="Add Publication",command=lambda: self.addPublication(), font=('arial', 12, 'bold'), width=20)
        self.btnAddPublication.grid(row=2, column=0, padx=40, pady=22)

        self.btnEditPublications = Button(self.frame1, text="Edit Publications",command=lambda: self.editPublication(), font=('arial', 12, 'bold'), width=20)
        self.btnEditPublications.grid(row=3, column=0, padx=40, pady=22)

        self.btnCustomerBills = Button(self.frame1, text="Show Customer Bills",command=lambda: self.customerBills(), font=('arial', 12, 'bold'), width=20)
        self.btnCustomerBills.grid(row=4, column=0, padx=40, pady=22)

        self.btnSummary = Button(self.frame1, text="Show Summary", command=lambda: self.summary(), font=('arial', 12, 'bold'), width=20)
        self.btnSummary.grid(row=5, column=0, padx=40, pady=22)

        self.btnAddDeliverer = Button(self.frame1, text="Add Deliverer", command=lambda: self.addDeliverer(), font=('arial', 12, 'bold'),width=20)
        self.btnAddDeliverer.grid(row=6, column=0, padx=40, pady=22)

        self.btnDeliveryDetails = Button(self.frame1, text="Deliverer Details", command=lambda: self.delivererDetails(), font=('arial', 12, 'bold'),width=20)
        self.btnDeliveryDetails.grid(row=7, column=0, padx=40, pady=22)

        self.master.mainloop()

    def addCustomers(self):
        self.reset()
        # ====================            ADD CUST0MERS HEADING             ===================================================================================

        self.labelAddCustomers = Label(self.frame2, text="Add Customers", font=('arial', 17, 'bold'),
                                       bd=20)
        self.labelAddCustomers.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       CUSTOMER DETAILS FRAME            ===================================================================================

        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)


        self.labelName = Label(self.frameDetails, text="Full Name ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2", justify=LEFT)
        self.labelName.grid(row=0, column=0, rowspan=2)
        self.name = StringVar()
        self.eName = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid", borderwidth=1,
                            textvariable=self.name)
        self.eName.grid(row=2, column=0,padx=10)



        self.labelID = Label(self.frameDetails, text="Customer ID", font=('arial', 12, 'bold'), bd=10,
                                      bg="SkyBlue2", justify=LEFT)
        self.labelID.grid(row=0, column=1, rowspan=2)
        self.cID = StringVar()
        self.ecID = Entry(self.frameDetails, width=12, font=('arial', 12), bg="white", fg="black", relief="solid",
                           borderwidth=1,
                           textvariable=self.cID)
        self.ecID.grid(row=2, column=1, padx=10)



        self.labelPhoneNumber = Label(self.frameDetails, text="Phone Number", font=('arial', 12, 'bold'), bd=10,
                                      bg="SkyBlue2", justify = LEFT)
        self.labelPhoneNumber.grid(row=0, column=2, rowspan=2)
        self.phNo = StringVar()
        self.ePhNo = Entry(self.frameDetails, width=12, font=('arial', 12), bg="white", fg="black", relief="solid", borderwidth=1,
                            textvariable=self.phNo)
        self.ePhNo.grid(row=2, column=2, padx=10)

        # ====================            ADDRESS DETAILS            ===================================================================================

        self.labelAddress = Label(self.frameDetails, text="Address", font=('arial', 12, 'bold'), bd=20,
                                      bg="SkyBlue2")
        self.labelAddress.grid(row=0, column=3, columnspan=3)



        self.labelStreetNo = Label(self.frameDetails, text="Street No.", font=('arial', 10, 'bold'), bd=10,
                                  bg="SkyBlue2", justify=LEFT)
        self.labelStreetNo.grid(row=1, column=4)
        self.SNo = IntVar()
        self.eSNo = Entry(self.frameDetails, width=5, font=('arial', 12), bg="white", fg="black", relief="solid", borderwidth=1,
                            textvariable=self.SNo)
        self.eSNo.grid(row=2, column=4, padx=10, pady=10)



        self.labelRoadNo = Label(self.frameDetails, text="Road No.", font=('arial', 10, 'bold'), bd=10,
                                   bg="SkyBlue2", justify=LEFT)
        self.labelRoadNo.grid(row=1, column=5)
        self.RNo = IntVar()
        self.eRNo = Entry(self.frameDetails, width=5, font=('arial', 12), bg="white", fg="black", relief="solid", borderwidth=1,
                           textvariable=self.RNo)
        self.eRNo.grid(row=2, column=5, padx=10, pady=10)


        self.labelHouseNo = Label(self.frameDetails, text="House No.", font=('arial', 10, 'bold'), bd=10,
                                 bg="SkyBlue2", justify=LEFT)
        self.labelHouseNo.grid(row=1, column=6)
        self.HNo = StringVar()
        self.eHNo = Entry(self.frameDetails, width=5, font=('arial', 12), bg="white", fg="black", relief="solid", borderwidth=1,
                           textvariable=self.HNo)
        self.eHNo.grid(row=2, column=6, padx=10, pady=10)

        # ====================          ADD SUBSCRIPTIONS FRAME            ===================================================================================

        self.frameSubs = LabelFrame(self.frame2, text="Add Subscriptions", font=('arial', 12, 'bold'), padx=12)
        self.frameSubs.grid(row=3, column=0, pady=20)

        self.paperLanguage = Label(self.frameSubs, text="Language ", font=('arial', 12, 'bold'), bd=10)
        self.paperLanguage.grid(row=0, column=0)

        self.v1 = StringVar(self.frameSubs, "English")
        Radiobutton(self.frameSubs, text="English", variable=self.v1, font=('arial', 10), command=lambda: self.dropDownPubForSub(),
                    value="English").grid(row=1, column=0)
        Radiobutton(self.frameSubs, text="Hindi", variable=self.v1, font=('arial', 10), command=lambda: self.dropDownPubForSub(),
                    value="Hindi").grid(row=1, column=1)
        Radiobutton(self.frameSubs, text="Telugu", variable=self.v1, font=('arial', 10), command=lambda: self.dropDownPubForSub(),
                    value="Telugu").grid(row=1, column=2)

        self.clickedPublication = StringVar()
        self.clickedPublication.set("Select Publication")
        self.publicationNames = []
        for i in publications_:
            if i["Language"].casefold() == self.v1.get().casefold():
                self.publicationNames.append(i["PaperName"])
        self.publicationsDrop = OptionMenu(self.frameSubs, self.clickedPublication, *self.publicationNames)
        self.publicationsDrop.config(font=('arial', 10, 'bold'))
        self.publicationsDrop.grid(row=2, column=0, padx=10, columnspan=3)

        # ====================          FROM-DATE AND TO-DATE            ===================================================================================

        self.labelFromDate = Label(self.frameSubs, text="From Date", font=('arial', 12, 'bold'), bd=10,
                               justify=LEFT)
        self.labelFromDate.grid(row=1, column=4, padx=10)

        self.calFrom = DateEntry(self.frameSubs, width=12, background='darkblue',
                        foreground='white', borderwidth=2)
        self.calFrom.grid(row=1, column=5, padx=10)

        self.labelToDate = Label(self.frameSubs, text="To Date", font=('arial', 12, 'bold'), bd=10,
                                   justify=LEFT)
        self.labelToDate.grid(row=2, column=4, padx=10)

        self.calTo = DateEntry(self.frameSubs, width=12, background='darkblue',
                             foreground='white', borderwidth=2)
        self.calTo.grid(row=2, column=5, padx=10)

        self.btnCancel = Button(self.frameSubs, text="Cancel", font=('arial', 12, 'bold'), width=20, command=lambda : self.cancelCust())
        self.btnCancel.grid(row=0, column=6, padx=30)

        self.btnAdd = Button(self.frameSubs, text="Add", font=('arial', 12, 'bold'), width=20,command=lambda: self.addSubs() )
        self.btnAdd.grid(row=1, column=6, padx=30)

        self.btnDone = Button(self.frameSubs, text="Done", font=('arial', 12, 'bold'), width=20,command=lambda: self.doneSubs())
        self.btnDone.grid(row=2, column=6, padx=30)

        for child in self.frameSubs.winfo_children():
            child.configure(state="disable")

        self.subs = []
        self.btnAddTop = Button(self.frameDetails, text="Add", font=('arial', 12, 'bold'), width=5,
                             command=lambda: self.addDet())
        self.btnAddTop.grid(row=2, column=7, padx=20)


    def addDet(self):
        l = [i["PhoneNumber"] for i in customers_]
        if self.phNo.get() == "" or self.cID.get()=="" or self.name.get() == "" or self.RNo.get() == 0 or self.SNo.get() == 0 or self.HNo.get()=="":
            messagebox.showwarning("Empty Entries!", "Fill all the Entries", parent=self.master)
        elif self.cID.get() in IDs:
            messagebox.showerror("Unique IDs", "Enter a unique ID", parent=self.master)
        elif len(self.PhNo.get())!=10:
            messagebox.showwarning("Invlaid Phone Number", "Enter a valid Phone Number", parent=self.master)
        elif self.phNo.get() in l:
            c = ""
            for i in customers_:
                if i["PhoneNumber"]==self.phNo.get():
                    c=i["CustomerName"]
                    break
            messagebox.showwarning("Phone Number exists", self.phNo.get() + "already exists\n Customer Name : "+c, parent=self.master)
        else:
            for child in self.frameSubs.winfo_children():
                child.configure(state="normal")
            for child in self.frameDetails.winfo_children():
                child.configure(state="disable")
            self.subs = []
    def cancelCust(self):
        choice = messagebox.askquestion("Cancel", "Are you sure?", parent=self.master)
        if choice=="yes":
            for child in self.frameSubs.winfo_children():
                child.configure(state="disable")
            for child in self.frameDetails.winfo_children():
                child.configure(state="normal")
            self.resetSubs()
            self.name.set("")
            self.cID.set("")
            self.phNo.set("")
            self.SNo.set(0)
            self.RNo.set(0)
            self.HNo.set("")

    def resetSubs(self):
        self.clickedPublication.set("Select Publication")

    def addSubs(self):
        t = self.calTo.get().split("/")
        t = [int(k) for k in t]
        f = self.calFrom.get().split("/")
        f = [int(k) for k in f]
        df = date(2000+f[2],f[0],f[1])
        dt = date(2000+t[2],t[0],t[1])
        if df>=dt:
            messagebox.showwarning("From-date and To-date", "To-date should come after From-date", parent=self.master)
        elif self.clickedPublication.get()=="Select Publication":
            messagebox.showwarning("Unselected Value!", "Select Publication!", parent=self.master)
        else:
            d = {"name" : self.clickedPublication.get(), "from_date": self.calFrom.get(), "to_date": self.calTo.get()}
            self.subs.append(d)
            self.resetSubs()
            messagebox.showinfo("Success", "Subscription added successfully", parent=self.master)


    def doneSubs(self):
        customers_.append({"CustomerID" : self.cID.get(), "CustomerName": self.name.get(),"PhoneNumber" : self.phNo.get(),"Address" : [self.SNo.get(),self.RNo.get(),self.HNo.get()], "Subscriptions":self.subs})
        with open("./Data/CustomerDetails.json", "w") as write_file:
            json.dump(customers_, write_file, indent=4, sort_keys=True)
        IDs.append(self.cID.get())
        messagebox.showinfo("Success", "Customer added successfully", parent=self.master)
        for child in self.frameSubs.winfo_children():
            child.configure(state="disable")
        for child in self.frameDetails.winfo_children():
            child.configure(state="normal")
        self.resetSubs()
        self.name.set("")
        self.cID.set("")
        self.phNo.set("")
        self.SNo.set(0)
        self.RNo.set(0)
        self.HNo.set("")


    def dropDownPubForSub(self):
        self.clickedPublication = StringVar()
        self.clickedPublication.set("Select Publication")
        self.publicationNames = []
        for i in publications_:
            if i["Language"].casefold() == self.v1.get().casefold():
                self.publicationNames.append(i["PaperName"])
        self.publicationsDrop.destroy()
        self.publicationsDrop = OptionMenu(self.frameSubs, self.clickedPublication, *self.publicationNames)
        self.publicationsDrop.config(font=('arial', 10, 'bold'))
        self.publicationsDrop.grid(row=2, column=0, padx=10, columnspan=3)

    def addPublication(self):
        self.reset()
        # ====================            HEADING             ========================================================================
        self.labelAddPublications = Label(self.frame2, text="Add Publications", font=('arial', 17, 'bold'), bd=20)
        self.labelAddPublications.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================            DETAILS FRAME            ===================================================================
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge', padx=12, pady=12,
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.paperid = Label(self.frameDetails, text="Paper Id ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2")
        self.paperid.grid(row=0, column=0)
        self.pid = StringVar()
        self.ePaperID = Entry(self.frameDetails, width=20, font=('arial', 12), bg="white", fg="black", relief="solid", borderwidth=1,
                          textvariable=self.pid)
        self.ePaperID.grid(row=1, column=0, padx=10)

        self.paperName = Label(self.frameDetails, text="Paper Name ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2")
        self.paperName.grid(row=0, column=1)
        self.pName = StringVar()
        self.ePaperName = Entry(self.frameDetails, width=20, font=('arial', 12), bg="white", fg="black", relief="solid", borderwidth=1, textvariable=self.pName)
        self.ePaperName.grid(row=1, column=1, padx=10)

        self.paperType = Label(self.frameDetails, text="Paper Type ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2")
        self.paperType.grid(row=2, column=1)
        self.pType = StringVar()
        self.ePaperType = Entry(self.frameDetails, width=20, font=('arial', 12), bg="white", fg="black",relief="solid", borderwidth=1, textvariable=self.pType)
        self.ePaperType.grid(row=3, column=1, padx=10)

        self.paperLanguage = Label(self.frameDetails, text="Language ", font=('arial', 12, 'bold'), bd=10,
                                   bg="SkyBlue2")
        self.paperLanguage.grid(row=2, column=0)


        self.v = StringVar(self.frameDetails, "English")
        self.values = {"English": "English", "Hindi": "Hindi", "Telugu": "Telugu"}
        Radiobutton(self.frameDetails, text="English", variable=self.v, bg="skyblue2", font=('arial',10),
                        value="English").grid(row=3, column=0)
        Radiobutton(self.frameDetails, text="Hindi", variable=self.v, bg="skyblue2",font=('arial',10),
                          value="Hindi").grid(row=4, column=0)
        Radiobutton(self.frameDetails, text="Telugu", variable=self.v, bg="skyblue2", font=('arial',10),
                          value="Telugu").grid(row=5, column=0)


        self.paperPrice = Label(self.frameDetails, text="Price", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2")
        self.paperPrice.grid(row=4, column=1)
        self.pPrice = DoubleVar()
        self.ePrice = Entry(self.frameDetails, width=20, font=('arial', 12), bg="white", fg="black", relief="solid",
                                borderwidth=1, textvariable=self.pPrice)
        self.ePrice.grid(row=5, column=1, padx=10)


        self.btnAddPub = Button(self.frameDetails, text="Add", font=('arial', 12, 'bold'),command=lambda: self.addPub(), width=20)
        self.btnAddPub.grid(row=6, column=1, padx=40, pady=25)


    def addPub(self):
        l = [i["PaperName"].lower() for i in publications_]
        if self.pPrice.get()==0 or self.pType.get()=="" or self.pid.get()=="" or self.pName.get()=="":
            messagebox.showwarning("Empty Entries!", "Fill all the Entries", parent=self.master)
        elif self.pid.get() in IDs:
            messagebox.showerror("Unique IDs", "Enter a unique ID", parent=self.master)
        elif self.pName.get().lower() in l:
            messagebox.showwarning("Publication exists", self.pName.get()+ " already exists", parent=self.master)
        else:
            publications_.append({"PaperID": self.pid.get(),"PaperName": self.pName.get(),"PaperType": self.pType.get(),"Language": self.v.get(),"Price": self.pPrice.get()})
            sPublications[self.pName.get()]=Publication(self.pid.get(),self.pName.get(),self.pType.get(),self.v.get(),self.pPrice.get())
            with open("./Data/Publications.json", "w") as write_file:
                json.dump(publications_, write_file, indent=4, sort_keys=True)
            IDs.append(self.pid.get())
            self.pName.set("")
            self.pid.set("")
            self.pType.set("")
            self.pPrice.set(0.0)
            messagebox.showinfo("Success", "Publication added successfully", parent=self.master)
        self.btnAddPub.mainloop()


    def editPublication(self):
        self.reset()

        # ====================            DETAILS FRAME            ===================================================================
        self.frameEditPub = Frame(self.frame2, width=2000, height=500, bd=7, relief='flat', padx=12, pady=12,
                                  bg="SkyBlue2")
        self.frameEditPub.grid(row=1, column=0)
        self.Language = Label(self.frameEditPub, text="Language ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2")
        self.Language.grid(row=0, column=0)
        self.v1 = StringVar(self.frameEditPub, "English")
        Radiobutton(self.frameEditPub, text="English", variable=self.v1, font=('arial', 10), bg="SkyBlue2",
                    command=lambda: self.dropDownPubForSub1(),
                    value="English").grid(row=1, column=0, padx=5)
        Radiobutton(self.frameEditPub, text="Hindi", variable=self.v1, font=('arial', 10), bg="SkyBlue2",
                    command=lambda: self.dropDownPubForSub1(),
                    value="Hindi").grid(row=1, column=1, padx=5)
        Radiobutton(self.frameEditPub, text="Telugu", variable=self.v1, font=('arial', 10), bg="SkyBlue2",
                    command=lambda: self.dropDownPubForSub1(),
                    value="Telugu").grid(row=1, column=2, padx=5)

        self.clickedPublication = StringVar()
        self.clickedPublication.set("Select Publication")
        self.publicationNames = []
        for i in publications_:
            if i["Language"].casefold() == self.v1.get().casefold():
                self.publicationNames.append(i["PaperName"])
        self.publicationsDrop = OptionMenu(self.frameEditPub, self.clickedPublication, *self.publicationNames)
        self.publicationsDrop.config(font=('arial', 10, 'bold'))
        self.publicationsDrop.grid(row=2, column=0, padx=10, columnspan=3)

        self.btnEditPub = Button(self.frameEditPub, text="Edit", font=('arial', 12, 'bold'),
                                command=lambda: self.EditPub(self.clickedPublication.get()), width=20)
        self.btnEditPub.grid(row=3, column=1, padx=40, pady=25)

    def reset(self):
        for widget in self.frame2.winfo_children():
            widget.destroy()

    def EditPub(self, pubName):
        if pubName == "Select Publication":
            messagebox.showwarning("Unselected Value!", "Select Publication!", parent=self.master)
        else:
            self.reset()
            self.labelTitle = Label(self.frame2, text="Edit Publication", font=('arial', 15, 'bold'),
                                    bd=20)
            self.labelTitle.grid(row=0, column=0, columnspan=2, pady=40)
            self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                      bg="SkyBlue2")
            self.frameDetails.grid(row=1, column=0)

            self.labelPubID = Label(self.frameDetails, text="Publication ID : ", font=('arial', 10, 'bold'), bd=10,
                                    bg="SkyBlue2", justify=LEFT)
            self.labelPubID.grid(row=1, column=0)
            self.labelPubName = Label(self.frameDetails, text="Publication Name : ", font=('arial', 10, 'bold'), bd=10,
                                      bg="SkyBlue2", justify=LEFT)
            self.labelPubName.grid(row=2, column=0)
            self.labelPubLang = Label(self.frameDetails, text="Publication Language : ", font=('arial', 10, 'bold'),
                                      bd=10,
                                      bg="SkyBlue2", justify=LEFT)
            self.labelPubLang.grid(row=3, column=0)

            self.labelPubType = Label(self.frameDetails, text="Publication Type : ", font=('arial', 10, 'bold'), bd=10,
                                      bg="SkyBlue2", justify=LEFT)
            self.labelPubType.grid(row=4, column=0)

            self.labelPubPrice = Label(self.frameDetails, text="Publication Price : ", font=('arial', 10, 'bold'), bd=10,
                                      bg="SkyBlue2", justify=LEFT)
            self.labelPubPrice.grid(row=5, column=0)

            self.labelPrevPub = Label(self.frameDetails, text="Previous Values", font=('arial', 10, 'bold'), bd=10,
                                      bg="SkyBlue2", justify=LEFT)
            self.labelPrevPub.grid(row=0, column=1)

            self.labelPubID = Label(self.frameDetails, text=sPublications[pubName].paper_id, font=('arial', 10, 'bold'),
                                    bd=10,
                                    bg="SkyBlue2", justify=LEFT)
            self.labelPubID.grid(row=1, column=1)
            self.labelPubName = Label(self.frameDetails, text=sPublications[pubName].paper_name, font=('arial', 10, 'bold'), bd=10,
                                      bg="SkyBlue2", justify=LEFT)
            self.labelPubName.grid(row=2, column=1)
            self.labelPubLang = Label(self.frameDetails, text=sPublications[pubName].language, font=('arial', 10, 'bold'),
                                      bd=10,
                                      bg="SkyBlue2", justify=LEFT)
            self.labelPubLang.grid(row=3, column=1)
            self.labelPubType = Label(self.frameDetails, text=sPublications[pubName].paper_type, font=('arial', 10, 'bold'), bd=10,
                                      bg="SkyBlue2", justify=LEFT)
            self.labelPubType.grid(row=4, column=1)
            self.labelPubPrice = Label(self.frameDetails, text=sPublications[pubName].price, font=('arial', 10, 'bold'),
                                       bd=10,
                                       bg="SkyBlue2", justify=LEFT)
            self.labelPubPrice.grid(row=5, column=1)

            self.labelNewPub = Label(self.frameDetails, text="Change Values", font=('arial', 10, 'bold'), bd=10,
                                      bg="SkyBlue2", justify=LEFT)
            self.labelNewPub.grid(row=0, column=2)

            self.labelPubID = Label(self.frameDetails, text=sPublications[pubName].paper_id, font=('arial', 10, 'bold'),
                                    bd=10,
                                    bg="SkyBlue2", justify=LEFT)
            self.labelPubID.grid(row=1, column=2)

            self.labelPubLang = Label(self.frameDetails, text=sPublications[pubName].language,
                                      font=('arial', 10, 'bold'),
                                      bd=10,
                                      bg="SkyBlue2", justify=LEFT)
            self.labelPubLang.grid(row=3, column=2)
            self.labelPubType = Label(self.frameDetails, text=sPublications[pubName].paper_type,
                                      font=('arial', 10, 'bold'), bd=10,
                                      bg="SkyBlue2", justify=LEFT)
            self.labelPubType.grid(row=4, column=2)


            self.newpName = StringVar()
            self.eNewpName = Entry(self.frameDetails, width=15, font=('arial', 12), bg="white", fg="black", relief="solid",
                              borderwidth=1,
                              textvariable=self.newpName)
            self.eNewpName.grid(row=2, column=2, padx=10, pady=10)

            self.newpPrice = DoubleVar()
            self.eNewpPrice = Entry(self.frameDetails, width=5, font=('arial', 12), bg="white", fg="black",
                                   relief="solid",
                                   borderwidth=1,
                                   textvariable=self.newpPrice)
            self.eNewpPrice.grid(row=5, column=2, padx=10, pady=10)

            self.btnReset = Button(self.frameDetails, text="Reset", command=lambda: self.resetPub(),
                                    font=('arial', 12, 'bold'), width=10)
            self.btnReset.grid(row=3, column=4, padx=40)

            self.btnReturn = Button(self.frameDetails, text="Return", command=lambda: self.returnPub(),
                                    font=('arial', 12, 'bold'), width=10)
            self.btnReturn.grid(row=4, column=4, padx=40)

            self.btnSave = Button(self.frameDetails, text="Save", command=lambda: self.savePub(pubName),
                                  font=('arial', 12, 'bold'), width=10)
            self.btnSave.grid(row=5, column=4, padx=40)

    def resetPub(self):
        self.newpPrice.set(0.0)
        self.newpName.set("")

    def returnPub(self):
        self.reset()
        self.editPublication()

    def savePub(self, pubName):
        l = [i["PaperName"].lower() for i in publications_]
        if self.newpName.get().lower() in l:
            messagebox.showwarning("Publication exists", self.newpName.get()+ " already exists", parent=self.master)
            return
        sPublications[pubName].paper_name = self.newpName.get()
        sPublications[pubName].price = self.newpPrice.get()
        sPublications[self.newpName.get()]=sPublications[pubName]
        sPublications.pop(pubName)
        for i in publications_:
            if i["PaperName"] == pubName:
                i["PaperName"]=self.newpName.get()
                i["Price"] = self.newpPrice.get()
                break
        json.dump(publications_, open("./Data/Publications.json", "w"), indent=3, sort_keys=True)
        messagebox.showinfo("Success", "Publication edited Successfully", parent=self.master)
        self.editPublication()

    def dropDownPubForSub1(self):
        self.clickedPublication = StringVar()
        self.clickedPublication.set("Select Publication")
        self.publicationNames = []
        for i in publications_:
            if i["Language"].casefold() == self.v1.get().casefold():
                self.publicationNames.append(i["PaperName"])
        self.publicationsDrop.destroy()
        self.publicationsDrop = OptionMenu(self.frameEditPub, self.clickedPublication, *self.publicationNames)
        self.publicationsDrop.config(font=('arial', 10, 'bold'))
        self.publicationsDrop.grid(row=2, column=0, padx=10, columnspan=3)

    def editCustomer(self):
        self.reset()
        self.labelTitle = Label(self.frame2, text="Edit Customer Details", font=('arial', 15, 'bold'),
                                bd=20)
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=40)

        self.editFrame = Frame(self.frame2, width=542, height=70, bd=7, bg="SkyBlue2", relief='ridge', padx=12, pady=12)
        self.editFrame.grid(row=1, column=1)
        self.labelUser = Label(self.editFrame, text="Cutomer ID   ", font=('arial', 12, 'bold'), bg="SkyBlue2", bd=20)
        self.labelUser.grid(row=1, column=0, padx=20)
        self.editID = StringVar()
        self.eUsername = Entry(self.editFrame, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                               borderwidth=1,
                               textvariable=self.editID)
        self.eUsername.grid(row=2, column=0, padx=20)

        self.labelUser = Label(self.editFrame, text="Customer Name  ", font=('arial', 12, 'bold'), bg="SkyBlue2", bd=20)
        self.labelUser.grid(row=1, column=1, padx=20)
        self.editName = StringVar()
        self.eUsername = Entry(self.editFrame, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                               borderwidth=1,
                               textvariable=self.editName)
        self.eUsername.grid(row=2, column=1, padx=20)

        self.btnEditEnter = Button(self.editFrame, text="Enter", command=lambda: self.editDecide(),
                                   font=('arial', 12, 'bold'), width=20)
        self.btnEditEnter.grid(row=1, column=2, rowspan=2, padx=40, pady=25)


    def editDecide(self):
        flag = False
        if self.editName.get() == "" or self.editID.get() == "":
            messagebox.showwarning("Invalid Entries!", "Fill all boxes", parent=self.master)
            flag = True
        for i in customers_:
            if (i["CustomerName"] == self.editName.get() and i["CustomerID"] == self.editID.get()):
                flag = True
                self.displayButtons(i)
                break
        if flag == False:
            messagebox.showwarning("Invalid Entries!", "User Not Found", parent=self.master)

    def displayButtons(self, customer):
        self.btnEditAddress = Button(self.editFrame, text="Edit Address", command=lambda: self.editAddress(customer),
                                     font=('arial', 12, 'bold'), width=20)
        self.btnEditAddress.grid(row=3, column=0, pady=25)
        self.btnEditAdd = Button(self.editFrame, text="Add Subscriptions", command=lambda: self.addSubscriptions(customer),
                                 font=('arial', 12, 'bold'), width=20)
        self.btnEditAdd.grid(row=3, column=1, pady=25)
        self.btnEditDuration = Button(self.editFrame, text="Edit Duration", command=lambda: self.editDuration(customer),
                                      font=('arial', 12, 'bold'), width=20)
        self.btnEditDuration.grid(row=4, column=0, pady=25)
        self.btnEditCancel = Button(self.editFrame, text="Cancel Subscription",
                                    command=lambda: self.cancelSubscription(customer),
                                    font=('arial', 12, 'bold'), width=20)
        self.btnEditCancel.grid(row=4, column=1, pady=25)


    def editAddress(self, customer):
        self.reset()
        self.labelTitle = Label(self.frame2, text="Edit Address", font=('arial', 15, 'bold'), bd=20)
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=40)
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labelStreetNo = Label(self.frameDetails, text="Street No.", font=('arial', 10, 'bold'), bd=10,
                                   bg="SkyBlue2", justify=LEFT)
        self.labelStreetNo.grid(row=1, column=3)
        self.labelRoadNo = Label(self.frameDetails, text="Road No.", font=('arial', 10, 'bold'), bd=10,
                                 bg="SkyBlue2", justify=LEFT)
        self.labelRoadNo.grid(row=2, column=3)
        self.labelHouseNo = Label(self.frameDetails, text="House No.", font=('arial', 10, 'bold'), bd=10,
                                  bg="SkyBlue2", justify=LEFT)
        self.labelHouseNo.grid(row=3, column=3)
        # ====================            Previous Address        ===================================================================
        self.prevAddress = Label(self.frameDetails, text="Previous Address", font=('arial', 10, 'bold'), bd=10,
                                 bg="SkyBlue2", justify=LEFT)
        self.prevAddress.grid(row=0, column=4)

        self.labelPrevStreetNo = Label(self.frameDetails, text=customer["Address"][0], font=('arial', 10, 'bold'),
                                       bd=10,
                                       bg="SkyBlue2", justify=LEFT)
        self.labelPrevStreetNo.grid(row=1, column=4)

        self.labelPrevRoadNo = Label(self.frameDetails, text=customer["Address"][1], font=('arial', 10, 'bold'),
                                     bd=10,
                                     bg="SkyBlue2", justify=LEFT)
        self.labelPrevRoadNo.grid(row=2, column=4)

        self.labelPrevHouseNo = Label(self.frameDetails, text=customer["Address"][2], font=('arial', 10, 'bold'),
                                      bd=10,
                                      bg="SkyBlue2", justify=LEFT)
        self.labelPrevHouseNo.grid(row=3, column=4)

        # ====================            New Address        ========================================================
        self.prevAddress = Label(self.frameDetails, text="New Address", font=('arial', 10, 'bold'), bd=10,
                                 bg="SkyBlue2", justify=LEFT)
        self.prevAddress.grid(row=0, column=5)
        self.SNo = IntVar()
        self.eSNo = Entry(self.frameDetails, width=5, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.SNo)
        self.eSNo.grid(row=1, column=5, padx=10, pady=10)

        self.RNo = IntVar()
        self.eRNo = Entry(self.frameDetails, width=5, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.RNo)
        self.eRNo.grid(row=2, column=5, padx=10, pady=10)

        self.HNo = StringVar()
        self.eHNo = Entry(self.frameDetails, width=5, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.HNo)
        self.eHNo.grid(row=3, column=5, padx=10, pady=10)

        self.btnReturn = Button(self.frameDetails, text="Return", command=lambda: self.editCustomer(),
                                font=('arial', 12, 'bold'), width=10)
        self.btnReturn.grid(row=1, column=6, padx=40)

        self.btnAdd1 = Button(self.frameDetails, text="Edit Address", command=lambda: self.decideAddress(customer),
                              font=('arial', 12, 'bold'), width=20)
        self.btnAdd1.grid(row=2, column=6, padx=40)

    def decideAddress(self, customer):
        if self.SNo.get() == 0 or self.HNo.get() == 0 or self.HNo.get() == "":
            messagebox.showwarning("Invalid Entries!", "Fill all boxes", parent=self.master)
        else:
            self.changeAddress(customer)

    def changeAddress(self, customer):
        customer["Address"] = [self.SNo.get(), self.RNo.get(), self.HNo.get()]
        json.dump(customers_, open("./Data/CustomerDetails.json", "w"), indent=3, sort_keys=True)
        messagebox.showinfo("Success", "Address changed Successfully", parent=self.master)
        self.editCustomer()

    def editDuration(self, customer):
        self.reset()

        self.frameSubs = LabelFrame(self.frame2, text="Select Subscription", font=('arial', 12, 'bold'), padx=12)
        self.frameSubs.grid(row=3, column=0, pady=20)

        self.paperLanguage = Label(self.frameSubs, text="Language ", font=('arial', 12, 'bold'), bd=10)
        self.paperLanguage.grid(row=0, column=0)
        self.publicationNames = [""]
        self.v1 = StringVar(self.frameSubs, "English")
        self.clickedPublication = StringVar()
        self.clickedPublication.set("Select Publication")
        for i in customer["Subscriptions"]:
            if sPublications[i["name"]].language.casefold() == self.v1.get().casefold():
                self.publicationNames.append(i["name"])
        self.publicationsDrop2 = OptionMenu(self.frameSubs, self.clickedPublication, *self.publicationNames)

        Radiobutton(self.frameSubs, text="English", variable=self.v1, font=('arial', 10),
                    command=lambda: self.dropDownPubForSub2(customer),
                    value="English").grid(row=1, column=0)
        Radiobutton(self.frameSubs, text="Hindi", variable=self.v1, font=('arial', 10),
                    command=lambda: self.dropDownPubForSub2(customer),
                    value="Hindi").grid(row=1, column=1)
        Radiobutton(self.frameSubs, text="Telugu", variable=self.v1, font=('arial', 10),
                    command=lambda: self.dropDownPubForSub2(customer),
                    value="Telugu").grid(row=1, column=2)

        self.clickedPublication = StringVar()
        self.clickedPublication.set("Select Publication")
        self.publicationNames = []
        for i in customer["Subscriptions"]:
            if sPublications[i["name"]].language.casefold() == self.v1.get().casefold():
                # print(i["name"])
                self.publicationNames.append(i["name"])
        if len(self.publicationNames) != 0:
            self.publicationsDrop2 = OptionMenu(self.frameSubs, self.clickedPublication, *self.publicationNames)
            self.publicationsDrop2.config(font=('arial', 10, 'bold'))
            self.publicationsDrop2.grid(row=2, column=0, padx=10, columnspan=3)
        self.btnSelect = Button(self.frameSubs, text="Select", font=('arial', 12, 'bold'),
                                command=lambda: self.editDur(customer), width=20)
        self.btnSelect.grid(row=0, column=6, rowspan=2, padx=30)

    def editDur(self, customer):
        self.reset()
        self.labelTitle = Label(self.frame2, text="Edit Duration", font=('arial', 15, 'bold'), bd=20)
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=40)
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labelPubID = Label(self.frameDetails, text="Publication ID : ", font=('arial', 10, 'bold'), bd=10,
                                   bg="SkyBlue2", justify=LEFT)
        self.labelPubID.grid(row=1, column=3)
        self.labelPubName = Label(self.frameDetails, text="Publication Name : ", font=('arial', 10, 'bold'), bd=10,
                                 bg="SkyBlue2", justify=LEFT)
        self.labelPubName.grid(row=2, column=3)
        self.labelPubLang = Label(self.frameDetails, text="Publication Language : ", font=('arial', 10, 'bold'), bd=10,
                                  bg="SkyBlue2", justify=LEFT)
        self.labelPubLang.grid(row=3, column=3)


        # ====================            Previous Address        ===================================================================
        self.prevValues = Label(self.frameDetails, text="Previous Values", font=('arial', 10, 'bold'), bd=10,
                                 bg="SkyBlue2", justify=LEFT)
        self.prevValues.grid(row=0, column=4)

        self.labelPrevStreetNo = Label(self.frameDetails, text=customer["Address"][0], font=('arial', 10, 'bold'),
                                       bd=10,
                                       bg="SkyBlue2", justify=LEFT)
        self.labelPrevStreetNo.grid(row=1, column=4)

        self.labelPrevRoadNo = Label(self.frameDetails, text=customer["Address"][1], font=('arial', 10, 'bold'),
                                     bd=10,
                                     bg="SkyBlue2", justify=LEFT)
        self.labelPrevRoadNo.grid(row=2, column=4)

        self.labelPrevHouseNo = Label(self.frameDetails, text=customer["Address"][2], font=('arial', 10, 'bold'),
                                      bd=10,
                                      bg="SkyBlue2", justify=LEFT)
        self.labelPrevHouseNo.grid(row=3, column=4)

        # ====================            New Address        ========================================================
        self.prevAddress = Label(self.frameDetails, text="New Address", font=('arial', 10, 'bold'), bd=10,
                                 bg="SkyBlue2", justify=LEFT)
        self.prevAddress.grid(row=0, column=5)
        self.SNo = IntVar()
        self.eSNo = Entry(self.frameDetails, width=5, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.SNo)
        self.eSNo.grid(row=1, column=5, padx=10, pady=10)

        self.RNo = IntVar()
        self.eRNo = Entry(self.frameDetails, width=5, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.RNo)
        self.eRNo.grid(row=2, column=5, padx=10, pady=10)

        self.HNo = StringVar()
        self.eHNo = Entry(self.frameDetails, width=5, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.HNo)
        self.eHNo.grid(row=3, column=5, padx=10, pady=10)

        self.btnReturn = Button(self.frameDetails, text="Return", command=lambda: self.editCustomer(),
                                font=('arial', 12, 'bold'), width=10)
        self.btnReturn.grid(row=1, column=6, padx=40)

        self.btnAdd1 = Button(self.frameDetails, text="Edit Address", command=lambda: self.decideAddress(customer),
                              font=('arial', 12, 'bold'), width=20)
        self.btnAdd1.grid(row=2, column=6, padx=40)


    # def dropDownPubForSub2(self, customer):
    #     self.clickedPublication = StringVar()
    #     self.clickedPublication.set("Select Publication")
    #     self.publicationNames = []
    #     for i in customer["Subscriptions"]:
    #         if sPublications[i["name"]].language.casefold() == self.v1.get().casefold():
    #             self.publicationNames.append(i["name"])
    #     if len(self.publicationNames) != 0:
    #         self.publicationsDrop2 = OptionMenu(self.frameSubs, self.clickedPublication, *self.publicationNames)
    #         self.publicationsDrop2.config(font=('arial', 10, 'bold'))
    #         self.publicationsDrop2.grid(row=2, column=0, padx=10, columnspan=3)
    #     else:
    #         self.publicationsDrop2.destroy()
    #
    # def delSubscription(self, customer):
    #     if self.clickedPublication.get() == "Select Publication":
    #         messagebox.showwarning("Unselected Value!", "Select Publication!", parent=self.master)
    #     else:
    #         for i in range(len(customer["Subscriptions"])):
    #             if customer["Subscriptions"][i]["name"] == self.clickedPublication.get():
    #                 customer["Subscriptions"] = customer["Subscriptions"][:i] + customer["Subscriptions"][i + 1:]
    #                 json.dump(customers_, open("./Data/CustomerDetails.json", "w"), indent=3, sort_keys=True)
    #                 messagebox.showinfo("Success", "Subscription removed Successfully", parent=self.master)
    #                 break

    def addSubscriptions(self, customer):
        self.reset()
        self.labelTitle1 = Label(self.frame2, text="Add Subscription", font=('arial', 15, 'bold'),
                                 bd=20)
        self.labelTitle1.grid(row=0, column=0, columnspan=2, pady=40)

        self.frameSubs = LabelFrame(self.frame2, text="Add Subscriptions", font=('arial', 12, 'bold'), padx=12)
        self.frameSubs.grid(row=3, column=0, pady=20)

        self.paperLanguage1 = Label(self.frameSubs, text="Language ", font=('arial', 12, 'bold'), bd=10)
        self.paperLanguage1.grid(row=0, column=0)

        self.v1 = StringVar(self.frameSubs, "English")
        Radiobutton(self.frameSubs, text="English", variable=self.v1, font=('arial', 10),
                    command=lambda: self.dropDownPubForSub3(),
                    value="English").grid(row=1, column=0)
        Radiobutton(self.frameSubs, text="Hindi", variable=self.v1, font=('arial', 10),
                    command=lambda: self.dropDownPubForSub3(),
                    value="Hindi").grid(row=1, column=1)
        Radiobutton(self.frameSubs, text="Telugu", variable=self.v1, font=('arial', 10),
                    command=lambda: self.dropDownPubForSub3(),
                    value="Telugu").grid(row=1, column=2)

        self.clickedPublication = StringVar()
        self.clickedPublication.set("Select Publication")
        self.publicationNames = []
        for i in publications_:
            if i["Language"].casefold() == self.v1.get().casefold():
                self.publicationNames.append(i["PaperName"])
        self.publicationsDrop1 = OptionMenu(self.frameSubs, self.clickedPublication, *self.publicationNames)
        self.publicationsDrop1.config(font=('arial', 10, 'bold'))
        self.publicationsDrop1.grid(row=2, column=0, padx=10, columnspan=3)

        self.labelFromDate1 = Label(self.frameSubs, text="From Date", font=('arial', 12, 'bold'), bd=10,
                                    justify=LEFT)
        self.labelFromDate1.grid(row=1, column=4, padx=10)

        self.calFrom1 = DateEntry(self.frameSubs, width=12, background='darkblue',
                              foreground='white', borderwidth=2)
        self.calFrom1.grid(row=1, column=5, padx=10)

        self.labelToDate1 = Label(self.frameSubs, text="To Date", font=('arial', 12, 'bold'), bd=10,
                                  justify=LEFT)
        self.labelToDate1.grid(row=2, column=4, padx=10)

        self.calTo1 = DateEntry(self.frameSubs, width=12, background='darkblue',
                              foreground='white', borderwidth=2)
        self.calTo1.grid(row=2, column=5, padx=10)

        self.btnAdd1 = Button(self.frameSubs, text="Add", font=('arial', 12, 'bold'), width=20, command=lambda: self.editAdd(customer))
        self.btnAdd1.grid(row=0, column=6, rowspan=2, padx=30)

    def dropDownPubForSub3(self):
        self.clickedPublication = StringVar()
        self.clickedPublication.set("Select Publication")
        self.publicationNames = []
        for i in publications_:
            if i["Language"].casefold() == self.v1.get().casefold():
                self.publicationNames.append(i["PaperName"])
        self.publicationsDrop1.destroy()
        self.publicationsDrop1 = OptionMenu(self.frameSubs, self.clickedPublication, *self.publicationNames)
        self.publicationsDrop1.config(font=('arial', 10, 'bold'))
        self.publicationsDrop1.grid(row=2, column=0, padx=10, columnspan=3)

    def editAdd(self, customer):
        if self.calFrom1.get() == self.calTo1.get():
            messagebox.showwarning("From-date and To-date", "From-date and To-date cannot be same",
                                   parent=self.master)
        elif self.clickedPublication.get()=="Select Publication":
            messagebox.showwarning("Unselected Value!", "Select Publication!", parent=self.master)
        else:
            customer["Subscriptions"].append({"name":self.clickedPublication.get(), "from_date": self.calFrom1.get(), "to_date": self.calTo1.get()})
            json.dump(customers_, open("./Data/CustomerDetails.json", "w"), indent=3, sort_keys=True)
            messagebox.showinfo("Success", "Subscription added Successfully", parent=self.master)

    def cancelSubscription(self, customer):
        self.reset()
        self.labelTitle = Label(self.frame2, text="Cancel Subscription", font=('arial', 15, 'bold'),
                                bd=20)
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=40)
        self.frameSubs = LabelFrame(self.frame2, text="Cancel Subscriptions", font=('arial', 12, 'bold'), padx=12)
        self.frameSubs.grid(row=3, column=0, pady=20)

        self.paperLanguage = Label(self.frameSubs, text="Language ", font=('arial', 12, 'bold'), bd=10)
        self.paperLanguage.grid(row=0, column=0)
        self.publicationNames = [""]
        self.v1 = StringVar(self.frameSubs, "English")
        self.clickedPublication = StringVar()
        self.clickedPublication.set("Select Publication")
        for i in customer["Subscriptions"]:
            if sPublications[i["name"]].language.casefold() == self.v1.get().casefold():
                self.publicationNames.append(i["name"])
        self.publicationsDrop2 = OptionMenu(self.frameSubs, self.clickedPublication, *self.publicationNames)

        Radiobutton(self.frameSubs, text="English", variable=self.v1, font=('arial', 10),
                    command=lambda: self.dropDownPubForSub2(customer),
                    value="English").grid(row=1, column=0)
        Radiobutton(self.frameSubs, text="Hindi", variable=self.v1, font=('arial', 10),
                    command=lambda: self.dropDownPubForSub2(customer),
                    value="Hindi").grid(row=1, column=1)
        Radiobutton(self.frameSubs, text="Telugu", variable=self.v1, font=('arial', 10),
                    command=lambda: self.dropDownPubForSub2(customer),
                    value="Telugu").grid(row=1, column=2)

        self.clickedPublication = StringVar()
        self.clickedPublication.set("Select Publication")
        self.publicationNames = []
        for i in customer["Subscriptions"]:
            if sPublications[i["name"]].language.casefold() == self.v1.get().casefold():
                # print(i["name"])
                self.publicationNames.append(i["name"])
        if len(self.publicationNames) != 0:
            self.publicationsDrop2 = OptionMenu(self.frameSubs, self.clickedPublication, *self.publicationNames)
            self.publicationsDrop2.config(font=('arial', 10, 'bold'))
            self.publicationsDrop2.grid(row=2, column=0, padx=10, columnspan=3)
        self.cancelBtn = Button(self.frameSubs, text="Delete Subscription", font=('arial', 12, 'bold'),
                                command=lambda: self.delSubscription(customer), width=20)
        self.cancelBtn.grid(row=0, column=6, rowspan=2, padx=30)

    def dropDownPubForSub2(self,customer):
        self.clickedPublication = StringVar()
        self.clickedPublication.set("Select Publication")
        self.publicationNames = []
        for i in customer["Subscriptions"]:
            if sPublications[i["name"]].language.casefold() == self.v1.get().casefold():
                self.publicationNames.append(i["name"])
        if len(self.publicationNames) != 0:
            self.publicationsDrop2 = OptionMenu(self.frameSubs, self.clickedPublication, *self.publicationNames)
            self.publicationsDrop2.config(font=('arial', 10, 'bold'))
            self.publicationsDrop2.grid(row=2, column=0, padx=10, columnspan=3)
        else:
            self.publicationsDrop2.destroy()

    def delSubscription(self,customer):
        if self.clickedPublication.get() == "Select Publication":
            messagebox.showwarning("Unselected Value!", "Select Publication!", parent=self.master)
        else:
            for i in range(len(customer["Subscriptions"])):
                if customer["Subscriptions"][i]["name"] == self.clickedPublication.get():
                    customer["Subscriptions"]=customer["Subscriptions"][:i]+customer["Subscriptions"][i+1:]
                    json.dump(customers_, open("./Data/CustomerDetails.json", "w"), indent=3, sort_keys=True)
                    messagebox.showinfo("Success", "Subscription removed Successfully", parent=self.master)
                    break

    def customerBills(self):
        self.reset()
        self.labelTitle = Label(self.frame2, text="Edit Customer Details", font=('arial', 15, 'bold'),
                                bd=20)
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=40)


        self.labelUser = Label(self.frame2, text="Cutomer ID   ", font=('arial', 12, 'bold'), bd=20)
        self.labelUser.grid(row=1, column=0, padx=20)
        self.editID = StringVar()
        self.eUsername = Entry(self.frame2, width=30, font=('arial', 12), bg="gray80", fg="black", borderwidth=3,
                               textvariable=self.editID)
        self.eUsername.grid(row=2, column=0, padx=20)

        self.labelUser = Label(self.frame2, text="Customer Name  ", font=('arial', 12, 'bold'), bd=20)
        self.labelUser.grid(row=1, column=1, padx=20)
        self.editName = StringVar()
        self.eUsername = Entry(self.frame2, width=30, font=('arial', 12), bg="gray80", fg="black", borderwidth=3,
                               textvariable=self.editName)
        self.eUsername.grid(row=2, column=1, padx=20)

        self.btnEditEnter = Button(self.frame2, text="Enter", command=lambda: self.editDecide(Customer),
                                   font=('arial', 12, 'bold'), width=20)
        self.btnEditEnter.grid(row=1, column=2, rowspan=2, padx=40, pady=25)

    def summary(self):
        self.reset()
        self.frame1.destroy()

        # ====================            ADD CUST0MERS HEADING             ===================================================================================

        self.labelAddCustomers = Label(self.frame2, text="Summary of The Month", font=('arial', 17, 'bold'),
                                       bd=20)
        self.labelAddCustomers.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       CUSTOMER DETAILS FRAME            ===================================================================================

        self.frameDetails = Frame(self.frame2, width=1000, height=1000, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        # self.btnEditEnter = Button(self.frame2, text="Return", command=lambda: self.addCustomers(),
        #                            font=('arial', 12, 'bold'), width=20)
        # self.btnEditEnter.grid(row=0, column=2, padx=40, pady=25)

        self.labelName = Label(self.frameDetails, text="Full Name ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=0, column=0, rowspan=2)


        self.labelID = Label(self.frameDetails, text="Customer ID", font=('arial', 12, 'bold'), bd=10,
                             bg="SkyBlue2", justify=LEFT)
        self.labelID.grid(row=0, column=1, rowspan=2)


        self.labelPhoneNumber = Label(self.frameDetails, text="Phone Number", font=('arial', 12, 'bold'), bd=10,
                                      bg="SkyBlue2", justify=LEFT)
        self.labelPhoneNumber.grid(row=0, column=2, rowspan=2)
        # ====================            ADDRESS DETAILS            ===================================================================================

        self.labelAddress = Label(self.frameDetails, text="Address", font=('arial', 12, 'bold'), bd=20,
                                  bg="SkyBlue2")
        self.labelAddress.grid(row=0, column=3, columnspan=4)

        self.labelStreetNo = Label(self.frameDetails, text="Street No.", font=('arial', 10, 'bold'), bd=10,
                                   bg="SkyBlue2", justify=LEFT)
        self.labelStreetNo.grid(row=1, column=4)

        self.labelRoadNo = Label(self.frameDetails, text="Road No.", font=('arial', 10, 'bold'), bd=10,
                                 bg="SkyBlue2", justify=LEFT)
        self.labelRoadNo.grid(row=1, column=5)

        self.labelHouseNo = Label(self.frameDetails, text="House No.", font=('arial', 10, 'bold'), bd=10,
                                  bg="SkyBlue2", justify=LEFT)
        self.labelHouseNo.grid(row=1, column=6)
        # ====================            Subscriptions           ===================================================================================
        self.labelSubscriptions=Label(self.frameDetails, text="Subscription", font=('arial', 12, 'bold'), bd=20,
                                  bg="SkyBlue2")
        self.labelSubscriptions.grid(row=0,column=7,columnspan=6)

        self.labelSubscriptionsName=Label(self.frameDetails, text="Subscription Name", font=('arial', 10, 'bold'), bd=10,
                                   bg="SkyBlue2", justify=LEFT)
        self.labelSubscriptionsName.grid(row=1,column=7)

        self.labelSubscriptionsID = Label(self.frameDetails, text="Subscription ID", font=('arial', 10, 'bold'), bd=10,
                                            bg="SkyBlue2", justify=LEFT)
        self.labelSubscriptionsID.grid(row=1, column=8)

        self.labelSubscriptionsFromDate = Label(self.frameDetails, text="From Date", font=('arial', 10, 'bold'), bd=10,
                                            bg="SkyBlue2", justify=LEFT)
        self.labelSubscriptionsFromDate.grid(row=1, column=9)

        self.labelSubscriptionsToDate = Label(self.frameDetails, text="To Date", font=('arial', 10, 'bold'), bd=10,
                                            bg="SkyBlue2", justify=LEFT)
        self.labelSubscriptionsToDate.grid(row=1, column=10)

        ind=2

        for i in customers:
            flag=False
            for j in i.subscriptions:
                if j.from_date <= SetDate and j.to_date >= SetDate-datetime.timedelta(days=31):
                    flag=True
                    break
            if flag==True:
                self.labelSubscriptionsToDate = Label(self.frameDetails, text=i.name, font=('arial', 10, 'bold'), bd=10,
                                                      bg="SkyBlue2", justify=LEFT)
                self.labelSubscriptionsToDate.grid(row=ind, column=0)
                self.labelSubscriptionsToDate = Label(self.frameDetails, text=i.ID, font=('arial', 10, 'bold'), bd=10,
                                                      bg="SkyBlue2", justify=LEFT)
                self.labelSubscriptionsToDate.grid(row=ind, column=1)
                self.labelSubscriptionsToDate = Label(self.frameDetails, text=i.phone_number,
                                                      font=('arial', 10, 'bold'), bd=10,
                                                      bg="SkyBlue2", justify=LEFT)
                self.labelSubscriptionsToDate.grid(row=ind, column=2)
                self.labelSubscriptionsToDate = Label(self.frameDetails, text=i.address.street_number,
                                                      font=('arial', 10, 'bold'), bd=10,
                                                      bg="SkyBlue2", justify=LEFT)
                self.labelSubscriptionsToDate.grid(row=ind, column=4)
                self.labelSubscriptionsToDate = Label(self.frameDetails, text=i.address.road_number,
                                                      font=('arial', 10, 'bold'), bd=10,
                                                      bg="SkyBlue2", justify=LEFT)
                self.labelSubscriptionsToDate.grid(row=ind, column=5)
                self.labelSubscriptionsToDate = Label(self.frameDetails, text=i.address.house_number,
                                                      font=('arial', 10, 'bold'), bd=10,
                                                      bg="SkyBlue2", justify=LEFT)
                self.labelSubscriptionsToDate.grid(row=ind, column=6)
                for j in i.subscriptions:
                    if j.from_date <= SetDate and j.to_date >= SetDate-datetime.timedelta(days=31):
                        self.labelSubscriptionsToDate = Label(self.frameDetails, text=j.publication.paper_name,
                                                              font=('arial', 10, 'bold'), bd=10,
                                                              bg="SkyBlue2", justify=LEFT)
                        self.labelSubscriptionsToDate.grid(row=ind, column=7)
                        self.labelSubscriptionsToDate = Label(self.frameDetails, text=j.publication.paper_id,
                                                              font=('arial', 10, 'bold'), bd=10,
                                                              bg="SkyBlue2", justify=LEFT)
                        self.labelSubscriptionsToDate.grid(row=ind, column=8)
                        format="%d/%m/%Y"
                        # now=date.today()
                        now=j.from_date
                        j.from_date=now.strftime(format)
                        self.labelSubscriptionsToDate = Label(self.frameDetails, text=j.from_date,
                                                              font=('arial', 10, 'bold'), bd=10,
                                                              bg="SkyBlue2", justify=LEFT)
                        self.labelSubscriptionsToDate.grid(row=ind, column=9)
                        now=j.to_date
                        j.to_date=now .strftime(format)
                        self.labelSubscriptionsToDate = Label(self.frameDetails, text=j.to_date,
                                                              font=('arial', 10, 'bold'), bd=10,
                                                              bg="SkyBlue2", justify=LEFT)
                        self.labelSubscriptionsToDate.grid(row=ind, column=10)
                        ind = ind + 1


                # if j.from_date<SetDate:
                #     print(SetDate-j.from_date)
                #     print(j.from_date)
            ind = ind + 1
        pass

    def addDeliverer(self):
        self.reset()

        self.labelAddDeliverer = Label(self.frame2, text="Add Deliverer", font=('arial', 17, 'bold'),
                                       bd=20)
        self.labelAddDeliverer.grid(row=0, column=0, columnspan=2, pady=40)

        # ====================       CUSTOMER DETAILS FRAME            ===================================================================================

        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labelName = Label(self.frameDetails, text="Deliverer Name ", font=('arial', 12, 'bold'), bd=10,
                               bg="SkyBlue2", justify=LEFT)
        self.labelName.grid(row=0, column=0, rowspan=2)
        self.name = StringVar()
        self.eName = Entry(self.frameDetails, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                           borderwidth=1,
                           textvariable=self.name)
        self.eName.grid(row=2, column=0, padx=10)

        self.labelID = Label(self.frameDetails, text="Deliverer ID", font=('arial', 12, 'bold'), bd=10,
                             bg="SkyBlue2", justify=LEFT)
        self.labelID.grid(row=0, column=1, rowspan=2)
        self.cID = StringVar()
        self.ecID = Entry(self.frameDetails, width=12, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.cID)
        self.ecID.grid(row=2, column=1, padx=10)

        self.labelPassword = Label(self.frameDetails, text="Deliverer Password", font=('arial', 12, 'bold'), bd=10,
                                   bg="SkyBlue2", justify=LEFT)
        self.labelPassword.grid(row=0, column=2, rowspan=2)
        self.password = StringVar()
        self.epassword = Entry(self.frameDetails, width=12, font=('arial', 12), bg="white", fg="black", relief="solid",
                               borderwidth=1,
                               textvariable=self.password)
        self.epassword.grid(row=2, column=2, padx=10)

        self.btnAdd = Button(self.frameDetails, text="Add", font=('arial', 12, 'bold'), width=10)
        self.btnAdd.grid(row=2, column=6, padx=30)


    def addDelDet(self):

        if self.password.get() == "" or self.cID.get() == "" or self.name.get() == "":
            messagebox.showwarning("Empty Entries!", "Fill all the Entries", parent=self.master)
        elif self.cID.get() in IDs:
            messagebox.showerror("Unique IDs", "Enter a unique ID", parent=self.master)
        else:
            IDs.append(self.cID.get())
            deliverers_.append({"Username":  self.name.get(), "UserID":  self.cID.get(), "Password": self.password.get()})
            json.dump(deliverers_, open("./Data/DelivererDetails.json", "w"), indent=3, sort_keys=True)
            messagebox.showinfo("Success", "Deliverer added successfully", parent=self.master)

    def delivererDetails(self):
        self.reset()

        self.labelAddDeliverer = Label(self.frame2, text="Deliverers Details", font=('arial', 17, 'bold'),
                                       bd=20)
        self.labelAddDeliverer.grid(row=0, column=0, columnspan=2, pady=40)

        self.frameDetails = Frame(self.frame2, width=1000, height=1000, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)

        self.labeldName = Label(self.frameDetails, text="Deliverer Name", font=('arial', 10, 'bold'), bd=10,
                                   bg="SkyBlue2", justify=LEFT)
        self.labeldName.grid(row=0, column=0)
        self.dName = StringVar()
        self.edName = Entry(self.frameDetails, width=12, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.dName)
        self.edName.grid(row=0, column=1, padx=10)


        self.labeldID = Label(self.frameDetails, text="Deliverer ID", font=('arial', 10, 'bold'), bd=10,
                                   bg="SkyBlue2", justify=LEFT)
        self.labeldID.grid(row=1, column=0)

        self.dID = StringVar()
        self.edID = Entry(self.frameDetails, width=12, font=('arial', 12), bg="white", fg="black", relief="solid",
                          borderwidth=1,
                          textvariable=self.dID)
        self.edID.grid(row=1, column=1, padx=10)

        self.btndEnter = Button(self.frameDetails, text="Enter", command=lambda: self.dDecide(),
                                   font=('arial', 12, 'bold'), width=20)
        self.btndEnter.grid(row=1, column=2, rowspan=2, padx=40, pady=25)

    def dDecide(self):
        flag = False
        if self.dName.get() == "" or self.dID.get() == "":
            messagebox.showwarning("Invalid Entries!", "Fill all boxes", parent=self.master)
            flag = True
        for i in deliverers_:
            if (i["Username"] == self.dName.get() and i["UserID"] == self.dID.get()):
                flag = True
                self.dDetails(i["Username"])
                break
        if flag == False:
            messagebox.showwarning("Invalid Entries!", "User Not Found", parent=self.master)

    def dDetails(self, deliverer):
        self.wage = 0
        for i in deliverers:
            if i.name == deliverer:
                for j in i.Customers:
                    for k in j.subscriptions:
                        if k.from_date <= SetDate and k.to_date >= SetDate:
                            self.wage+=0.025*k.publication.price
        self.labelWage = Label(self.frameDetails, text="Today's Wage : "+str(self.wage), font=('arial', 12, 'bold'), bg="SkyBlue2", bd=20)
        self.labelWage.grid(row=2, column=1, padx=20)

    def customerBills(self):
        self.reset()
        self.labelTitle = Label(self.frame2, text="Customer bills", font=('arial', 15, 'bold'),
                                bd=20)
        self.labelTitle.grid(row=0, column=0, columnspan=2, pady=40)

        self.editFrame = Frame(self.frame2, width=542, height=70, bd=7, bg="SkyBlue2", relief='ridge', padx=12, pady=12)
        self.editFrame.grid(row=1, column=1)
        self.labelUser = Label(self.editFrame, text="Cutomer ID   ", font=('arial', 12, 'bold'), bg="SkyBlue2", bd=20)
        self.labelUser.grid(row=1, column=0, padx=20)
        self.editID = StringVar()
        self.eUsername = Entry(self.editFrame, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                               borderwidth=1,
                               textvariable=self.editID)
        self.eUsername.grid(row=2, column=0, padx=20)

        self.labelUser = Label(self.editFrame, text="Customer Name  ", font=('arial', 12, 'bold'), bg="SkyBlue2", bd=20)
        self.labelUser.grid(row=1, column=1, padx=20)
        self.editName = StringVar()
        self.eUsername = Entry(self.editFrame, width=30, font=('arial', 12), bg="white", fg="black", relief="solid",
                               borderwidth=1,
                               textvariable=self.editName)
        self.eUsername.grid(row=2, column=1, padx=20)

        self.btnEditEnter = Button(self.editFrame, text="Enter", command=lambda: self.editDecide2(),
                                   font=('arial', 12, 'bold'), width=20)
        self.btnEditEnter.grid(row=1, column=2, rowspan=2, padx=40, pady=25)

    def editDecide2(self):
        flag = False
        if self.editName.get() == "" or self.editID.get() == "":
            messagebox.showwarning("Invalid Entries!", "Fill all boxes", parent=self.master)
            flag = True

        for i in customers_:
            if (i["CustomerName"] == self.editName.get() and i["CustomerID"] == self.editID.get()):
                flag = True

                self.displaySubscription(i)
                break
        if flag == False:
            messagebox.showwarning("Invalid Entries!", "User Not Found", parent=self.master)

    def displaySubscription(self, customer):
        self.reset()
        self.labelAddCustomers = Label(self.frame2, text="Customer Bills", font=('arial', 17, 'bold'),
                                       bd=20)
        self.labelAddCustomers.grid(row=0, column=0, columnspan=2, pady=40)
        self.frameDetails = Frame(self.frame2, width=1000, height=100, bd=7, relief='ridge',
                                  bg="SkyBlue2")
        self.frameDetails.grid(row=1, column=0)
        self.subscriptionDetails = LabelFrame(self.frame2, text="Subscriptions", width=1000, height=100, bd=7,
                                              relief='ridge')
        self.subscriptionDetails.grid(row=2, column=0)
        self.labelName = Label(self.frameDetails, text="Full Name ", font=('arial', 12, 'bold'), bd=10, bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=0, column=0)
        self.labelName = Label(self.frameDetails, text=customer["CustomerName"], font=('arial', 12, 'bold'), bd=10,
                               bg="SkyBlue2",
                               justify=LEFT)
        self.labelName.grid(row=0, column=1)
        self.labelID = Label(self.frameDetails, text="Customer ID", font=('arial', 12, 'bold'), bd=10,
                             bg="SkyBlue2", justify=LEFT)
        self.labelID.grid(row=1, column=0)
        self.labelID = Label(self.frameDetails, text=customer["CustomerID"], font=('arial', 12, 'bold'), bd=10,
                             bg="SkyBlue2", justify=LEFT)
        self.labelID.grid(row=1, column=1)

        self.labelPhoneNumber = Label(self.frameDetails, text="Phone Number", font=('arial', 12, 'bold'), bd=10,
                                      bg="SkyBlue2", justify=LEFT)
        self.labelPhoneNumber.grid(row=2, column=0)
        self.labelPhoneNumber = Label(self.frameDetails, text=customer["PhoneNumber"], font=('arial', 12, 'bold'),
                                      bd=10,
                                      bg="SkyBlue2", justify=LEFT)
        self.labelPhoneNumber.grid(row=2, column=1)
        # ====================            Subscriptions          ===================================================================================

        self.labelSubscriptionsName = Label(self.subscriptionDetails, text="Subscription Name",
                                            font=('arial', 10, 'bold'),
                                            bd=10,
                                            justify=LEFT)
        self.labelSubscriptionsName.grid(row=0, column=0)

        self.labelSubscriptionsID = Label(self.subscriptionDetails, text="Subscription ID", font=('arial', 10, 'bold'),
                                          bd=10,
                                          justify=LEFT)
        self.labelSubscriptionsID.grid(row=0, column=1)

        self.labelSubscriptionsFromDate = Label(self.subscriptionDetails, text="From Date", font=('arial', 10, 'bold'),
                                                bd=10,
                                                justify=LEFT)
        self.labelSubscriptionsFromDate.grid(row=0, column=2)

        self.labelSubscriptionsToDate = Label(self.subscriptionDetails, text="To Date", font=('arial', 10, 'bold'),
                                              bd=10,
                                              justify=LEFT)
        self.labelSubscriptionsToDate.grid(row=0, column=3)
        self.labelSubscriptionsToDate = Label(self.subscriptionDetails, text="Paper Price", font=('arial', 10, 'bold'),
                                              bd=10, justify=LEFT)
        self.labelSubscriptionsToDate.grid(row=0, column=4)
        self.labelSubscriptionsToDate = Label(self.subscriptionDetails, text="Duration", font=('arial', 10, 'bold'),
                                              bd=10, justify=LEFT)
        self.labelSubscriptionsToDate.grid(row=0, column=5)
        self.labelSubscriptionsToDate = Label(self.subscriptionDetails, text="Amount", font=('arial', 10, 'bold'),
                                              bd=10, justify=LEFT)
        self.labelSubscriptionsToDate.grid(row=0, column=6)

        customer2 = []
        for i in customers:
            if customer["CustomerName"] == i.name:
                customer2 = i
                break
        ind = 1
        TotalCost = 0.0
        for i in customer2.subscriptions:
            self.labelSubscriptionsToDate = Label(self.subscriptionDetails, text=i.publication.paper_name,
                                                  font=('arial', 10, 'bold'),
                                                  bd=10, justify=LEFT)
            self.labelSubscriptionsToDate.grid(row=ind, column=0)
            self.labelSubscriptionsToDate = Label(self.subscriptionDetails, text=i.publication.paper_id,
                                                  font=('arial', 10, 'bold'),
                                                  bd=10, justify=LEFT)
            self.labelSubscriptionsToDate.grid(row=ind, column=1)
            duration = SetDate - i.from_date
            format = "%d/%m/%Y"
            # now=date.today()
            now = i.from_date
            i.from_date = now.strftime(format)
            self.labelSubscriptionsToDate = Label(self.subscriptionDetails, text=i.from_date,
                                                  font=('arial', 10, 'bold'),
                                                  bd=10, justify=LEFT)
            self.labelSubscriptionsToDate.grid(row=ind, column=2)
            format = "%d/%m/%Y"
            now = date.today()
            now = SetDate
            now = now.strftime(format)
            self.labelSubscriptionsToDate = Label(self.subscriptionDetails, text=now, font=('arial', 10, 'bold'),
                                                  bd=10, justify=LEFT)
            self.labelSubscriptionsToDate.grid(row=ind, column=3)

            # duration = i.to_date - no
            duration = duration.days
            temp = i.publication.price
            cost = 0.0
            if i.publication.paper_type == "Magazine":
                cost = temp * int(duration / 7)
                temp = str(temp)
                temp = temp + "\week"
            else:
                cost = temp * duration
                temp = str(temp)
                temp = temp + "\day"
            TotalCost = TotalCost + cost
            self.labelSubscriptionsToDate = Label(self.subscriptionDetails, text=temp, font=('arial', 10, 'bold'),
                                                  bd=10, justify=LEFT)
            self.labelSubscriptionsToDate.grid(row=ind, column=4)
            duration = str(duration)
            duration = duration + 'days'
            self.labelSubscriptionsToDate = Label(self.subscriptionDetails, text=duration, font=('arial', 10, 'bold'),
                                                  bd=10, justify=LEFT)
            self.labelSubscriptionsToDate.grid(row=ind, column=5)
            self.labelSubscriptionsToDate = Label(self.subscriptionDetails, text=cost, font=('arial', 10, 'bold'),
                                                  bd=10, justify=LEFT)
            self.labelSubscriptionsToDate.grid(row=ind, column=6)
            ind = ind + 1
        self.labelSubscriptionsToDate = Label(self.subscriptionDetails, text="TOTAL COST", font=('arial', 10, 'bold'),
                                              bd=10, justify=LEFT)
        self.labelSubscriptionsToDate.grid(row=ind, column=5)
        self.labelSubscriptionsToDate = Label(self.subscriptionDetails, text=TotalCost, font=('arial', 10, 'bold'),
                                              bd=10, justify=LEFT)
        self.labelSubscriptionsToDate.grid(row=ind, column=6)
        self.labelSubscriptionsToDate = Button(self.subscriptionDetails, text="PAID", font=('arial', 10, 'bold'),
                                               bd=10, width=10, bg="SkyBlue2", command=lambda: self.changeFromDate(i),
                                               justify=LEFT)
        self.labelSubscriptionsToDate.grid(row=ind + 1, column=5)
        self.labelSubscriptionsToDate = Button(self.subscriptionDetails, text="EXIT", font=('arial', 10, 'bold'),
                                               bd=10, width=10, bg="SkyBlue2", command=lambda: self.clear(),
                                               justify=LEFT)
        self.labelSubscriptionsToDate.grid(row=ind + 1, column=6)

    def clear(self):
        self.reset()


class DelivererWindow:
    def __init__(self, master, deliverer):
        self.master = master
        self.master.title("Deliverer Page")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        # ====================             FRAMES             ===================================================================================

        self.frame1 = Frame(self.frame, width=1350, height=750, bd=7, relief='ridge', bg="SkyBlue2")
        self.frame1.grid(row=0, column=0, sticky="news")

        # ====================             LABELS              ===================================================================================

        self.labelCustomerName = Label(self.frame1, text="Customer Name", font=('arial', 10, 'bold'),bg="Skyblue2",
                                       bd=20)
        self.labelCustomerName.grid(row=0, column=0, padx=10, pady=5)

        self.labelPhoneNum = Label(self.frame1, text="Customer Phone Number", font=('arial', 10, 'bold'),bg="Skyblue2",
                                       bd=20)
        self.labelPhoneNum.grid(row=0, column=1, padx=10, pady=5)

        self.labelStreetNum = Label(self.frame1, text="Street No", font=('arial', 10, 'bold'),bg="Skyblue2",
                                       bd=20)
        self.labelStreetNum.grid(row=0, column=2, padx=10, pady=5)

        self.labelRoadNum = Label(self.frame1, text="Road No", font=('arial', 10, 'bold'), bg="Skyblue2",
                                   bd=20)
        self.labelRoadNum.grid(row=0, column=3, padx=10, pady=5)

        self.labelHouseNum = Label(self.frame1, text="House No", font=('arial', 10, 'bold'), bg="Skyblue2",
                                       bd=20)
        self.labelHouseNum.grid(row=0, column=4, padx=10, pady=5)

        self.labelCustomerSub = Label(self.frame1, text="Subscription", font=('arial', 10, 'bold'), bg="Skyblue2",
                                       bd=20)
        self.labelCustomerSub.grid(row=0, column=5, padx=10, pady=5)

        self.labelTFare = Label(self.frame1, text="Total Fare", font=('arial', 10, 'bold'), bg="Skyblue2",
                                   bd=20)
        self.labelTFare.grid(row=0, column=6, padx=10, pady=5)

        # =========================================Printing Details =================================================
        k=0
        for i in deliverer.Customers:
            self.labelcustomerN = Label(self.frame1, text=i.name, font=('arial', 10, 'bold'),bg="Skyblue2",
                                           bd=20)
            self.labelcustomerN.grid(row=k+1, column=0, padx=10)

            self.labelcustomerPh = Label(self.frame1, text=i.phone_number, font=('arial', 10, 'bold'),width=15,bg="Skyblue2",
                                       bd=20)
            self.labelcustomerPh.grid(row=k+1, column=1, padx=10)

            self.labelcustomerSt = Label(self.frame1, text=i.address.street_number, font=('arial', 10, 'bold'),bg="Skyblue2",
                                         bd=20)
            self.labelcustomerSt.grid(row=k + 1, column=2, padx=10)

            self.labelcustomerRd = Label(self.frame1, text=i.address.road_number, font=('arial', 10, 'bold'),bg="Skyblue2",
                                         bd=20)
            self.labelcustomerRd.grid(row=k + 1, column=3, padx=10)

            self.labelcustomerHs = Label(self.frame1, text=i.address.house_number, font=('arial', 10, 'bold'),bg="Skyblue2",
                                         bd=20)
            self.labelcustomerHs.grid(row=k + 1, column=4, padx=10)

            for j in i.subscriptions :
                self.labelcustomerSub = Label(self.frame1, text=j.publication.paper_name, font=('arial', 10, 'bold'),
                                             bg="Skyblue2",
                                             bd=20)
                self.labelcustomerSub.grid(row=k + 1, column=5, padx=10)
                k=k+1



# def compare(c1, c2):
#     l1 = [c1.address.street_number, c1.address.road_number, c1.address.house_number]
#     l2 = [c2.address.street_number, c2.address.road_number, c2.address.house_number]
#     return l1<l2
#
# def compare1(c1, c2):
#     return c1["Address"]<c2["Address"]
SetDate = date.today()

IDs = []
manager_ = json.load(open("./Data/ManagerDetails.json"))
manager = Manager(manager_["UserID"],manager_["Username"],manager_["Password"])
IDs.append(manager_["UserID"])

languages = json.load(open("./Data/Languages.json"))


publications_ = json.load(open("./Data/Publications.json"))
sPublications = {}
publications = []
for i in publications_:
    publications.append(Publication(i["PaperID"],i["PaperName"],i["PaperType"],i["Language"],i["Price"]))
    IDs.append(i["PaperID"])
for i in publications:
    sPublications[i.paper_name] = i
customers_ = json.load(open("./Data/CustomerDetails.json"))
print(customers_)
customers_ = sorted(customers_, key=lambda i: i["Address"])
print(customers_)

customers = []
for i in customers_:
    IDs.append(i["CustomerID"])
    subscriptions = []
    for j in i["Subscriptions"]:
        t = j["to_date"].split("/")
        t = [int(k) for k in t]
        f = j["from_date"].split("/")
        f = [int(k) for k in f]
        subscriptions.append(Subscription(sPublications[j["name"]], date(2000+f[2],f[0],f[1]), date(2000+t[2],t[0],t[1])))
    customers.append(Customer(i['CustomerID'], i["CustomerName"], Address(i["Address"][0],i["Address"][1],i["Address"][2]), i["PhoneNumber"], subscriptions))

for i in customers:
    print(i.address)
    for j in i.subscriptions:
        print(j.from_date.strftime("%d/%m/%Y"))


deliverers_ = json.load(open("./Data/DelivererDetails.json"))
deliverers = []
countDeliverers = 0
for i in deliverers_:
    deliverers.append(Deliverer(i["UserID"],i["Username"],i["Password"]))
    IDs.append(i["UserID"])
    countDeliverers+=1

factor = len(customers)//countDeliverers
r = len(customers)%countDeliverers
l = [0 for i in range(countDeliverers+1)]
for i in range(r):
    l[i+1]+=1
for i in range(countDeliverers):
    l[i+1]+=factor
for i in range(countDeliverers):
    l[i+1]+=l[i]
for i in range(countDeliverers):
    deliverers[i].Customers = customers[l[i]:l[i+1]]


def main():
    root1 = Tk()
    app = MainWindow(root1)
    d={}
    # print(datetime.date(2002, 12, 2))
    # d['date'] = str(datetime.date(2002, 12, 2))
    """
    root1.title("Login Page")
    root1.geometry('1350x750+0+0')
    Grid.rowconfigure(root1, 0, weight=1)
    Grid.columnconfigure(root1, 0, weight=1)
    label1 = Label(root1, text="Select your role")
    label1.grid(row=0, column=0, sticky="NEWS")

    buttonManager = Button(root1, text="MANAGER",command=lambda:ManagerPage())
    buttonManager.grid(row=1, column=0, sticky="NEWS")

    buttonDeliverer = Button(root1, text="DELIVERER")
    buttonDeliverer.grid(row=2, column=0, sticky="NEWS")

    root1.mainloop()
    """
if __name__ == '__main__':
    main()


