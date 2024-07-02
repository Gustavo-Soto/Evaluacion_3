#cat premiun
import os
import time
import csv

limpieza_pantalla = ('cls')

registro = {'Nro Pedido'
            'Nombre',
            'Comuna',
            'Detalle pedido',
            'Saco 5kg',
            'Saco 10kg',
            'Saco 20kg',
            }

san_bernardo = 0
calera_de_tango = 0
buin = 0

#Hago llamado a mi archivo para iniciarlo
with open('archivo.csv','w', newline='') as archivo_csv:
    archivo_csv.write('')

 #llamamos esta funcion para ingresar datos al csv
def lista ():
    with open('archivo.csv','r') as archivo_csv:
        archivo_csv.read(registro)
        
ingreso = 1  
while ingreso < 4:
    
    try:
        print(f'='*40) 
        print('MENU')
        print(f'='*40)
        print('1.-Registrar pedido')
        print('2.-Listar todos los pedidos')
        print('3.-Imprimir hoja de ruta')
        print('4.-Salir del programa')
        
        seleccion = int(input('Elija el numero de su eleccion\n'))
        
        time.sleep(1)
        os.system(limpieza_pantalla)
        
        if seleccion == 1:
            #Lo siento, no supe usar random
            nombre = input('Ingresar nombre')
            registro = ['nombre'],nombre
            
            comuna = input('Ingrese la comuna del pedido\n1.-San bernardo\n2.-Calera de tango\n3.-Buin\n')
            
            if comuna == 1:
                san_bernardo = san_bernardo+1
                registro = ['comuna'],comuna

            elif comuna == 2:
                calera_de_tango = calera_de_tango+1
                registro = ['comuna'],comuna
            else:
                buin = buin+1
                registro = ['comuna'],comuna
                
            time.sleep(2)
            os.system(limpieza_pantalla)
                
            Detalle_pedido = int(input('Seleccione el tipo de saco \n1.-Saco de 5k\n2.-Saco de 10\n3.-Saco de 20'))
            
            
            if Detalle_pedido == 1:
                print('Seleccionaste el saco de 5kg')
                registro = ['Saco 5kg'], Detalle_pedido
                
            elif Detalle_pedido == 2:
                print('Seleccionaste el saco de 10kg')
                registro = ['Saco 10kg']
            else:
                print('seleccionaste el saco de 20kg')
                registro = ['Saco 20kg'], Detalle_pedido
            
            print(nombre, comuna, Detalle_pedido)
            
            time.sleep(3)
            os.system(limpieza_pantalla)
            
        elif seleccion == 2:
            print('Esta es la lista de pedidos:')
            print('')
            print(registro)
            
            time.sleep(2)
            os.system(limpieza_pantalla)
            
        elif seleccion == 3:
            print('')
                
        else:
            print('')
            
        
    except ValueError:
        print('valor incorrecto, intentelo nuevamente')
    

print('Saliendo del programa')
            
        
        
        
        
    
    
    
