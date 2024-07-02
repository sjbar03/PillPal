import tkinter as tk

from tkinter import ttk
from ListTable import *
from ProfileDisplay import *

import Patient
import PatientGen

import threading


class PalApplication(tk.Tk):

    def __init__(self, col_names=[], contents:list[list[str]]=[]):
        super().__init__()

        # Initialize patient pool and current patient to None
        self.pool = PatientGen.PatientPool()
        self.curr_patient = Patient.Patient.placeholder()

        # Initialize Widgets
        self.add_profile()
        self.add_table(col_names, contents)
        self.add_new_patient_button()
        self.add_gen_meds_button()

        # Initialize frame theme
        self.set_style()
        self.grid_propagate(0)
        self.configure(width= 1000, height= 1000)
        tk.Grid.rowconfigure(self, 0, weight = 1)
        tk.Grid.columnconfigure(self, 0, weight=1)
        
    '''
    Add the medication table to the main pal interface. This table has set proportions at 25, 25, 30, 20 and a set width at 100
    '''
    def add_table(self, col_names, contents):
        self.table = ListTable(self, col_names=col_names, contents=contents, col_sizes= [25,25,30,20], width=100)
        self.table.grid(row=3, column=0, columnspan=4, sticky= 'S')

    '''
    Add Patient profile interface to the main window.
    '''
    def add_profile(self):
        self.profile = Profile(self)
        self.profile.grid(row=0, column=0, columnspan=2, rowspan = 3) 

    '''
    Add new patient button to main window.
    '''
    def add_new_patient_button(self):
        self.new_button = ttk.Button(text= "Next Patient", command=self.populate_fields)
        self.new_button.grid(row=0, column=1)

    '''
    Set style of main window and profile frame. Set both to 'classic'
    '''
    def set_style(self):
        main_style = ttk.Style(self)
        profile_style = ttk.Style(self.profile)
        main_style.theme_use('classic')
        profile_style.theme_use('classic')
        self.configure(background=main_style.lookup('classic','background'))

    '''
    Command to be called by new patient button. Generates a new patient, then loads it into self.patient, then populates profile boxes.
    '''
    def populate_fields(self):
        self.pool.generate_patient()
        self.curr_patient = self.pool.next_patient
        self.profile.populate_boxes(self.curr_patient)
        self.table.clear_table()

    '''
    Add generate meds button to main window.
    '''
    def add_gen_meds_button(self):
        self.meds_button = ttk.Button(self, text= "Generate Meds", command=self.async_gen_meds)
        self.meds_button.grid(row=1, column=1)

    '''
    Command to be called by gen meds button. Generates meds for self.curr_patient using the pool, then populates the med table.
    '''
    def gen_meds_command(self, pool, table):
        pool.generate_meds(self.curr_patient)
        table.populate_table(self.curr_patient)

    '''
    Call gen_meds_command in a worker thread so as not to hang the GUI. (The openfda get request can block for ~3-5 seconds.)
    '''
    def async_gen_meds(self):
        t = threading.Thread(target= self.gen_meds_command, args= [self.pool, self.table])
        t.start()

    '''
    Do all necessary starting operations, then enter mainloop.
    '''
    def start_gui(self):
        self.mainloop()

if __name__ == '__main__':
    
    pal = PalApplication(col_names=["Brand", "Generic", "For", "RXCUI"])
    pal.start_gui()
