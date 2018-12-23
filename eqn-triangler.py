# eqn-triangler by Llamax
# Github: llamax1/eqn-triangler
# This program uses Python 3

# Import libraries
from tkinter import Tk, Entry, Button

# Set up an instance of Tkinter called 'root'
root = Tk()

# Variable names
# 
#       /\
#      /  \                                       No source code is complete
#     /  a \                                    without a silly comment. Enjoy! :)
#    /______\                                         ####################
#   /    |   \                                        #******************#
#  /  b  | c  \                                       #*  (__)   ____   *#
# /______|_____\                                      #*  (00)  |Moo!|  *#
#                                                     #*   \/  /____/   *#
#                                                     #******************#
#                                                     ####################

input_a = Entry()
input_b = Entry()
input_c = Entry()
calc_button = Button()

# Values from input widget
a = 0
b = 0
c = 0

# Gets all of the values from input boxes and calculates the missing one.
# Next line of code sets existing variables as default functions inside function.
def get_calculate(local_input_a=input_a, local_a=a, local_input_b=input_b, local_b=b, local_input_c=input_c, local_c=c):
    local_a = local_input_a.get()
    local_b = local_input_b.get()
    local_c = local_input_c.get()
    #local_input_b.insert(0, local_a)
    print(local_a)
    print(local_b)
    print(local_c)
    print("read")
    #root.update_idletasks()
    #root.update()

def input_box(window_name, widget_name, grid_row, grid_col, col_span):
    widget_name = Entry(window_name, width=5, justify="center")
    widget_name.grid(row=grid_row, column=grid_col, columnspan=col_span)

def a_button(window_name, widget_name, text, command, grid_row, grid_col, col_span):
    widget_name = Button(window_name, text=text, command=command, justify="center")
    widget_name.grid(row=grid_row, column=grid_col, columnspan=col_span)

input_box(root, input_a, 1, 1, 2)
input_box(root, input_b, 2, 1, 1)
input_box(root, input_c, 2, 2, 1)
a_button(root, calc_button, "Calculate!", get_calculate, 3, 1, 2)

root.mainloop()

#while (True):
#    root.update_idletasks()
#    root.update()
