import transaction;
from ZODB import DB;
from ZODB.FileStorage import FileStorage;

class AgendaDAO:
    def __init__(self, db_path='agenda.fs'):
        self.storage = FileStorage(db_path);
        self.db = DB(self.storage);
        self.connection = self.db.open();
        self.root = self.connection.root();

        if 'agenda' not in self.root:
            self.root['agendas'] = {};

    def agregar_agenda(self, agenda):
        self.root['agendas'][agenda.id] = agenda;
        transaction.commit();
    

    def obtener_agenda(self, id):
        return self.root['agendas'].get(id, None);


    def editar_contacto(self, id, persona):
        if id in self.root['agendas']:
            self.root['agendas'][id].editar_contacto(persona);
            transaction.commit();
        else:
            print("No existe la agenda con id: ", id);
    
    def eliminar_contacto(self, id, telefono):
        if id in self.root['agendas']:
            self.root['agendas'][id].eliminar_contacto(telefono);
            transaction.commit();
        else:
            print("No existe la agenda con id: ", id);
        
    def cerrar_conexion(self):
        try:
            transaction.commit()
        except Exception as e:
            print("Error al confirmar la transacción:", e)
        finally:
            self.connection.close()