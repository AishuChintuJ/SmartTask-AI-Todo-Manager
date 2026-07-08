import customtkinter as ctk



class PomodoroPage(ctk.CTkFrame):


    def __init__(self,parent,controller):

        super().__init__(parent)


        self.controller = controller


        self.default_time = 25 * 60

        self.time = self.default_time


        self.running = False

        self.paused = False



        title = ctk.CTkLabel(

            self,

            text="⏱ Pomodoro Timer",

            font=("Arial",30,"bold")

        )

        title.pack(
            pady=30
        )



        self.label = ctk.CTkLabel(

            self,

            text="25:00",

            font=("Arial",60,"bold")

        )


        self.label.pack(
            pady=30
        )



        # START


        self.start_btn = ctk.CTkButton(

            self,

            text="Start",

            command=self.start

        )


        self.start_btn.pack(
            pady=10
        )



        # PAUSE


        self.pause_btn = ctk.CTkButton(

            self,

            text="Pause",

            command=self.pause

        )


        self.pause_btn.pack(
            pady=10
        )



        # STOP


        self.stop_btn = ctk.CTkButton(

            self,

            text="Stop",

            command=self.stop

        )


        self.stop_btn.pack(
            pady=10
        )



        # BACK


        ctk.CTkButton(

            self,

            text="Back Dashboard",

            command=lambda:
            controller.show_page("Dashboard")

        ).pack(
            pady=20
        )





    # TIMER DISPLAY


    def update_display(self):


        mins = self.time // 60

        secs = self.time % 60


        self.label.configure(

            text=f"{mins:02d}:{secs:02d}"

        )





    # START / RESUME


    def start(self):


        if self.running == False:


            self.running = True

            self.paused = False


            self.countdown()



        elif self.paused:


            self.paused = False


            self.countdown()





    # COUNTDOWN


    def countdown(self):


        if self.running and not self.paused:


            self.update_display()



            if self.time > 0:


                self.time -= 1


                self.after(

                    1000,

                    self.countdown

                )


            else:


                self.running = False





    # PAUSE


    def pause(self):


        if self.running:


            self.paused = True





    # STOP


    def stop(self):


        self.running = False

        self.paused = False


        self.time = self.default_time


        self.update_display()