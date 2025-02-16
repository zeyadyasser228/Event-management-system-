import os
import sqlite3
import string
from tkinter import messagebox
from tkinter import *
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from PIL import Image, ImageTk
import random


def apply():
    passs = enter_new_password.get()
    confirmpass = Confirm_new_password.get()
    username = Enter_user_name.get()

    if passs == confirmpass and passs != "" and confirmpass != "":
        conn = sqlite3.connect("database.db")
        try:
            changeepass = conn.cursor()
            changeepass.execute("SELECT * FROM user WHERE username=?", (username,))
            user = changeepass.fetchone()

            if user:
                changeepass.execute("UPDATE user SET password=? WHERE username=?", (passs, username))
                conn.commit()
                CTkMessagebox(title="Success", message="Password successfully go back and login in again",
                              button_color="#7B9976", button_hover_color="#7B9976", bg_color="#262724",
                              font=('Times New Roman', 15, 'bold'), fg_color="#7B9976", title_color="#7B9976",
                              option_1="OK", button_text_color="#262724")
                root.destroy()
                os.system("python User_Loginn.py")
            else:
                CTkMessagebox(title="Username Error", message="Invaild Usernane", button_color="#7B9976",
                              button_hover_color="#7B9976", bg_color="#262724",
                              font=('Times New Roman', 15, 'bold'), icon="warning", fg_color="#7B9976",
                              title_color="#7B9976",
                              option_1="OK", button_text_color="#262724")
        except Exception as e:
            CTkMessagebox(title="Error", message=str(e))
        conn.close()
    elif passs != confirmpass:
        CTkMessagebox(title="Error", message="Password Doesn't match", button_color="#7B9976",
                      button_hover_color="#7B9976", bg_color="#262724",
                      font=('Times New Roman', 15, 'bold'), icon="warning", fg_color="#7B9976", title_color="#7B9976",
                      option_1="OK", button_text_color="#262724")
    else:
        CTkMessagebox(title="Error", message="Password fields cannot be empty", button_color="#7B9976",
                      button_hover_color="#7B9976", bg_color="#262724",
                      font=('Times New Roman', 15, 'bold'), icon="warning", fg_color="#7B9976", title_color="#7B9976",
                      option_1="OK", button_text_color="#262724")

def back():
    root.destroy()
    os.system("python Forget_password.py")




def hide():
    hide_but = ctk.CTkButton(loginFrame, fg_color="#7B9976", image=hide_image, command=show, hover_color='#7E9779',
                             text='', width=5, height=5)
    hide_but.place(x=520, y=250)
    enter_new_password.configure(show='*')


def show():
    show_but = ctk.CTkButton(loginFrame, fg_color="#7B9976", image=show_image, command=hide, hover_color='#7E9779',
                             text='', width=5, height=5)
    show_but.place(x=520, y=250)
    enter_new_password.configure(show='')




def hide2():
    hide_but2 = ctk.CTkButton(loginFrame, fg_color="#7B9976", image=hide_image, command=show2, hover_color='#7E9779',
                              text='', width=5, height=5)
    hide_but2.place(x=520, y=315)
    Confirm_new_password.configure(show='*')


def show2():
    show_but2 = ctk.CTkButton(loginFrame, fg_color="#7B9976", image=show_image, command=hide2, hover_color='#7E9779',
                              text='', width=5, height=5)
    show_but2.place(x=520, y=315)
    Confirm_new_password.configure(show='')


def generator_password():
    pass_len = 12  # default password length
    password = ''.join(
        random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for _ in
        range(pass_len))
    pass_str.set(password)
    enter_new_password.delete(0, END)
    enter_new_password.insert(0, password)
    Confirm_new_password.delete(0, END)
    Confirm_new_password.insert(0, password)


def change_theme():
    if ctk.get_appearance_mode() == "Dark":
        ctk.set_appearance_mode("Light")
    else:
        ctk.set_appearance_mode("Dark")


root = ctk.CTk()

ctk.set_appearance_mode('system')
ctk.set_default_color_theme('blue')
root.title('Event Management System')

root.iconbitmap("assests/ticket_856232.ico")
screen_width = root.winfo_screenwidth()
screen_heigth = root.winfo_screenheight()

img1 = ImageTk.PhotoImage(Image.open('assests/bk.png'))
label_photo = Label(root, image=img1)
label_photo.pack()

center_x = 0
center_y = 0
root.geometry(f'{screen_width}x{screen_heigth}+{center_x}+{center_y}')

loginFrame = ctk.CTkFrame(root, corner_radius=50, width=600, height=500, bg_color='#7E9779')

loginFrame.place(x=100, y=150)

hide_image = ImageTk.PhotoImage(file='assests/eye.png')
show_image = ImageTk.PhotoImage(file='assests/view.png')

show_but = ctk.CTkButton(loginFrame, fg_color="#7B9976", image=hide_image, command=show, hover_color='#7E9779', text='',
                         width=5, height=5, corner_radius=5)
show_but.place(x=520, y=250)

show_but2 = ctk.CTkButton(loginFrame, fg_color="#7B9976", image=hide_image, command=show2, hover_color='#7E9779',
                          text='', width=5, height=5, corner_radius=5)
show_but2.place(x=520, y=315)

Label(loginFrame, text='User name', fg="#7b987e", bg="#262724", font=('Times New Roman', 24, 'bold')).place(x=70,
                                                                                                               y=210)
Label(loginFrame, text='New Password', fg="#7b987e", bg="#262724", font=('Times New Roman', 24, 'bold')).place(x=70,
                                                                                                               y=310)
Label(loginFrame, fg="#7b987e", text='Confirm New Password', bg="#262724", font=('Times New Roman', 24, 'bold')).place(
    x=20, y=395)

label = ctk.CTkLabel(loginFrame, text_color="#7b987e", text='Change Your Password',
                     font=('Times New Roman', 30, 'bold'))
label.place(x=140, y=40)


Enter_user_name = ctk.CTkEntry(loginFrame, width=200, placeholder_text="User name",
                                  font=('Times New Roman', 15, 'bold'), show="")
Enter_user_name.place(x=300, y=175)


enter_new_password = ctk.CTkEntry(loginFrame, width=200, placeholder_text="New Password",
                                  font=('Times New Roman', 15, 'bold'), show="*")
enter_new_password.place(x=300, y=250)

Confirm_new_password = ctk.CTkEntry(loginFrame, width=200, placeholder_text="Confirm new Password",
                                    font=('Times New Roman', 15, 'bold'), show="*")
Confirm_new_password.place(x=300, y=320)

pass_str = StringVar()

Apply_button = ctk.CTkButton(loginFrame, fg_color="#7B9976", text_color="#262724", text='Apply',hover_color="#7B9976",
                             font=('Times New Roman', 20, 'bold'),command=apply)
Apply_button.place(x=230, y=370)

Remember_Button = ctk.CTkButton(loginFrame, fg_color="#7B9976", text_color="#262724", text='Click to generate password',
                                hover_color="#7B9976",font=('Times New Roman', 20, 'bold'), command=generator_password)
Remember_Button.place(x=180, y=432)

back_image = ImageTk.PhotoImage(file='assests/backspace.png')
but_back = ctk.CTkButton(loginFrame, text='', fg_color='#262724', image=back_image, width=40, hover_color='#7B9B75',hover='#262724',
                         command=back)
but_back.place(x=20, y=20)
change_theme_box = ctk.CTkSwitch(master=root, text='', bg_color='#7B9976', progress_color='#262724', fg_color='#262724',
                                 font=('Times New Roman', 20, 'bold'), command=change_theme)
change_theme_box.place(x=0, y=0)

root.mainloop()
