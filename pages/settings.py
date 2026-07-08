import customtkinter as ctk



class SettingsPage(ctk.CTkFrame):


    def __init__(
        self,
        parent,
        controller
    ):

        super().__init__(parent)


        title = ctk.CTkLabel(

            self,

            text="⚙ Settings",

            font=(
                "Segoe UI",
                30,
                "bold"
            )

        )

        title.pack(
            pady=40
        )



        ctk.CTkButton(

            self,

            text="🌙 Dark Mode",

            width=200,

            command=self.dark

        ).pack(
            pady=15
        )



        ctk.CTkButton(

            self,

            text="☀ Light Mode",

            width=200,

            command=self.light

        ).pack(
            pady=15
        )



        ctk.CTkButton(

            self,

            text="Back Dashboard",

            width=200,

            command=lambda:
            controller.show_page(
                "Dashboard"
            )

        ).pack(
            pady=40
        )




    def dark(self):

        ctk.set_appearance_mode(
            "dark"
        )




    def light(self):

        ctk.set_appearance_mode(
            "light"
        )