import gi
from gi.overrides.Gtk import TreeStore

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk
from ConexionDB import *


class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo con Treeview arbol")
        self.set_size_request(250, 150)  # definimos el tamaño de la ventana
        self.set_resizable(False)  # indicamos que no se puede estirar la ventana


        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.modelo = TreeStore(str, int)
        for avo in range(5):
            punteiroAvo = self.modelo.append(None, ["Avo %i " % (avo, ), avo])
            for pai in range(4):
                punteiroPai = self.modelo.append(punteiroAvo, ["Pai %i do avo %i" % (pai, avo), pai])
                for fillo in range(2):
                    self.modelo.append(punteiroPai, ["Neto %i do pai %i do avo %i" % (fillo, pai, avo), fillo])

        self.treeVista = Gtk.TreeView(model = self.modelo)
        self.treeColumna = Gtk.TreeViewColumn("Parentesco")
        self.treeVista.append_column(self.treeColumna)
        self.celdaVista = Gtk.CellRendererText()
        self.treeColumna.pack_start(self.celdaVista, True)
        self.treeColumna.add_attribute(self.celdaVista, 'text', 0)

        self.treeColumna2 = Gtk.TreeViewColumn("Orde")
        self.treeVista.append_column(self.treeColumna2)
        self.celdaVista2 = Gtk.CellRendererText()
        self.treeColumna2.pack_start(self.celdaVista2, True)
        self.treeColumna2.add_attribute(self.celdaVista2, 'text', 1)

        self.cajaVertical.pack_start(self.treeVista, True, True, 0)

        self.add(self.cajaVertical)
        self.show_all()



if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  # si cerramos la pp, se cierra todo
    Gtk.main()


'''
importar libreria pathLib
Path() -> creamos el objeto path
'''