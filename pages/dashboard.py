import customtkinter as ctk

from components.sidebar import Sidebar

from components.card import StatCard

from database.db import task_statistics

from themes.theme import COLORS, FONT



class DashboardPage(ctk.CTkFrame):


    def __init__(self, parent, controller):

        super().__init__(
            parent,
            fg_color=COLORS["bg"]
        )


        self.controller = controller



        # Sidebar

        Sidebar(
            self,
            controller

        ).pack(
            side="left",
            fill="y"
        )



        # Main Area

        main = ctk.CTkFrame(

            self,

            fg_color="transparent"

        )


        main.pack(

            expand=True,

            fill="both",

            padx=50,

            pady=40

        )



        # Heading


        ctk.CTkLabel(

            main,

            text="Dashboard Overview",

            font=FONT["title"]

        ).pack(
            anchor="w"
        )



        # Cards Container


        card_area = ctk.CTkFrame(

            main,

            fg_color="transparent"

        )


        card_area.pack(
            pady=50
        )



        # Total Card


        self.total_card = StatCard(

            card_area,

            "📋",

            "Total Tasks",

            "0"

        )


        self.total_card.grid(

            row=0,

            column=0,

            padx=20

        )




        # Completed Card


        self.completed_card = StatCard(

            card_area,

            "✅",

            "Completed",

            "0"

        )


        self.completed_card.grid(

            row=0,

            column=1,

            padx=20

        )




        # Pending Card


        self.pending_card = StatCard(

            card_area,

            "⏳",

            "Pending",

            "0"

        )


        self.pending_card.grid(

            row=0,

            column=2,

            padx=20

        )





    def load_dashboard(self):


        if self.controller.current_user:


            total, completed, pending = task_statistics(

                self.controller.current_user[0]

            )



            self.total_card.update_value(

                total

            )



            self.completed_card.update_value(

                completed

            )



            self.pending_card.update_value(

                pending

            )