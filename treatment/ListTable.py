import tkinter as tk
from tkinter import ttk

class ListTable(ttk.Frame):

    def __init__(self, master, col_names=[], contents: list[list[str]]=[[]], col_sizes=[], width=100):
        assert len(contents) == 0 or len(col_names) == len(contents[0])
        super().__init__(master)

        # Configure grid method for Frame
        self.configure(width= width, height= 500)
#       tk.Grid.rowconfigure(self, 0, weight=1)
#       tk.Grid.columnconfigure(self, 0, weight=1)

        # Assign default column ratio if proper col_sizes was not passed
        if len(col_sizes) == len(col_names):
            self.col_ratio = col_sizes
        else:
            ratio = 100 / len(col_names)
            self.col_ratio = []
            for i in range(len(col_names)):
                self.col_ratio.append(ratio)

        # Configure frame attributes
        self.box_width = width
        self.columns:list[tk.Listbox] = []
        self.num_rows = len(contents)
        self.col_names = col_names

        # Add all columns 
        for i in range(len(col_names)):
            col_content = []

            for row in contents:
                col_content.append(row[i])

            self.add_col(col_names[i],col_content, i)
        self.add_headers(col_names)

        # Add scroll logic and tie columns together
        self.selected_row = 0
        self.create_y_scroll()
        self.add_headers(col_names)

    '''
    Remove all entries from the table (clear each column)
    '''
    def clear_table(self):
        for col in self.columns:

            col.configure(listvariable=tk.StringVar(self, value=[]))

    '''
    Add column with name [ col_name ], contents [ body ], at position [ index ] in the table.
    '''
    def add_col(self, col_name, body, index):
        new_col = tk.Listbox(self, 
                             listvariable=tk.StringVar(self, value=body, name=col_name), 
                             bg="white", fg="black", exportselection=False, selectmode="single",
                             width= int(self.col_ratio[index] / 100 * self.box_width), font= ('Times', 14),
                             height=20)

        # Configure Grid object for this specific column
        #tk.Grid.columnconfigure(new_col, 0, weight=1)
        #tk.Grid.rowconfigure(new_col, 0, weight=1)
        new_col.grid(row=1, column=len(self.columns))

        # Add all necessary bindings for united scrolling
        new_col.bind("<<ListboxSelect>>", self.select_row)
        new_col.bind("<MouseWheel>", self.on_mouse_wheel)
        new_col.bind("<Button-4>", self.on_mouse_wheel)
        new_col.bind("<Button-5>", self.on_mouse_wheel)

        self.columns.append(new_col)

    '''
    Populate the column witht the medicine prescribed to [ patient ].
    '''
    def populate_table(self, patient):

        new_content = patient.meds_to_table()

        for i in range(len(self.columns)):
            col_content = []

            for row in new_content:
                col_content.append(row[i])

            self.columns[i].configure(listvariable= tk.StringVar(self, value = col_content, name = self.col_names[i]))

    '''
    Add header labels above each column with names corresponding to each index.
    '''
    def add_headers(self, col_names): 

        col = 0
        for name in col_names:

            head = ttk.Label(self, text=name, justify='center', width=self.col_ratio[col] / 100 * self.box_width)
            head.grid(row=0,column=col)
            col += 1

    '''
    Unifying selection function. Ensures that when any column has a row selected, the other columns update to match the selection.
    '''
    def select_row(self, evt):
        selection = evt.widget.curselection()
        if selection:

            # Update table-wide selected_row attribute
            self.selected_row = selection[0]

            for col in self.columns:
                curr = col.curselection()
                col.selection_clear(0,tk.END)
                col.selection_set(self.selected_row)

    '''
    Create and grid the y-dimension scrollbar for the table. Scrolls all columns syncronously.
    '''
    def create_y_scroll(self):
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.on_vsb) # Custom on_vsb function that unifies each column.
        self.y_scroll = scrollbar
        self.y_scroll.grid(row= 0,column= len(self.columns) + 1)

    '''
    Recieves scroll_bar input and updates each column according to args.
    '''
    def on_vsb(self, *args):
        for box in self.columns:
            box.yview(*args)

    '''
    When mouse wheel event is detected, update each columns yview accordingly.
    '''
    def on_mouse_wheel(self, evt):
        # 4 and 5 -> linux key binds
        if evt.num == 4:
            delta = -1
        elif evt.num == 5:
            delta = 1
        else:
            # macos and windows keybinds.
            delta =  -evt.delta

        for box in self.columns:
            box.yview('scroll', delta, 'units')

        return 'break'
