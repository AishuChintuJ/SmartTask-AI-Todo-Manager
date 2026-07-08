import customtkinter as ctk

from themes.theme import COLORS, FONT



class StatCard(ctk.CTkFrame):


    def __init__(
            self,
            parent,
            icon,
            title,
            value
    ):


        super().__init__(

            parent,

            width=260,

            height=160,

            corner_radius=25,

            fg_color=COLORS["card"]

        )


        self.pack_propagate(False)



        # ICON

        ctk.CTkLabel(

            self,

            text=icon,

            font=("Segoe UI",35)

        ).pack(
            pady=(20,5)
        )



        # TITLE

        ctk.CTkLabel(

            self,

            text=title,

            font=FONT["heading"]

        ).pack()



        # NUMBER

        self.value = ctk.CTkLabel(

            self,

            text=value,

            font=FONT["big"]

        )


        self.value.pack()




    def update_value(self,value):


        self.value.configure(

            text=str(value)

        )