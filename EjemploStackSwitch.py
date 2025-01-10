import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo con StackSwitch")
        self.set_size_request(400, 400) #definimos el tamaño de la ventana
        self.set_resizable(False) #indicamos que no se puede estirar la ventana

        cajaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        stackLayout = Gtk.Stack()
        stackLayout.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        stackLayout.set_transition_duration(1000)

        chkPulsame = Gtk.CheckButton(label = "Púlsame")
        stackLayout.add_titled(chkPulsame, "chk", "Check para pulsar")

        lblEtiqueta = Gtk.Label()
        lblEtiqueta.set_markup("<big> Una etiqueta </big>")

        stackLayout.add_titled(lblEtiqueta, "lbl", "Etiqueta elegante")

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(stackLayout)

        cajaV.pack_start(stack_switcher, True, True, 0)
        cajaV.pack_start(stackLayout, True, True, 0)
        self.add(cajaV)
        self.show_all() #mostramos los elementos




if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  #si cerramos la pp, se cierra todo
    Gtk.main()