import tkinter as tk
from tkinter import ttk
from ListTable import *


class PalApplication(tk.Tk):

    def __init__(self, col_names=[], contents:list[list[str]]=[[]]):
        super().__init__()
        self.configure(background="white")
        self.set_style()
        self.add_table(col_names, contents)

    def add_table(self, col_names, contents):
        self.table = ListTable(self, col_names=col_names, contents=contents)
        self.table.grid()

    def set_style(self):
        self.style = ttk.Style(self)
        self.style.theme_use('classic')

    def start_gui(self):
        self.mainloop()

table = [["Stephen", "Pearl", "Benjamin", "Oswald"], ["20", "19", "3", "1"], ["Orange", "Yellow", "Purple", "Black"]]
pal = PalApplication(col_names=["Col One", "Col Two", "Col Three"], contents=table)
pal.mainloop()
