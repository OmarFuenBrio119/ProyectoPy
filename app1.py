
lista_elements = [{
    "id" : "1",
    "name" : "Emmanuel",
    "last_name" : "Aguilar"
}]



def add_element():
    id = int(input('Ingresa el ID de la persona'))
    name = input("Escribe el nombre: ")
    last_name = input("Ingresa el apellido: ")
    person = {
        "name": name,
        "last_name" : last_name
    }
    lista_elements.append(person)
    pass

def remove_element():
    pass

def show_element():
    for elemnt in lista_elements:
        for key, value in elemnt.items(): 
         print(f"{key} -> {value}")
    pass

def show_elements():
    pass

def edit_element():
    pass



if __name__ == '__main__':
    menu = '''
    implementacion de CRUD de Elemento
    Elige una opcion 
    1.-Insectar
    2.-Mostarr todos
    3.-Buscar por id
    4.-Editar 
    5.-Eliminar
    6.-Salir
    '''

    while True:
        opcion = input(menu)
        if opcion == '1':
            print("Insectar elemento")
            add_element()
        elif opcion == '2':
            print("Mostar todos los elemntos")
            show_element()
        elif opcion == '3':
            print("Buscar po ID")
        elif opcion == '4':
            print("Editar elemento")
        elif opcion == '15':
            print("Elimi9nar elemnto")    
        elif opcion == '6':
            print('Bye')
        else :
            print("Opcion incorrecta")
            break;
