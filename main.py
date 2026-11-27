from tkinter import Tk
from views.coches_view import CochesView
print("\033c")

class App:
    def __init__(self, ventana):
        self.ventana=ventana
        self.ventana=CochesView(self.ventana)


if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()
