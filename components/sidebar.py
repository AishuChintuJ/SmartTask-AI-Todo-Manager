import customtkinter as ctk

from themes.theme import COLORS



class Sidebar(ctk.CTkFrame):


    def __init__(self,parent,controller):

        super().__init__(
            parent,
            width=260,
            fg_color=COLORS["sidebar"]
        )


        self.controller = controller


        self.pack_propagate(False)



        # APP TITLE

        ctk.CTkLabel(

            self,

            text="🚀 SmartTask\nAI",

            font=("Segoe UI",30,"bold")

        ).pack(
            pady=40
        )



        # MENU


        menus=[

            ("🏠 Dashboard","Dashboard"),

            ("📝 Tasks","Tasks"),

            ("📅 Calendar","Calendar"),

            ("⏱ Focus","Pomodoro"),

            ("⚙ Settings","Settings")

        ]



        for text,page in menus:


            ctk.CTkButton(

                self,

                text=text,

                width=210,

                height=50,

                corner_radius=15,

                anchor="w",

                fg_color=COLORS["button"],

                hover_color=COLORS["hover"],

                command=lambda p=page:
                self.controller.show_page(p)

            ).pack(
                pady=8
            )




        # LOGOUT BUTTON


        ctk.CTkButton(

            self,

            text="🚪 Logout",

            width=210,

            height=50,

            corner_radius=15,

            fg_color=COLORS["red"],

            command=self.logout

        ).pack(

            side="bottom",

            pady=30

        )




    def logout(self):


        self.controller.current_user = None


        self.controller.show_page(

            "Login"

        )