import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from ConexionDB import ConexionBD

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Ejercicio usuarios")
        self.set_resizable(False)
        self.set_size_request(400,400)

        self.cajaVertical = Gtk.Box(Gtk.Orientation.VERTICAL, spacing=6)

        self.base = ConexionBD("perfisUsuarios.bd")

        self.datos = self.base.consultaSenParametros("SELECT dni, nome FROM usuarios")




        self.modeloDatos = Gtk.ListStore(str, str, str)



        for dato in self.datos:
            self.modeloDatos.append([dato[0], dato[1], "jeje"])




        self.viewUsuarios = Gtk.TreeView(model = self.modeloDatos)

        self.cajaVertical.pack_start(self.viewUsuarios, True, True, 0)

        self.add(self.cajaVertical)
        self.show_all()

if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()
