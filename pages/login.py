import customtkinter as ctk
from tkinter import messagebox

from database.db import login_user


class LoginPage(ctk.CTkFrame):

    def __init__(self, parent, controller):

        super().__init__(parent)

        self.controller = controller


        title = ctk.CTkLabel(
            self,
            text="SmartTask AI Login",
            font=("Arial",25)
        )
        title.pack(pady=40)


        self.email = ctk.CTkEntry(
            self,
            placeholder_text="Email",
            width=250
        )
        self.email.pack(pady=10)


        self.password = ctk.CTkEntry(
            self,
            placeholder_text="Password",
            show="*",
            width=250
        )
        self.password.pack(pady=10)


        login_btn = ctk.CTkButton(
            self,
            text="Login",
            command=self.login
        )
        login_btn.pack(pady=20)


        register_btn = ctk.CTkButton(
            self,
            text="Create Account",
            command=lambda:
            controller.show_page("Register")
        )
        register_btn.pack()



    def login(self):

        email = self.email.get()
        password = self.password.get()


        if email == "" or password == "":

            messagebox.showwarning(
                "Warning",
                "Enter Email and Password"
            )

            return


        user = login_user(
            email,
            password
        )


        if user:

            messagebox.showinfo(
                "Success",
                "Login Successful"
            )

            self.controller.current_user = user

            self.controller.show_page(
                "Dashboard"
            )


        else:

            messagebox.showerror(
                "Error",
                "Invalid Email or Password"
            )