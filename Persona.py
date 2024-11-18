from persistent import Persistent;

class Persona(Persistent):
    def __init__(self, nombre, edad, genero, telefono, direccion):
        self.nombre = nombre;
        self.edad = edad;
        self.genero = genero;
        self.telefono = telefono;
        self.direccion = direccion;

    def consultar_informacion(self):
        return f"\nNombre: {self.nombre}, Edad: {self.edad}, Genero: {self.edad}, Telefono: {self.telefono}, Direccion: {self.direccion}\n";
