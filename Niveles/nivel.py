class Nivel:
    def __init__(self):
        self.nivel = []

    def seleccion(self, ven, cont):
        archivo = "Nivel_" + str(cont+1) + ".txt"
        self.leerNivel(archivo)
        ven.cargarFondo(self.nivel)

    def leerNivel(self, archivo):
        f = open(archivo, 'r')
        for linea in f:
            self.nivel.append(linea.strip().split())
        f.close()
