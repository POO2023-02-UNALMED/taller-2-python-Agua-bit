class Auto:
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        self.cantidadCreados += 1
    
    def cantidadAsientos(self):
        return self.asientos

    def verificarIntegridad(self):
        if self.registro == Asiento.registro  and Asiento.registro == Motor.registro:
            print("Auto original")
        else:
            print("Las piezas no son originales")



class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

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
        