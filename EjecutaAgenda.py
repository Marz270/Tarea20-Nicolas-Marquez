from Agenda import Agenda;
from AgendaDAO import AgendaDAO;
from Persona import Persona;

def main():
    # Creamos una instancia de AgendaDAO
    agendaDAO = AgendaDAO();

    # Se crea un objecto de tipo Agenda y se agrega a la base de datos
    agenda = Agenda(1);
    agendaDAO.agregar_agenda(agenda);

    # Accedemos a la agenda con id 1 y mostramos los contactos
    agendaDAO.obtener_agenda(1).mostrarContactos();


    # Creamos tres instancias de Persona
    persona1 = Persona("Juan", 20, "Masculino", 12345678, "Calle 1");
    persona2 = Persona("Maria", 25, "Femenino", 87654321, "Calle 2");
    persona3 = Persona("Pedro", 30, "Masculino", 11223344, "Calle 3");

    # Agregamos los contactos a la agenda
    agenda.agregar_contacto(persona1);
    agenda.agregar_contacto(persona2);
    agenda.agregar_contacto(persona3);

    # Mostramos los contactos de la agenda nuevamente
    agendaDAO.obtener_agenda(1).mostrarContactos();


    # Editamos un contacto de la agenda
    personaEditada = Persona("Juan", 22, "Masculino", 12345678, "Calle 1");
    agendaDAO.editar_contacto(1, personaEditada);

    # Mostramos los contactos de la agenda nuevamente
    agendaDAO.obtener_agenda(1).mostrarContactos();


    # Eliminamos un contacto de la agenda
    agendaDAO.eliminar_contacto(1, 12345678);

    # Mostramos los contactos de la agenda nuevamente
    agendaDAO.obtener_agenda(1).mostrarContactos();


    agendaDAO.cerrar_conexion();


if __name__ == "__main__":
    main();