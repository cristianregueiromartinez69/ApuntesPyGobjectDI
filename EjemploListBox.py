import gi


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

class ListBoxConDatos(Gtk.ListBoxRow):
    def __init__(self, dato):
        super().__init__()
        self.dato = dato
        self.add(Gtk.Label(label=dato))



class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo con ListBox")
        self.set_size_request(400, 400)  # definimos el tamaño de la ventana
        self.set_resizable(False)  # indicamos que no se puede estirar la ventana

        self.cajaPrincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.listBox = Gtk.ListBox()
        self.listBox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.cajaPrincipal.pack_start(self.listBox, True, True, 0)

        self.fila = Gtk.ListBoxRow()
        self.cajaHorizontal = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.fila.add(self.cajaHorizontal)

        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.cajaHorizontal.pack_start(self.cajaVertical, True, True, 0)

        self.lblEtiqueta1 = Gtk.Label(label= "Fecha y hora automáticas")
        self.lblEtiqueta2 = Gtk.Label(label= "Acceso a intered")
        self.cajaVertical.pack_start(self.lblEtiqueta1, True, True, 0)
        self.cajaVertical.pack_start(self.lblEtiqueta2, True, True, 0)


        int = Gtk.Switch()
        int.props.valign = Gtk.Align.CENTER

        self.cajaHorizontal.pack_start(int, False, False, 0)
        self.listBox.add(self.fila)

        self.fila2 = Gtk.ListBoxRow()
        self.cajaHFila2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.fila2.add(self.cajaHFila2)

        self.lblEtiqueta3 = Gtk.Label(label= "Permite actualiación automática", xalign=0)
        check = Gtk.CheckButton()
        self.cajaHFila2.pack_start(self.lblEtiqueta3, True, True, 0)
        self.cajaHFila2.pack_start(check, False, False, 0)

        self.listBox.add(self.fila2)

        self.listBox2 = Gtk.ListBox()
        self.listBox2.set_sort_func(self.funcion_ordenacion) #Permite pasar una funcion que ordene bajo el criterio que decidas lo que es la lista
        self.listBox2.set_filter_func(self.funcion_filtracion)
        elementos = "Esta es una lista con elementos desordenada".split()
        for elemento in elementos:
            self.listBox2.add(ListBoxConDatos(elemento))

        self.listBox2.connect("row-activated", self.on_row_activated)
        self.cajaPrincipal.pack_start(self.listBox2, True, True, 0)



        self.listBox2.show_all()


        self.add(self.cajaPrincipal)
        self.show_all()  # mostramos los elementos

    def on_row_activated(self, listBox, fila):
        print(fila.dato)

    def funcion_ordenacion(self, fila1, fila2):
        return fila1.dato.lower() < fila2.dato.lower()

    def funcion_filtracion(self, fila):
        return False if fila.dato == "lista" else True


if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  # si cerramos la pp, se cierra todo
    Gtk.main()
