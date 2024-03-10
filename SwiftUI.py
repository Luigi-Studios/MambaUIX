# should work as SwiftUI
# import libraries
import tkinter

# TODO: bessere Verwendung für if name == main


# class view, which creates a new window
class View:
    def __init__(self):
        window = tkinter.Tk()
        window.mainloop()


# through running the SwiftUI-Library File, you get the demo-View with tests so everything works as expected
if __name__ == '__main__':
    demoView = View()
