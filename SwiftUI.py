# should work as SwiftUI
# import libraries
import tkinter


# class view, which creates a new window
class View:
    def __init__(self):
        self.window = tkinter.Tk()


class Button(View):

    def __init__(self):
        super().__init__()
        self.createButton = tkinter.Button(self.window, text="Test")
        self.createButton.pack()


# through running the SwiftUI-Library File, you get the demo-View with tests so everything works as expected
if __name__ == '__main__':
    demoView = View()
