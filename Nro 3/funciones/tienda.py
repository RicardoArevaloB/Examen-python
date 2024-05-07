import funciones.globales as gf
import modules.corefiles as cf
import main 
def newproducto():
    title = """
    ***************************
    * REGISTRO DE PRODUCTOS *
    ***************************
    """
    id = input('ingrese el Id del producto')
    nombre = input('ingrese el nombre del producto ')
    valorUnitario = input('ingrese el valor del producto')
    stockmin = input('ingrese el estok min del producto')
    stockmax= input('ingresa el stockmaximo del producto')

    productos = {
        'id': id,
        'nombre':nombre,
        'valorUnitario':valorUnitario,
        'stock minimo': stockmin,
        'stockmax': stockmax
    }
    

    cf.AddData('data',id,productos)
    gf.Tienda.get('data').update({id:productos})
    if(bool(input('Desea registrar otro producto S(Si) o Enter(No)'))):
        newproducto()
    else:
       main.mainMenu(0)


