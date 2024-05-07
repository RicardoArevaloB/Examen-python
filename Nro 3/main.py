import os 
import modules.corefiles as mcf
import funciones.globales as fg
import funciones.tienda as ft


def mainMenu (op):
    os.system('cls')
    title = '''
    *********************
    *** BODEGA TIENDA ***
    *********************
    '''
    mainMenuOP = '1. Registrar producto \n2.Salir'
    if (op != 4):
        print (title)
        print (mainMenuOP)
        print(fg.Tienda)
        try:
            opcion = int (input(':)_ '))
        except ValueError:
            print('opcion ingresada no valida')
            os.system('pause')
            mainMenu(0)
        else:
            match(opcion):
                case 1:
                    ft.newproducto(0)
                case 2:
                    print('Regrese Pronto')
                    os.system('pause')
                case _:
                    print('La opcion ingresasda no es valida')
                    os.system('pause')
                    mainMenu(0)
if __name__ == '__main__':
    mcf.MY_DATABASE = 'data/productos.json'
    mcf.checkFile(fg.Tienda)   
    mainMenu(0)
