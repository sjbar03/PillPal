import tkinter as tk

from tkinter import ttk
from ListTable import *

import Patient


class PalApplication(tk.Tk):

    def __init__(self, col_names=[], contents:list[list[str]]=[[]]):
        super().__init__()
        self.configure(background="white")
        self.set_style()
        self.add_table(col_names, contents)

    def add_table(self, col_names, contents):
        self.table = ListTable(self, col_names=col_names, contents=contents, col_sizes= [35,35,15,15])
        self.table.grid()

    def set_style(self):
        self.style = ttk.Style(self)
        self.style.theme_use('classic')

    def start_gui(self):
        self.mainloop()


p = Patient.Patient("Stephen", '10/09/2003', 'United Healthcare')
p.generate_meds()

pal = PalApplication(col_names=["Brand","Generic", "Dosage Form", "NDC"], contents=p.meds_to_table())
pal.mainloop()
