
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from ConexionDB import ConexionBD

class FiestraPrincipal(Gtk.Window):
    def __init__(self):
        super().__init__()

        self.set_title("Ejemplo de albaran")
        self.set_resizable(False)
        self.set_size_request(300,300)

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

        self.boton_engadir.connect("clicked", self.on_engadir_boton)

        self.grid_datos_botones.attach(self.boton_engadir,  0, 0, 1, 1)
        self.grid_datos_botones.attach_next_to(self.boton_editar, self.boton_engadir, Gtk.PositionType.RIGHT, 1, 1)
        self.grid_datos_botones.attach_next_to(self.boton_borrar, self.boton_editar, Gtk.PositionType.RIGHT, 1, 1)

        self.texto_codigo_producto = Gtk.Entry()
        self.texto_cantidade_producto = Gtk.Entry()
        self.texto_prezo_producto = Gtk.Entry()

        self.caja_horizontal_engadir_textos = Gtk.Box(Gtk.Orientation.HORIZONTAL, spacing=5)
        self.caja_horizontal_engadir_textos.pack_start(self.texto_codigo_producto, True, True, 0)
        self.caja_horizontal_engadir_textos.pack_start(self.texto_cantidade_producto, True, True, 0)
        self.caja_horizontal_engadir_textos.pack_start(self.texto_prezo_producto, True, True, 0)



        #tabla
        self.modelo_datos_tabla = Gtk.ListStore(int, str, int, float)

        self.aux_albaran = None

        self.datos_ejemplo = self.base.consultaConParametros("SELECT d.codigoProduto as codigo_produto, p.nomeProduto as nome_produto, d.cantidade as cantidade_produto, d.prezoUnitario as prezo_produto from detalleVentas d LEFT JOIN produtos p on  p.codigoProduto = d.codigoProduto where numeroAlbaran = ?", (self.aux_albaran, ))
        for dato in self.datos_ejemplo:
            self.modelo_datos_tabla.append([dato[0], dato[1], dato[2], dato[3]])

        self.view_tabla = Gtk.TreeView(model = self.modelo_datos_tabla)



        self.celda_dos = Gtk.CellRendererText()
        self.columna_dos = Gtk.TreeViewColumn("Codigo producto", self.celda_dos, text=0)
        self.view_tabla.append_column(self.columna_dos)

        self.celda_tres = Gtk.CellRendererText()
        self.columna_tres = Gtk.TreeViewColumn("Nome do producto", self.celda_tres, text=1)
        self.view_tabla.append_column(self.columna_tres)

        self.celda_cuatro = Gtk.CellRendererText()
        self.columna_cuatro = Gtk.TreeViewColumn("Cantidade", self.celda_cuatro, text=2)
        self.view_tabla.append_column(self.columna_cuatro)

        self.celda_cinco = Gtk.CellRendererText()
        self.columna_cinco = Gtk.TreeViewColumn("Prezo unitario", self.celda_cinco, text=3)
        self.view_tabla.append_column(self.columna_cinco)

        #conexiones
        self.numero_albara_combo.connect("changed", self.on_numero_albara_changed)


        self.caja_boton_cancelar = Gtk.Button(label="Cancelar")
        self.caja_boton_aceptar = Gtk.Button(label="Aceptar")

        self.caja_horizontal_botones_aceptar_cancelar = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        self.caja_horizontal_botones_aceptar_cancelar.pack_start(self.caja_boton_cancelar, True, True, 0)
        self.caja_horizontal_botones_aceptar_cancelar.pack_start(self.caja_boton_aceptar, True, True, 0)

        self.caja_boton_cancelar.connect("clicked", self.on_boton_cancelar_connect)
        self.caja_boton_aceptar.connect("clicked", self.on_boton_aceptar_connect)

        self.caja_vertical.pack_start(self.grid_datos, True, True, 0)
        self.caja_vertical.pack_start(self.grid_datos_botones, True, True, 0)
        self.caja_vertical.pack_start(self.caja_horizontal_engadir_textos, True, True, 0)
        self.caja_vertical.pack_start(self.view_tabla, True, True, 0)
        self.caja_vertical.pack_start(self.caja_horizontal_botones_aceptar_cancelar, True, True, 0)

        self.operation = None

        self.add(self.caja_vertical)
        self.show_all()

    def on_numero_albara_changed(self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            self.modelo_datos_combo = combo.get_model()
            numero = self.modelo_datos_combo[fila][0]
            self.aux_albaran = numero

            # Consulta para obtener los datos del albarán
            consulta = self.base.consultaConParametros(
                "SELECT a.numeroAlbara, a.dataAlbara, a.numeroCliente, a.dataEntrega, c.nomeCliente, c.apelidosCliente "
                "FROM ventas a "
                "LEFT JOIN clientes c ON c.numeroCliente = a.numeroCliente "
                "WHERE a.numeroAlbara = ?", (numero,))

            for dato in consulta:
                self.data_entry.set_text(str(dato[1]))  # Data Albará
                self.numero_cliente_entry.set_text(str(dato[2]))  # Número Cliente
                self.data_entrega_entry.set_text(str(dato[3]))  # Data Entrega
                self.nome_cliente_entry.set_text(str(dato[4]))  # Nome Cliente
                self.apellidos_entry.set_text(str(dato[5]))  # Apellidos Cliente

            # Limpiar la tabla antes de actualizarla
            self.modelo_datos_tabla.clear()

            datos_productos = self.base.consultaConParametros(
                "SELECT d.codigoProduto, p.nomeProduto, d.cantidade, d.prezoUnitario "
                "FROM detalleVentas d "
                "LEFT JOIN produtos p ON p.codigoProduto = d.codigoProduto "
                "WHERE d.numeroAlbaran = ?", (numero,))

            for producto in datos_productos:
                self.modelo_datos_tabla.append([int(producto[0]), str(producto[1]), int(producto[2]), float(producto[3])])

    def on_engadir_boton(self, boton):
        self.operation = "Engadir"
        self.mostrar_controler(True)
        self.bloquear_controler(False)
        self.bloquear_controler_edicion(True)
        self.limpiar_controler()

    def mostrar_controler(self, mostrar):
        self.texto_codigo_producto.set_visible(mostrar)
        self.texto_cantidade_producto.set_visible(mostrar)
        self.texto_prezo_producto.set_visible(mostrar)

    def bloquear_controler(self, mostrar):
        self.caja_boton_aceptar.set_sensitive(mostrar)
        self.caja_boton_cancelar.set_sensitive(mostrar)

    def bloquear_controler_edicion(self, mostrar):
        self.boton_engadir.set_sensitive(mostrar)
        self.boton_editar.set_sensitive(mostrar)
        self.boton_borrar.set_sensitive(mostrar)


    def limpiar_controler(self):
        self.texto_codigo_producto.set_text("")
        self.texto_cantidade_producto.set_text("")
        self.texto_prezo_producto.set_text("")

    def on_boton_cancelar_connect(self, boton):
        if self.operation == "Engadir":
            pass


    def on_boton_aceptar_connect(self, boton):
        print("Pulsaste el boton de aceptar")


if __name__ == '__main__':
    win = FiestraPrincipal()
    win.connect("destroy", Gtk.main_quit)  #si cerramos la pp, se cierra todo
    Gtk.main()



'''
SELECT d.codigoProduto as codigo_produto, 
p.nomeProduto as nome_produto,
d.cantidade as cantidade_produto,
d.prezoUnitario as prezo_produto
from detalleVentas d LEFT JOIN produtos p on  p.codigoProduto = d.codigoProduto where numeroAlbaran = 1
'''