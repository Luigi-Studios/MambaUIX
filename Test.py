# TODO: Fix HStack
# TODO: Make VStack better

import tkinter


# creates window
window = tkinter.Tk()
window.title("Test Window for V/H/ZStacks")
window.geometry("500x500")


# function used to align multiple elements evenly across y-axis
def VStack(*args):

    # gets the current values
    window.update()
    window_height = window.winfo_height()
    window_width = window.winfo_width()
    amount_of_buttons = len(args)
    button_height = 28

    # calculates the even spacing between the elements
    Abstand = (window_height - (button_height * amount_of_buttons)) / (amount_of_buttons+1)

    for button in range(len(args)):
        create_button = tkinter.Button(window, text="Test")
        create_button.pack()

        button_pos_x = (window_height / 2) - button_height
        button_pos_y = (Abstand * (button + 1)) + (button_height * button)

        create_button.place(x=button_pos_x, y=button_pos_y)

    window.update()


window.update()
VStack(1, 2, 3)
window.mainloop()