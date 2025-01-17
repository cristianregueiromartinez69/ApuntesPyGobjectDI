import gi


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo con ComboBox")
        self.set_size_request(200, 100)  # definimos el tamaño de la ventana
        self.set_resizable(False)  # indicamos que no se puede estirar la ventana

        self.modelo = Gtk.ListStore(int, str)

        self.modelo.append([1, "Ana Pérez"])
        self.modelo.append((12, "Rosa Gómez"))
        self.modelo.append((13, "Roque Ros"))
        self.modelo.append((77, "Jośe féliz díaz"))
        self.modelo.append((25, "Tomás Roncero"))

        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.comnoNombres = Gtk.ComboBox.new_with_model_and_entry(model=self.modelo)

        self.comnoNombres.set_entry_text_column(1)

        self.cajaVertical.pack_start(self.comnoNombres, True, True, 0)





        self.add(self.cajaVertical)
        self.show_all()  #



if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  # si cerramos la pp, se cierra todo
    Gtk.main()
