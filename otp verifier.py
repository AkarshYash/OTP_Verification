from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox

class OTPVerifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x550")
        self.resizable(False, False)
        self.n = random.randint(1000, 9999)
        self.client = Client("ACeacdd556a87f15bb145bd1213acd6860", "c3263c8ef43da3449098c5e3521be8df")
        self.client.messages.create(to="7742148084", from_="+14176412180", body=str(self.n))

    def labels(self):
        self.c = Canvas(self, bg="white", width=400, height=280)
        self.c.place(x=100, y=60)
        self.login_title = Label(self, text="OTP Verification", font="bold, 20", bg="white")
        self.login_title.place(x=210, y=90)

    def entry(self):
        self.user_name = Text(self, borderwidth=2, highlightthickness=0, wrap=WORD, height=2)
        self.user_name.place(x=190, y=160)

    def buttons(self):
        self.submitbuttonimage = PhotoImage(file="submit.png")
        self.submitbutton = Button(self, image=self.submitbuttonimage, command=self.check_otp, border=0)
        self.submitbutton.place(x=208, y=400)

        self.resendOTPimage = PhotoImage(file="resendotp.png")
        self.resendotp = Button(self, image=self.resendOTPimage, command=self.resend_otp, border=0)
        self.resendotp.place(x=208, y=400)

    def check_otp(self):
        try:
            self.userInput = int(self.user_name.get(1.0, "end-1c"))
            if self.userInput == self.n:
                messagebox.showinfo("Info", "Login successful")
                self.n = "done"
            elif self.n == "done":
                messagebox.showinfo("Info", "Already logged in")
            else:
                messagebox.showinfo("Info", "Wrong OTP")
        except:
            messagebox.showinfo("Info", "Invalid OTP")

    def resend_otp(self):
        self.n = random.randint(1000, 9999)
        self.client = Client("ACeacdd556a87f15bb145bd1213acd6860", "c3263c8ef43da3449098c5e3521be8df")
        self.client.messages.create(to="7742148084", from_="+14176412180", body=str(self.n))

if __name__ == "__main__":
    window = OTPVerifier()
    window.labels()
    window.entry()
    window.buttons()
    window.mainloop()
