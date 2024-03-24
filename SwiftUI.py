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


# class Button to achieve Button() in main.py file

class Button(View):

    def __init__(self):
        super().__init__()
        self.createButton = tkinter.Button(self.window, text="Test")
        self.createButton.pack()


# through running the SwiftUI-Library File, you get the demo-View with tests so everything works as expected
if __name__ == '__main__':
    demoView = View()
