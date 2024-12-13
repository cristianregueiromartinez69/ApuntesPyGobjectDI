import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("EjemploGtkGrid")
        self.set_size_request(100, 250) #definimos el tamaño de la ventana
        self.set_resizable(False) #indicamos que no se puede estirar la ventana

        self.maia = Gtk.Grid()

        self.boton1 = Gtk.Button(label="1")
        self.boton2 = Gtk.Button(label="2")
        self.boton3 = Gtk.Button(label="3")
        self.boton4 = Gtk.Button(label="4")
        self.boton5 = Gtk.Button(label="5")
        self.boton6 = Gtk.Button(label="6")
        self.boton7 = Gtk.Button(label="7")
        self.boton8 = Gtk.Button(label="8")
        self.boton9 = Gtk.Button(label="9")
        self.boton10 = Gtk.Button(label="10")
        self.boton11 = Gtk.Button(label="11")
        self.boton12 = Gtk.Button(label="12")


        self.maia.attach(self.boton1, 0, 0, 1, 1)
        self.maia.attach(self.boton2, 1, 0, 2, 1)
        self.maia.attach_next_to(self.boton3, self.boton1, Gtk.PositionType.BOTTOM, 1, 4)
        self.maia.attach_next_to(self.boton4, self.boton2, Gtk.PositionType.BOTTOM, 2, 3)
        self.maia.attach_next_to(self.boton5, self.boton4, Gtk.PositionType.BOTTOM, 1, 1)
        self.maia.attach_next_to(self.boton6, self.boton5, Gtk.PositionType.RIGHT, 1, 1)
        self.maia.attach_next_to(self.boton7, self.boton3, Gtk.PositionType.BOTTOM, 4, 4)

        self.maia.attach_next_to(self.boton8, self.boton7, Gtk.PositionType.BOTTOM, 2, 2)
        self.maia.attach_next_to(self.boton9, self.boton8, Gtk.PositionType.BOTTOM, 1, 1)
        self.maia.attach_next_to(self.boton10, self.boton9, Gtk.PositionType.RIGHT, 1, 1)
        self.maia.attach_next_to(self.boton11, self.boton9, Gtk.PositionType.BOTTOM, 2, 3)
        self.maia.attach_next_to(self.boton12, self.boton8, Gtk.PositionType.RIGHT, 4, 6)

        self.add(self.maia)


        self.show_all() #mostramos los elementos




if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  #si cerramos la pp, se cierra todo
    Gtk.main()