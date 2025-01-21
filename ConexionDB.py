import sqlite3

class ConexionBD:
    def __init__(self, rutaBd):
        """Inicializa la conexión a la base de datos y prepara el cursor."""
        self.rutaBd = rutaBd
        self.conexion = None
        self.cursor = None
        self.conectaBD()

    def conectaBD(self):
        """Conecta a la base de datos SQLite."""
        try:
            self.conexion = sqlite3.connect(self.rutaBd)
            self.cursor = self.conexion.cursor()
            print("Conexión de base de datos realizada")
        except sqlite3.Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def crear_tabla(self):
        """Crea la tabla 'usuarios' si no existe."""
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    dni TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    apelido TEXT NOT NULL,
                    numtelf Integer
                )
            """)
            self.conexion.commit()
            print("Tabla usuarios creada correctamente")
        except sqlite3.Error as e:
            print(f"Error al crear la tabla: {e}")

    def consultaSenParametros(self, consultaSQL):
        """Realiza una consulta sin parámetros."""
        try:
            self.cursor.execute(consultaSQL)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error en la consulta: {e}")
            return None

    def consultaConParametros(self, consultaSQL, parametros=()):
        """Realiza una consulta con parámetros."""
        try:
            self.cursor.execute(consultaSQL, parametros)
            self.conexion.commit()
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error en la consulta con parámetros: {e}")
            return None

    def pechaBD(self):
        """Cierra la conexión con la base de datos."""
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()



    def insertar_usuario(self, datos):
        try:
            self.cursor.execute(
                "INSERT INTO usuarios (dni, name, apelido, numtelf) VALUES(?, ?, ?, ?)",
                datos,
            )
            self.conexion.commit()
            print("Usuario inserido correctamente.")
        except sqlite3.Error as e:
            print(f"Error al insertar datos usuarios: {e}")