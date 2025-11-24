import tkinter as tk
from pages.prompt_page import PromptPage
from pages.home_page import HomePage
from pages.game_page import *

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("800x600")

        self.username = ""
        self.current_rounds = 0

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (HomePage, PromptPage):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, stick="nsew", padx=20, pady=20)

        self.show_frame(PromptPage)

            
    def show_frame(self, frame):
        content = self.frames[frame]
        content.tkraise()


