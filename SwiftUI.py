# Notes

""" Important: in order to have multiple tkinter windows opened at the same time, you first need to create the windows
 and afterward, run them."""

# should work as SwiftUI

# import libraries

import tkinter


# class view, which creates a new window
class View:

    # takes the elements as a tuple, and create some default values, e.g. width, height
    def __init__(self, *args, width=300, height=300):

        # creates and sets window values (title, width, height)
        self.window = tkinter.Tk()
        self.window.title("made with MambaUIX")
        self.window.geometry(f"{width}x{height}")

        # preparing the elements for the view
        for arg in args:
            if type(arg) is Button:
                self.create_button = tkinter.Button(self.window, text=arg)
                self.create_button.pack()

    # shows the window on the screen by calling window.mainloop()

    """ Why we need to do this:
        1. We don't know, when the user stops adding elements to his widgets and by calling this method at the end,
           we make sure that everything is ready
        2. The way that the widgets are build by tkinter, we need to create all widgets first and then execute them
           otherwise they won't work as expected"""

    def start(self):
        self.window.mainloop()


# class Button to achieve Button() in main.py file

class Button:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


# through running the SwiftUI-Library File, you get the demo-View with tests so everything works as expected
if __name__ == '__main__':
    demoView = View(Button("made with MambaUIX"))
    demoView.start()
