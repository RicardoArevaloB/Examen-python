import os
os.system('cls')

def gestion():
    title = """
    ******************
    *REGISTRO USUARIO*
    ******************
    """
    print (title)
    id = input('ingrese su identificacion: ')
    Nombres = input('ingrese su nombre: ')
    Apellidos = input('ingresesu apellido: ')
    direcion = input('ingrese su direccion: ')
    ciudad = input('ingrese la ciudad donde vive: ')
    longlat= input('ingrese la longitud: ')
    lat= input('ingrese su latitud: ')
    email = input('ingrese su email: ')
    edad = input('ingrese su edad: ')
    ocupacion = input ('ingrese su ocupacion: ')
    usuario = {
        'id':id,
        'Nombres':Nombres,
        'Apellidos':Apellidos,
        'direcion':direcion,
        'ciudad':ciudad,
        'longitud':longlat,
        'latitud':lat,
        'email':email,
        'edad':edad,
        'ocupación':ocupacion

    }
    


def mainmenu (op):
    title ="""
    **********************
    *****INFO USUARIO*****
    **********************
    """
    menuop = ('1.Regitrar usuario \n2.info usuario \n3.Salir) ')
    if (op != 3):
        print (title)
        print (menuop)
        try:
            op =int(input(':)_'))
        except ValueError:
            print('error en la opcon selecionada ')
            os.system('pause')
            mainmenu(0)
        else:
            match(op):
                case 1:
                    gestion()
                case 2:
                    pass
                case 3:
                    print('hasta luego ')
                    os.system('pause')
                case _:
                    print('error en la opcion ingresasda')
                    os.system ('pause')
                    mainmenu(0)

if __name__=='__main__':
    mainmenu(0)

