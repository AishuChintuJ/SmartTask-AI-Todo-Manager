import customtkinter as ctk

from tkinter import messagebox

from database.db import (
    add_task,
    get_tasks,
    search_task,
    filter_task,
    update_task_status
)

from utils.export import export_csv

from tkcalendar import DateEntry



class TaskPage(ctk.CTkFrame):


    def __init__(self,parent,controller):

        super().__init__(parent)

        self.controller = controller


        title = ctk.CTkLabel(
            self,
            text="📝 My Tasks",
            font=("Arial",30,"bold")
        )

        title.pack(pady=15)


        # Search


        self.search = ctk.CTkEntry(
            self,
            placeholder_text="Search Task",
            width=300
        )

        self.search.pack(pady=5)


        ctk.CTkButton(
            self,
            text="Search",
            command=self.search_tasks
        ).pack(pady=5)



        # Task Entry


        self.task = ctk.CTkEntry(
            self,
            placeholder_text="Task Name",
            width=300
        )

        self.task.pack(pady=5)



        self.category = ctk.CTkComboBox(
            self,
            values=[
                "Study",
                "Coding",
                "Personal",
                "Work"
            ]
        )

        self.category.pack(pady=5)




        self.priority = ctk.CTkComboBox(
            self,
            values=[
                "High",
                "Medium",
                "Low"
            ]
        )

        self.priority.pack(pady=5)



        self.date = DateEntry(
            self,
            date_pattern="yyyy-mm-dd"
        )

        self.date.pack(pady=5)



        ctk.CTkButton(
            self,
            text="Add Task",
            command=self.save_task

        ).pack(pady=10)



        # Task List


        self.task_frame = ctk.CTkScrollableFrame(
            self,
            width=650,
            height=250
        )

        self.task_frame.pack(pady=10)




        # Buttons


        ctk.CTkButton(
            self,
            text="Refresh",
            command=self.load_tasks

        ).pack(pady=5)



        ctk.CTkButton(
            self,
            text="Completed Tasks",

            command=lambda:
            self.filter_tasks("Completed")

        ).pack(pady=5)




        ctk.CTkButton(
            self,
            text="Pending Tasks",

            command=lambda:
            self.filter_tasks("Pending")

        ).pack(pady=5)




        ctk.CTkButton(
            self,
            text="Export CSV",

            command=self.export_tasks

        ).pack(pady=5)



        ctk.CTkButton(
            self,
            text="Back Dashboard",

            command=lambda:
            controller.show_page("Dashboard")

        ).pack(pady=10)




    # Add Task


    def save_task(self):


        if self.task.get()=="":

            messagebox.showerror(
                "Error",
                "Enter Task"
            )

            return



        user=self.controller.current_user



        add_task(

            user[0],

            self.task.get(),

            self.category.get(),

            self.priority.get(),

            self.date.get()

        )


        messagebox.showinfo(
            "Success",
            "Task Added"
        )


        self.load_tasks()






    # Display


    def display(self,tasks):


        for widget in self.task_frame.winfo_children():

            widget.destroy()



        for task in tasks:


            var = ctk.IntVar()



            if task[6]=="Completed":

                var.set(1)


            else:

                var.set(0)



            checkbox = ctk.CTkCheckBox(

                self.task_frame,


                text=f"{task[2]} | {task[4]} | {task[6]}",


                variable=var,


                command=lambda id=task[0],v=var:
                self.change_status(id,v)

            )


            checkbox.pack(
                anchor="w",
                pady=5
            )






    # Update Status


    def change_status(self,task_id,var):


        if var.get()==1:

            status="Completed"


        else:

            status="Pending"



        update_task_status(

            task_id,

            status

        )


        self.load_tasks()






    # Load Tasks


    def load_tasks(self):


        user=self.controller.current_user


        tasks=get_tasks(
            user[0]
        )


        self.display(tasks)






    # Search


    def search_tasks(self):


        result=search_task(

            self.controller.current_user[0],

            self.search.get()

        )


        self.display(result)






    # Filter


    def filter_tasks(self,status):


        result=filter_task(

            self.controller.current_user[0],

            status

        )


        self.display(result)






    # Export


    def export_tasks(self):


        export_csv(

            self.controller.current_user[0]

        )


        messagebox.showinfo(

            "Success",

            "Export Completed"

        )