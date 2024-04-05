# import tkinter as tk
# from tkinter import messagebox

# class ATM(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self.title('ATM Machine')
#         self.geometry('400x300')
#         self.current_frame = None
#         self.pin = "1234"  # Set the PIN
#         self.balance = 50000  # Set the account balance
#         self.switch_frame(WelcomePage)

#     def switch_frame(self, frame_class):
#         new_frame = frame_class(self)
#         if self.current_frame is not None:
#             self.current_frame.destroy()
#         self.current_frame = new_frame
#         self.current_frame.pack(expand=True, fill='both')


# class WelcomePage(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)

#         label = tk.Label(self, text='Welcome to ATM Machine', font=('Arial', 18))
#         label.pack(pady=20)

#         button = tk.Button(self, text='Enter', command=lambda: master.switch_frame(PinPage))
#         button.pack()


# class PinPage(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)

#         label = tk.Label(self, text='Please enter your PIN', font=('Arial', 14))
#         label.pack(pady=10)

#         self.pin_entry = tk.Entry(self, show='*')
#         self.pin_entry.pack(pady=10)

#         submit_button = tk.Button(self, text='Submit', command=lambda: self.validate_pin(master))
#         submit_button.pack(pady=10)

#     def validate_pin(self, master):
#         pin = self.pin_entry.get()
#         if pin == master.pin:
#             master.switch_frame(TransactionPage)
#         else:
#             messagebox.showerror("Error", "Incorrect PIN")


# class TransactionPage(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)

#         label = tk.Label(self, text='Select Transaction', font=('Arial', 14))
#         label.pack(pady=10)

#         withdraw_button = tk.Button(self, text='Withdraw', command=lambda: master.switch_frame(WithdrawPage))
#         withdraw_button.pack()

#         balance_button = tk.Button(self, text='Check Balance', command=lambda: master.switch_frame(BalancePage))
#         balance_button.pack()

#         exit_button = tk.Button(self, text='Exit', command=master.quit)
#         exit_button.pack()


# class WithdrawPage(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)

#         label = tk.Label(self, text='Withdraw Money', font=('Arial', 14))
#         label.pack(pady=10)

#         self.amount_entry = tk.Entry(self)
#         self.amount_entry.pack(pady=10)

#         withdraw_button = tk.Button(self, text='Withdraw', command=lambda: self.withdraw_money(master))
#         withdraw_button.pack(pady=10)

#         back_button = tk.Button(self, text='Back', command=lambda: master.switch_frame(TransactionPage))
#         back_button.pack()

#     def withdraw_money(self, master):
#         amount = int(self.amount_entry.get())
#         if master.balance >= amount:
#             master.balance -= amount
#             messagebox.showinfo("Success", "Please collect your cash and card.")
#             master.switch_frame(TransactionPage)
#         else:
#             messagebox.showerror("Error", "Insufficient balance")


# class BalancePage(tk.Frame):
#     def __init__(self, master):
#         tk.Frame.__init__(self, master)

#         label = tk.Label(self, text='Your Balance:  ₹' + str(master.balance), font=('Arial', 14))
#         label.pack(pady=10)

#         back_button = tk.Button(self, text='Back', command=lambda: master.switch_frame(TransactionPage))
#         back_button.pack()


# if __name__ == "__main__":
#     app = ATM()
#     app.mainloop()

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class ATM(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('ATM Machine')
        self.geometry('400x300')
        self.current_frame = None
        self.pin = "1234"  # Set the PIN
        self.balance = 50000  # Set the account balance
        self.switch_frame(WelcomePage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(expand=True, fill='both')


class WelcomePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        label = tk.Label(self, text='Welcome to ATM Machine', font=('Arial', 18))
        label.pack(pady=20)

        button = ttk.Button(self, text='Enter', command=lambda: master.switch_frame(PinPage))
        button.pack()


class PinPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        label = tk.Label(self, text='Please enter your PIN', font=('Arial', 14))
        label.pack(pady=10)

        self.pin_entry = tk.Entry(self, show='*')
        self.pin_entry.pack(pady=10)

        submit_button = ttk.Button(self, text='Submit', command=lambda: self.validate_pin(master))
        submit_button.pack(pady=10)

    def validate_pin(self, master):
        pin = self.pin_entry.get()
        if pin == master.pin:
            master.switch_frame(TransactionPage)
        else:
            messagebox.showerror("Error", "Incorrect PIN")


class TransactionPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        label = tk.Label(self, text='Select Transaction', font=('Arial', 14))
        label.pack(pady=10)

        withdraw_button = ttk.Button(self, text='Withdraw', command=lambda: master.switch_frame(WithdrawPage))
        withdraw_button.pack()

        balance_button = ttk.Button(self, text='Check Balance', command=lambda: master.switch_frame(BalancePage))
        balance_button.pack()

        exit_button = ttk.Button(self, text='Exit', command=master.quit)
        exit_button.pack()


class WithdrawPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        label = tk.Label(self, text='Withdraw Money', font=('Arial', 14))
        label.pack(pady=10)

        self.amount_entry = tk.Entry(self)
        self.amount_entry.pack(pady=10)

        withdraw_button = ttk.Button(self, text='Withdraw', command=lambda: self.withdraw_money(master))
        withdraw_button.pack(pady=10)

        back_button = ttk.Button(self, text='Back', command=lambda: master.switch_frame(TransactionPage))
        back_button.pack()

    def withdraw_money(self, master):
        amount = int(self.amount_entry.get())
        if master.balance >= amount:
            master.balance -= amount
            messagebox.showinfo("Success", "Please collect your cash and card.")
            master.switch_frame(TransactionPage)
        else:
            messagebox.showerror("Error", "Insufficient balance")


class BalancePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        label = tk.Label(self, text='Your Balance:  ₹' + str(master.balance), font=('Arial', 14))
        label.pack(pady=10)

        back_button = ttk.Button(self, text='Back', command=lambda: master.switch_frame(TransactionPage))
        back_button.pack()


if __name__ == "__main__":
    app = ATM()
    app.mainloop()

