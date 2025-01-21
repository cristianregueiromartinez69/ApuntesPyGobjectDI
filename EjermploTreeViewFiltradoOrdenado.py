import gi


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from ConexionDB import *


class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo con Treeview de filtrado y ordenado")
        self.set_size_request(400, 150)  # definimos el tamaño de la ventana
        self.set_resizable(False)  # indicamos que no se puede estirar la ventana

        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.base = ConexionBD("usuarios.db")

        self.filtradoGenero = None
        self.modelo = Gtk.ListStore(str, str, int, str, bool)

        self.datosbase = self.base.consultaSenParametros("SELECT * FROM usuarios2")

        for registro in self.datosbase:
            self.modelo.append(registro)

        '''
        self.datos = [
                    ("12345678K", "pepe", 18, "masculino", 0),
                    ("12312312H", "Javier", 30, "masculino", 1),
                    ("98778965", "Veronica", 89, "femenino", 1),
                    ("67675454", "Alejandro", 67, "masculino", 0),
                ]
        '''

        self.trvDatosUsuarios = Gtk.TreeView(model = self.modelo)
        self.seleccion = self.trvDatosUsuarios.get_selection()

        for i, tituloColumna in enumerate(["Dni", "Nome"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(tituloColumna, celda, text = i)
            self.trvDatosUsuarios.append_column(columna)

        self.celdaProgress = Gtk.CellRendererProgress()
        self.columna = Gtk.TreeViewColumn("Edade", self.celdaProgress, value = 0)
        self.trvDatosUsuarios.append_column(self.columna)

        self.modeloCombo = Gtk.ListStore(str)
        self.modeloCombo.append(["Muller"])
        self.modeloCombo.append(["Home"])
        self.modeloCombo.append(["No hay más"])

        self.celdaCombo = Gtk.CellRendererCombo()
        self.celdaCombo.set_property("editable", True)
        self.celdaCombo.props.model = self.modeloCombo
        self.celdaCombo.set_property("text-column", 0)
        self.celdaCombo.set_property("has-entry", False)
        self.celdaCombo.connect("edited", self.on_celdaXenero_edited, self.modelo, 3)
        self.columnagenero = Gtk.TreeViewColumn("Xenero", self.celdaCombo, text = 3)

        self.trvDatosUsuarios.append_column(self.columnagenero)


        #dni, nome,. edade, genero, fallecido

        self.cajaVertical.pack_start(self.trvDatosUsuarios, False, True, 0)

        self.add(self.cajaVertical)
        self.show_all()

    def on_celdaXenero_edited(self):
        pass


if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  # si cerramos la pp, se cierra todo
    Gtk.main()
