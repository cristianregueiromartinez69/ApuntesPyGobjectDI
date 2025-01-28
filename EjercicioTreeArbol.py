import pathlib

import gi
from gi.overrides.Gtk import TreeStore

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk



class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo con Treeview de explorador de archivos")
        self.set_size_request(250, 150)  # definimos el tamaño de la ventana
        self.set_resizable(True)  # indicamos que no se puede estirar la ventana

        self.modelo = TreeStore(str, str)

        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.explorarDirectorio("/home/dam", None, self.modelo)


        self.treeVista = Gtk.TreeView(model=self.modelo)
        self.treeColumna1 = Gtk.TreeViewColumn()
        self.treeVista.append_column(self.treeColumna1)
        self.celdaGraficos = Gtk.CellRendererPixbuf()
        self.treeColumna1.pack_start(self.celdaGraficos, True)
        self.treeColumna1.add_attribute(self.celdaGraficos, "icon_name", 0)




        self.treeColumna2 = Gtk.TreeViewColumn()
        self.treeVista.append_column(self.treeColumna2)
        self.celdaVista = Gtk.CellRendererText()
        self.treeColumna2.pack_start(self.celdaVista, True)
        self.treeColumna2.add_attribute(self.celdaVista, 'text', 1)

        self.explorarDirectorio("/home/dam", None, self.modelo)


        self.cajaVertical.pack_start(self.treeVista, True, True, 0)


        self.add(self.cajaVertical)
        self.show_all()

    def explorarDirectorio(self, path, parent, modelo):
        contenidoDir = pathlib.Path(path)
        for entrada in contenidoDir.iterdir():
            if entrada.is_dir():
                punteiroFillo = modelo.append(parent, ("folder", entrada.name))
                self.explorarDirectorio(path + '/' + entrada.name, punteiroFillo, modelo)
            else:
                modelo.append(parent, ("emblem-documents", entrada.name))




if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  # si cerramos la pp, se cierra todo
    Gtk.main()


'''
  self.directorio = pathlib.Path("/home/dam")
        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.modelo = TreeStore(str, str)

        for item in self.directorio.iterdir():
            nombre = item.name
            tipo = "Directorio" if item.is_dir() else "Archivo"
            self.modelo.append(None, [nombre, tipo])

        self.treeview = Gtk.TreeView(model=self.modelo)

        for i, tituloColumna in enumerate(["Nombre", "Tipo"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(tituloColumna, celda, text=i)
            self.treeview.append_column(columna)
'''