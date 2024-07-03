import tkinter as tk

from tkinter import ttk
from ListTable import *
from ProfileDisplay import *
from ConditionDisplay import *

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
        self.add_button_frame()
        self.add_condition_frame()

        # Initialize frame theme
        self.geometry('840x730')
        self.minsize(840,730)
        self.set_style()
        self.configure(width= 1000, height= 1000)
        for i in range(4):
            tk.Grid.columnconfigure(self, i, weight=1)
            tk.Grid.rowconfigure(self, i, weight=1)

        # Set icon
        img = tk.PhotoImage(file= 'data/perc.png')
        self.iconphoto(False, img)
        self.title("PillPal")
        
    def add_condition_frame(self):
        self.condition_frame = ConditonDisplay(self)
        self.condition_frame.grid(row= 0, column=2, columnspan=2, rowspan=3, sticky='N')

    def add_button_frame(self):
        self.button_frame = ttk.Frame(self, padding=20)
        self.add_new_patient_button(self.button_frame)
        self.add_gen_meds_button(self.button_frame)
        self.button_frame.grid(row = 3, column= 3, sticky= 'E')

    '''
    Add the medication table to the main pal interface. This table has set proportions at 25, 25, 30, 20 and a set width at 100
    '''
    def add_table(self, col_names, contents):
        self.table = ListTable(self, col_names=col_names, contents=contents, col_sizes= [25,25,30,20], width=100)
        self.table.grid(row=4,column=0, columnspan=4, sticky= 'S')

    '''
    Add Patient profile interface to the main window.
    '''
    def add_profile(self):
        self.profile = Profile(self)
        self.profile.grid(row=0, column=0, columnspan=2, rowspan = 3, sticky = "W") 

    '''
    Add new patient button to main window.
    '''
    def add_new_patient_button(self, frame):
        self.new_button = ttk.Button(frame, text= "Next Patient ->", command=self.populate_fields, padding=20)
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
        self.condition_frame.populate_conditions(self.curr_patient)
        self.table.clear_table()

        # Call OpenFDA to prepare medcines in background.
        self.async_gen_meds()

    '''
    Add generate meds button to main window.
    '''
    def add_gen_meds_button(self, frame):
        self.meds_button = ttk.Button(frame, text= "Generate Meds", command=self.async_gen_meds, padding=20)
        self.meds_button.grid(row=0, column=0)

    '''
    Command to be called by gen meds button. Generates meds for self.curr_patient using the pool, then populates the med table.
    '''
    def gen_meds_command(self, pool, table):
        # First load in existing medicine list.
        table.populate_table(self.curr_patient)

        # Generate new meds to be loaded in next time button is clicked.
        try:
            pool.generate_meds(self.curr_patient)
        except:
            self.meds_button.state(["!disabled"])
            print("No internet connection.")
            return
        self.meds_button.state(['!disabled'])

    '''
    Call gen_meds_command in a worker thread so as not to hang the GUI. (The openfda get request can block for ~3-5 seconds.)
    '''
    def async_gen_meds(self):
        self.meds_button.state(['disabled'])
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
