import pymysql
from random import shuffle


class cConexion:
    def __init__(self):
        self.lista_destino = []

    def llenar_lista(self):
        self.db = pymysql.connect('127.0.0.1', 'root', '', 'game')
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT `palabra` FROM palabras_2")
        lista = self.cursor.fetchall()

        for i in lista:
            palabra = i[0]
            self.lista_destino.append(palabra)
        if len(self.lista_destino) == 0:
            self.cursor.execute("SELECT `palabra` FROM palabras")
            lista = self.cursor.fetchall()
            for i in lista:
                palabra = i[0]
                self.lista_destino.append(palabra)
            shuffle(self.lista_destino)
        self.db.close()
        return self.lista_destino

    def imprimir_listas(self):
        name = self.lista_destino.pop()
        self.salva_palabra(name)
        return name

    def impPalabras(self):
        sqlq = 'SELECT * FROM palabras'
        self.cursor.execute(sqlq)
        lista = self.cursor.fetchall()
        for i in lista:
            id = i[0]
            palabra = i[1]
            print("id: {0}, palabra: {1}"
                  .format(id, palabra))

        self.db.close()

    def salva_palabra(self, n):
        self.db = pymysql.connect('127.0.0.1', 'root', '', 'game')
        self.cursor = self.db.cursor()

        self.cursor.execute('SELECT `palabra` FROM palabras_2')
        dest = self.cursor.fetchall()
        for l in dest:
            palabra = l[0]
            if palabra == n:
                self.cursor.execute(f"DELETE FROM `palabras_2` WHERE (`palabra` = '{palabra}')")

        self.cursor.execute('SELECT `palabra` FROM `palabras_2`')
        dest=self.cursor.fetchall()
        for l in dest:
            palabra=l[0]
            if n==palabra:
                self.cursor.execute(f"DELETE FROM `palabras_2` WHERE(`palabra` = '{palabra}')")

        self.db.commit()
        self.db.close()

    def nueva_palabra(self, p):
        self.db = pymysql.connect('127.0.0.1', 'root', '', 'game')
        self.cursor = self.db.cursor()
        self.cursor.execute(f"INSERT INTO `palabras`(`palabra`) VALUES('{p}')")
        self.db.commit()
        self.db.close()
        return "palabra agregada con exito!"

    def resetear(self):
        self.db = pymysql.connect('127.0.0.1', 'root', '', 'game')
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT `palabra` FROM palabras")
        lista = []
        for i in self.cursor.fetchall():
            pal = i[0]
            lista.append(pal)
        shuffle(lista)

        self.cursor.execute("DROP TABLE `palabras_2`")
        self.cursor.execute("""
        CREATE TABLE palabras_2 (id int auto_increment not null primary key, 
        palabra varchar(20) not null)""")
        for i in lista:
            self.cursor.execute(f"INSERT INTO `palabras_2`(`palabra`) VALUES('{i}')")
        self.db.commit()
        self.db.close()
        return "lista reestablecida °w°"


    def eliminar_txt(self):
        self.db = pymysql.connect("127.0.0.1", "root", "", "game")
        self.cursor = self.db.cursor()
        self.cursor.execute("SELECT `palabra` FROM palabras_2")
        l = []
        for x in self.cursor.fetchall():
            pal = x[0]
            l.append(pal)
        
        self.destino = [linea.rstrip() for linea in open("lista_destino.txt")]
        

        for i,e in enumerate(self.destino):
            if e not in l:
                self.destino.remove(e)
        
        self.dest = open("lista_destino.txt","w")
        self.cadena = "\n".join(str(x) for x in self.destino)
        self.dest.write(self.cadena)
        self.dest.close() 
# limpiar el codigo X
# clases estaticas
# consulta para eliminar el ultimo registro
# agregar nombre

