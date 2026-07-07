from conexion import conexionDB
from menus import *
from clases.funcionario import *

import os


cliente = conexionDB().conectarse()

colFuncionarios = cliente["funcionarios"]
colReparaciones = cliente["reparacion"]

#crear autoinsert


while True:
    os.system('clear')
    opcion = menu_principal()
    
    if opcion == 0: # Salir
        print("Saliendo del programa...")
        break


    elif opcion == 1: # ------------------- Funcionarios
        opt_f = menu_funcionarios()
        if opt_f == 1: # ver
            ver_funcionarios(colFuncionarios)
            ok = input("\nPresione Enter para continuar: ")

        elif opt_f == 2: # agregar
            agregar_funcionario(colFuncionarios)
            ok = input("\nPresione Enter para continuar: ")

        elif opt_f == 3: # eliminar
            eliminar_funcionario(colFuncionarios)
            ok = input("\nPresione Enter para continuar: ")



    elif opcion == 2: # ------------------- Reparaciones
        opt_r = menu_reparaciones()



    elif opcion == 3: # ------------------- Vehiculos
        opt_v = menu_vehiculos()


