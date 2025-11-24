import tkinter as tk
from tkinter import ttk 


class PromptPage(ttk.Frame):
    fonts = {
        "formInput" : ("Helvetica 16 normal")
    }

    def __init__(self, parent, controller):
        super().__init__(parent)    

        cur_name = controller.username
        current_rounds = controller.current_rounds

        username = tk.StringVar(cur_name)
        rounds = tk.IntVar(current_rounds)

        username_input = tk.Entry(self, textvariable=username, font=self.fonts["formInput"])
        username_input.pack()

        rounds_input = tk.Entry(self, textvariable=rounds, font=self.fonts["formInput"])
        rounds_input.pack()