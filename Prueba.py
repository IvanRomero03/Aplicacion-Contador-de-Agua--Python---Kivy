from ConectorDB import BaseDeDatos, desplegarTabla
DB = BaseDeDatos()


correo = 'A00833623@itesm.mx'
contraseña = 'asd'


usuarios = DB.verUsuarios()
print(usuarios)

idUsuario = -1

for columna in usuarios:
    print(columna)
    if columna[2] == correo and columna[3] == contraseña:
        idUsuario = columna[0]
        print(columna)
        break

if idUsuario == -1:
    print('usuario no encontrado')
else:
    print('usuario encontrado')

    print(DB.verUsuario(idUsuario))

    print(idUsuario)
    print('\n')
    registros = DB.selectRegistrosUsuario(idUsuario)
    print(registros)
    print('\n')
    desplegarTabla(registros)
    print('\n')
    DB.cerrar()