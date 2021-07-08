#JUEGO DE SUDOKU - JUAN PEDRO VÁSQUEZ, GUSTAVO PEREZ, PAOLO VÁSQUEZ

from Funciones import *
borrarPantalla = lambda: os.system ("cls")
import copy

def sudoku():
    while True:
        opcion = menu()
        if opcion == "1":
            tablero = dificultad()
            if tablero == "1":
                tablero4x4()
            elif tablero == "2":
                tablero9x9()
            else:
                sudoku()
        elif opcion == "2":
            instrucciones()
        elif opcion == "3":
            exit()

def menu():
    borrarPantalla()
    print("")
    print()
    print(Cursor.FORWARD(39) + Fore.YELLOW +  "+"*35)
    print(Cursor.FORWARD(39) + Fore.YELLOW +  "+             SUDOKU              +")
    print(Cursor.FORWARD(39) + Fore.YELLOW +  "+"*35)
    print(Cursor.FORWARD(41) + Cursor.DOWN(2) + Fore.GREEN + "(1) Empezar nueva partida (1)")
    print(Cursor.FORWARD(45) + Cursor.DOWN(1) + Fore.CYAN + "(2) Instrucciones (2)")
    print(Cursor.FORWARD(44) + Cursor.DOWN(1) + Fore.RED + "(3) Salir del juego (3)")
    print(Cursor.FORWARD(46) + Fore.WHITE + Cursor.DOWN(2) + "Eliga una opcion ( )" + Back.RESET)
    eleccion = input(Cursor.UP(1) + Cursor.FORWARD(64))
    if eleccion != "1" and eleccion != "2" and eleccion != "3":
        sudoku()
    borrarPantalla()
    return eleccion

def dificultad():
    borrarPantalla()
    print("")
    print()
    print(Cursor.FORWARD(39) + Fore.YELLOW +  "+"*35)
    print(Cursor.FORWARD(39) + Fore.YELLOW +  "+            DIFICULTAD           +")
    print(Cursor.FORWARD(39) + Fore.YELLOW +  "+"*35)
    print(Cursor.FORWARD(43) + Cursor.DOWN(2) + Fore.GREEN + "(1) Facil: Tablero 4x4 (1)")
    print(Cursor.FORWARD(42) + Cursor.DOWN(1) + Fore.RED + "(2) Dificil: Tablero 9x9 (2)")
    print(Cursor.FORWARD(44) + Cursor.DOWN(1) + Fore.YELLOW + "(3) Regresar al menú (3)")
    print(Cursor.FORWARD(47) + Fore.WHITE + Cursor.DOWN(2) + "Eliga una opcion ( )" + Back.RESET)
    tablero = input(Cursor.UP(1) + Cursor.FORWARD(65))
    if tablero != "1" and tablero != "2" and tablero != "3":
        dificultad()
    borrarPantalla()
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

def tablero4x4():
    final,confirmador,Verde,contador,espaciosv,veces = 0,0,49,0,0,0
    borrarPantalla()
    lista2 = []
    inicio = time.time()
    dic = {"A":1,"B":2,"C":3,"D":4}
    Letras = ["A","B","C","D"]
    Numeros = [1,2,3,4]
    random = randint(1,20)
    tablero = d4[random]
    sudoku = tableroaleatorio4x4(tablero)
    sudoku1 = copy.deepcopy(sudoku)
    for i in range (len(d4[random])):
        for j in range(len(d4[random][0])):
            if d4[random][i][j] == " ":
                espaciosv = espaciosv + 1
    while veces < espaciosv:
        V1, B1 = 1,1
        if Verde == 50:
            borrarPantalla()
            mostrarTablero_4x4_V(sudoku, y - 1, dic[x] - 1)
            print(Cursor.DOWN(1) + Cursor.FORWARD(52) + Fore.GREEN + "Movimiento válido")
        if confirmador == 30:
            while B1 == 1 or B1 == 3:
                if B1 == 3:
                    borrarPantalla()
                    mostrarTablero_4x4_JC(tablero, lista2)
                    print(Cursor.DOWN(1) + Cursor.FORWARD(41) + Fore.RED + "Posicion invalida, ingrese nuevamente: ")
                else:
                    borrarPantalla()
                    mostrarTablero_4x4_JC(tablero, lista2)
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
            if len(lista2) != 0:
                print(Cursor.FORWARD(46) + Fore.WHITE + Cursor.DOWN(1) + "(5) ¿Desea borrar jugadas? (5)" + Back.RESET)
            print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
            reiniciar_partida = '6'
            while reiniciar_partida != '1' and reiniciar_partida != '2'and reiniciar_partida != '3'and reiniciar_partida != '4' and reiniciar_partida != "5":
                reiniciar_partida = input(Cursor.UP(1) + Cursor.FORWARD(69))
                if reiniciar_partida == '1':
                    veces,contador = 0,0
                    sudoku = copy.deepcopy(sudoku1)
                    inicio = time.time()
                if reiniciar_partida == '2':
                    veces =  espaciosv + 2
                if reiniciar_partida == '3':
                    veces = espaciosv + 1
                if reiniciar_partida == '4':
                    pass
                if reiniciar_partida == "5":
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
            if len(lista2) != 0:
                print(Cursor.FORWARD(46) + Fore.WHITE + Cursor.DOWN(1) + "(5) ¿Desea borrar jugadas? (5)" + Back.RESET)
            print(Cursor.FORWARD(51) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
            reiniciar_partida = '6'
            while reiniciar_partida != '1' and reiniciar_partida != '2'and reiniciar_partida != '3'and reiniciar_partida != '4' and reiniciar_partida != "5":
                reiniciar_partida = input(Cursor.UP(1) + Cursor.FORWARD(69))
                if reiniciar_partida == '1':
                    veces,contador = 0,0
                    sudoku = copy.deepcopy(sudoku1)
                    inicio = time.time()
                    Verde = 49
                if reiniciar_partida == '2':
                    veces = espaciosv + 2
                if reiniciar_partida == '3':
                    veces = espaciosv + 1
                if reiniciar_partida == '4':
                    pass
                if reiniciar_partida == "5":
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
    	    tablero4x4()
        elif escoger == "2":
    	    None
        else:
    	    exit()
    elif veces == espaciosv + 1:
        None
    else:
        tablero4x4()

def tablero9x9():
    final,confirmador,Verde,contador,espaciosv,veces = 0,0,49,0,0,0
    borrarPantalla()
    lista2 = []
    inicio = time.time()
    dic = {"A": 1, "B": 2, "C": 3, "D": 4,"E":5,"F":6,"G":7,"H":8,"I":9}
    Letras = ["A", "B", "C", "D","E","F","G","H","I"]
    Numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random = randint(1, 20)
    tablero = d9[random]
    sudoku = tableroaleatorio9x9(tablero)
    sudoku1 = copy.deepcopy(sudoku)
    for i in range(len(d9[random])):
        for j in range(len(d9[random][0])):
            if d9[random][i][j] == " ":
                espaciosv = espaciosv + 1
    while veces < espaciosv:
        V1,B1 = 1,1
        if Verde == 50:
            borrarPantalla()
            mostrarTablero_9x9_V(sudoku, y - 1, dic[x] - 1)
            print(Cursor.DOWN(1) + Cursor.FORWARD(37) + Fore.GREEN + "Movimiento válido")
        if confirmador == 30:
            while B1 == 1 or B1 == 3:
                if B1 == 3:
                    borrarPantalla()
                    mostrarTablero_9x9_JC(tablero, lista2)
                    print(Cursor.DOWN(1) + Cursor.FORWARD(
                        27) + Fore.RED + "Posicion invalida, ingrese nuevamente: ")
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
            if len(lista2) != 0:
                print(Cursor.FORWARD(31) + Fore.WHITE + Cursor.DOWN(1) + "(5) ¿Desea borrar jugadas? (5)" + Back.RESET)
            print(Cursor.FORWARD(37) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
            reiniciar_partida = '6'
            while reiniciar_partida != '1' and reiniciar_partida != '2' and reiniciar_partida != '3' and reiniciar_partida != '4' and reiniciar_partida != "5":
                reiniciar_partida = input(Cursor.UP(1) + Cursor.FORWARD(55))
                if reiniciar_partida == '1':
                    veces = 0
                    sudoku = copy.deepcopy(sudoku1)
                    contador = 0
                    inicio = time.time()
                if reiniciar_partida == '2':
                    veces = espaciosv + 2
                if reiniciar_partida == '3':
                    veces = espaciosv + 1
                if reiniciar_partida == '4':
                    pass
                if reiniciar_partida == "5":
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
            if len(lista2) != 0:
                print(Cursor.FORWARD(31) + Fore.WHITE + Cursor.DOWN(1) + "(5) ¿Desea borrar jugadas? (5)" + Back.RESET)
            print(Cursor.FORWARD(37) + Fore.WHITE + Cursor.DOWN(2) + "Elija una opción ( )" + Back.RESET)
            reiniciar_partida = '6'
            while reiniciar_partida != '1' and reiniciar_partida != '2' and reiniciar_partida != '3' and reiniciar_partida != '4' and reiniciar_partida != "5":
                reiniciar_partida = input(Cursor.UP(1) + Cursor.FORWARD(55))
                if reiniciar_partida == '1':
                    veces,contador = 0,0
                    sudoku = copy.deepcopy(sudoku1)
                    inicio = time.time()
                if reiniciar_partida == '2':
                    veces = espaciosv + 2
                if reiniciar_partida == '3':
                    veces = espaciosv + 1
                if reiniciar_partida == '4':
                    pass
                if reiniciar_partida == "5":
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
        mostrarTablero_4x4_(sudoku)
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
            tablero9x9()
        elif escoger == "2":
            None
        else:
            exit()
    elif veces == espaciosv + 1:
        None
    else:
        tablero9x9()

sudoku()
