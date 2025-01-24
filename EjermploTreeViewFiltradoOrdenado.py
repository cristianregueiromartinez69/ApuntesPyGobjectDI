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
        self.modelo_filtrado = self.modelo.filter_new()
        self.modelo_filtrado.set_visible_func(self.filtro_usuario_xenero)


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

       # self.trvDatosUsuarios = Gtk.TreeView(model = self.modelo)
        self.trvDatosUsuarios = Gtk.TreeView(model=self.modelo_filtrado)
        self.seleccion = self.trvDatosUsuarios.get_selection()
        self.seleccion.connect("changed", self.on_seleccion_changed)
        self.celdaInicio = Gtk.CellRendererText()

        for i, tituloColumna in enumerate(["Dni", "Nome"]):
            self.celdaInicio = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(tituloColumna, self.celdaInicio, text = i)
            self.trvDatosUsuarios.append_column(columna)



        self.celdaProgress = Gtk.CellRendererProgress()
        self.columna = Gtk.TreeViewColumn("Edade", self.celdaProgress, value = 2)
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
        self.celdaCombo.connect("changed", self.on_celdaXenero_changed, self.modelo, 3)
        self.columnagenero = Gtk.TreeViewColumn("Xenero", self.celdaCombo, text = 3)
        self.trvDatosUsuarios.append_column(self.columnagenero)

        #añadiendo a los fallecidos
        self.celdaFallecido = Gtk.CellRendererToggle()
        self.celdaFallecido.set_property("activatable", True)  # Hacer que sea interactiva
        self.columnaFallecido = Gtk.TreeViewColumn("Fallecido", self.celdaFallecido, active = 4)
        self.trvDatosUsuarios.append_column(self.columnaFallecido)

        self.cajaFiltrarHorizontal = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        self.rbButtonHome = Gtk.RadioButton(label = "Home")
        self.rbButtonMuller = Gtk.RadioButton(label = "Muller")
        self.rbButtonNoHayMas = Gtk.RadioButton(label = "No Hay Mas")

        self.cajaFiltrarHorizontal.pack_start(self.rbButtonHome, False, False, 0)
        self.cajaFiltrarHorizontal.pack_start(self.rbButtonMuller, False, False, 0)
        self.cajaFiltrarHorizontal.pack_start(self.rbButtonNoHayMas, False, False, 0)

        self.rbButtonHome.connect("toggled", self.on_genero_toggled, "Home", self.modelo)
        self.rbButtonHome.connect("toggled", self.on_genero_toggled, "Muller", self.modelo)
        self.rbButtonHome.connect("toggled", self.on_genero_toggled, "No hay más", self.modelo)

        self.cajaVertical.pack_start(self.cajaFiltrarHorizontal, False, False, 0)


        self.celdaFallecido.connect("toggled", self.on_toogled_chanded, self.modelo)

        self.cajaVertical.pack_start(self.trvDatosUsuarios, False, True, 0)

        self.add(self.cajaVertical)
        self.show_all()

    def on_seleccion_changed(self, seleccion):
        model, iterador = seleccion.get_selected()
        if iterador != None:
            dni = model[iterador][0]
            return dni

    def on_celdaXenero_changed(self, celda, fila, filaXenero, modelo, columna):
        print(celda.props.model[filaXenero][0])
        print(modelo[fila][columna])
        modelo[fila][columna] = celda.props.model[filaXenero][0]
        newGenero = celda.props.model[filaXenero][0]
        dni = self.on_seleccion_changed(self.seleccion)
        self.base.update_usuarios2(newGenero, dni)

    def on_toogled_chanded(self, control, fila, modelo):
        #modelo[fila][4] = not modelo[fila][4]
        modelo[fila][4] = False if  control.get_active() else True
        print(modelo[fila][4])
        dni = self.on_seleccion_changed(self.seleccion)
        if modelo[fila][4]:
            self.base.update_fallecido(1, dni)
        else:
            self.base.update_fallecido(0, dni)

    def on_genero_toggled(self, radioButton, genero, modelo):
        if radioButton.get_active():
            self.filtradoGenero = genero
            #self.filtradoGenero = radioButton.props.label
            self.modelo.refilter()

    def filtro_usuario_xenero(self, modelo, fila, datos):
        if self.filtradoGenero is None or self.filtradoGenero == "None":
            return True
        else:
            return modelo[fila][3] == self.filtradoGenero

'''
Mostra el ultimo campo de la tabla de usuarios2 que es un bool
1. que se muestra
2. si clicamos que se cambie le modelo
3. que tenga repercusión en la tabla
'''

if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  # si cerramos la pp, se cierra todo
    Gtk.main()
