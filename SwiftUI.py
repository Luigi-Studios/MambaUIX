# sollte wie SwiftUI funktionieren
# Bibliotheken importieren
import tkinter

# TODO: bessere Verwendung für if name == main


# die Klasse View, die ein neues Fenster erstellt
class View:
    def __init__(self):
        window = tkinter.Tk()
        window.mainloop()


# durch das Ausführen der SwiftUI-Bibliothek wird (erstmal) die Version ausgegeben
if __name__ == '__main__':
    print("Version 1.0")
