from tkinter import ttk
import tkinter as tk
from windows import set_dpi_awareness
from adding_mysql import *

set_dpi_awareness()


class main_frame(tk.Tk):
    def __init__(self):
        super().__init__()
        style=ttk.Style()
        self.title('loginPage')
        self.geometry('400x250')
        self.resizable(False,False)
        self.user_name=tk.StringVar()
        self.password=tk.StringVar()
        self.admin_password=tk.StringVar()
        self.signup_name=tk.StringVar()
        self.signup_password=tk.StringVar()
        label_name = ttk.Label(self,text='Name:',font=('Helvetica',15))
        label_password = ttk.Label(self,text='Password:',font=('Helvetica',15))
        entry_name = ttk.Entry(self,font=('Helvetica',15),textvariable=self.user_name)
        entry_password = ttk.Entry(self,font=('Helvetica',15),textvariable=self.password)
        button_login = ttk.Button(self,text='login',style='small.TButton',command=self.master_fn)
        self.bind('<Return>',self.master_fn)
        label_name.grid(row=0,column=0,padx=(60,0),pady=(10,40))
        label_password.grid(row=1, column=0,padx=(60,0),pady=(10,40))
        entry_name.grid(row=0,column=1,pady=(10,40))
        entry_password.grid(row=1,column=1,pady=(10,40))
        button_login.grid(row=2,column=1,padx=(0,0))
        style.configure('small.TButton', font=('Helvetica', 15))

    def master_fn(self,*args):
       name=self.user_name.get()
       password=self.password.get()
       self.user_name.set(value='')
       self.password.set(value='')
       # correct value if we get a match for user name and password in the database
       result=fetch_single(name,password)
       print(result)

       try:
           if name == result[0][0] and password == result[0][1]:
               self.correct_option()
       except:
           self.wrong_options()



    def correct_option(self):
        window = tk.Toplevel()
        window.geometry('300x150')
        window.title('Login Successful')
        window.resizable(False, False)
        label=ttk.Label(window,text='You are logged in successfuly!',font=('Helvetica',11))
        label.pack()
        label_signup = ttk.Label(window, text='Check all the users if you are pseudo user', font=('Helvetica', 11))
        label_signup.pack(pady=(10, 0))
        button = ttk.Button(window, text='Check', style='small.TButton',command=self.check)
        button.pack(pady=(20, 0))


    def wrong_options(self):
        window = tk.Toplevel()
        window.geometry('300x150')
        window.title('Login Failed')
        window.resizable(False, False)
        label = ttk.Label(window, text='No such entry found in the database!',font=('Helvetica',11))
        label.pack()
        label_signup =ttk.Label(window,text='Signup instead',font=('Helvetica',16))
        label_signup.pack(pady=(10,0))
        button=ttk.Button(window,text='Signup',style='small.TButton',command=self.signup)
        button.pack(pady=(20,0))

    def signup(self):
        window=tk.Toplevel()
        window.title('loginPage')
        window.geometry('400x250')
        window.resizable(False, False)
        label_name = ttk.Label(window, text='Name:', font=('Helvetica', 15))
        label_password = ttk.Label(window, text='Password:', font=('Helvetica', 15))
        entry_name = ttk.Entry(window,textvariable=self.signup_name, font=('Helvetica', 15))
        entry_password = ttk.Entry(window,textvariable=self.signup_password, font=('Helvetica', 15))
        button_login = ttk.Button(window, text='signup', style='small.TButton', command=self.validate_signup)
        label_name.grid(row=0, column=0, padx=(60, 0), pady=(10, 40))
        label_password.grid(row=1, column=0, padx=(60, 0), pady=(10, 40))
        entry_name.grid(row=0, column=1, pady=(10, 40))
        entry_password.grid(row=1, column=1, pady=(10, 40))
        button_login.grid(row=2, column=1, padx=(0, 0))


    def check(self):
        window = tk.Toplevel()
        window.title('Admin login')
        window.geometry('450x150')
        window.resizable(False, False)
        label_password = ttk.Label(window, text='Admin password:', font=('Helvetica', 15))
        entry_password = ttk.Entry(window, textvariable=self.admin_password,font=('Helvetica', 15))
        button_login = ttk.Button(window, text='check', style='small.TButton', command=self.check_admin)


        label_password.grid(row=0, column=0, padx=(60, 0), pady=(10, 40))
        entry_password.grid(row=0, column=1, pady=(10, 40))
        button_login.grid(row=1, column=1, padx=(0, 0))

    def check_users(self,*args):
        window = tk.Toplevel()
        window.geometry('250x750')
        window.title('All users')
        window.resizable(True,False)
        listbox = tk.Listbox(window,width=50)
        # Adding Listbox to the left
        # side of root window
        listbox.pack(side='left', fill='both')
        # Creating a Scrollbar and
        # attaching it to root window
        # we are taking entries of table and storing it in a list box

        scrollbar = ttk.Scrollbar(window)

        # Adding Scrollbar to the right
        # side of root window
        scrollbar.pack(side='right', fill='both')

        # Insert elements into the listbox
        result=fetch_values()
        i=0
        for value in result:
            entry=f"{value[0]}:{value[1]}"
            listbox.insert(i,entry)
            i=i+1


        # Attaching Listbox to Scrollbar
        # Since we need to have a vertical
        # scroll we use yscrollcommand
        listbox.config(yscrollcommand=scrollbar.set)

        # setting scrollbar command parameter
        # to listbox.yview method its yview because
        # we need to have a vertical view
        scrollbar.config(command=listbox.yview)

    def not_admin(self):
        window = tk.Toplevel()
        window.geometry('250x150')
        window.title('Signup failed')
        window.resizable(False, False)
        label = ttk.Label(window, text='You are not admin so fuck off!', font=('Helvetica', 11))
        label.pack()
        self.admin_password.set(value='')

    def validate_signup(self):
        pass
        user=self.signup_name.get()
        password=self.signup_password.get()
        print(user)
        print(password)
        result=fetch_single(user,password)
        try:
            result[0][0] == user
            self.user_exists()
        except:
            insert_values(user,password)
            self.signup_successful()

        #if user already exists display an error widow
        # else close this windo
    def signup_successful(self):
        window = tk.Toplevel()
        window.geometry('250x250')
        window.title('Signup failed')
        window.resizable(False, False)
        label = ttk.Label(window, text='Registered successflly!!', font=('Helvetica', 14))
        label.pack()

    def user_exists(self):
        window = tk.Toplevel()
        window.geometry('250x250')
        window.title('Signup failed')
        window.resizable(False, False)
        label = ttk.Label(window, text='User already exists!',font=('Helvetica',14))
        label.pack()

    def check_admin(self,*args):
        if self.admin_password.get() == "ROOPAMC":
            self.check_users()
            self.admin_password.set(value='')
        else:
            self.not_admin()



root = main_frame()
style = ttk.Style(root)  # Pass in which application this style is for.

# Get the themes available in your system
print(style.theme_names())
print(style.theme_use("vista"))
root.mainloop()