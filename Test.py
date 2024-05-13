# TODO: Fix HStack

import tkinter

window = tkinter.Tk()
window.title("Test Window for V/H/ZStacks")
window.geometry("500x500")


def VStack(*args):
    window.update()
    window_height = window.winfo_height()
    window_width = window.winfo_width()
    amount_of_buttons = len(args)
    Button_height = 28

    Abstand = (window_height - (Button_height * len(args))) / (len(args)+1)
    print(Abstand)

    for button in range(len(args)):
        create_button = tkinter.Button(window, text="Test")
        create_button.pack()

        button_x = (window_height / 2) - Button_height
        button_y = (Abstand * (button + 1)) + (Button_height * button)

        create_button.place(x=button_x, y=button_y)

    window.update()


def HStack(*args):
    window.update()
    window_height = window.winfo_height()
    window_width = window.winfo_width()
    amount_of_buttons = len(args)
    Button_height = 28
    Button_width = 63

    Abstand = (window_width - (Button_width * len(args))) / (len(args)+1)
    print(Abstand)

    for button in range(len(args)):
        create_button = tkinter.Button(window, text="Test")
        create_button.pack()

        button_x = (Abstand * (button + 1)) + (Button_width * button)
        button_y = (window_height / 2) - Button_height

        create_button.place(x=button_x, y=button_y)

    window.update()


window.update()
VStack(1, 2, 3)
window.mainloop()
