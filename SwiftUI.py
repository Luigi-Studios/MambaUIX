# should work as SwiftUI
# import libraries
import tkinter

# TODO: bessere Verwendung für if name == main


# class view, which creates a new window
class View:
    def __init__(self):
        window = tkinter.Tk()
        window.mainloop()


# through running die SwiftUI-Library File, you get (for now) the versions
if __name__ == '__main__':
    demoView = View()
