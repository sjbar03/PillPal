import tkinter as tk
from tkinter import ttk

class ListTable(ttk.Frame):

    def __init__(self, master, col_names=[], contents: list[list[str]]=[[]], col_sizes=[], width=100):
        assert len(col_names) == len(contents[0])
        super().__init__(master)

        if len(col_sizes) == len(col_names):
            self.col_ratio = col_sizes
        else:
            ratio = 100 / len(col_names)
            self.col_ratio = []
            for i in range(len(col_names)):
                self.col_ratio.append(ratio)

        self.box_width = width
        self.columns:list[tk.Listbox] = []
        self.num_rows = len(contents)

        for i in range(len(col_names)):
            col_content = []

            for row in contents:
                col_content.append(row[i])

            self.add_col(col_names[i],col_content, i)

        self.selected_row = 0
        self.create_y_scroll()
        self.add_headers(col_names)

    def add_col(self, col_name, body, index):
        
        new_col = tk.Listbox(self, 
                             listvariable=tk.StringVar(self, value=body, name=col_name), 
                             bg="white", fg="black", exportselection=False, selectmode="single",
                             width= int(self.col_ratio[index] / 100 * self.box_width), font= ('Times', 14))

        new_col.grid(row=1, column=len(self.columns))
        new_col.bind("<<ListboxSelect>>", self.select_row)
        new_col.bind("<MouseWheel>", self.on_mouse_wheel)
        new_col.bind("<Button-4>", self.on_mouse_wheel)
        new_col.bind("<Button-5>", self.on_mouse_wheel)
        self.columns.append(new_col)

    def add_headers(self, col_names): 

        col = 0
        for name in col_names:

            head = ttk.Label(self, text=name, justify='center', width=self.col_ratio[col] / 100 * self.box_width)
            head.grid(row=0,column=col)
            col += 1

    def select_row(self, evt):
        selection = evt.widget.curselection()
        if selection:

            self.selected_row = selection[0]

            for col in self.columns:

                curr = col.curselection()

                col.selection_clear(0,tk.END)
                col.selection_set(self.selected_row)

    def create_y_scroll(self):

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.on_vsb)
        self.y_scroll = scrollbar
        self.y_scroll.grid(row= 0,column= len(self.columns) + 1)

    def on_vsb(self, *args):
        for box in self.columns:
            box.yview(*args)

    def on_mouse_wheel(self, evt):
        if evt.num == 4:
            delta = -1
        elif evt.num == 5:
            delta = 1
        else:
            delta =  -evt.delta

        for box in self.columns:
            box.yview('scroll', delta, 'units')

        return 'break'
