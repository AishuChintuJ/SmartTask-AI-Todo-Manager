import customtkinter as ctk


from database.db import (
    create_tables,
    create_task_table
)


from pages.login import LoginPage

from pages.register import RegisterPage

from pages.dashboard import DashboardPage

from pages.tasks import TaskPage

from pages.calendar_page import CalendarPage

from pages.pomodoro import PomodoroPage

from pages.settings import SettingsPage


from themes.theme import apply_theme



class App(ctk.CTk):


    def __init__(self):

        super().__init__()


        self.current_user=None


        self.title(
            "SmartTask AI"
        )


        self.geometry(
            "1000x650"
        )



        container=ctk.CTkFrame(
            self
        )


        container.pack(
            fill="both",
            expand=True
        )


        self.frames={}



        pages=[

            (LoginPage,"Login"),

            (RegisterPage,"Register"),

            (DashboardPage,"Dashboard"),

            (TaskPage,"Tasks"),

            (CalendarPage,"Calendar"),

            (PomodoroPage,"Pomodoro"),

            (SettingsPage,"Settings")

        ]



        for Page,name in pages:


            frame=Page(

                container,

                self

            )


            self.frames[name]=frame



            frame.place(

                x=0,

                y=0,

                relwidth=1,

                relheight=1

            )



        self.show_page(
            "Login"
        )





    def show_page(self,name):


        frame=self.frames[name]


        frame.tkraise()



        if name=="Dashboard":


            try:

                frame.load_dashboard()


            except:

                pass






if __name__=="__main__":


    apply_theme()


    create_tables()


    create_task_table()


    app=App()


    app.mainloop()