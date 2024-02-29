# sollte wie SwiftUI funktionieren
# Bibliotheken importieren
import tkinter

# TODO: view in Klasse View einen besseren Namen geben, bessere Verwendung für if name == main


# die Klasse View, die ein neues Fenster erstellt
class View:
    def __init__(self):
        view = tkinter.Tk()
        view.mainloop()


# durch das Ausführen der SwiftUI-Bibliothek wird (erstmal) die Version ausgegeben
if __name__ == '__main__':
    print("Version 1.0")
