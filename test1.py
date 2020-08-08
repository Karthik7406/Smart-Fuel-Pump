# =====SMART FUEL PUMP SYSTEM=============

# ======================importing dependencies======================
import tkinter as tk
from tkinter import ttk
# import numpy as np
from tkinter import messagebox
import time

LARGE_FONT = ("Helvetica", 25, 'bold italic')


# ========================DATABASE======================


def save_database(dictionary):
    try:
        f1 = open('database.txt', 'w')
        for x, y in dictionary.items():
            #f1.write(f'{x} {y[0]} {y[1]} \n')
            f1.write('{0} {1} {2} \n'.format(x, y[0], y[1]))

    finally:
        f1.close()


def load_database():
    d = {}
    with open("/home/pi/Desktop/final/Smart-Fuel-Pump/database..txt") as f:
        for line in f:
            key, val, amount = line.split()
            d[key] = [val, amount]
    return d


# load the database using load_database function
DATABASE = load_database()
print(DATABASE)

# =================GLOBAL VARIABLES=============
matched = 0
current_user_name = None


#

#
# ======================================================

#

# =================Application class( Main class) ======================


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Smart Fuel Pump System")

        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # self.von_ueberall_erreichbar = 0
        self.frames = {}

        for F in (StartPage, PageOne, PageTwo, Add_new_user, PetrolFrame, DeisalFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)
        '''
    def getVUE(self):
        return self.von_ueberall_erreichbar

    def raiseVUE(self, targetFrame):
        self.von_ueberall_erreichbar += 1
        self.frames[targetFrame].label2.config(text=self.getVUE())'''

    def show_frame(self, targetFrame):
        frame = self.frames[targetFrame]
        # self.frames[targetFrame].label2.config(text=self.getVUE())
        frame.tkraise()


#

# ==========Password verification==============

def password_verify(name, key, label):
    global matched
    users_data = DATABASE

    if users_data[name][0] == key:
        label.configure(text='Passwords Matched', fg='black', bg='green')
        print('PASSWORD MATCHED')
        matched = 1
        return 'PASSWORD MATCHED'
    elif users_data[name][0] != key:
        print('users_data[name] == ', users_data[name], '\n', 'key=', key)
        print('Name', name)
        label.configure(text='Passwords Donot Match', bg='red')
        print('PASSWORDS DONOT MATCH')
        matched = 0
        return 'PASSWORD DONOT MATCH, PLEASE TRY AGAIN'


#


def pass_label(matched):
    print("PaSS label function")
    if matched == 0:
        messagebox.showinfo('Passwords donot match')
        return 'Passwords Donot Match'

    elif matched == 1:
        messagebox.showinfo('Passwords  match')
        return 'Passwords matched'


def create_user(name, password, amount):
    global DATABASE
    user_name = name.get()
    user_password = password.get()
    user_amount = amount.get()

    if user_name in DATABASE.keys():
        print('User Already Exists')

    else:
        DATABASE[user_name] = [user_password, user_amount]
        print(DATABASE)
        save_database(DATABASE)


#

# ===================Adding new user to the database======================

class Add_new_user(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label11 = tk.Label(self, text='Adding New User', font=('Helvetica', 30, 'bold italic'),
                           fg='blue', bg='cyan')
        label11.pack(padx=5, pady=1)

        name_entry_label = tk.Label(self, text='USERNAME', font=('Helvetica', 20, 'bold italic'),
                                    fg='black', bg='cyan')
        name_entry_label.place(x=50, y=60)

        name_entry_widget = tk.Entry(self, bg='cyan', font=('Helvetica', 20, 'bold italic'))
        name_entry_widget.place(x=180, y=60, height=40)

        password_entry_label = tk.Label(self, text='PASSWORD', font=('Helvetica', 20, 'bold italic'),
                                        fg='black', bg='cyan')
        password_entry_label.place(x=50, y=110)

        password_entry_widget = tk.Entry(self, bg='yellow', font=('Helvetica', 30, 'bold italic'), width=15)
        password_entry_widget.place(x=180, y=110, height=40)

        amount_entry_label = tk.Label(self, text='Initial Amount', font=('Helvetica', 20, 'bold italic'),
                                      fg='black', bg='cyan')
        amount_entry_label.place(x=10, y=180)

        amount_entry_widget = tk.Entry(self, font=('Helvetica', 30, 'bold italic'), width=15)
        amount_entry_widget.place(x=220, y=180)

        sel_button = tk.Button(self, text='CREATE USER', font=('Helvetica', 20, 'bold italic'),
                               fg='brown', bg='magenta',
                               command=lambda: create_user(name_entry_widget, password_entry_widget,
                                                           amount_entry_widget))
        sel_button.place(x=200, y=240)

        button1 = tk.Button(self, text="Back to Home", bg='lightgreen',
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=450, y=400)


#

# ============Main page========================

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='steel blue')
        text1 = 'Smart Automatic Fuel System'
        label = tk.Label(self, text=text1, font=('Helvetica', 35, 'bold italic'), fg='blue', bg='yellow')
        label.pack(pady=10, padx=10)

        # self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        # self.label2.pack(pady=10, padx=10)

        label2 = tk.Label(self, text='Petrol Price Today ==>', font=('Helvetica', 20, 'bold italic'), fg='green',
                          bg='cyan')
        label2.place(x=30, y=80)

        petrol_price = 75
        petrol_price_label = tk.Label(self, text=str(petrol_price), font=('Helvetica', 20, 'bold italic'), fg='red',
                                      bg='cyan')
        petrol_price_label.place(x=380, y=80)

        label3 = tk.Label(self, text='Deisel Price Today ==>', font=('Helvetica', 20, 'bold italic'), fg='red',
                          bg='cyan')
        label3.place(x=30, y=120)

        diesel_price = 75
        diesel_price_label = tk.Label(self, text=str(diesel_price), font=('Helvetica', 20, 'bold italic'), fg='red',
                                      bg='cyan')
        diesel_price_label.place(x=380, y=120)
        text2 = 'Please scan Your RFID card'
        rfid_card_info = tk.Label(self, text=text2, font=('Helvetica', 20, 'bold italic'), fg='red')
        text3 = 'Press Here to Scan the RFID card'

        scan_button = tk.Button(self, text=text3, bg='magenta', font=('Helvetica', 16, 'bold italic'),
                                command=lambda: controller.show_frame(PageOne))
        scan_button.place(x=200, y=180)

        new_user_button = tk.Button(self, text='Add New User', font=('Helvetica', 25, 'bold italic'),
                                    fg='black', bg='yellow', command=lambda: controller.show_frame(Add_new_user))
        new_user_button.place(x=550, y=300)
        '''
        button2 = ttk.Button(self, text="Visit Page 2",
                             command=lambda: controller.show_frame(PageTwo))
        button2.pack()

        button3 = ttk.Button(self, text="+1",
                             command=lambda: controller.raiseVUE(StartPage))
        button3.pack()'''


def rfid():
    print('Executing rfid function')
    num = int(input('Enter the number'))
    list1 = ['karthik', 'hari', 'dennis']
    username = list1[num - 1]
    return username


def show_entry_feilds(entry):
    value = entry.get()

    print("Entered Value = ", entry.get())
    return value


def verify(self, controller):
    global matched

    if matched == 0:
        self.button2.configure(bg='red')
    if matched == 1:
        self.button2.configure(bg='green', command=lambda: controller.show_frame(PageTwo))


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='cyan')

        label = ttk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        # self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        # self.label2.pack(pady=10, padx=10)

        username_label = lambda: rfid()
        name = username_label()
        global current_user_name
        global matched
        current_user_name = name
        label4 = tk.Label(self, text='Hello!' + '   ' + name, font=('Helvetica', 30, 'bold italic'), fg='blue',
                          bg='green')
        label4.pack()

        label5 = tk.Label(self, text='Please Enter Yor password', font=('Helvetica', 18, 'bold italic'), fg='blue',
                          bg='green')
        label5.pack(padx=15, pady=15)
        label6 = tk.Label(self, text='(max 6 characters long)', font=('Helvetica', 12, 'bold italic'), fg='blue',
                          bg='red')
        label6.place(x=552, y=160)

        self.entry = tk.Entry(self, font=('Helvetica', 30, 'bold italic'), width=16, relief='raised')
        self.entry.pack(padx=15, pady=17)

        # print(entry.get())

        # text = lambda : password_verify(name, show_entry_feilds(entry))

        disp_text = '- - - - - - '
        label7 = tk.Label(self, text=disp_text, font=('Helvetica', 20, 'bold italic'),
                          fg='green', bg='red')
        label7.place(x=20, y=220)

        sel_button = tk.Button(self, text='VERIFY PASSWORD',
                               command=lambda: password_verify(name, show_entry_feilds(self.entry), label7),
                               font=('Helvetica', 25, 'bold italic'), fg='green', bg='#fefefe')
        sel_button.place(x=200, y=270)

        # disp_text = tk.StringVar()
        # disp_text = text()

        # label7 = tk.Label(self, text=disp_text, font=('Helvetica', 20,'bold italic'),
        #                  fg='green', bg='red')
        # label7.pack()

        self.button2 = tk.Button(self, text="Press Here to fill the fuel", font=('Helvetica', 15, 'bold italic'),
                                 command=lambda: verify(self, controller))

        #         command=lambda: controller.show_frame(PageTwo)

        self.button2.place(x=100, y=320, height=40)

        # if matched==1:
        # button2.configure(bg='green', command=lambda: controller.show_frame(PageTwo))

        button1 = tk.Button(self, text="Back to Home", font=('Helvetica', 20, 'bold italic'),
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=300, y=420)

        # =============Number Pad======================

        calc_font = ('Helvetica', 30, 'bold italic')

        p1_button7 = tk.Button(self, text='7', font=calc_font, bg='#12bd03', fg='#0000ff', foreground='cyan',
                               borderwidth='1', command=self.seven_clicked)
        p1_button7.place(x=520, y=200, height=44, width=67, )
        p1_button8 = tk.Button(self, text='''8''', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                               borderwidth='1', command=self.eight_clicked)
        p1_button8.place(x=590, y=200, height=44, width=67)
        p1_button9 = tk.Button(self, text='9', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                               borderwidth='1', command=self.nine_clicked)
        p1_button9.place(x=660, y=200, height=44, width=67)

        p1_button4 = tk.Button(self, text='4', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                               borderwidth='1', command=self.four_clicked)
        p1_button4.place(x=520, y=250, height=44, width=67, )
        p1_button5 = tk.Button(self, text='5', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                               borderwidth='1', command=self.five_clicked)
        p1_button5.place(x=590, y=250, height=44, width=67)
        p1_button6 = tk.Button(self, text='6', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                               borderwidth='1', command=self.six_clicked)
        p1_button6.place(x=660, y=250, height=44, width=67)

        p1_button1 = tk.Button(self, text='1', font=calc_font, bg='#12bd03', foreground='cyan', borderwidth='1',
                               command=self.one_clicked)
        p1_button1.place(x=520, y=300, height=44, width=67, )
        p1_button2 = tk.Button(self, text='2', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                               borderwidth='1', command=self.two_clicked)
        p1_button2.place(x=590, y=300, height=44, width=67)
        p1_button3 = tk.Button(self, text='3', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                               borderwidth='1', command=self.three_clicked)
        p1_button3.place(x=660, y=300, height=44, width=67)

        p1_button0 = tk.Button(self, text='0', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                               borderwidth='1', command=self.zero_clicked)
        p1_button0.place(x=520, y=350, height=44, width=130)

        p1_del_button = tk.Button(self, text='DEL', bg='red', fg='black', font=calc_font, borderwidth='2',
                                  command=self.clear)
        p1_del_button.place(x=660, y=350, height=44, width=67)

    def one_clicked(self):
        self.entry.insert(16, "1")

    def two_clicked(self):
        self.entry.insert(16, "2")

    def three_clicked(self):
        self.entry.insert(16, "3")

    def four_clicked(self):
        self.entry.insert(16, "4")

    def five_clicked(self):
        self.entry.insert(16, "5")

    def six_clicked(self):
        self.entry.insert(16, "6")

    def seven_clicked(self):
        self.entry.insert(16, "7")

    def eight_clicked(self):
        self.entry.insert(16, "8")

    def nine_clicked(self):
        self.entry.insert(16, "9")

    def zero_clicked(self):
        self.entry.insert(16, '0')

    def clear(self):
        self.entry.delete(0, 20)


# ===================Fill Petrol====================================================

def fill_petrol(widget):
    amount_widget = widget.entry_label
    global DATABASE
    global current_user_name
    entered_amount = amount_widget.get()
    transaction = False

    user_existing_amount = DATABASE[current_user_name][1]
    user_existing_amount = int(user_existing_amount)
    try:
        entered_amount = int(entered_amount)

        if entered_amount > user_existing_amount:
            widget.failure_label = tk.Label(widget, text='Insufficient Balance', fg='black', bg='red',
                                            font=('Helvetica', 20, 'bold italic'))
            widget.failure_label.place(x=150, y=250)
        else:
            print('Transaction Successful')
            widget.success_label = tk.Label(widget, text='Transaction Successful', fg='black', bg='green',
                                            font=('Helvetica', 20, 'bold italic'))
            widget.success_label.place(x=150, y=250)
            transaction = True

            DATABASE[current_user_name][1] = user_existing_amount - entered_amount
            save_database(DATABASE)

            widget.put_pipe_label = tk.Label(widget, text='Please Put the Pipe into the Tank \n Press FILL', fg='black',
                                             bg='green', font=('Helvetica', 15, 'bold italic'))
            widget.put_pipe_label.place(x=10, y=300)

            widget.petrol_fill_button = tk.Button(widget, text='FILL', fg='black', bg='#12de89',
                                                  font=('Helvetica', 30, 'bold italic'))
            widget.petrol_fill_button.place(x=50, y=370)

    except ValueError:
        widget.enter_amount_label = tk.Label(widget, text='Please Enter the amount', fg='black', bg='red',
                                             font=('Helvetica', 20, 'bold italic'))
        widget.enter_amount_label.place(x=100, y=250)
        # widget.after(2000, widget.__delattr__('enter_amount_label'))


def fill_deisel(widget):
    amount_widget = widget.entry_label
    global DATABASE
    global current_user_name
    entered_amount = amount_widget.get()

    user_existing_amount = DATABASE[current_user_name][1]
    user_existing_amount = int(user_existing_amount)
    try:
        entered_amount = int(entered_amount)

        if entered_amount > user_existing_amount:
            widget.failure_label = tk.Label(widget, text='Insufficient Balance', fg='black', bg='red',
                                            font=('Helvetica', 20, 'bold italic'))
            widget.failure_label.place(x=150, y=250)
        else:
            print('Transaction Successful')
            widget.success_label = tk.Label(widget, text='Transaction Successful', fg='black', bg='green',
                                            font=('Helvetica', 20, 'bold italic'))
            widget.success_label.place(x=150, y=250)
            widget.put_pipe_label = tk.Label(widget, text='Please Put the Pipe into the Tank \n Press FILL', fg='black',
                                             bg='green', font=('Helvetica', 15, 'bold italic'))
            widget.put_pipe_label.place(x=10, y=300)

            widget.petrol_fill_button = tk.Button(widget, text='FILL', fg='black', bg='#12de89',
                                                  font=('Helvetica', 30, 'bold italic'))
            widget.petrol_fill_button.place(x=50, y=370)
    except ValueError:
        widget.enter_amount_label = tk.Label(widget, text='Please Enter the amount', fg='black', bg='red',
                                             font=('Helvetica', 20, 'bold italic'))
        widget.enter_amount_label.place(x=100, y=250)
        # widget.after(2000, widget.__delattr__('enter_amount_label'))


# ==========================PETROL Frame======================================================================


class PetrolFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='steel blue')
        petrol_label = tk.Label(self, text='Petrol', font=('Helvetica', 40, 'bold italic'),
                                fg='#12edfe', bg='magenta')
        petrol_label.pack()

        amount_label = tk.Label(self, text='Enter Amount:', font=('Helvetica', 25, 'bold italic'),
                                fg='green', bg='cyan')
        amount_label.place(x=25, y=70)

        self.entry_label = tk.Entry(self, font=('Helvetica', 30, 'bold italic'), bg='cyan')
        self.entry_label.place(x=250, y=70, height=37)

        button22 = tk.Button(self, text='PROCEED', font=('Helvetica', 20, 'bold italic'),
                             fg='green', bg='yellow', command=lambda: fill_petrol(self))
        button22.place(x=200, y=200)

        # ============== Number Pad =====================

        calc_font = ('Helvetica', 30, 'bold italic')

        button7 = tk.Button(self, text='7', font=calc_font, bg='#12bd03', fg='#0000ff', foreground='cyan',
                            borderwidth='1', command=self.seven_clicked)
        button7.place(x=500, y=200, height=44, width=67, )
        button8 = tk.Button(self, text='8', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                            borderwidth='1', command=self.eight_clicked)
        button8.place(x=570, y=200, height=44, width=67)
        button9 = tk.Button(self, text='9', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                            borderwidth='1', command=self.nine_clicked)
        button9.place(x=640, y=200, height=44, width=67)

        button4 = tk.Button(self, text='4', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                            borderwidth='1', command=self.four_clicked)
        button4.place(x=500, y=250, height=44, width=67, )
        button5 = tk.Button(self, text='5', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                            borderwidth='1', command=self.five_clicked)
        button5.place(x=570, y=250, height=44, width=67)
        button6 = tk.Button(self, text='6', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                            borderwidth='1', command=self.six_clicked)
        button6.place(x=640, y=250, height=44, width=67)

        button1 = tk.Button(self, text='1', font=calc_font, bg='#12bd03', foreground='cyan', borderwidth='1',
                            command=self.one_clicked)
        button1.place(x=500, y=300, height=44, width=67, )
        button2 = tk.Button(self, text='2', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                            borderwidth='1', command=self.two_clicked)
        button2.place(x=570, y=300, height=44, width=67)
        button3 = tk.Button(self, text='3', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                            borderwidth='1', command=self.three_clicked)
        button3.place(x=640, y=300, height=44, width=67)

        button0 = tk.Button(self, text='0', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                            borderwidth='1', command=self.zero_clicked)
        button0.place(x=500, y=350, height=44, width=130)

        del_button = tk.Button(self, text='DEL', bg='red', fg='black', font=calc_font, borderwidth='2',
                               command=self.clear)
        del_button.place(x=640, y=350, height=44, width=67)

        back_button = tk.Button(self, text='BACK', font=('Helvetica', 20, 'bold italic'),
                                command=lambda: controller.show_frame(PageTwo))
        back_button.place(x=350, y=400)

    def one_clicked(self):
        self.entry_label.insert(16, "1")

    def two_clicked(self):
        self.entry_label.insert(16, "2")

    def three_clicked(self):
        self.entry_label.insert(16, "3")

    def four_clicked(self):
        self.entry_label.insert(16, "4")

    def five_clicked(self):
        self.entry_label.insert(16, "5")

    def six_clicked(self):
        self.entry_label.insert(16, "6")

    def seven_clicked(self):
        self.entry_label.insert(16, "7")

    def eight_clicked(self):
        self.entry_label.insert(16, "8")

    def nine_clicked(self):
        self.entry_label.insert(16, "9")

    def zero_clicked(self):
        self.entry_label.insert(16, '0')

    def clear(self):
        self.entry_label.delete(0, 20)


# ==========================Deisal Frame===============================================

class DeisalFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='steel blue')
        diesal_label = tk.Label(self, text='Deisal', font=('Helvetica', 40, 'bold italic'),
                                fg='#12edfe', bg='#edfead')
        diesal_label.pack()

        amount_label = tk.Label(self, text='Enter Amount:', font=('Helvetica', 25, 'bold italic'),
                                fg='green', bg='cyan')
        amount_label.place(x=25, y=70)

        self.entry_label = tk.Entry(self, font=('Helvetica', 30, 'bold italic'), bg='cyan')
        self.entry_label.place(x=250, y=70, height=37)

        button22 = tk.Button(self, text='PROCEED', font=('Helvetica', 20, 'bold italic'),
                             fg='green', bg='yellow', command=lambda: fill_deisel(self))
        button22.place(x=200, y=200)

        # ============== Number Pad =====================

        calc_font = ('Helvetica', 30, 'bold italic')

        button7 = tk.Button(self, text='7', font=calc_font, bg='#12bd03', fg='#0000ff', foreground='cyan',
                            borderwidth='1', command=self.seven_clicked)
        button7.place(x=500, y=200, height=44, width=67, )
        button8 = tk.Button(self, text='8', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                            borderwidth='1', command=self.eight_clicked)
        button8.place(x=570, y=200, height=44, width=67)
        button9 = tk.Button(self, text='9', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                            borderwidth='1', command=self.nine_clicked)
        button9.place(x=640, y=200, height=44, width=67)

        button4 = tk.Button(self, text='4', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                            borderwidth='1', command=self.four_clicked)
        button4.place(x=500, y=250, height=44, width=67, )
        button5 = tk.Button(self, text='5', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                            borderwidth='1', command=self.five_clicked)
        button5.place(x=570, y=250, height=44, width=67)
        button6 = tk.Button(self, text='6', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                            borderwidth='1', command=self.six_clicked)
        button6.place(x=640, y=250, height=44, width=67)

        button1 = tk.Button(self, text='1', font=calc_font, bg='#12bd03', foreground='cyan', borderwidth='1',
                            command=self.one_clicked)
        button1.place(x=500, y=300, height=44, width=67, )
        button2 = tk.Button(self, text='2', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                            borderwidth='1', command=self.two_clicked)
        button2.place(x=570, y=300, height=44, width=67)
        button3 = tk.Button(self, text='3', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                            borderwidth='1', command=self.three_clicked)
        button3.place(x=640, y=300, height=44, width=67)

        button0 = tk.Button(self, text='0', font=calc_font, bg='#12bd03', fg='#ffffff', foreground='cyan',
                            borderwidth='1', command=self.zero_clicked)
        button0.place(x=500, y=350, height=44, width=130)

        del_button = tk.Button(self, text='DEL', bg='red', fg='black', font=calc_font, borderwidth='2',
                               command=self.clear)
        del_button.place(x=640, y=350, height=44, width=67)

        back_button = tk.Button(self, text='BACK', font=('Helvetica', 20, 'bold italic'),
                                command=lambda: controller.show_frame(PageTwo))
        back_button.place(x=350, y=400)

    def one_clicked(self):
        self.entry_label.insert(16, "1")

    def two_clicked(self):
        self.entry_label.insert(16, "2")

    def three_clicked(self):
        self.entry_label.insert(16, "3")

    def four_clicked(self):
        self.entry_label.insert(16, "4")

    def five_clicked(self):
        self.entry_label.insert(16, "5")

    def six_clicked(self):
        self.entry_label.insert(16, "6")

    def seven_clicked(self):
        self.entry_label.insert(16, "7")

    def eight_clicked(self):
        self.entry_label.insert(16, "8")

    def nine_clicked(self):
        self.entry_label.insert(16, "9")

    def zero_clicked(self):
        self.entry_label.insert(16, '0')

    def clear(self):
        self.entry_label.delete(0, 20)


def check_balance(self):
    global DATABASE, current_user_name
    current_amount_user = DATABASE[current_user_name][1]
    self.amount_label_func = tk.Label(self, text=str(current_amount_user), font=('Helvetica', 30, 'bold italic'),
                                      fg='black', bg='steel blue')
    self.amount_label_func.place(x=420, y=70, height=40)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='steel blue')

        label = ttk.Label(self, text="Page Two!!!", font=('Helvetica', 30, 'bold italic'))
        label.pack(pady=10, padx=10)

        # self.label2 = ttk.Label(self, text=controller.getVUE(), font=LARGE_FONT)
        # self.label2.pack(pady=10, padx=10)

        self.amount_button = tk.Button(self, text='Check Available Balance:', font=('Helvetica', 20, 'bold italic'),
                                       fg='black', bg='steel blue', command=lambda: check_balance(self))
        self.amount_button.place(x=50, y=70)

        label21 = tk.Label(self, text='Select Fuel ', font=('Helvetica', 40, 'bold italic'),
                           fg='blue', bg='magenta')
        label21.place(x=220, y=130)

        petrol_button = tk.Button(self, text='PETROL', font=('Helvetica', 20, 'bold italic'),
                                  fg='red', bg='cyan', command=lambda: controller.show_frame(PetrolFrame))
        petrol_button.place(x=150, y=190)

        deisel_button = tk.Button(self, text='DEISEL', font=('Helvetica', 20, 'bold italic'),
                                  fg='red', bg='cyan', command=lambda: controller.show_frame(DeisalFrame))
        deisel_button.place(x=450, y=190)

        # entry = tk.Entry(self,bg='cyan')

        button1 = tk.Button(self, text="Back to Home", font=('Helvetica', 20, 'bold italic'),
                            command=lambda: controller.show_frame(StartPage))
        button1.place(x=300, y=340)

        button2 = tk.Button(self, text="BACK", font=('Helvetica', 20, 'bold italic'),
                            command=lambda: controller.show_frame(PageOne))
        button2.place(x=300, y=300)

        # button3 = ttk.Button(self, text="+1",
        # command=lambda: controller.raiseVUE(PageTwo))
        # button3.pack()


app = Application()

# set window size
app.geometry("800x480")

# init menubar
menubar = tk.Menu(app)

# creating the menus
menuManage = tk.Menu(menubar, tearoff=0)

# list of menubar elements
menubar.add_cascade(menu=menuManage, label="Frame")
save_database(DATABASE)
# menu: manage
menuManage.add_command(label="P1", command=lambda: app.show_frame(PageOne))
menuManage.add_command(label="P2", command=lambda: app.show_frame(PageTwo))
menuManage.add_command(label="Start", command=lambda: app.show_frame(StartPage))

# attach menubar
app.config(menu=menubar)

app.mainloop()
