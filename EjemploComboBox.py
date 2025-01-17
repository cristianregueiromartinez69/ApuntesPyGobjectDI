import gi


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo con ComboBox")
        self.set_size_request(200, 100)  # definimos el tamaño de la ventana
        self.set_resizable(False)  # indicamos que no se puede estirar la ventana

        self.modelo = Gtk.ListStore(int, str)

        self.modelo.append([1, "Ana Pérez"])
        self.modelo.append((12, "Rosa Gómez"))
        self.modelo.append((13, "Roque Ros"))
        self.modelo.append((77, "José féliz díaz"))
        self.modelo.append((25, "Tomás Roncero"))

        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.comnoNombres = Gtk.ComboBox.new_with_model_and_entry(model=self.modelo)

        self.comnoNombres.set_entry_text_column(1)

        self.comnoNombres.connect("changed", self.on_comboNomes_changed)

        self.txtCadroTexto = self.comnoNombres.get_child()
        self.txtCadroTexto.connect("activate", self.on_txtCadroTexto_activate)

        self.cajaVertical.pack_start(self.comnoNombres, True, True, 0)

        self.modelo_paises = Gtk.ListStore(str)
        self.paises = ["Portugal", "Irlanda", "Países Bajos", "España", "Jovenlandia", "Noruega", "China", "Estados Unidos", "Suiza", "Ghana"]
        for pais in self.paises:
            self.modelo_paises.append((pais,))

        self.cmbPaises = Gtk.ComboBox.new_with_model(model=self.modelo_paises)

        # Esto es igual que lo de arriba self.cmbPaises = Gtk.ComboBox()
        # esto es igual que lo dce arriba self.cmbPaises.set_model(self.modelo_paises)

        self.celdaTexto = Gtk.CellRendererText()
        self.cmbPaises.pack_start(self.celdaTexto, True)
        self.cmbPaises.add_attribute(self.celdaTexto, "text", 0)

        self.cajaVertical.pack_start(self.cmbPaises, True, True, 0)


        self.add(self.cajaVertical)
        self.show_all()

    def on_comboNomes_changed(self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            self.modelo = combo.get_model()
            num, nome = self.modelo[fila][:2]

            '''
            Esto de aquí es lo mismo que lo de arriba
            '''
            num = self.modelo[fila][0]
            nome = self.modelo[fila][1]
            print("Seleccionado : \nNum = %d \nNome = %s" % (num, nome))

    def on_txtCadroTexto_activate(self, cadroTexto):
        print("Tecleado: %s" % cadroTexto.get_text())
        self.modelo.append((288, cadroTexto.get_text()))


if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  # si cerramos la pp, se cierra todo
    Gtk.main()
