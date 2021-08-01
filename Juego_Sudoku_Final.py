#JUEGO DE SUDOKU - JUAN PEDRO VÁSQUEZ, GUSTAVO PEREZ, ISAAC GARAY, PAOLO VÁSQUEZ

from Funciones import *
borrarPantalla = lambda: os.system ("cls")
import copy

def sudoku():
    while True:
        opcion = menu()
        if opcion == "1":
            tablero = dificultad()
            if tablero == "1":
                nivel4x4 = nivel()
                if nivel4x4 == "1":
                    tablero4x4("S","No","ES/4x4F.json","PR/4x4F.json","TBLR/4x4F.json","LIST/4x4F.json")
                elif nivel4x4 == "2":
                    tablero4x4("M","No","ES/4x4M.json","PR/4x4M.json","TBLR/4x4M.json","LIST/4x4M.json")
                elif nivel4x4 == "3":
                    tablero4x4("A","No","ES/4x4D.json","PR/4x4D.json","TBLR/4x4D.json","LIST/4x4D.json")
                else:
                    sudoku()
            elif tablero == "2":
                nivel9x9 = nivel()
                if nivel9x9 == "1":
                    tablero9x9("S","No","ES/9x9F.json","PR/9x9F.json","TBLR/9x9F.json","LIST/9x9F.json")
                elif nivel9x9 == "2":
                    tablero9x9("M","No","ES/9x9M.json","PR/9x9M.json","TBLR/9x9M.json","LIST/9x9M.json")
                elif nivel9x9 == "3":
                    tablero9x9("A","No","ES/9x9D.json","PR/9x9D.json","TBLR/9x9D.json","LIST/9x9D.json")
                else:
                    sudoku()
            else:
                sudoku()
        elif opcion == "2":
            tablero = dificultad()
            if tablero == "1":
                nivel4x4 = nivel()
                if nivel4x4 == "1":
                    tablero4x4("S","Si","ES/4x4F.json","PR/4x4F.json","TBLR/4x4F.json","LIST/4x4F.json")
                elif nivel4x4 == "2":
                    tablero4x4("M","Si","ES/4x4M.json","PR/4x4M.json","TBLR/4x4M.json","LIST/4x4M.json")
                elif nivel4x4 == "3":
                    tablero4x4("A","Si","ES/4x4D.json","PR/4x4D.json","TBLR/4x4D.json","LIST/4x4D.json")
                else:
                    sudoku()
            elif tablero == "2":
                nivel9x9 = nivel()
                if nivel9x9 == "1":
                    tablero9x9("S","Si","ES/9x9F.json","PR/9x9F.json","TBLR/9x9F.json","LIST/9x9F.json")
                elif nivel9x9 == "2":
                    tablero9x9("M","Si","ES/9x9M.json","PR/9x9M.json","TBLR/9x9M.json","LIST/9x9M.json")
                elif nivel9x9 == "3":
                    tablero9x9("A","Si","ES/9x9D.json","PR/9x9D.json","TBLR/9x9D.json","LIST/9x9D.json")
                else:
                    sudoku()
            else:
                sudoku()
        elif opcion == "3":
            tablero = dificultad()
            if tablero == "1":
                nivel4x4 = nivel()
                if nivel4x4 == "1":
                    borrar("ES/4x4F.json","PR/4x4F.json","TBLR/4x4F.json","LIST/4x4F.json")
                elif nivel4x4 == "2":
                    borrar("ES/4x4M.json","PR/4x4M.json","TBLR/4x4M.json","LIST/4x4M.json")
                elif nivel4x4 == "3":
                    borrar("ES/4x4D.json","PR/4x4D.json","TBLR/4x4D.json","LIST/4x4D.json")
                else:
                    sudoku()
            elif tablero == "2":
                nivel9x9 = nivel()
                if nivel9x9 == "1":
                    borrar("ES/9x9F.json","PR/9x9F.json","TBLR/9x9F.json","LIST/9x9F.json")
                elif nivel9x9 == "2":
                    borrar("ES/9x9M.json","PR/9x9M.json","TBLR/9x9M.json","LIST/9x9M.json")
                elif nivel9x9 == "3":
                    borrar("ES/9x9D.json","PR/9x9D.json","TBLR/9x9D.json","LIST/9x9D.json")
                else:
                    sudoku()
        elif opcion == "4":
            instrucciones()
        elif opcion == "5":
            eleccion = estadis()
            if eleccion == "1":
                tablero = dificultad()
                if tablero == "1":
                    nivel4x4 = nivel()
                    if nivel4x4 == "1":
                        borrarPantalla()
                        lecturajsonestadis("ES/4x4F.json")
                        print(Fore.WHITE + Cursor.DOWN(2) + Cursor.FORWARD(41) + "Para volver al menú presione enter ( )" + Back.RESET)
                        entrada = input(Cursor.UP(1) + Cursor.FORWARD(77))
                        borrarPantalla()
                        sudoku()
                    elif nivel4x4 == "2":
                        borrarPantalla()
                        lecturajsonestadis("ES/4x4M.json")
                        print(Fore.WHITE + Cursor.DOWN(2) + Cursor.FORWARD(41) + "Para volver al menú presione enter ( )" + Back.RESET)
                        entrada = input(Cursor.UP(1) + Cursor.FORWARD(77))
                        borrarPantalla()
                        sudoku()
                    elif nivel4x4 == "3":
                        borrarPantalla()
                        lecturajsonestadis("ES/4x4D.json")
                        print(Fore.WHITE + Cursor.DOWN(2) + Cursor.FORWARD(41) + "Para volver al menú presione enter ( )" + Back.RESET)
                        entrada = input(Cursor.UP(1) + Cursor.FORWARD(77))
                        borrarPantalla()
                        sudoku()
                    else:
                        sudoku()
                elif tablero == "2":
                    nivel9x9 = nivel()
                    if nivel9x9 == "1":
                        borrarPantalla()
                        lecturajsonestadis("ES/9x9F.json")
                        print(Fore.WHITE + Cursor.DOWN(2) + Cursor.FORWARD(41) + "Para volver al menú presione enter ( )" + Back.RESET)
                        entrada = input(Cursor.UP(1) + Cursor.FORWARD(71))
                        borrarPantalla()
                        sudoku()
                    elif nivel9x9 == "2":
                        borrarPantalla()
                        lecturajsonestadis("ES/9x9M.json")
                        print(Fore.WHITE + Cursor.DOWN(2) + Cursor.FORWARD(41) + "Para volver al menú presione enter ( )" + Back.RESET)
                        entrada = input(Cursor.UP(1) + Cursor.FORWARD(77))
                        borrarPantalla()
                        sudoku()
                    elif nivel9x9 == "3":
                        borrarPantalla()
                        lecturajsonestadis("ES/9x9D.json")
                        print(Fore.WHITE + Cursor.DOWN(2) + Cursor.FORWARD(41) + "Para volver al menú presione enter ( )" + Back.RESET)
                        entrada = input(Cursor.UP(1) + Cursor.FORWARD(77))
                        borrarPantalla()
                        sudoku()
                    else:
                        sudoku()
                else:
                    sudoku()
            elif eleccion == "2":
                tablero = dificultad()
                if tablero == "1":
                    nivel4x4 = nivel()
                    if nivel4x4 == "1":
                        borrarPantalla()
                        lecturajsonmatrices("TBLR/4x4F.json")
                        print(Fore.WHITE + Cursor.DOWN(2) + Cursor.FORWARD(42) + "Para volver al menú presione enter ( )" + Back.RESET)
                        entrada = input(Cursor.UP(1) + Cursor.FORWARD(78))
                        borrarPantalla()
                        sudoku()
                    elif nivel4x4 == "2":
                        borrarPantalla()
                        lecturajsonmatrices("TBLR/4x4M.json")
                        print(Fore.WHITE + Cursor.DOWN(2) + Cursor.FORWARD(42) + "Para volver al menú presione enter ( )" + Back.RESET)
                        entrada = input(Cursor.UP(1) + Cursor.FORWARD(78))
                        borrarPantalla()
                        sudoku()
                    elif nivel4x4 == "3":
                        borrarPantalla()
                        lecturajsonmatrices("TBLR/4x4D.json")
                        print(Fore.WHITE + Cursor.DOWN(2) + Cursor.FORWARD(42) + "Para volver al menú presione enter ( )" + Back.RESET)
                        entrada = input(Cursor.UP(1) + Cursor.FORWARD(78))
                        borrarPantalla()
                        sudoku()
                    else:
                        sudoku()
                elif tablero == "2":
                    nivel9x9 = nivel()
                    if nivel9x9 == "1":
                        borrarPantalla()
                        lecturajsonmatrices("TBLR/9x9F.json")
                        print(Fore.WHITE + Cursor.DOWN(2) + Cursor.FORWARD(27) + "Para volver al menú presione enter ( )" + Back.RESET)
                        entrada = input(Cursor.UP(1) + Cursor.FORWARD(63))
                        borrarPantalla()
                        sudoku()
                    elif nivel9x9 == "2":
                        borrarPantalla()
                        lecturajsonmatrices("TBLR/9x9M.json")
                        print(Fore.WHITE + Cursor.DOWN(2) + Cursor.FORWARD(27) + "Para volver al menú presione enter ( )" + Back.RESET)
                        entrada = input(Cursor.UP(1) + Cursor.FORWARD(63))
                        borrarPantalla()
                        sudoku()
                    elif nivel9x9 == "3":
                        borrarPantalla()
                        lecturajsonmat("TBLR/9x9M.json")
                        print(Fore.WHITE + Cursor.DOWN(2) + Cursor.FORWARD(27) + "Para volver al menú presione enter ( )" + Back.RESET)
                        entrada = input(Cursor.UP(1) + Cursor.FORWARD(63))
                        borrarPantalla()
                        sudoku()
                    else:
                        sudoku()
                else:
                    sudoku()
            else:
                sudoku()
        elif opcion == "6":
            exit()

def menu():
    borrarPantalla()
    print("")
    print()
    print(Cursor.FORWARD(39) + Fore.YELLOW +  "+"*35)
    print(Cursor.FORWARD(39) + Fore.YELLOW +  "+             SUDOKU              +")
    print(Cursor.FORWARD(39) + Fore.YELLOW +  "+"*35)
    print(Cursor.FORWARD(41) + Cursor.DOWN(2) + Fore.GREEN + "(1) Empezar nueva partida (1)")
    print(Cursor.FORWARD(39) + Cursor.DOWN(1)+ Fore.MAGENTA + "(2) Continuar partida guardada (2)")
    print(Cursor.FORWARD(40) + Cursor.DOWN(1)+Fore.BLUE + "(3) Borrar partidas guardadas (3)")
    print(Cursor.FORWARD(45) + Cursor.DOWN(1) + Fore.CYAN + "(4) Instrucciones (4)")
    print(Cursor.FORWARD(45) + Cursor.DOWN(1) + Fore.YELLOW + "(5) Estadísticas (5)")
    print(Cursor.FORWARD(44) + Cursor.DOWN(1) + Fore.RED + "(6) Salir del juego (6)")
    print(Cursor.FORWARD(46) + Fore.WHITE + Cursor.DOWN(2) + "Eliga una opcion ( )" + Back.RESET)
    eleccion = input(Cursor.UP(1) + Cursor.FORWARD(64))
    if eleccion != "1" and eleccion != "2" and eleccion != "3" and eleccion != "4" and eleccion != "5" and eleccion != "6":
        sudoku()
    borrarPantalla()
    return eleccion

def dificultad():
    tablero = "4"
    while tablero != "1" and tablero != "2" and tablero != "3":
        borrarPantalla()
        print("")
        print()
        print(Cursor.FORWARD(39) + Fore.YELLOW +  "+"*35)
        print(Cursor.FORWARD(39) + Fore.YELLOW +  "+           DIFICULTAD            +")
        print(Cursor.FORWARD(39) + Fore.YELLOW +  "+"*35)
        print(Cursor.FORWARD(43) + Cursor.DOWN(2) + Fore.GREEN + "(1) Facil: Tablero 4x4 (1)")
        print(Cursor.FORWARD(42) + Cursor.DOWN(1) + Fore.RED + "(2) Dificil: Tablero 9x9 (2)")
        print(Cursor.FORWARD(44) + Cursor.DOWN(1) + Fore.YELLOW + "(3) Regresar al menú (3)")
        print(Cursor.FORWARD(47) + Fore.WHITE + Cursor.DOWN(2) + "Eliga una opcion ( )" + Back.RESET)
        tablero = input(Cursor.UP(1) + Cursor.FORWARD(65))
    return tablero

def nivel():
    nivel = "5"
    while nivel != "1" and nivel != "2" and nivel != "3" and nivel != "4":
        borrarPantalla()
        print("")
        print()
        print(Cursor.FORWARD(39) + Fore.YELLOW +  "+"*35)
        print(Cursor.FORWARD(39) + Fore.YELLOW +  "+             NIVEL               +")
        print(Cursor.FORWARD(39) + Fore.YELLOW +  "+"*35)
        print(Cursor.FORWARD(40) + Cursor.DOWN(2) + Fore.GREEN + "(1) Sencillo: 1/2 de tablero (1)")
        print(Cursor.FORWARD(41) + Cursor.DOWN(1) + Fore.CYAN + "(2) Medio: 1/3 de tablero (2)")
        print(Cursor.FORWARD(40) + Cursor.DOWN(1) + Fore.RED + "(3) Avanzado: 1/4 de tablero (3)")
        print(Cursor.FORWARD(44) + Cursor.DOWN(1) + Fore.YELLOW + "(4) Regresar al menú (4)")
        print(Cursor.FORWARD(47) + Fore.WHITE + Cursor.DOWN(2) + "Eliga una opcion ( )" + Back.RESET)
        nivel = input(Cursor.UP(1) + Cursor.FORWARD(65))
    return nivel

def borrar(archivo1,archivo2,archivo3,archivo4):
    borrarPantalla()
    vacio = esvacio(archivo2)
    if vacio == True:
        print(Cursor.FORWARD(44) + Cursor.DOWN(3) + Fore.RED + "No hay partidas guardadas")
        print(Cursor.FORWARD(38) + Fore.WHITE + Cursor.DOWN(2) + "Para volver al menú presione enter ( )" + Back.RESET)
        entrada = input(Cursor.UP(1) + Cursor.FORWARD(74))
        borrarPantalla()
        sudoku()
    print("")
    if "4" in archivo2:
        print(Cursor.FORWARD(40) + Fore.YELLOW +  "+"*39)
        print(Cursor.FORWARD(40) + Fore.YELLOW +  "+          PARTIDAS GUARDADAS         +")
        print(Cursor.FORWARD(40) + Fore.YELLOW +  "+"*39)
        lecturajsonmatricesg(archivo2)
        nombre = input(Cursor.DOWN(2) + Cursor.FORWARD(40) + Fore.WHITE + "Ingrese el nombre de la partida: ")
    else:
        print(Cursor.FORWARD(27) + Fore.YELLOW +  "+"*39)
        print(Cursor.FORWARD(27) + Fore.YELLOW +  "+          PARTIDAS GUARDADAS         +")
        print(Cursor.FORWARD(27) + Fore.YELLOW +  "+"*39)
        lecturajsonmatricesg(archivo2)
        nombre = input(Cursor.DOWN(2) + Cursor.FORWARD(27) + Fore.WHITE + "Ingrese el nombre de la partida: ")
    criterio = enjson(nombre,archivo2)
    if criterio == True:
        borrarpartida(nombre,archivo2)
        borrarpartida(nombre,archivo4)
        confirmador = "3"
        while confirmador != "1" and confirmador != "2":
            borrarPantalla()
            print(Cursor.FORWARD(40) + Cursor.DOWN(3) + Fore.GREEN + "¡Partida borrada satisfactoriamente!")
            print(Cursor.FORWARD(38) + Cursor.DOWN(2) + Fore.WHITE + "¿Desea borrar otra partida? Si (1) No (2)")
            print(Cursor.FORWARD(49) + Fore.WHITE + Cursor.DOWN(2) + "Eliga una opcion ( )" + Back.RESET)
            confirmador = input(Cursor.UP(1) + Cursor.FORWARD(67))
        if confirmador == "1":
            borrar(archivo1,archivo2,archivo3,archivo4)
        else:
            sudoku()
    else:
        confirmador = "3"
        while confirmador != "1" and confirmador != "2":
            borrarPantalla()
            print(Cursor.FORWARD(40) + Cursor.DOWN(3) + Fore.RED + "Error: No existe partida con ese nombre")
            print(Cursor.FORWARD(38) + Cursor.DOWN(2) + Fore.WHITE + "¿Desea borrar otra partida? Si (1) No (2)")
            print(Cursor.FORWARD(49) + Fore.WHITE + Cursor.DOWN(2) + "Eliga una opcion ( )" + Back.RESET)
            confirmador = input(Cursor.UP(1) + Cursor.FORWARD(67))
        if confirmador == "1":
            borrar(archivo1,archivo2,archivo3,archivo4)
        else:
            sudoku()

def estadis():
    tablero = "4"
    while tablero != "1" and tablero != "2" and tablero != "3":
        borrarPantalla()
        print("")
        print()
        print(Cursor.FORWARD(39) + Fore.YELLOW +  "+"*35)
        print(Cursor.FORWARD(39) + Fore.YELLOW +  "+          ESTADÍSTICAS           +")
        print(Cursor.FORWARD(39) + Fore.YELLOW +  "+"*35)
        print(Cursor.FORWARD(43) + Cursor.DOWN(2) + Fore.RED + "(1) Partidas por jugador (1)")
        print(Cursor.FORWARD(39) + Cursor.DOWN(1)+ Fore.CYAN + "(2) Tableros de partidas pasadas (2)")
        print(Cursor.FORWARD(44) + Cursor.DOWN(1)+Fore.YELLOW + "(3) Regresar al menú (3)")
        print(Cursor.FORWARD(47) + Fore.WHITE + Cursor.DOWN(2) + "Eliga una opcion ( )" + Back.RESET)
        tablero = input(Cursor.UP(1) + Cursor.FORWARD(65))
    return tablero

def instrucciones():
    borrarPantalla()
    print("")
    print()
    print(Cursor.FORWARD(39) + Fore.YELLOW +  "+"*35)
    print(Cursor.FORWARD(39) + Fore.YELLOW +  "+          INSTRUCCIONES          +")
    print(Cursor.FORWARD(39) + Fore.YELLOW +  "+"*35)
    print(Cursor.FORWARD(28) + Cursor.DOWN(2) + Fore.GREEN + "a) Al hacerse una jugada correcta, se mostrará en verde")
    print(Cursor.FORWARD(28) + Cursor.DOWN(1) + Fore.RED + "b) Al hacerse una jugada incorrecta, se mostrará en rojo")
    print(Cursor.FORWARD(28) + Cursor.DOWN(1) + Fore.CYAN + "c) Las jugadas posibles a borrar se mostrarán en azul")
    print(Cursor.FORWARD(28) + Cursor.DOWN(1) + Fore.YELLOW + "d) Mientras más sudokitos tengas peor es tu puntaje.")
    print(Cursor.FORWARD(38) + Fore.WHITE + Cursor.DOWN(2) + "Para volver al menú presione enter ( )" + Back.RESET)
    entrada = input(Cursor.UP(1) + Cursor.FORWARD(74))
    borrarPantalla()
    sudoku()

def tablero4x4(difi,guard,estadis,part,tblr,jgds):
    final,confirmador,Verde,contador,espaciosv,veces,pasar = 0,0,49,0,0,0,0
    borrarPantalla()
    if guard == "Si":
        vacio = esvacio(part)
        if vacio == True:
            print(Cursor.FORWARD(44) + Cursor.DOWN(3) + Fore.RED + "No hay partidas guardadas")
            print(Cursor.FORWARD(38) + Fore.WHITE + Cursor.DOWN(2) + "Para volver al menú presione enter ( )" + Back.RESET)
            entrada = input(Cursor.UP(1) + Cursor.FORWARD(74))
            borrarPantalla()
            pasar = "1"
            veces = espaciosv + 1
        else:
            print(Cursor.FORWARD(40) + Fore.YELLOW +  "+"*39)
            print(Cursor.FORWARD(40) + Fore.YELLOW +  "+          PARTIDAS GUARDADAS         +")
            print(Cursor.FORWARD(40) + Fore.YELLOW +  "+"*39)
            lecturajsonmatricesg(part)
            nombre = input(Cursor.DOWN(2) + Cursor.FORWARD(40) + Fore.WHITE + "Ingrese el nombre de la partida: ")
    else:
        nombre = input(Cursor.FORWARD(40) + Cursor.DOWN(2) + Fore.WHITE + "Ingrese el nombre de la partida: ")
    borrarPantalla()
    if pasar != "1":
        lista2 = []
        inicio = time.time()
        dic = {"A":1,"B":2,"C":3,"D":4}
        Letras = ["A","B","C","D"]
        Numeros = [1,2,3,4]
        if guard == "Si":
            sudoku = definirmatriz(nombre,part)
            sudoku1 = copy.deepcopy(sudoku)
            contador = definirpunt(nombre,part)
            lista2 = definirjugadas(nombre,jgds)
        else:
            random = randint(1,20)
            tablero = d4[random]
            if difi == "S":
                sudoku = tableroaleatorio4x4(tablero,8,9)
                sudoku1 = copy.deepcopy(sudoku)
            elif difi == "M":
                sudoku = tableroaleatorio4x4(tablero,10,11)
                sudoku1 = copy.deepcopy(sudoku)
            else:
                sudoku = tableroaleatorio4x4(tablero,12,13)
                sudoku1 = copy.deepcopy(sudoku)
        for i in range (len(sudoku)):
            for j in range(len(sudoku[0])):
                if sudoku[i][j] == " ":
                    espaciosv = espaciosv + 1
    while veces < espaciosv:
        V1, B1 = 1,1
        if Verde == 50:
            borrarPantalla()
            mostrarTablero_4x4_V(sudoku, y - 1, dic[x] - 1)
            print(Cursor.DOWN(1) + Cursor.FORWARD(52) + Fore.GREEN + "Movimiento válido")
            print(Cursor.FORWARD(44) + Fore.WHITE + Cursor.DOWN(1)+ "(1) ¿Desea seguir la partida? (1)" + Back.RESET)
            print(Cursor.FORWARD(40) + Fore.WHITE + Cursor.DOWN(1)+ "(2) ¿Quiere guardar la partida y seguir? (2)" + Back.RESET)
            print(Cursor.FORWARD(38) + Fore.WHITE + Cursor.DOWN(1)+ "(3) ¿Quiere guardar la partida y jugar otra? (3)" + Back.RESET)
            print(Cursor.FORWARD(38) + Fore.WHITE + Cursor.DOWN(1)+ "(4) ¿Quiere guardar la partida e ir al menú? (4)" + Back.RESET)
            print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
            reiniciar_partida = '5'
            while reiniciar_partida != '1' and reiniciar_partida != '2'and reiniciar_partida != '3' and reiniciar_partida != "4":
                reiniciar_partida = input(Cursor.UP(1) + Cursor.FORWARD(69))
            if reiniciar_partida == "1":
                borrarPantalla()
                mostrarTablero_4x4_(sudoku)
                pass
            if reiniciar_partida == "2":
                guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                guardarjugadas(nombre,lista2,jgds)
                guardartableros(nombre,sudoku,tblr)
                borrarPantalla()
                mostrarTablero_4x4_(sudoku)
            if reiniciar_partida == "3":
                borrarPantalla()
                guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                guardarjugadas(nombre,lista2,jgds)
                guardartableros(nombre,sudoku,tblr)
                guardada = "3"
                while guardada != "1" and guardada != "2":
                    print(Cursor.FORWARD(43) + Fore.WHITE + Cursor.DOWN(1) + "¿Desea partida guardada? Si(1) No(2)" + Back.RESET)
                    print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
                    guardada = input(Cursor.UP(1) + Cursor.FORWARD(69))
                if guardada == "1":
                    guard = "Si"
                else:
                    guard = "No"
                veces =  espaciosv + 2
                break
            if reiniciar_partida == "4":
                guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                guardarjugadas(nombre,lista2,jgds)
                guardartableros(nombre,sudoku,tblr)
                veces = espaciosv + 1
                break
        if confirmador == 30:
            while B1 == 1 or B1 == 3:
                if B1 == 3:
                    borrarPantalla()
                    mostrarTablero_4x4_JC(sudoku, lista2)
                    print(Cursor.DOWN(1) + Cursor.FORWARD(41) + Fore.RED + "Posicion invalida, ingrese nuevamente: ")
                else:
                    borrarPantalla()
                    mostrarTablero_4x4_JC(sudoku, lista2)
                x = input(Cursor.DOWN(1) + Cursor.FORWARD(49) + Fore.WHITE + "Ingrese la columna: ").upper()
                y = int(input(Cursor.DOWN(1) + Cursor.FORWARD(49) + Fore.WHITE + "Ingrese la fila: "))
                if x.upper() in Letras and y in Numeros and [y-1,dic[x]-1] in lista2:
                    B1 = 2
                    lista2.remove([y-1,dic[x]-1])
                    sudoku[y-1][dic[x]-1] = " "
                    veces = veces - 1
                    if len(lista2) != 0:
                        print(Cursor.FORWARD(40) + Fore.WHITE + Cursor.DOWN(2) + "¿Desea borrar otra jugada? Si(1) No(2)" + Back.RESET)
                        print(Cursor.FORWARD(49) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
                        borrar = input(Cursor.UP(1) + Cursor.FORWARD(67))
                        if borrar == "1":
                            B1 = 1
                        if borrar == "2":
                            B1 = 2
                            confirmador = 0
                else:
                    B1 = 3
        if final == 0 and B1 != 2:
            borrarPantalla()
            mostrarTablero_4x4_(sudoku)
        if B1 == 2:
            borrarPantalla()
            mostrarTablero_4x4_(sudoku)
        while V1 == 1 or V1 == 3:
            if V1 == 3:
                borrarPantalla()
                mostrarTablero_4x4_(sudoku)
                print(Cursor.DOWN(1) + Cursor.FORWARD(41)+Fore.RED+"Posicion invalida, ingrese nuevamente: ")
            x = input(Cursor.DOWN(1) + Cursor.FORWARD(49)+Fore.WHITE+"Ingrese la columna: ").upper()
            y = int(input(Cursor.DOWN(1) + Cursor.FORWARD(49) + Fore.WHITE + "Ingrese la fila: "))
            num = int(input(Cursor.DOWN(1) + Cursor.FORWARD(49) + Fore.WHITE + "Ingrese el número: "))
            if x.upper() in Letras and y in Numeros and num in Numeros:
                V1 = 2
            else:
                V1 = 3
        if sudoku[y-1][dic[x]-1] != " ":
            confirmador, final, Verde = 0,0,49
            contador += 1
            borrarPantalla()
            mostrarTablero_4x4_R(sudoku,y-1,dic[x]-1)
            print(Cursor.DOWN(1)+Cursor.FORWARD(51) + Fore.RED + "Movimiento invalido")
            print(Cursor.FORWARD(43) + Fore.WHITE + Cursor.DOWN(2) + "(1) ¿Desea reiniciar la partida? (1)" + Back.RESET)
            print(Cursor.FORWARD(46) + Fore.WHITE + Cursor.DOWN(1) + "(2) ¿Quiere otro tablero? (2)" + Back.RESET)
            print(Cursor.FORWARD(45) + Fore.WHITE + Cursor.DOWN(1) + "(3) ¿Quiere volver al menú? (3)" + Back.RESET)
            print(Cursor.FORWARD(45) + Fore.WHITE + Cursor.DOWN(1) + "(4) ¿Seguir con la partida? (4)" + Back.RESET)
            print(Cursor.FORWARD(40) + Fore.WHITE + Cursor.DOWN(1)+ "(5) ¿Quiere guardar la partida y seguir? (5)" + Back.RESET)
            print(Cursor.FORWARD(38) + Fore.WHITE + Cursor.DOWN(1)+ "(6) ¿Quiere guardar la partida y jugar otra? (6)" + Back.RESET)
            print(Cursor.FORWARD(38) + Fore.WHITE + Cursor.DOWN(1)+ "(7) ¿Quiere guardar la partida e ir al menú? (7)" + Back.RESET)
            if len(lista2) != 0:
                print(Cursor.FORWARD(46) + Fore.WHITE + Cursor.DOWN(1) + "(8) ¿Desea borrar jugadas? (8)" + Back.RESET)
            print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
            reiniciar_partida = '9'
            while reiniciar_partida != '1' and reiniciar_partida != '2'and reiniciar_partida != '3'and reiniciar_partida != '4' and reiniciar_partida != "5" and reiniciar_partida != "6" and reiniciar_partida != "7" and reiniciar_partida != "8":
                reiniciar_partida = input(Cursor.UP(1) + Cursor.FORWARD(69))
                if reiniciar_partida == '1':
                    veces,contador = 0,0
                    sudoku = copy.deepcopy(sudoku1)
                    inicio = time.time()
                if reiniciar_partida == '2':
                    borrarPantalla()
                    guardartableros(nombre,sudoku,tblr)
                    guardada = "3"
                    while guardada != "1" and guardada != "2":
                        print(Cursor.FORWARD(43) + Fore.WHITE + Cursor.DOWN(1) + "¿Desea partida guardada? Si(1) No(2)" + Back.RESET)
                        print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
                        guardada = input(Cursor.UP(1) + Cursor.FORWARD(69))
                    if guardada == "1":
                        guard = "Si"
                    else:
                        guard = "No"
                    veces =  espaciosv + 2
                    break
                    veces =  espaciosv + 2
                if reiniciar_partida == '3':
                    guardartableros(nombre,sudoku,tblr)
                    veces = espaciosv + 1
                if reiniciar_partida == '4':
                    pass
                if reiniciar_partida == "5":
                    guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                    guardarjugadas(nombre,lista2,jgds)
                    guardartableros(nombre,sudoku,tblr)
                    pass
                if reiniciar_partida == "6":
                    borrarPantalla()
                    guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                    guardarjugadas(nombre,lista2,jgds)
                    guardartableros(nombre,sudoku,tblr)
                    guardada = "3"
                    while guardada != "1" and guardada != "2":
                        print(Cursor.FORWARD(43) + Fore.WHITE + Cursor.DOWN(1) + "¿Desea partida guardada? Si(1) No(2)" + Back.RESET)
                        print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
                        guardada = input(Cursor.UP(1) + Cursor.FORWARD(69))
                    if guardada == "1":
                        guard = "Si"
                    else:
                        guard = "No"
                    veces =  espaciosv + 2
                if reiniciar_partida == "7":
                    guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                    guardarjugadas(nombre,lista2,jgds)
                    guardartableros(nombre,sudoku,tblr)
                    veces = espaciosv + 1
                if reiniciar_partida == "8":
                    confirmador = 30
        elif comprobar4x4(sudoku,num,y-1,dic[x]-1) == False:
            confirmador, final, Verde = 0,0,49
            contador += 1
            borrarPantalla()
            sudoku[y-1][dic[x]-1] = num
            mostrarTablero_4x4_R(sudoku,y-1,dic[x]-1)
            sudoku[y-1][dic[x]-1] = " "
            print(Cursor.DOWN(1)+Cursor.FORWARD(51) + Fore.RED + "Movimiento invalido")
            print(Cursor.FORWARD(43) + Fore.WHITE + Cursor.DOWN(2) + "(1) ¿Desea reiniciar la partida? (1)" + Back.RESET)
            print(Cursor.FORWARD(46) + Fore.WHITE + Cursor.DOWN(1) + "(2) ¿Quiere otro tablero? (2)" + Back.RESET)
            print(Cursor.FORWARD(45) + Fore.WHITE + Cursor.DOWN(1) + "(3) ¿Quiere volver al menú? (3)" + Back.RESET)
            print(Cursor.FORWARD(45) + Fore.WHITE + Cursor.DOWN(1) + "(4) ¿Seguir con la partida? (4)" + Back.RESET)
            print(Cursor.FORWARD(40) + Fore.WHITE + Cursor.DOWN(1)+ "(5) ¿Quiere guardar la partida y seguir? (5)" + Back.RESET)
            print(Cursor.FORWARD(38) + Fore.WHITE + Cursor.DOWN(1)+ "(6) ¿Quiere guardar la partida y jugar otra? (6)" + Back.RESET)
            print(Cursor.FORWARD(38) + Fore.WHITE + Cursor.DOWN(1)+ "(7) ¿Quiere guardar la partida e ir al menú? (7)" + Back.RESET)
            if len(lista2) != 0:
                print(Cursor.FORWARD(46) + Fore.WHITE + Cursor.DOWN(1) + "(8) ¿Desea borrar jugadas? (8)" + Back.RESET)
            print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
            reiniciar_partida = '9'
            while reiniciar_partida != '1' and reiniciar_partida != '2'and reiniciar_partida != '3'and reiniciar_partida != '4' and reiniciar_partida != "5" and reiniciar_partida != "6" and reiniciar_partida != "7" and reiniciar_partida != "8":
                reiniciar_partida = input(Cursor.UP(1) + Cursor.FORWARD(69))
                if reiniciar_partida == '1':
                    veces,contador = 0,0
                    sudoku = copy.deepcopy(sudoku1)
                    inicio = time.time()
                    Verde = 49
                if reiniciar_partida == '2':
                    borrarPantalla()
                    guardartableros(nombre,sudoku,tblr)
                    guardada = "3"
                    while guardada != "1" and guardada != "2":
                        print(Cursor.FORWARD(43) + Fore.WHITE + Cursor.DOWN(1) + "¿Desea partida guardada? Si(1) No(2)" + Back.RESET)
                        print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
                        guardada = input(Cursor.UP(1) + Cursor.FORWARD(69))
                    if guardada == "1":
                        guard = "Si"
                    else:
                        guard = "No"
                    veces = espaciosv + 2
                    break
                if reiniciar_partida == '3':
                    guardartableros(nombre,sudoku,tblr)
                    veces = espaciosv + 1
                if reiniciar_partida == '4':
                    pass
                if reiniciar_partida == "5":
                    guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                    guardarjugadas(nombre,lista2,jgds)
                    guardartableros(nombre,sudoku,tblr)
                    pass
                if reiniciar_partida == "6":
                    borrarPantalla()
                    guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                    guardarjugadas(nombre,lista2,jgds)
                    guardartableros(nombre,sudoku,tblr)
                    guardada = "3"
                    while guardada != "1" and guardada != "2":
                        print(Cursor.FORWARD(43) + Fore.WHITE + Cursor.DOWN(1) + "¿Desea partida guardada? Si(1) No(2)" + Back.RESET)
                        print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
                        guardada = input(Cursor.UP(1) + Cursor.FORWARD(69))
                    if guardada == "1":
                        guard = "Si"
                    else:
                        guard = "No"
                    veces =  espaciosv + 2
                if reiniciar_partida == "7":
                    guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                    guardarjugadas(nombre,lista2,jgds)
                    guardartableros(nombre,sudoku,tblr)
                    veces = espaciosv + 1
                if reiniciar_partida == "8":
                    confirmador = 30
        else:
            Verde, final,confirmador = 50,1,0
            veces = veces + 1
            sudoku[y-1][dic[x]-1] = num
            lista2.append([(y-1),(dic[x]-1)])
    Fore.WHITE
    if veces == espaciosv:
        final = time.time()
        tiempo = round(final-inicio,0)
        puntaje = int(contador + tiempo)
        borrarPantalla()
        mostrarTablero_4x4_(sudoku)
        borrarpartida(nombre,part)
        borrarpartida(nombre,jgds)
        guardarestadisticas(nombre,puntaje,estadis)
        guardartableros(nombre,sudoku,tblr)
        print(Cursor.DOWN(1)+Cursor.FORWARD(47)+Fore.GREEN +" " + "¡Felicidades, has ganado!")
        print(Cursor.DOWN(1)+Cursor.FORWARD(46)+Fore.YELLOW +" " + "Tu puntaje es:", puntaje, 'sudokitos')
        print(" ")
        print(Cursor.FORWARD(49) + Cursor.DOWN(1) + Fore.YELLOW + "(1) Jugar de nuevo (1)")
        print(Cursor.FORWARD(51) + Cursor.DOWN(1) + Fore.CYAN + "(2) Ir al menú (2)")
        print(Cursor.FORWARD(48) + Cursor.DOWN(1) + Fore.RED + "(3) Salir del juego (3)")
        print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Eliga una opcion ( )" + Back.RESET)
        escoger = "4"
        while escoger != "1" and escoger != "2" and escoger != "3":
            escoger = input(Cursor.UP(1) + Cursor.FORWARD(69))
        if escoger == "1":
            borrarPantalla()
            guardada = "3"
            while guardada != "1" and guardada != "2":
                print(Cursor.FORWARD(43) + Fore.WHITE + Cursor.DOWN(1) + "¿Desea partida guardada? Si(1) No(2)" + Back.RESET)
                print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
                guardada = input(Cursor.UP(1) + Cursor.FORWARD(69))
            if guardada == "1":
                guard = "Si"
            else:
                guard = "No"
            tablero4x4(difi,guard,estadis,part,tblr,jgds)
        elif escoger == "2":
    	    None
        else:
    	    exit()
    elif veces == espaciosv + 1:
        None
    else:
        tablero4x4(difi,guard,estadis,part,tblr,jgds)

def tablero9x9(difi,guard,estadis,part,tblr,jgds):
    final,confirmador,Verde,contador,espaciosv,veces,pasar = 0,0,49,0,0,0,0
    borrarPantalla()
    if guard == "Si":
        vacio = esvacio(part)
        if vacio == True:
            print(Cursor.FORWARD(44) + Cursor.DOWN(3) + Fore.RED + "No hay partidas guardadas")
            print(Cursor.FORWARD(38) + Fore.WHITE + Cursor.DOWN(2) + "Para volver al menú presione enter ( )" + Back.RESET)
            entrada = input(Cursor.UP(1) + Cursor.FORWARD(74))
            borrarPantalla()
            pasar = "1"
            veces = espaciosv + 1
        else:
            print(Cursor.FORWARD(27) + Fore.YELLOW +  "+"*39)
            print(Cursor.FORWARD(27) + Fore.YELLOW +  "+          PARTIDAS GUARDADAS         +")
            print(Cursor.FORWARD(27) + Fore.YELLOW +  "+"*39)
            lecturajsonmatricesg(part)
            nombre = input(Cursor.DOWN(2) + Cursor.FORWARD(27) + Fore.WHITE + "Ingrese el nombre de la partida: ")
    else:
        nombre = input(Cursor.FORWARD(40) + Cursor.DOWN(2) + Fore.WHITE + "Ingrese el nombre de la partida: ")
    borrarPantalla()
    if pasar != "1":
        lista2 = []
        inicio = time.time()
        dic = {"A": 1, "B": 2, "C": 3, "D": 4,"E":5,"F":6,"G":7,"H":8,"I":9}
        Letras = ["A", "B", "C", "D","E","F","G","H","I"]
        Numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        if guard == "Si":
            sudoku = definirmatriz(nombre,part)
            sudoku1 = copy.deepcopy(sudoku)
            contador = definirpunt(nombre,part)
            lista2 = definirjugadas(nombre,jgds)
        else:
            random = randint(1, 20)
            tablero = d9[random]
            if difi == "S":
                sudoku = tableroaleatorio9x9(tablero,40,41)
                sudoku1 = copy.deepcopy(sudoku)
            elif difi == "M":
                sudoku = tableroaleatorio9x9(tablero,53,54)
                sudoku1 = copy.deepcopy(sudoku)
            else:
                sudoku = tableroaleatorio9x9(tablero,60,61)
                sudoku1 = copy.deepcopy(sudoku)
        for i in range(len(sudoku)):
            for j in range(len(sudoku[0])):
                if sudoku[i][j] == " ":
                    espaciosv = espaciosv + 1
    while veces < espaciosv:
        V1,B1 = 1,1
        if Verde == 50:
            borrarPantalla()
            mostrarTablero_9x9_V(sudoku, y - 1, dic[x] - 1)
            print(Cursor.DOWN(1) + Cursor.FORWARD(38) + Fore.GREEN + "Movimiento válido")
            print(Cursor.FORWARD(31) + Fore.WHITE + Cursor.DOWN(1)+ "(1) ¿Desea seguir la partida? (1)" + Back.RESET)
            print(Cursor.FORWARD(25) + Fore.WHITE + Cursor.DOWN(1)+ "(2) ¿Quiere guardar la partida y seguir? (2)" + Back.RESET)
            print(Cursor.FORWARD(23) + Fore.WHITE + Cursor.DOWN(1)+ "(3) ¿Quiere guardar la partida y jugar otra? (3)" + Back.RESET)
            print(Cursor.FORWARD(23) + Fore.WHITE + Cursor.DOWN(1)+ "(4) ¿Quiere guardar la partida e ir al menú? (4)" + Back.RESET)
            print(Cursor.FORWARD(38) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
            reiniciar_partida = '5'
            while reiniciar_partida != '1' and reiniciar_partida != '2'and reiniciar_partida != '3' and reiniciar_partida != "4":
                reiniciar_partida = input(Cursor.UP(1) + Cursor.FORWARD(56))
            if reiniciar_partida == "1":
                borrarPantalla()
                mostrarTablero_9x9_(sudoku)
                pass
            if reiniciar_partida == "2":
                guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                guardarjugadas(nombre,lista2,jgds)
                guardartableros(nombre,sudoku,tblr)
                borrarPantalla()
                mostrarTablero_4x4_(sudoku)
            if reiniciar_partida == "3":
                borrarPantalla()
                guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                guardarjugadas(nombre,lista2,jgds)
                guardartableros(nombre,sudoku,tblr)
                guardada = "3"
                while guardada != "1" and guardada != "2":
                    print(Cursor.FORWARD(43) + Fore.WHITE + Cursor.DOWN(1) + "¿Desea partida guardada? Si(1) No(2)" + Back.RESET)
                    print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
                    guardada = input(Cursor.UP(1) + Cursor.FORWARD(69))
                if guardada == "1":
                    guard = "Si"
                else:
                    guard = "No"
                veces =  espaciosv + 2
                break
            if reiniciar_partida == "4":
                guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                guardarjugadas(nombre,lista2,jgds)
                guardartableros(nombre,sudoku,tblr)
                veces = espaciosv + 1
                break
        if confirmador == 30:
            while B1 == 1 or B1 == 3:
                if B1 == 3:
                    borrarPantalla()
                    mostrarTablero_9x9_JC(tablero, lista2)
                    print(Cursor.DOWN(1) + Cursor.FORWARD(27) + Fore.RED + "Posicion invalida, ingrese nuevamente: ")
                else:
                    borrarPantalla()
                    mostrarTablero_9x9_JC(tablero, lista2)
                x = input(Cursor.DOWN(1) + Cursor.FORWARD(35) + Fore.WHITE + "Ingrese la columna: ").upper()
                y = int(input(Cursor.DOWN(1) + Cursor.FORWARD(35) + Fore.WHITE + "Ingrese la fila: "))
                if x.upper() in Letras and y in Numeros and [y - 1, dic[x] - 1] in lista2:
                    B1 = 2
                    lista2.remove([y - 1, dic[x] - 1])
                    sudoku[y - 1][dic[x] - 1] = " "
                    veces = veces - 1
                    if len(lista2) != 0:
                        print(Cursor.FORWARD(26) + Fore.WHITE + Cursor.DOWN(2) + "¿Desea borrar otra jugada? Si(1) No(2)" + Back.RESET)
                        print(Cursor.FORWARD(35) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
                        borrar = input(Cursor.UP(1) + Cursor.FORWARD(53))
                        if borrar == "1":
                            B1 = 1
                        if borrar == "2":
                            B1 = 2
                            confirmador = 0
                else:
                    B1 = 3
        if final == 0 and B1 != 2:
            borrarPantalla()
            mostrarTablero_9x9_(sudoku)
        if B1 == 2:
            borrarPantalla()
            mostrarTablero_9x9_(sudoku)
        while V1 == 1 or V1 == 3:
            if V1 == 3:
                borrarPantalla()
                mostrarTablero_9x9_(sudoku)
                print(Cursor.DOWN(1) + Cursor.FORWARD(27) + Fore.RED + "Posicion invalida, ingrese nuevamente: ")
            x = input(Cursor.DOWN(1) + Cursor.FORWARD(35) + Fore.WHITE + "Ingrese la columna: ").upper()
            y = int(input(Cursor.DOWN(1) + Cursor.FORWARD(35) + Fore.WHITE + "Ingrese la fila: "))
            num = int(input(Cursor.DOWN(1) + Cursor.FORWARD(35) + Fore.WHITE + "Ingrese el número: "))
            if x.upper() in Letras and y in Numeros and num in Numeros:
                V1 = 2
            else:
                V1 = 3
        if sudoku[y - 1][dic[x] - 1] != " ":
            confirmador,final,Verde = 0,0,49
            contador += 1
            borrarPantalla()
            mostrarTablero_9x9_R(sudoku, y - 1, dic[x] - 1)
            print(Cursor.DOWN(1) + Cursor.FORWARD(37) + Fore.RED + "Movimiento invalido")
            print(Cursor.FORWARD(29) + Fore.WHITE + Cursor.DOWN(2) + "(1) ¿Desea reiniciar la partida? (1)" + Back.RESET)
            print(Cursor.FORWARD(32) + Fore.WHITE + Cursor.DOWN(1) + "(2) ¿Quiere otro tablero? (2)" + Back.RESET)
            print(Cursor.FORWARD(31) + Fore.WHITE + Cursor.DOWN(1) + "(3) ¿Quiere volver al menú? (3)" + Back.RESET)
            print(Cursor.FORWARD(31) + Fore.WHITE + Cursor.DOWN(1) + "(4) ¿Seguir con la partida? (4)" + Back.RESET)
            print(Cursor.FORWARD(24) + Fore.WHITE + Cursor.DOWN(1)+ "(5) ¿Quiere guardar la partida y seguir? (5)" + Back.RESET)
            print(Cursor.FORWARD(22) + Fore.WHITE + Cursor.DOWN(1)+ "(6) ¿Quiere guardar la partida y jugar otra? (6)" + Back.RESET)
            print(Cursor.FORWARD(22) + Fore.WHITE + Cursor.DOWN(1)+ "(7) ¿Quiere guardar la partida e ir al menú? (7)" + Back.RESET)
            if len(lista2) != 0:
                print(Cursor.FORWARD(31) + Fore.WHITE + Cursor.DOWN(1) + "(8) ¿Desea borrar jugadas? (8)" + Back.RESET)
            print(Cursor.FORWARD(36) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
            reiniciar_partida = '9'
            while reiniciar_partida != '1' and reiniciar_partida != '2'and reiniciar_partida != '3'and reiniciar_partida != '4' and reiniciar_partida != "5" and reiniciar_partida != "6" and reiniciar_partida != "7" and reiniciar_partida != "8":
                reiniciar_partida = input(Cursor.UP(1) + Cursor.FORWARD(54))
                if reiniciar_partida == '1':
                    veces,contador = 0,0
                    sudoku = copy.deepcopy(sudoku1)
                    inicio = time.time()
                if reiniciar_partida == '2':
                    borrarPantalla()
                    guardartableros(nombre,sudoku,tblr)
                    guardada = "3"
                    while guardada != "1" and guardada != "2":
                        print(Cursor.FORWARD(43) + Fore.WHITE + Cursor.DOWN(1) + "¿Desea partida guardada? Si(1) No(2)" + Back.RESET)
                        print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
                        guardada = input(Cursor.UP(1) + Cursor.FORWARD(69))
                    if guardada == "1":
                        guard = "Si"
                    else:
                        guard = "No"
                    veces =  espaciosv + 2
                    break
                if reiniciar_partida == '3':
                    guardartableros(nombre,sudoku,tblr)
                    veces = espaciosv + 1
                if reiniciar_partida == '4':
                    pass
                if reiniciar_partida == "5":
                    guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                    guardarjugadas(nombre,lista2,jgds)
                    guardartableros(nombre,sudoku,tblr)
                    pass
                if reiniciar_partida == "6":
                    borrarPantalla()
                    guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                    guardarjugadas(nombre,lista2,jgds)
                    guardartableros(nombre,sudoku,tblr)
                    guardada = "3"
                    while guardada != "1" and guardada != "2":
                        print(Cursor.FORWARD(43) + Fore.WHITE + Cursor.DOWN(1) + "¿Desea partida guardada? Si(1) No(2)" + Back.RESET)
                        print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
                        guardada = input(Cursor.UP(1) + Cursor.FORWARD(69))
                    if guardada == "1":
                        guard = "Si"
                    else:
                        guard = "No"
                    veces =  espaciosv + 2
                if reiniciar_partida == "7":
                    guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                    guardarjugadas(nombre,lista2,jgds)
                    guardartableros(nombre,sudoku,tblr)
                    veces = espaciosv + 1
                if reiniciar_partida == "8":
                    confirmador = 30
        elif comprobar9x9(sudoku, num, y - 1, dic[x] - 1) == False:
            final,confirmador,Verde = 0,0,49
            contador +=1
            borrarPantalla()
            sudoku[y - 1][dic[x] - 1] = num
            mostrarTablero_9x9_R(sudoku, y - 1, dic[x] - 1)
            sudoku[y - 1][dic[x] - 1] = " "
            print(Cursor.DOWN(1) + Cursor.FORWARD(37) + Fore.RED + "Movimiento invalido")
            print(
                Cursor.FORWARD(29) + Fore.WHITE + Cursor.DOWN(2) + "(1) ¿Desea reiniciar la partida? (1)" + Back.RESET)
            print(Cursor.FORWARD(32) + Fore.WHITE + Cursor.DOWN(1) + "(2) ¿Quiere otro tablero? (2)" + Back.RESET)
            print(Cursor.FORWARD(31) + Fore.WHITE + Cursor.DOWN(1) + "(3) ¿Quiere volver al menú? (3)" + Back.RESET)
            print(Cursor.FORWARD(31) + Fore.WHITE + Cursor.DOWN(1) + "(4) ¿Seguir con la partida? (4)" + Back.RESET)
            print(Cursor.FORWARD(24) + Fore.WHITE + Cursor.DOWN(1)+ "(5) ¿Quiere guardar la partida y seguir? (5)" + Back.RESET)
            print(Cursor.FORWARD(22) + Fore.WHITE + Cursor.DOWN(1)+ "(6) ¿Quiere guardar la partida y jugar otra? (6)" + Back.RESET)
            print(Cursor.FORWARD(22) + Fore.WHITE + Cursor.DOWN(1)+ "(7) ¿Quiere guardar la partida e ir al menú? (7)" + Back.RESET)
            if len(lista2) != 0:
                print(Cursor.FORWARD(31) + Fore.WHITE + Cursor.DOWN(1) + "(8) ¿Desea borrar jugadas? (8)" + Back.RESET)
            print(Cursor.FORWARD(36) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
            reiniciar_partida = '9'
            while reiniciar_partida != '1' and reiniciar_partida != '2'and reiniciar_partida != '3'and reiniciar_partida != '4' and reiniciar_partida != "5" and reiniciar_partida != "6" and reiniciar_partida != "7" and reiniciar_partida != "8":
                reiniciar_partida = input(Cursor.UP(1) + Cursor.FORWARD(54))
                if reiniciar_partida == '1':
                    veces,contador = 0,0
                    sudoku = copy.deepcopy(sudoku1)
                    inicio = time.time()
                if reiniciar_partida == '2':
                    borrarPantalla()
                    guardartableros(nombre,sudoku,tblr)
                    guardada = "3"
                    while guardada != "1" and guardada != "2":
                        print(Cursor.FORWARD(43) + Fore.WHITE + Cursor.DOWN(1) + "¿Desea partida guardada? Si(1) No(2)" + Back.RESET)
                        print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
                        guardada = input(Cursor.UP(1) + Cursor.FORWARD(69))
                    if guardada == "1":
                        guard = "Si"
                    else:
                        guard = "No"
                    veces =  espaciosv + 2
                    break
                if reiniciar_partida == '3':
                    guardartableros(nombre,sudoku,tblr)
                    veces = espaciosv + 1
                if reiniciar_partida == '4':
                    pass
                if reiniciar_partida == "5":
                    guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                    guardarjugadas(nombre,lista2,jgds)
                    guardartableros(nombre,sudoku,tblr)
                    pass
                if reiniciar_partida == "6":
                    borrarPantalla()
                    guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                    guardarjugadas(nombre,lista2,jgds)
                    guardartableros(nombre,sudoku,tblr)
                    guardada = "3"
                    while guardada != "1" and guardada != "2":
                        print(Cursor.FORWARD(43) + Fore.WHITE + Cursor.DOWN(1) + "¿Desea partida guardada? Si(1) No(2)" + Back.RESET)
                        print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
                        guardada = input(Cursor.UP(1) + Cursor.FORWARD(69))
                    if guardada == "1":
                        guard = "Si"
                    else:
                        guard = "No"
                    veces =  espaciosv + 2
                if reiniciar_partida == "7":
                    guardarpartida(nombre,[sudoku,(time.time()-inicio)+contador],part)
                    guardarjugadas(nombre,lista2,jgds)
                    guardartableros(nombre,sudoku,tblr)
                    veces = espaciosv + 1
                if reiniciar_partida == "8":
                    confirmador = 30
        else:
            Verde,final,confirmador = 50,1,0
            sudoku[y - 1][dic[x] - 1] = num
            veces = veces + 1
            lista2.append([(y - 1), (dic[x] - 1)])
    Fore.WHITE
    if veces == espaciosv:
        final = time.time()
        tiempo = round(final - inicio, 0)
        puntaje = int(contador + tiempo)
        borrarPantalla()
        mostrarTablero_9x9_(sudoku)
        mostrarTablero_4x4_(sudoku)
        borrarpartida(nombre,part)
        borrarpartida(nombre,jgds)
        guardarestadisticas(nombre,puntaje,estadis)
        guardartableros(nombre,sudoku,tblr)
        print(Cursor.DOWN(1) + Cursor.FORWARD(33) + Fore.GREEN + " " + "¡Felicidades, has ganado!")
        print(Cursor.DOWN(1) + Cursor.FORWARD(31) + Fore.YELLOW + " " + "Tu puntaje es:", puntaje, 'sudokitos')
        print(" ")
        print(Cursor.FORWARD(35) + Cursor.DOWN(1) + Fore.YELLOW + "(1) Jugar de nuevo (1)")
        print(Cursor.FORWARD(37) + Cursor.DOWN(1) + Fore.CYAN + "(2) Ir al menú (2)")
        print(Cursor.FORWARD(34) + Cursor.DOWN(1) + Fore.RED + "  (3) Salir del juego (3)")
        print(Cursor.FORWARD(37) + Fore.WHITE + Cursor.DOWN(2) + "Eliga una opcion ( )" + Back.RESET)
        escoger = 4
        while escoger != "1" and escoger != "2" and escoger != "3":
            escoger = input(Cursor.UP(1) + Cursor.FORWARD(55))
        if escoger == "1":
            borrarPantalla()
            guardada = "3"
            while guardada != "1" and guardada != "2":
                print(Cursor.FORWARD(43) + Fore.WHITE + Cursor.DOWN(1) + "¿Desea partida guardada? Si(1) No(2)" + Back.RESET)
                print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
                guardada = input(Cursor.UP(1) + Cursor.FORWARD(69))
            if guardada == "1":
                guard = "Si"
            else:
                guard = "No"
            tablero4x4(difi,guard,estadis,part,tblr,jgds)
        elif escoger == "2":
            None
        else:
            exit()
    elif veces == espaciosv + 1:
        None
    else:
        tablero9x9(difi,guard,estadis,part,tblr,jgds)

sudoku()
