#FUNCIONES Y LIBRERARIAS GENERALES
from colorama import *
from random import randint
import numpy as np
import os
import sys
import time

#FUNCIONES TABLERO 4X4

def mostrarTablero_4x4_(tablero):
    for i in range(len(tablero)):
        print("")
        if i == 0:
            print(Cursor.FORWARD(53) + Fore.YELLOW + "A" + " " * 3 + "B" + " " * 5 + "C" + " " * 3 + "D")
            print(Cursor.FORWARD(49) + Fore.WHITE + " " + "+" + "-" * 19 + "+")
        if i % 2 == 0 and i != 0:
            print(Cursor.FORWARD(49) + Fore.WHITE + " " + "+" + "-" * 9 + "+" + "-" * 9 + "+")

        for j in range(len(tablero[0])):
            if j == 0:
                print(Cursor.FORWARD(45) + Fore.YELLOW, i + 1, " ", end="")
                print(Fore.WHITE + " |", end="")
            if j % 2 == 0 and j != 0:
                print(Fore.WHITE + " |", end="")

            if j == 3:
                print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")
                print(Fore.WHITE + " |", end="")
            else:
                if j == 0:
                    print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")
                else:
                    print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")

        if i == len(tablero) - 1:
            print("")
            print(Cursor.FORWARD(49) + Fore.WHITE + " " + "+" + "-" * 19 + "+")
def mostrarTablero_4x4_R(tablero, y, x):
    for i in range(len(tablero)):
        print("")
        if i == 0:
            print(Cursor.FORWARD(53) + Fore.YELLOW + "A" + " " * 3 + "B" + " " * 5 + "C" + " " * 3 + "D")
            print(Cursor.FORWARD(49) + Fore.WHITE + " " + "+" + "-" * 19 + "+")
        if i % 2 == 0 and i != 0:
            print(Cursor.FORWARD(49) + Fore.WHITE + " " + "+" + "-" * 9 + "+" + "-" * 9 + "+")

        for j in range(len(tablero[0])):
            if j == 0:
                print(Cursor.FORWARD(45) + Fore.YELLOW, i + 1, " ", end="")
                print(Fore.WHITE + " |", end="")
            if j % 2 == 0 and j != 0:
                print(Fore.WHITE + " |", end="")

            if y == i and x == j:
                if j == 3:
                    print(Fore.RED + " ", str(tablero[i][j]) + " ", end="")
                    print(Fore.WHITE + " |", end="")
                else:
                    print(Fore.RED + " ", str(tablero[i][j]) + " ", end="")
            else:
                if j == 3:
                    print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")
                    print(Fore.WHITE + " |", end="")
                else:
                    if j == 0:
                        print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")
                    else:
                        print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")

        if i == len(tablero) - 1:
            print("")
            print(Cursor.FORWARD(49) + Fore.WHITE + " " + "+" + "-" * 19 + "+")
def mostrarTablero_4x4_V(tablero, y, x):
    for i in range(len(tablero)):
        print("")
        if i == 0:
            print(Cursor.FORWARD(53) + Fore.YELLOW + "A" + " " * 3 + "B" + " " * 5 + "C" + " " * 3 + "D")
            print(Cursor.FORWARD(49) + Fore.WHITE + " " + "+" + "-" * 19 + "+")
        if i % 2 == 0 and i != 0:
            print(Cursor.FORWARD(49) + Fore.WHITE + " " + "+" + "-" * 9 + "+" + "-" * 9 + "+")

        for j in range(len(tablero[0])):
            if j == 0:
                print(Cursor.FORWARD(45) + Fore.YELLOW, i + 1, " ", end="")
                print(Fore.WHITE + " |", end="")
            if j % 2 == 0 and j != 0:
                print(Fore.WHITE + " |", end="")

            if y == i and x == j:
                if j == 3:
                    print(Fore.GREEN + " ", str(tablero[i][j]) + " ", end="")
                    print(Fore.WHITE + " |", end="")
                else:
                    print(Fore.GREEN + " ", str(tablero[i][j]) + " ", end="")
            else:
                if j == 3:
                    print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")
                    print(Fore.WHITE + " |", end="")
                else:
                    if j == 0:
                        print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")
                    else:
                        print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")

        if i == len(tablero) - 1:
            print("")
            print(Cursor.FORWARD(49) + Fore.WHITE + " " + "+" + "-" * 19 + "+")
def mostrarTablero_4x4_JC(tablero, lista):
    for i in range(len(tablero)):
        print("")
        if i == 0:
            print(Cursor.FORWARD(53) + Fore.YELLOW + "A" + " " * 3 + "B" + " " * 5 + "C" + " " * 3 + "D")
            print(Cursor.FORWARD(49) + Fore.WHITE + " " + "+" + "-" * 19 + "+")
        if i % 2 == 0 and i != 0:
            print(Cursor.FORWARD(49) + Fore.WHITE + " " + "+" + "-" * 9 + "+" + "-" * 9 + "+")

        for j in range(len(tablero[0])):
            if j == 0:
                print(Cursor.FORWARD(45) + Fore.YELLOW, i + 1, " ", end="")
                print(Fore.WHITE + " |", end="")
            if j % 2 == 0 and j != 0:
                print(Fore.WHITE + " |", end="")

            if j == 3:
                if [i, j] in lista:
                    print(Fore.CYAN + " ", str(tablero[i][j]) + " ", end="")
                    print(Fore.WHITE + " |", end="")
                else:
                    print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")
                    print(Fore.WHITE + " |", end="")
            else:
                if j == 0:
                    if [i, j] in lista:
                        print(Fore.CYAN + " ", str(tablero[i][j]) + " ", end="")
                    else:
                        print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")
                else:
                    if [i, j] in lista:
                        print(Fore.CYAN + " ", str(tablero[i][j]) + " ", end="")
                    else:
                        print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")

        if i == len(tablero) - 1:
            print("")
            print(Cursor.FORWARD(49) + Fore.WHITE + " " + "+" + "-" * 19 + "+")
def comprobar4x4(matriz, numero, y, x):
    for i in range(len(matriz)):
        if matriz[y][i] == numero:
            return False
    for i in range(len(matriz)):
        if matriz[i][x] == numero:
            return False
    x1 = (x // 2) * 2
    y1 = (y // 2) * 2
    for i in range(0, 2):
        for j in range(0, 2):
            if matriz[y1 + i][x1 + j] == numero:
                return False
def tableroaleatorio4x4(tablero):
    x = 0
    y = randint(10, 12)
    while x < y:
        a = randint(0, 3)
        b = randint(0, 3)
        w = tablero[a][b]
        if w == " ":
            x = x
        else:
            x = x + 1
        tablero[a][b] = " "

    return tablero


#FUNCIONES TABLERO 9X9

def mostrarTablero_9x9_(tablero):
        for i in range(len(tablero)):
            if i == 0:
                print(Cursor.FORWARD(
                    28) + Fore.YELLOW + "A" + " " * 3 + "B" + " " * 3 + "C" + " " * 5 + "D" + " " * 3 + "E" + " " * 3 + "F" + " " * 5 + "G" + " " * 3 + "H" + " " * 3 + "I")
                print(Cursor.FORWARD(24) + Fore.WHITE + " " + "+" + "-" * 41 + "+")
            if i % 3 == 0 and i != 0:
                print(Cursor.FORWARD(25) + Fore.WHITE + "+" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 13 + "+")

            for j in range(len(tablero[0])):
                if j == 0:
                    print(Cursor.FORWARD(20) + Fore.YELLOW, i + 1, " ", end="")
                    print(Fore.WHITE + " |", end="")
                if j % 3 == 0 and j != 0:
                    print(Fore.WHITE + " |", end="")

                if j == 8:
                    print(Fore.WHITE + " ", str(tablero[i][j]), end=" ")
                    print(Fore.WHITE + " |")
                else:
                    if j == 0:
                        print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")
                    else:
                        print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")
            if i == 8:
                print(Cursor.FORWARD(24) + Fore.WHITE + " " + "+" + "-" * 41 + "+")
def mostrarTablero_9x9_V(tablero, y, x):
    for i in range(len(tablero)):
        if i == 0:
            print(Cursor.FORWARD(
                28) + Fore.YELLOW + "A" + " " * 3 + "B" + " " * 3 + "C" + " " * 5 + "D" + " " * 3 + "E" + " " * 3 + "F" + " " * 5 + "G" + " " * 3 + "H" + " " * 3 + "I")
            print(Cursor.FORWARD(24) + Fore.WHITE + " " + "+" + "-" * 41 + "+")
        if i % 3 == 0 and i != 0:
            print(Cursor.FORWARD(25) + Fore.WHITE + "+" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 13 + "+")

        for j in range(len(tablero[0])):

            if j % 3 == 0 and j != 0:
                print(Fore.WHITE + " |", end="")
            if y == i and x == j:
                if j == 0:
                    print(Cursor.FORWARD(20) + Fore.YELLOW, i + 1, " ", end="")
                    print(Fore.WHITE + " |", end="")
                    print(Fore.GREEN + " ", str(tablero[i][j]) + " ", end="")
                else:
                    if j == 8:
                        print(Fore.GREEN + " ", str(tablero[i][j]) + " ", end="")
                        print(Fore.WHITE + " |")
                    else:
                        print(Fore.GREEN + " ", str(tablero[i][j]) + " ", end="")

            else:
                if j == 8:
                    print(Fore.WHITE + "  " + str(tablero[i][j]) + " ", end="")
                    print(Fore.WHITE + " |")
                else:
                    if j == 0:
                        print(Cursor.FORWARD(20) + Fore.YELLOW, i + 1, " ", end="")
                        print(Fore.WHITE + " |", end="")
                        print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")
                    else:
                        print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")

        if i == 8:
            print(Cursor.FORWARD(24) + Fore.WHITE + " " + "+" + "-" * 41 + "+")
def mostrarTablero_9x9_R(tablero, y, x):
    for i in range(len(tablero)):
        if i == 0:
            print(Cursor.FORWARD(
                28) + Fore.YELLOW + "A" + " " * 3 + "B" + " " * 3 + "C" + " " * 5 + "D" + " " * 3 + "E" + " " * 3 + "F" + " " * 5 + "G" + " " * 3 + "H" + " " * 3 + "I")
            print(Cursor.FORWARD(24) + Fore.WHITE + " " + "+" + "-" * 41 + "+")
        if i % 3 == 0 and i != 0:
            print(Cursor.FORWARD(25) + Fore.WHITE + "+" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 13 + "+")

        for j in range(len(tablero[0])):

            if j % 3 == 0 and j != 0:
                print(Fore.WHITE + " |", end="")
            if y == i and x == j:
                if j == 0:
                    print(Cursor.FORWARD(20) + Fore.YELLOW, i + 1, " ", end="")
                    print(Fore.WHITE + " |", end="")
                    print(Fore.RED + " ", str(tablero[i][j]) + " ", end="")
                else:
                    if j == 8:
                        print(Fore.RED + " ", str(tablero[i][j]) + " ", end="")
                        print(Fore.WHITE + " |")
                    else:
                        print(Fore.RED + " ", str(tablero[i][j]) + " ", end="")

            else:
                if j == 8:
                    print(Fore.WHITE + "  " + str(tablero[i][j]) + " ", end="")
                    print(Fore.WHITE + " |")
                else:
                    if j == 0:
                        print(Cursor.FORWARD(20) + Fore.YELLOW, i + 1, " ", end="")
                        print(Fore.WHITE + " |", end="")
                        print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")
                    else:
                        print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")

        if i == 8:
            print(Cursor.FORWARD(24) + Fore.WHITE + " " + "+" + "-" * 41 + "+")
def mostrarTablero_9x9_JC(tablero, lista):
    for i in range(len(tablero)):
        if i == 0:
            print(Cursor.FORWARD(
                28) + Fore.YELLOW + "A" + " " * 3 + "B" + " " * 3 + "C" + " " * 5 + "D" + " " * 3 + "E" + " " * 3 + "F" + " " * 5 + "G" + " " * 3 + "H" + " " * 3 + "I")
            print(Cursor.FORWARD(24) + Fore.WHITE + " " + "+" + "-" * 41 + "+")
        if i % 3 == 0 and i != 0:
            print(Cursor.FORWARD(25) + Fore.WHITE + "+" + "-" * 13 + "+" + "-" * 13 + "+" + "-" * 13 + "+")

        for j in range(len(tablero[0])):
            if j == 0:
                print(Cursor.FORWARD(20) + Fore.YELLOW, i + 1, " ", end="")
                print(Fore.WHITE + " |", end="")
            if j % 3 == 0 and j != 0:
                print(Fore.WHITE + " |", end="")

            if j == 8:
                if [i, j] in lista:
                    print(Fore.CYAN + " ", str(tablero[i][j]) + " ", end="")
                    print(Fore.WHITE + " |", end="")
                else:
                    print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")
                    print(Fore.WHITE + " |")
            else:
                if j == 0:
                    if [i, j] in lista:
                        print(Fore.CYAN + " ", str(tablero[i][j]) + " ", end="")
                    else:
                        if [i, j] in lista:
                            print(Fore.CYAN + " ", str(tablero[i][j]) + " ", end="")
                        else:
                            print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")
                else:
                    if [i, j] in lista:
                        print(Fore.CYAN + " ", str(tablero[i][j]) + " ", end="")
                    else:
                        print(Fore.WHITE + " ", str(tablero[i][j]) + " ", end="")
        if i == 8:
            print(Cursor.FORWARD(24) + Fore.WHITE + " " + "+" + "-" * 41 + "+")
def comprobar9x9(matriz, numero, y, x):
    for i in range(len(matriz)):
        if matriz[y][i] == numero:
            return False
    for i in range(len(matriz)):
        if matriz[i][x] == numero:
            return False
    x1 = (x // 3) * 3
    y1 = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if matriz[y1 + i][x1 + j] == numero:
                return False
def tableroaleatorio9x9(tablero):
    x = 0
    y = randint(45, 50)
    while x < y:
        a = randint(0, 8)
        b = randint(0, 8)
        w = tablero[a][b]
        if w == " ":
            x = x
        else:
            x = x + 1
        tablero[a][b] = " "

    return tablero


#REPOSITORIOS TABLEROS

#1. 4X4
d4 = {1:[[1,4,3,2],[3,2,1,4],[4,3,2,1],[2,1,4,3]],2:[[2,3,4,1],[4,1,3,2], [1,4,2,3],[3,2,1,4]],3:[[3,2,4,1],[1,4,2,3],[2,1,3,4],[4,3,1,2]],4: [[1,3,2,4],[2,4,1,3],[4,1,3,2],  [3,2,4,1]],5:[[1,2,3,4],[3,4,1,2], [2,1,4,3], [4,3,2,1]]
,6:[[2,3,1,4], [4,1,3,2],[3,2,4,1],[1,4,2,3]],7:[[2,3,1,4],[4,1,2,3],[1,4,3,2],[3,2,4,1]],8:[ [1,3,4,2],[2,4,3,1], [4,2,1,3], [3,1,2,4]],9:[ [1,4,3,2], [3,2,1,4],[2,3,4,1],[4,1,2,3]],10:[[2,3,1,4],[4,1,2,3],[1,4,3,2],[3,2,4,1]],
11:[[3,4,1,2],[2,1,4,3],[1,3,2,4],[4,2,3,1]],12: [[1,4,3,2], [2,3,4,1], [3,2,1,4],[4,1,2,3]],13:[ [3,4,1,2],[1,2,3,4], [2,1,4,3], [4,3,2,1]],14:[[2,3,4,1],[4,1,2,3],[1,4,3,2],[3,2,1,4]],15:[ [1,2,3,4], [3,4,1,2], [4,1,2,3], [2,3,4,1]],
16:[[3,4,2,1], [1,2,3,4],[4,3,1,2],[2,1,4,3]],17:[ [1,2,3,4],[3,4,1,2],[4,3,2,1], [2,1,4,3]],18:[[1,3,4,2], [4,2,1,3], [2,4,3,1], [3,1,2,4]],19:[ [4,1,3,2], [3,2,4,1], [1,4,2,3], [2,3,1,4]],20: [[3,4,1,2], [1,2,3,4], [4,1,2,3], [2,3,4,1]]}


#2. 9X9
d9 = {1:[[5,3,4,6,7,8,9,1,2],[6,7,2,1,9,5,3,4,8],[1,9,8,3,4,2,5,6,7],[8,5,9,7,6,1,4,2,3],[4,2,6,8,5,3,7,9,1],
    [7,1,3,9,2,4,8,5,6],[9,6,1,5,3,7,2,8,4],[2,8,7,4,1,9,6,3,5],[3,4,5,1,8,6,1,7,9]],2:[[9,6,3,1,7,4,2,5,8],
    [1,7,8,3,2,5,6,4,9],[2,5,4,6,8,9,7,3,1],[8,2,1,4,3,7,5,9,6],[4,9,6,8,5,2,3,1,7],[7,3,5,9,6,1,8,2,4],
    [5,8,9,7,1,3,4,6,2],[3,1,7,2,4,6,9,8,5],[6,4,2,5,9,8,1,7,3]],3:[[1,5,6,8,3,7,2,9,4],[9,2,4,1,6,5,7,3,8],
    [7,8,3,4,9,2,5,6,1],[2,7,5,3,4,6,8,1,9],[6,4,1,9,2,8,3,5,7],[3,9,8,5,7,1,6,4,2],[4,1,2,6,8,3,9,7,5],
    [5,6,7,2,1,9,4,8,3],[8,3,9,7,5,4,1,2,6]],4: [[9,4,5,2,7,1,8,3,6],[8,1,6,3,9,5,4,2,7],[7,3,2,6,8,4,5,1,9],
    [2,5,8,4,6,7,3,9,1],[6,9,4,1,3,8,7,5,2],[3,7,1,5,2,9,6,4,8],[4,6,7,9,5,2,1,8,3],[1,2,3,8,4,6,9,7,5],
    [5,8,9,7,1,3,2,6,4]],5:[[1,2,3,4,6,9,7,5,8],[8,4,6,5,7,1,2,9,3],[9,5,7,2,8,3,6,4,1],[3,1,2,7,5,8,4,6,9],
    [4,6,8,3,9,2,1,7,5],[5,7,9,1,4,6,8,3,2],[2,3,4,6,1,5,9,8,7],[6,8,1,9,3,7,5,2,4],[7,9,5,8,2,4,3,1,6]],6: [
    [2,1,9,5,4,3,6,7,8],[5,4,3,8,7,6,9,1,2],[8,7,6,2,1,9,3,4,5],[4,3,2,7,6,5,8,9,1],[7,6,5,1,9,8,2,3,4],
    [1,9,8,4,3,2,5,6,7],[3,2,1,6,5,4,7,8,9],[6,5,4,9,8,7,1,2,3],[9,8,7,3,2,1,4,5,6]],7:[[7,8,6,2,5,4,1,9,3],
    [1,2,4,9,8,3,7,6,5],[9,5,3,6,1,7,4,2,8],[8,3,5,1,4,9,2,7,6],[6,1,7,3,2,8,9,5,4],[2,4,9,7,6,5,8,3,1],
    [3,6,2,4,9,1,5,8,7],[4,7,8,5,3,2,6,1,9],[5,9,1,8,7,6,3,4,2]],8:[[4,1,5,3,7,8,2,9,6],[2,3,7,1,6,9,4,8,5],
    [6,8,8,4,2,5,7,3,1],[8,9,3,7,5,1,6,2,4],[5,7,4,2,3,6,9,1,8],[1,6,2,9,8,4,3,5,7],[9,2,8,6,1,7,5,4,3],
    [7,4,1,5,9,3,8,6,2],[3,5,6,8,4,2,1,7,9]],9:[[2,7,1,5,6,4,8,3,9],[9,3,8,1,7,2,4,6,5],[6,4,5,3,9,8,1,2,7],
    [8,2,9,4,5,7,6,1,3],[5,6,4,9,3,1,7,8,2],[7,1,3,8,2,6,5,9,4],[3,8,7,2,1,5,9,4,6],[4,9,6,7,8,3,2,5,1],
    [1,5,2,6,4,9,3,7,8]],10:[[7,5,2,4,9,6,1,3,8],[3,9,1,2,5,8,4,6,7],[4,8,6,7,3,1,9,5,2],[8,3,9,6,7,5,2,1,4],
    [1,2,4,9,8,3,5,7,6],[6,7,5,1,4,2,8,9,3],[5,4,7,3,2,9,6,8,1],[2,6,8,5,1,7,3,4,9],[9,1,3,8,6,4,7,2,5]], 11:[
    [3,9,7,2,8,6,5,4,1],[4,1,2,5,3,9,7,6,8],[8,5,6,4,7,1,3,2,9],[2,8,4,1,9,5,6,3,7],[6,3,9,7,4,8,2,1,5],
    [5,7,1,3,6,2,8,9,4],[7,2,8,9,1,3,4,5,6],[1,6,3,8,5,4,9,7,2],[9,4,5,6,2,7,1,8,3]], 12:[[5,3,9,1,4,6,8,7,2],
    [8,4,7,9,2,5,3,1,6],[2,6,1,3,7,8,9,5,4],[6,7,5,4,8,1,2,9,3],[9,1,2,6,3,7,5,4,8],[4,8,3,5,9,2,7,6,1],
    [3,2,6,7,1,9,4,8,5],[7,5,8,2,6,4,1,3,9],[1,9,4,8,5,3,6,2,7]],13:[[7,9,2,1,5,4,3,8,6],[6,4,3,8,2,7,1,5,9],
    [8,5,1,3,9,6,7,2,4],[2,6,5,9,7,3,8,4,1],[4,8,9,5,6,1,2,7,3],[3,1,7,4,8,2,9,6,5],[1,3,6,7,4,8,5,9,2],
    [9,7,4,2,1,5,6,3,8],[5,2,8,6,3,9,4,1,7]],14: [[1,8,4,6,9,3,7,5,2],[2,5,7,8,1,4,3,9,6],[6,9,3,5,7,2,8,4,1],
    [5,7,1,4,2,8,9,6,3],[8,2,6,1,3,9,5,7,4],[4,3,9,7,6,5,2,1,8],[9,4,8,3,5,6,1,2,7],[7,6,2,9,8,1,4,3,5],
    [3,1,5,2,4,7,6,8,9]], 15:[[4,9,2,7,8,6,1,3,5],[7,1,3,5,9,4,6,2,8],[6,5,8,3,1,2,7,4,9],[8,6,7,2,5,3,4,9,1],
    [2,3,9,4,7,1,5,8,6],[5,4,1,8,6,9,2,7,3],[1,2,4,9,3,5,8,6,7],[9,8,6,1,4,7,3,5,2],[3,7,5,6,2,8,9,1,4]],16: [
    [8,7,6,4,9,3,2,5,1],[3,4,5,7,1,2,9,6,8],[2,9,1,5,6,8,4,7,3],[9,8,2,1,3,5,7,4,6],[7,5,4,8,2,6,3,1,9],
    [1,6,3,9,4,7,8,2,5],[4,1,7,3,5,9,6,8,2],[6,3,8,2,7,1,5,9,4],[5,2,9,6,8,4,1,3,7]],17:[[1,6,5,8,4,7,9,2,3],
    [7,8,9,3,1,2,5,4,6],[4,3,2,5,9,6,1,7,8],[2,9,7,4,6,3,8,5,1],[5,1,8,7,2,9,3,6,4],[3,4,6,1,5,8,2,9,7],
    [9,7,3,2,8,4,6,1,5],[8,2,1,6,7,5,4,3,9],[6,5,4,9,3,1,7,8,2]],18: [[2,1,5,3,7,9,8,6,4],[9,8,6,1,2,4,3,5,7],
    [7,3,4,8,5,6,2,1,9],[4,5,2,7,8,1,6,9,3],[8,6,9,5,4,3,1,7,2],[3,7,1,6,9,2,4,8,5],[5,2,7,4,1,8,9,3,6],
    [6,4,8,9,3,7,5,2,1],[1,9,3,2,6,5,7,4,8]],19: [[8,1,2,7,5,3,6,4,9],[9,4,3,6,8,2,1,7,5],[6,7,5,4,9,1,2,8,3],
    [1,5,4,2,4,7,8,9,6],[3,6,9,8,4,5,7,2,1],[2,8,7,1,6,9,5,3,4],[5,2,1,9,7,4,3,6,8],[4,3,8,5,2,6,9,1,7],
    [7,9,6,3,1,8,4,5,2]],20: [[5,4,8,9,6,3,2,7,1],[7,9,6,5,2,1,8,4,3],[2,3,1,7,8,4,5,6,9],[4,2,5,3,1,6,7,9,8],
    [3,1,7,2,9,8,6,5,4],[6,8,9,4,5,7,3,1,2],[9,5,4,6,3,2,1,8,7],[8,7,2,1,4,5,9,3,6],[1,6,3,8,7,9,4,2,5]]}
