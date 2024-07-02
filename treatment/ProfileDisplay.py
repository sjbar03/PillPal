import tkinter as tk
from tkinter import ttk
from Patient import *

class Profile(ttk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.configure(width=200, height= 500)
        self.add_labels()
        self.add_boxes()
        self.grid_propagate(0)


    def add_labels(self):
        # Create each label.
        self.name_label = ttk.Label(self, text="Name: ")
        self.age_label = ttk.Label(self, text= "Age: ")
        self.gender_label = ttk.Label(self, text= "Sex: ")

        # Grid each label
        self.name_label.grid(row=0, column=0)
        self.age_label.grid(row=1, column=0)
        self.gender_label.grid(row=2, column=0)

    def add_boxes(self):
        # Create each box
        self.name_box = ttk.Label(self, width=50, text="Place Holder")
        self.age_box = ttk.Label(self, width=50, text = "000")
        self.gender_box = ttk.Label(self, width=50, text="Non-Binary")

        # Grid each box
        self.name_box.grid(row= 0, column=1)
        self.age_box.grid(row=1, column=1)
        self.gender_box.grid(row=2, column=1)

    '''
    Place pertinent patient information into each label ('box') corresponding to it.
    '''
    def populate_boxes(self, patient: Patient):

        self.name_box.configure(text=patient.first_name + ' ' + patient.last_name)
        self.age_box.configure(text=str(patient.age))
        self.gender_box.configure(text= 'female' if patient.gender else 'male')


