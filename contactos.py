contactos = { }

print("---"*30)
print("AGENDA DE CONTACTOS")
print("---"*30)
volver_menu = True
while volver_menu:
    menu = int(input("Que desea hacer? \n" \
                    "(1) agregar contactos \n" \
                    "(2) Buscar contactos \n" \
                    "(3) actualizar contactos \n" \
                    "(4) Eliminar contactos \n"))
    if menu == 1:
        volver_agregar = True
        while volver_agregar:
            nombre = input("Ingrese el nombre del contacto: \n")
            email = input("Ingrese el correo del contacto: \n")
            numero = int(input("Ingrese el numero del contacto: \n"))

            contactos[nombre] = {"email": email , "numero":numero}
            
            respuesta_no_valida = True
            while respuesta_no_valida:
                otro = input("Desea agregar otro contacto? (si/no)")
                if otro == "si":
                    print("")
                    respuesta_no_valida = False
                elif otro == "no":
                    print("Contacto/s guardado/s con exito")
                    for i, n in contactos.items():
                        print(f"{i} {n["email"]} {n["numero"]}")
                    volver_agregar = False
                    respuesta_no_valida = False
                else:
                    print("Respuesta no valida, intentelo de nuevo")
    elif menu == 2:
        buscar_otro_contacto = True
        while buscar_otro_contacto:
            nombre_buscar = input("Ingrese el nombre del contacto que desea buscar, si desea verlos todos escriba todos, si desea volver al menu escriba volver: \n")
            if nombre_buscar == "volver":
                buscar_otro_contacto = False
            elif nombre_buscar == "todos":
                print("NOMBRE                 EMAIL                        NUMERO")
                for i, n in contactos.items():
                    print(f"{i:20} {n["email"]:20} {n["numero"]:20}")

            if nombre_buscar in contactos:
                info_contacto = contactos.get(nombre_buscar)
                print("Contacto encontrado")
                print("---"*30)
                print("NOMBRE                 EMAIL                        NUMERO")
                print(f"{nombre_buscar:20} {info_contacto["email"]:20} {info_contacto["numero"]:20}")
                print("---"*30)
    elif menu == 3:
        menu2_volver = True
        while menu2_volver:
            menu2 = int(input("Ingrese que desea actualizar: \n" \
                            "(1) actualizar email \n" \
                            "(2) actualizar numero\n"
                            "(3) salir al menu"))
            
            nombre_actualizar = input("Ingrese el nombre del contacto que desea actualizar: ")
            
            if nombre_actualizar in contactos:
                info_cont = contactos.get(nombre_actualizar)
                if menu2 == 1:
                    print("NOMBRE                 EMAIL                        NUMERO")
                    print(f"{nombre_actualizar:20} {info_cont["email"]:20} {info_cont["numero"]:20}")
                    email_actualizar = input("Ingrese el nuevo email: \n")
                    contactos[nombre_actualizar]["email"] = email_actualizar
                    print("Email actualizado con exito")
                    info_cont = contactos.get(nombre_actualizar)
                    print("NOMBRE                 EMAIL                        NUMERO")
                    print(f"{nombre_actualizar:20} {info_cont["email"]:20} {info_cont["numero"]:20}")
                if menu2 == 2:
                    print("NOMBRE                 EMAIL                        NUMERO")
                    print(f"{nombre_actualizar:20} {info_cont["email"]:20} {info_cont["numero"]:20}")
                    numero_nuevo = int(input("Ingrese el nuevo numero"))
                    contactos[nombre_actualizar]["numero"] = numero_nuevo
                    print("numero actualizado")
                    nfo_cont = contactos.get(nombre_actualizar)
                    print("NOMBRE                 EMAIL                        NUMERO")
                    print(f"{nombre_actualizar:20} {info_cont["email"]:20} {info_cont["numero"]:20}")
                else:
                    menu2_volver = False
            else:
                print("Contacto no encontrado, intentelo de nuevo")
    elif menu == 4:
        nombre_eliminar = input("Ingrese el nombre del contacto que desea eliminar: \n")
        if nombre_eliminar in contactos:
            del contactos[nombre_eliminar]
            print("contacto eliminado con exito")
        else: 
            print("Contacto no encontrado, intentelo de nuevo")
                



        