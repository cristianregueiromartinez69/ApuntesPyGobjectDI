import gi


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from ConexionDB import *


class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo con Treeview")
        self.set_size_request(250, 150)  # definimos el tamaño de la ventana
        self.set_resizable(False)  # indicamos que no se puede estirar la ventana

        self.base = ConexionBD("usuarios.db")


        self.datos_insertar = [("12345678K", "Pepe", "Pérez", "986 543 210"),
                               ("98765432A", "Ana", "Alonso", "982 345 678"),
                               ("12344321S", "Rosa", "Vila", "621 432 567"),
                               ("76567654C", "Jose", "Diaz", "657 890 012")]




        self.datosBase = self.base.consultaSenParametros("SELECT * FROM usuarios")

        self.columnas = ["DNI", "Nome", "Apelido", "Numero de teléfono"]

        self.listore = Gtk.ListStore(str, str, str, str)
        for registro in self.datosBase:
            self.listore.append(registro)



        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.vista = Gtk.TreeView(model=self.listore)

        self.objectoSeleccion = self.vista.get_selection()

        self.objectoSeleccion.connect("changed", self.on_obxetoSeleccion_changed)

        for i in range(len(self.columnas)):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(self.columnas[i], celda, text = i)
            if i == 1:
                columna.set_sort_column_id(i)
            self.vista.append_column(columna)

        self.cajaVertical.pack_start(self.vista, True, True, 0)


        self.add(self.cajaVertical)
        self.show_all()

    def on_obxetoSeleccion_changed(self, seleccion):
        (modelo, fila) = seleccion.get_selected()
        print(modelo[fila][0], modelo[fila][1], modelo[fila][2], modelo[fila][3])




if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  # si cerramos la pp, se cierra todo
    Gtk.main()
