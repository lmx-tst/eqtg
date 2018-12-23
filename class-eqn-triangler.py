# eqn-triangler by Llamax
# Github: llamax1/eqn-triangler
# This program uses Python 3

from tkinter import Tk, Entry, Button, DoubleVar
import time

def log (a):
    print(a)
    time.sleep(0.1)

class Window:
    def __init__(self, master):
        log("class inited")
        
        self.a = DoubleVar()
        self.b = DoubleVar()
        self.c = DoubleVar()
        
        self.input_a = Entry()
        self.input_b = Entry()
        self.input_c = Entry()
        self.calc_button = Button()
        
        self.input_box(master, self.input_a, self.a, 1, 1, 2)
        self.input_box(master, self.input_b, self.b, 2, 1, 1)
        self.input_box(master, self.input_c, self.c, 2, 2, 1)
        self.a_button(master, self.calc_button, "Calculate!", self.get_calculate, 3, 1, 2)
        
        #master.mainloop()
        
    def get_calculate(self):
        self.a = self.a.get()
        self.b = self.b.get()
        self.c = self.c.get()
        #input_b.insert(0, a)
        print(self.a)
        print(self.b)
        print(self.c)
        print("read2")

    def input_box(self, master, widget_name, txt_var, grid_row, grid_col, col_span):
        log("box")
        widget_name = Entry(master, width=5, justify="center", textvariable=txt_var)
        widget_name.grid(row=grid_row, column=grid_col, columnspan=col_span)

    def a_button(self, master, widget_name, text, command, grid_row, grid_col, col_span):
        widget_name = Button(master, text=text, command=command, justify="center")
        widget_name.grid(row=grid_row, column=grid_col, columnspan=col_span)


root = Tk()
log("root")
window = Window(root)
root.mainloop()
log("window")
