from tkinter import *
import login_details as ld


def login_page():
    root = Tk()

    root.title('CALCULATOR')

    ##Register
    def register():
        user = my_username_entry.get()
        my_pass = my_password_entry.get()

        ld.login_dict = {user: my_pass}
        ld.save_login_details()

        success_label = Label(root, text='Registration Successful')
        success_label.grid(row=4, column=1)

    my_username = Label(root, text='Username')
    my_username.grid(row=0, column=0)

    my_username_entry = Entry(root)
    my_username_entry.grid(row=0, column=1)

    my_password = Label(root, text='Password')
    my_password.grid(row=1, column=0)

    my_password_entry = Entry(root)
    my_password_entry.grid(row=1, column=1)

    my_register_button = Button(root, text='Register', command=register)
    my_register_button.grid(row=2, column=1)

    ##Login
    # def login_click():
    #     success_label = Label(root, text='Login Successful')
    #     success_label.grid(row=4, column=2)
    #
    #
    # username = Label(root, text='Username')
    # username.grid(row=1, column=1)
    #
    # username_entry = Entry(root)
    # username_entry.grid(row=1, column=2)
    #
    # password = Label(root, text='Password')
    # password.grid(row=2, column=1)
    #
    # password_entry = Entry(root)
    # password_entry.grid(row=2, column=2, columnspan=2)
    #
    # login_button = Button(root, text='Login', command=login_click)
    # login_button.grid(row=3, column=2, padx=20)

    root.mainloop()
