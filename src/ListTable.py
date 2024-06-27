import tkinter as tk
from tkinter import ttk

class ListTable(ttk.Frame):

    def __init__(self, master, col_names=[], contents: list[list[str]]=[[]]):
        assert len(col_names) == len(contents)

        super().__init__(master)
        
        self.columns:list[tk.Listbox] = []
        self.num_rows = len(contents)

        for i in range(len(col_names)):

            self.add_col(col_names[i], contents[i])

        self.selected_row = 0

    def add_col(self, col_name, body):

        new_col = tk.Listbox(self, listvariable=tk.StringVar(self, value=body, name=col_name), bg="white", fg="black", exportselection=False)
        new_col.grid(row=0, column=len(self.columns))
        new_col.bind("<<ListboxSelect>>", self.select_row)
        self.columns.append(new_col)

    def select_row(self, evt):
        selection = evt.widget.curselection()
        print("Selection: ", selection)

        if selection:

            self.selected_row = selection[0]
            print(self.selected_row)

            for col in self.columns:

                curr = col.curselection()
                
                if not (len(curr) > 0 and curr[0] == self.selected_row):
                    
                    col.selection_clear(first=0,last=self.num_rows) 
                    col.selection_set(self.selected_row)
