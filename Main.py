import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_size_request(200, 200)

        self.caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(self.caja)

        self.lbSaudo = Gtk.Label(label="Nombre: ")
        self.caja.pack_start(self.lbSaudo, True, True, 0)

        self.txtSaudo = Gtk.Entry()
        self.caja.pack_start(self.txtSaudo, True, True, 0)

        self.btnSaudo = Gtk.Button(label="Pulsame")
        self.caja.pack_start(self.btnSaudo, True, True, 0)

        self.btnSaudo.connect("clicked", self.saludo_boton)
        self.show_all()


    def saludo_boton(self, button):
        if self.txtSaudo.get_text() == "":
            print("El nombre está vacío")
        else:
            self.lbSaudo.set_label("Un saludo para " + self.txtSaudo.get_text())


if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  # Cerrar la ventana
    Gtk.main()