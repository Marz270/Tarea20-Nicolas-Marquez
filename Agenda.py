from persistent import Persistent;

class Agenda(Persistent):
    def __init__(self, id):
        self.id = id;
        self.Lista = [];
        self.numContactos = 0;
    
    def agregar_contacto(self, persona):
        self.Lista.append(persona);
        self.numContactos += 1;
    
    def eliminar_contacto(self, telefono):
        for persona in self.Lista:
            if persona.telefono == telefono:
                self.Lista.remove(persona);
                self.numContactos -= 1;
                break;
    
    def editar_contacto(self, persona):
        for i in range(len(self.Lista)):
            if self.Lista[i].telefono == persona.telefono:
                self.Lista[i] = persona;
                break
            else:
                print("No se encontro el contacto con el telefono: ", persona.telefono);

    def mostrarContactos(self):
        if len(self.Lista) == 0:
            print("No hay contactos en la agenda");
        else:
            print(f"\nContactos de la agenda con id: {self.id}\n");
            for persona in self.Lista:
                print(persona.consultar_informacion());

