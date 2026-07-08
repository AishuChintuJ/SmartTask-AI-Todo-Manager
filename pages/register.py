import customtkinter as ctk
from tkinter import messagebox

from database.db import register_user


class RegisterPage(ctk.CTkFrame):


    def __init__(self,parent,controller):

        super().__init__(parent)

        self.controller = controller


        title = ctk.CTkLabel(
            self,
            text="Create Account",
            font=("Arial",25)
        )

        title.pack(pady=30)


        self.username = ctk.CTkEntry(
            self,
            placeholder_text="Username"
        )

        self.username.pack(pady=10)


        self.email = ctk.CTkEntry(
            self,
            placeholder_text="Email"
        )

        self.email.pack(pady=10)


        self.password = ctk.CTkEntry(
            self,
            placeholder_text="Password",
            show="*"
        )

        self.password.pack(pady=10)



        btn = ctk.CTkButton(
            self,
            text="Register",
            command=self.register
        )

        btn.pack(pady=20)



        login = ctk.CTkButton(
            self,
            text="Login",
            command=lambda:
            controller.show_page("Login")
        )

        login.pack()



    def register(self):

        result = register_user(

            self.username.get(),
            self.email.get(),
            self.password.get()

        )


        if result:

            messagebox.showinfo(
                "Success",
                "Account Created"
            )

            self.controller.show_page(
                "Login"
            )


        else:

            messagebox.showerror(
                "Error",
                "Email already exists"
            )