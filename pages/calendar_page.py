import customtkinter as ctk

from tkcalendar import Calendar

from database.db import get_tasks

from datetime import datetime



class CalendarPage(ctk.CTkFrame):


    def __init__(self,parent,controller):

        super().__init__(parent)

        self.controller = controller


        title = ctk.CTkLabel(

            self,

            text="📅 Task Calendar",

            font=("Arial",30,"bold")

        )

        title.pack(
            pady=20
        )


        self.cal = Calendar(

            self,

            selectmode="day",

            date_pattern="yyyy-mm-dd"

        )

        self.cal.pack(
            pady=20
        )


        ctk.CTkButton(

            self,

            text="Show Tasks",

            command=self.show_tasks

        ).pack(
            pady=10
        )


        self.box = ctk.CTkTextbox(

            self,

            width=650,

            height=300

        )


        self.box.pack(
            pady=20
        )


        ctk.CTkButton(

            self,

            text="Back Dashboard",

            command=lambda:
            controller.show_page("Dashboard")

        ).pack(
            pady=10
        )



    def normalize_date(self,date):


        formats = [

            "%d-%m-%Y",

            "%Y-%m-%d",

            "%m/%d/%y"

        ]


        for f in formats:

            try:

                return datetime.strptime(
                    date,
                    f
                ).strftime(
                    "%Y-%m-%d"
                )

            except:

                pass


        return date




    def show_tasks(self):


        self.box.delete(

            "1.0",

            "end"

        )


        selected_date = self.normalize_date(

            self.cal.get_date()

        )


        user = self.controller.current_user



        tasks = get_tasks(

            user[0]

        )


        found=False



        for task in tasks:


            task_date = self.normalize_date(

                task[5]

            )


            if task_date == selected_date:


                found=True


                self.box.insert(

                    "end",

f"""

📝 Task:
{task[2]}


Category:
{task[3]}


Priority:
{task[4]}


Status:
{task[6]}


Due Date:
{task[5]}

----------------------

"""

                )



        if found == False:


            self.box.insert(

                "end",

                "No Tasks Found"

            )