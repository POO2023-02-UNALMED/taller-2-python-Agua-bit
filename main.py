class Auto:
    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1
    
    def cantidadAsientos(self):
        return Asiento.cantidadAsientos

    def verificarIntegridad(self):
        if self.registro == Asiento.registro == Motor.registro:
            print("Auto original")
        else:
            print("Las piezas no son originales")



class Asiento:
    listaAsientos = []
    cantidadAsientos = 0
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
        Asiento.listaAsientos.append
        if Asiento.listaAsientos[i] == None:
            pass
        else:
             Asiento.cantidadAsientos += 1

    def cambiarColor(self, nuevoColor):
        if nuevoColor == "rojo":
            self.color = "rojo"
        elif nuevoColor == "verde":
            self.color = "verde"
        elif nuevoColor == "amarillo":
            self.color = "amarillo"
        elif nuevoColor == "negro":
            self.color = "negro"
        elif nuevoColor == "blanco":
            self.color = "blanco"
        else:
            pass
            

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, numeroRegistro):
        self.registro = numeroRegistro

    def asignarTipo(self, nuevoTipo):
        if nuevoTipo == "electrico":
            self.tipo = "electrico"
        elif nuevoTipo == "gasolina":
            self.tipo = "gasolina"
        else:
            pass
        