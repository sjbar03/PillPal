import tkinter as tk
from tkinter import ttk

import Patient

class ConditonDisplay(ttk.Frame):

    def __init__(self, root):
        super().__init__(root,name="conditions", width=50, height= 200)

       # Add widgets 
        self.condition_label = ttk.Label(self, text = "Conditions: ", padding= 10)
        self.condition_box = tk.Listbox(self, width= 50, background= 'white', foreground='black')
        self.add_info_button()
        self.add_delete_button()

        # Grid widgets inside self
        self.condition_label.grid(row = 0, column= 1, sticky='NW')
        self.condition_box.grid(row = 1,rowspan = 10, column= 1, sticky= 'SW')

    def populate_conditions(self, patient:Patient.Patient):
        conditions = patient.diseases
        self.condition_box.configure(listvariable=tk.StringVar(self, value=conditions))

    def add_info_button(self):
#        self.q_img = tk.PhotoImage(file='data/question.png')
        self.info_button = ttk.Button(self, text= "❓", width=5)
        self.info_button.grid(row = 1, column=0, sticky="NSEW")

    def add_delete_button(self):
        self.del_button = ttk.Button(self, text='❌', width= 5, command=self.remove_condition)
        self.del_button.grid(row=2, column=0, sticky="NSEW")

    def remove_condition(self):

        sel = self.condition_box.curselection()

        if len(sel) > 0:

            for cond in sel:
                name = self.condition_box.get(cond)
                new_lines = []
                file = open('data/conditions.txt', 'r')
                for line in file:
                    if name not in line:
                        new_lines.append(line)
                file.close()
                
                file = open('data/conditions.txt', 'w')
                for line in new_lines:
                    file.write(line)
                file.close()

