def menu_principal() -> int:
    """
    1) Ver opciones de Funcionarios
    2) Ver opciones de Reparaciones
    4) Ver opciones de Vehiculos
    0) salir del sistema

    Returns:
        int: opcion seleccionada.
    """
    print(
        "Menu principal: \n"
        "1) Ver opciones de Funcionarios \n"
        "2) Ver opciones de Reparaciones \n"
        "3) Ver opciones de Vehiculos \n\n"
    
        "0) salir del sistema \n"
    )
    opt = int(input("Ingrese una opción (1-3): "))
    while opt < 0 or opt > 4:
        print("Opción invalida")
        opt = input("Ingrese una opción (1-4): ")

    return opt




# !!!! [agregar]   buscar un unico usuario

def menu_funcionarios() -> int:
    """1) Ver funcionarios
    2) Agregar funcionario
    3) Eliminar funcionario
    4) Actualizar funcionario"""
    print("""
Menú de Funcionarios
    1) Ver funcionarios
    2) Agregar funcionario
    3) Eliminar funcionario
    4) Actualizar funcionario

    0) Volver al menú principal
    """)
    opt = int(input("Ingrese una opción (1-4): "))
    while opt < 0 or opt > 4:
        print("Opción invalida")
        opt = input("Ingrese una opción (1-4): ")

    return opt






def menu_reparaciones() -> int:
    """1) Ver reparaciones
    2) Agregar reparacion
    3) Eliminar reparacion
    4) Actualizar reparacion"""
    print("""
Menú de Reparaciones:
    1) Ver reparaciones
    2) Agregar reparacion
    3) Eliminar reparacion
    4) Actualizar reparacion

    0) Volver al menú principal
    """)
    opt = int(input("Ingrese una opción (1-4): "))
    while opt < 0 or opt > 4:
        print("Opción invalida")
        opt = input("Ingrese una opción (1-4): ")

    return opt







def menu_vehiculos() -> int:
    """1) Ver vehiculos
    2) Agregar vehiculo
    3) Eliminar vehiculo
    4) Actualizar vehiculo"""
    print("""
Menú de Vehiculos:
    1) Ver vehiculos
    2) Agregar vehiculo
    3) Eliminar vehiculo
    4) Actualizar vehiculo

    0) Volver al menú principal
    """)
    opt = int(input("Ingrese una opción (1-4): "))
    while opt < 0 or opt > 4:
        print("Opción invalida")
        opt = input("Ingrese una opción (1-4): ")

    return opt