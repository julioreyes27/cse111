import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area Rectangle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """

    lbl_width = Label(frm_main, text="width:")
    ent_width = IntEntry(frm_main, width=4)

    lbl_heigth = Label(frm_main, text="heigth:")
    ent_heigth = IntEntry(frm_main, width=4)

    lbl_lenght_unit = Label(frm_main, text="cm")
    
    lbl_area = Label(frm_main, text="Area:")
    lbl_results = Label(frm_main, width=3)
    lbl_area_units = Label(frm_main, text="cm2")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_width.grid(      row=0, column=0, padx=3, pady=3)
    ent_width.grid(      row=0, column=1, padx=3, pady=3)
    lbl_lenght_unit.grid(row=0, column=2, padx=0, pady=3)
    
    lbl_heigth.grid(      row=1, column=0, padx=3, pady=3)
    ent_heigth.grid(      row=1, column=1, padx=3, pady=3)
    lbl_lenght_unit.grid(row=1, column=2, padx=0, pady=3)

    lbl_area.grid(     row=2, column=0, padx=(30,3), pady=3)
    lbl_results.grid(      row=2, column=1, padx=3, pady=3)
    lbl_area_units.grid(      row=2, column=2, padx=3, pady=3)

    btn_clear.grid(row=3, column=0, padx=3, pady=3, columnspan=4, sticky="w")


    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            width = ent_width.get()
            heigth = ent_heigth.get()
            area = width * heigth
            lbl_results.config(text=f"{area:.2f}")

        except ValueError:
            lbl_results.config(text="")

    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_width.clear()
        ent_heigth.clear()
        lbl_results.config(text="")
        ent_width.focus()

    ent_width.bind("<KeyRelease>", calculate)
    ent_heigth.bind("<KeyRelease>", calculate)

    btn_clear.config(command=clear)

    ent_width.focus()

if __name__ == "__main__":
    main()