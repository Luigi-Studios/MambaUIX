# Notes

""" Important: in order to have multiple tkinter windows opened at the same time, you first need to create the windows
 and afterward, run them."""

# should work as SwiftUI

# import libraries


import tkinter


# class view, which creates a new window
class View:
    def __init__(self):
        self.window = tkinter.Tk()

    # shows the window on the screen by calling window.mainloop()

    """ Why we need to do this:
        1. We don't know, when the user stops adding elements to his widgets and by calling this method at the end,
           we make sure that everything is ready
        2. The way that the widgets are build by tkinter, we need to create all widgets first and then execute them
           otherwise they won't work as expected"""

    def start(self):
        self.window.mainloop()


# class Button to achieve Button() in main.py file

class Button(View):

    def __init__(self):
        super().__init__()
        self.createButton = tkinter.Button(self.window, text="Test")
        self.createButton.pack()


# through running the SwiftUI-Library File, you get the demo-View with tests so everything works as expected
if __name__ == '__main__':
    demoView = View()
