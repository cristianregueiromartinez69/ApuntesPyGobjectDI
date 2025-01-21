import gi


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk


class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ejemplo con Treeview")
        self.set_size_request(250, 150)  # definimos el tamaño de la ventana
        self.set_resizable(False)  # indicamos que no se puede estirar la ventana

        self.columnas = ["Nome", "Apelido", "Numero de teléfono"]
        self.agendaTlefonica = [["Pepe", "Pérez", "986 543 210"],
                                ["Ana", "Alonso", "982 345 678"],
                                ["Rosa", "Vila", "621 432 567"],
                                ["Jose", "Diaz", "657 890 012"]]

        self.listore = Gtk.ListStore(str, str, str)
        for registro in self.agendaTlefonica:
            self.listore.append(registro)



        self.cajaVertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        self.vista = Gtk.TreeView(model=self.listore)

        for i in range(len(self.columnas)):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(self.columnas[i], celda, text = i)
            self.vista.append_column(columna)

        self.cajaVertical.pack_start(self.vista, True, True, 0)


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
