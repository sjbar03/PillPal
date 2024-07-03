import tkinter as tk
from tkinter import ttk

import Patient

class ConditonDisplay(ttk.Frame):

    def __init__(self, root):
        super().__init__(root,name="conditions", width=50, height= 200)

       # Add widgets 
        self.condition_label = ttk.Label(self, text = "Conditions: ")
        self.condition_box = tk.Listbox(self, width= 50, background= 'white', foreground='black')
        self.add_info_button()
        self.add_delete_button()

        # Grid widgets inside self
        self.condition_label.grid(row = 0, column= 1, sticky='NW')
        self.condition_box.grid(row = 1,rowspan = 10, column= 1, sticky= 'SW')

        # Theme config
        self.style = ttk.Style(self)
        self.style.theme_use('classic')

    def populate_conditions(self, patient:Patient.Patient):
        conditions = patient.diseases
        self.condition_box.configure(listvariable=tk.StringVar(self, value=conditions))

    def add_info_button(self):
        self.info_button = ttk.Button(self, text='H', padding=5)
        self.info_button.grid(row = 1, column=0)

    def add_delete_button(self):
        self.del_button = ttk.Button(self, text='X', padding=5)
        self.del_button.grid(row=2, column=0)
