from gettext import textdomain

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from ConexionDB import ConexionBD

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Ejemplo de albaran")
        self.set_resizable(False)
        self.set_size_request(500,500)

        self.caja_vertical = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

        #conexion
        self.base = ConexionBD("modelosClasicos.dat")
        self.base.conectaBD()

        datos_albara = self.base.consultaSenParametros("select DISTINCT numeroAlbaran from detalleVentas")



        self.modelo_datos_combo = Gtk.ListStore(int)

        for dato in datos_albara:
            self.modelo_datos_combo.append([dato[0]])




        self.numero_albara_label = Gtk.Label(label="Número albará")
        self.numero_cliente_label = Gtk.Label(label = "Número cliente")
        self.nome_cliente_label = Gtk.Label(label="Nome Cliente")
        self.data_label = Gtk.Label(label="Data")
        self.data_entrega_label = Gtk.Label(label="Data entrega")
        self.apellidos_label = Gtk.Label(label="Apellidos")

        self.numero_albara_combo = Gtk.ComboBox.new_with_model(model = self.modelo_datos_combo)

        self.celda_texto_numero_alabara = Gtk.CellRendererText()
        self.numero_albara_combo.pack_start(self.celda_texto_numero_alabara, True)
        self.numero_albara_combo.add_attribute(self.celda_texto_numero_alabara, "text", 0)

        self.numero_albara_combo.set_active(0)

        self.numero_cliente_entry = Gtk.Entry()
        self.nome_cliente_entry = Gtk.Entry()
        self.data_entry = Gtk.Entry()
        self.data_entrega_entry = Gtk.Entry()
        self.apellidos_entry = Gtk.Entry()


        self.grid_datos = Gtk.Grid()
        self.grid_datos.set_row_spacing(5)
        self.grid_datos.set_column_spacing(5)

        self.grid_datos.attach(self.numero_albara_label, 0, 0, 1, 1)
        self.grid_datos.attach_next_to(self.numero_albara_combo, self.numero_albara_label, Gtk.PositionType.RIGHT, 1, 1)

        self.grid_datos.attach_next_to(self.numero_cliente_label, self.numero_albara_label, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_datos.attach_next_to(self.numero_cliente_entry, self.numero_cliente_label, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_datos.attach_next_to(self.nome_cliente_label, self.numero_cliente_label, Gtk.PositionType.BOTTOM, 1, 1)

        self.grid_datos.attach_next_to(self.nome_cliente_entry, self.nome_cliente_label, Gtk.PositionType.RIGHT, 1, 1)

        self.grid_datos.attach_next_to(self.data_label, self.numero_albara_combo, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_datos.attach_next_to(self.data_entry, self.data_label, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_datos.attach_next_to(self.data_entrega_label, self.data_label, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_datos.attach_next_to(self.data_entrega_entry, self.data_entrega_label, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_datos.attach_next_to(self.apellidos_label, self.data_entrega_label, Gtk.PositionType.BOTTOM, 1, 1)
        self.grid_datos.attach_next_to(self.apellidos_entry, self.apellidos_label, Gtk.PositionType.RIGHT, 1, 1)

        self.grid_datos_botones = Gtk.Grid()
        self.grid_datos_botones.set_row_spacing(5)
        self.grid_datos_botones.set_column_spacing(10)
        self.boton_engadir = Gtk.Button(label="Engadir")
        self.boton_engadir.set_size_request(150,15)
        self.boton_editar = Gtk.Button(label="Editar")
        self.boton_editar.set_size_request(150,15)
        self.boton_borrar = Gtk.Button(label="Borrar")
        self.boton_borrar.set_size_request(150,15)

        self.grid_datos_botones.attach(self.boton_engadir,  0, 0, 1, 1)
        self.grid_datos_botones.attach_next_to(self.boton_editar, self.boton_engadir, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_datos_botones.attach_next_to(self.boton_borrar, self.boton_editar, Gtk.PositionType.RIGHT, 1, 1)


        #tabla
        self.modelo_datos_tabla = Gtk.ListStore(int, int, str, int, float)

        self.datos_ejemplo = [
            (1, 1, "Vespa 15D", 1, 10500.0),
            (2, 2, "Casco retro", 2, 106.0)
        ]

        for dato in self.datos_ejemplo:
            self.modelo_datos_tabla.append([dato[0], dato[1], dato[2], dato[3], dato[4]])

        self.view_tabla = Gtk.TreeView(model = self.modelo_datos_tabla)


        self.celda_uno = Gtk.CellRendererText()
        self.columna_uno = Gtk.TreeViewColumn("1", self.celda_uno, text = 0)
        self.view_tabla.append_column(self.columna_uno)

        self.celda_dos = Gtk.CellRendererText()
        self.columna_dos = Gtk.TreeViewColumn("2", self.celda_dos, text=1)
        self.view_tabla.append_column(self.columna_dos)

        self.celda_tres = Gtk.CellRendererText()
        self.columna_tres = Gtk.TreeViewColumn("3", self.celda_tres, text=2)
        self.view_tabla.append_column(self.columna_tres)

        self.celda_cuatro = Gtk.CellRendererText()
        self.columna_cuatro = Gtk.TreeViewColumn("4", self.celda_cuatro, text=3)
        self.view_tabla.append_column(self.columna_cuatro)

        self.celda_cinco = Gtk.CellRendererText()
        self.columna_cinco = Gtk.TreeViewColumn("5", self.celda_cinco, text=4)
        self.view_tabla.append_column(self.columna_cinco)

        #conexiones
        self.numero_albara_combo.connect("changed", self.on_numero_albara_changed)


        self.caja_vertical.pack_start(self.grid_datos, True, True, 0)
        self.caja_vertical.pack_start(self.grid_datos_botones, True, True, 0)
        self.caja_vertical.pack_start(self.view_tabla, True, True, 0)

        self.add(self.caja_vertical)
        self.show_all()

    def on_numero_albara_changed(self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            self.modelo_datos_combo = combo.get_model()
            numero = self.modelo_datos_combo[fila][0]

            consulta = self.base.consultaConParametros("select  a.numeroAlbara as nalb, a.dataAlbara, a.numeroCliente as numcliente, a.dataEntrega as dataent, c.nomeCliente as nomcliente, c.apelidosCliente as apecliente from ventas a left join clientes c on c.numeroCliente = a.numeroCliente where a.numeroAlbara = ?", (numero,))

            for dato in consulta:
                self.data_entry.set_text(str(dato[1]))
                self.numero_cliente_entry.set_text(str(dato[2]))
                self.data_entrega_entry.set_text(str(dato[3]))
                self.nome_cliente_entry.set_text(str(dato[4]))
                self.apellidos_entry.set_text(str(dato[5]))

if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  #si cerramos la pp, se cierra todo
    Gtk.main()

