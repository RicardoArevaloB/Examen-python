import os
os.system ('cls')

def dolarpeso():
    dolar = 3.944
    peso= int(input('ingrese el valor en peso que desea pasar a dolares: '))
    resultado = (peso*dolar)
    print (f'la convercion es {resultado} dolares')

def pesoeuro():
    euro = 4.279
    peso = int(input('ingrese el valor en peso que desea pasar a Euros: '))
    resultado =(peso*euro)
    print (f'la convercion es {resultado} euros')

def europeso ():
    peso = 4279
    euro = int(input('ingrese el valor en Euros que desea pasar a Pesos: '))
    resultado = (euro*peso)
    print (f'la convercion es {resultado} pesos')

def pesoyen ():
    yen =26.30
    peso = int(input('ingrese el valor en peso que desea pasar a Yenes: '))
    resultado = (yen*peso)
    print (f'la convercion es {resultado} pesos')

def mainmenu (op):
    title ="""
    **********************
    *CONVERSOR DE MONEDA *
    **********************
    """
    menuop = ('1.Peso a Dolar \n2.Peso a Euro \n3.Euro a Peso \n4.Peso a Yenes \n5.Salir)   ')
    if (op != 5):
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
                    dolarpeso()   
                case 2:
                    pesoeuro()
                case 3:
                    europeso()
                case 4:
                    pesoyen()
                case 5:
                    print('hasta luego ')
                    os.system('pause')
                case _:
                    print('error en la opcion ingresasda')
                    os.system ('pause')
                    mainmenu(0)

if __name__=='__main__':
    mainmenu(0)

            






        
        
    
        
