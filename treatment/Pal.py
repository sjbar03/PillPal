import tkinter as tk

from tkinter import ttk
from ListTable import *
from ProfileDisplay import *

import Patient
import PatientGen


class PalApplication(tk.Tk):

    def __init__(self, col_names=[], contents:list[list[str]]=[]):
        super().__init__()

        tk.Grid.rowconfigure(self, 0, weight = 1)
        tk.Grid.columnconfigure(self, 0, weight=1)
        
        self.add_profile()
        self.add_table(col_names, contents)
        self.add_new_patient_button()
        self.add_gen_meds_button()
        self.set_style()
        self.grid_propagate(0)
        self.configure(width= 1000, height= 1000)

        self.pool = PatientGen.PatientPool()
        self.curr_patient = None

    def add_table(self, col_names, contents):
        self.table = ListTable(self, col_names=col_names, contents=contents, col_sizes= [25,25,30,20], width=100)
        self.table.grid(row=3, column=0, columnspan=4, sticky= 'S')

    def add_profile(self):

        self.profile = Profile(self)
        self.profile.grid(row=0, column=0, columnspan=2, rowspan = 3) 

    def add_new_patient_button(self):
        self.new_button = ttk.Button(text= "Next Patient", command=self.populate_fields)
        self.new_button.grid(row=0, column=1)

    def set_style(self):
        main_style = ttk.Style(self)
        profile_style = ttk.Style(self.profile)
        
        main_style.theme_use('classic')
        profile_style.theme_use('classic')
        self.configure(background=main_style.lookup('classic','background'))

    def populate_fields(self):

        self.pool.generate_patient()
        self.curr_patient = self.pool.next_patient
        self.profile.populate_boxes(self.curr_patient)
        self.update()

    def add_gen_meds_button(self):
        self.meds_button = ttk.Button(self, text= "Generate Meds", command=self.gen_meds_command)
        self.meds_button.grid(row=1, column=1)

    def gen_meds_command(self):

        self.pool.generate_meds(self.curr_patient)
        self.table.populate_table(self.curr_patient)

    def start_gui(self):

        self.mainloop()

if __name__ == '__main__':
    
    pal = PalApplication(col_names=["Brand", "Generic", "For", "RXCUI"])
    pal.start_gui()
