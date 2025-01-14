import gi


gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk, GLib


class FiestraPrincipal:
    def __init__(self):

        self.temporizacion = None

        builder = Gtk.Builder()
        builder.add_from_file("diseñoInicio.glade")

        self.mainWindow = builder.get_object("main")
        self.cajaPrincipal = builder.get_object("cajaPrincipal")
        self.textoEntry = builder.get_object("textoEntry")
        self.cajaHorizontal = builder.get_object("cajaHorizontal")
        self.checkBEditable = builder.get_object("checkBEditable")
        self.checkBVisible = builder.get_object("checkBVisible")
        self.checkBPulso = builder.get_object("checkBPulso")
        self.checkBIcono = builder.get_object("checkBIcono")



        self.textoEntry.set_invisible_char("~") # cambiar el caracter del texto al ser invisible

        sinais = {
            "on_main_destroy" : self.on_main_destroy,
            "on_chkEditable_toogled" : self.on_chkEditable_toogled,
            "on_visible_toogle" : self.on_chkVisible_toogled,
            "on_chkIcono_toogle" : self.on_chkIcono_toogled,
            "on_pulso_toogle" : self.on_pulso_toogled
        }
        builder.connect_signals(sinais)

    def on_main_destroy(self, widget):
        Gtk.main_quit()

    def on_chkEditable_toogled(self, boton):
        pulsado = boton.get_active()
        self.textoEntry.set_editable(pulsado)

    def on_chkVisible_toogled(self, boton):
        self.textoEntry.set_visibility(boton.get_active())

    def on_chkIcono_toogled(self, boton):
        if boton.get_active():
            nome_icono = "system-search-symbolic"
        else:
            nome_icono = None

        self.textoEntry.set_icon_from_icon_name(Gtk.EntryIconPosition.PRIMARY, nome_icono)

    def on_pulso_toogled(self, boton):
        if boton.get_active():
            self.textoEntry.set_progress_pulse_step(0.2)
            self.temporizacion = GLib.timeout_add(200, self.on_pulso)


    def on_pulso(self):
        self.textoEntry.progress_pulse()
        return True

if __name__ == '__main__':
    win = FiestraPrincipal()
    Gtk.main()
