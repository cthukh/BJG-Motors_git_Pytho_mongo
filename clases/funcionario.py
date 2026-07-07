class Funcionario():
    def __init__(self,
                # id,
                nombre,
                rut,
                cargo,
                correo,
                telefono):
        # self.id         = id
        self.nombre     = nombre
        self.rut        = rut
        self.cargo      = cargo
        self.correo     = correo
        self.telefono   = telefono



def agregar_funcionario(coleccion_funcionarios):
    print("Ingresa datos de funcionario\n")
    nombre      = input("Ingresa nombre: ")
    rut         = input("Ingresa rut: ")
    cargo       = input("Ingresa cargo: ")
    correo      = input("Ingresa correo: ")
    telefono    = input("Ingresa telefono: ")

    #no seria necesario ¿
    nuevo_fun = Funcionario(nombre,rut,cargo,correo,telefono)

    try:
        coleccion_funcionarios.insert_one(
            {
                "nombre":nombre,
                "rut":rut,
                "cargo":cargo,
                "correo":correo,
                "telefono":telefono
            }
        )
        print("Funcionario guardado con exito.")
    except Exception as e:
        print(f"Error al guardar funcionario: {e}")


def eliminar_funcionario(coleccion_funcionarios):
    lista_ids = ver_funcionarios(coleccion_funcionarios)

    elim_id = str(input("Ingrese la id del funcionario a eliminar: ")) # se debe ingresar id visual

    for i in lista_ids:
        funcionario = i.get(elim_id)
        try:
            if funcionario:
                coleccion_funcionarios.delete_one(
                    {
                        "_id":funcionario
                    }
                )
        except Exception as e:
            print(f"Error al eliminar funcionario: {e}")







def ver_funcionarios(coleccion_funcionarios) -> list:
    """
    Returns:
        list: Lista con las ids de los funcionarios parceada a ids locales.
    """
    ids = []

    print("---------------- Lista de funcionarios ----------------\n")
    id_indice = 1
    for f in coleccion_funcionarios.find():
        print(f"#{id_indice} -- Funcionario: {f["nombre"]} | RUT: {f["rut"]} | Cargo/Rol: {f["cargo"]}\n")

        # une el valor de _id (del documento) a la clave id_indice (variable local) para poder buscar la id
        ids.append({str(id_indice):f["_id"]})

        id_indice+=1
    print("---------------------------------------------------------")

    return ids