from cProfile import label

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo con NoteBook")
        self.set_size_request(400, 400) #definimos el tamaño de la ventana
        self.set_resizable(False) #indicamos que no se puede estirar la ventana

        cajaNotebook = Gtk.Notebook()

        pagina1Notebook = Gtk.Box()
        pagina1Notebook.set_border_width(10)
        pagina1Notebook.add(Gtk.Label(label = "Pagina 1"))

        pagina2 = Gtk.Box()
        pagina2.set_spacing(10)
        pagina2.set_border_width(10)
        pagina2.add(Gtk.Label(label = "Pagina 2"))

        cajaNotebook.append_page(pagina1Notebook, Gtk.Label("Pagina 1"))

        cajaNotebook.append_page(pagina2, Gtk.Image.new_from_icon_name("help_about", Gtk.IconSize.MENU))


        self.add(cajaNotebook)
        self.show_all() #mostramos los elementos




if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  #si cerramos la pp, se cierra todo
    Gtk.main()