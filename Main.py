import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_size_request(200, 200) #definimos el tamaño de la ventana
        self.set_resizable(False) #indicamos que no se puede estirar la ventana

        self.caja = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10) #declaramos el layout, que será vertical
        self.add(self.caja)

        '''
        declaramos los label, botones y texto
        '''

        self.lbSaudo = Gtk.Label(label="Nombre: ")
        self.caja.pack_start(self.lbSaudo, True, True, 0)

        self.txtSaudo = Gtk.Entry()
        self.caja.pack_start(self.txtSaudo, True, True, 0)
        self.txtSaudo.connect("activate", self.saludo_boton) #activamos la tecla enter

        self.btnSaudo = Gtk.Button(label="Pulsame")
        self.caja.pack_start(self.btnSaudo, True, True, 0)

        self.btnSaudo.connect("clicked", self.saludo_boton) #conectamos el boton con una funcion
        self.show_all() #mostramos el layout


    def saludo_boton(self, button):
        if self.txtSaudo.get_text() == "":
            print("El nombre está vacío")
        else:
            self.lbSaudo.set_label("Un saludo para " + self.txtSaudo.get_text())
            self.txtSaudo.set_text("")




if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  #si cerramos la pp, se cierra
    Gtk.main()