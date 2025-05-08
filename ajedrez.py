""" 
Ajedrez en Python
Este es un programa simple de ajedrez en Python.
El tablero es representado como una matriz 8x8
y cada pieza representada por su simbolo en unicode.

El programa permite una partida entre dos jugadores,
donde cada jugador puede mover sus piezas de acuerdo a las reglas del ajedrez.
aun falta implementar el jaque, el enroque, el ahogado, y el evitar que las piezas 
que no sean caballos puedan saltar sobre otras piezas. 

La partida se juega desde la consola, ya que no cuenta con interfaz grafica.    
"""
# Iniciamos el tablero.
Tablero=[
    ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],
    [f"♙" for i in range(8)],
    ["    " for _ in range(8)],
    ["    " for _ in range(8)],
    ["    " for _ in range(8)],
    ["    " for _ in range(8)],
    [f"♟" for i in range(8)],
    ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]
    ]
# Definimos las piezas blancas y negras
piezas_blancas = ["♖", "♘", "♗", "♕", "♔", "♙"]
piezas_negras = ["♜", "♞", "♝", "♛", "♚", "♟"]
Move_list=[]    # Lista para guardar los movimientos y mostrarlos al final
Turnos= 1    # Contador de turnos

def promocion(pieza, c, d): # Cambia la pieza de peón a otra pieza elegida por el jugador
    print("¡Promoción de peón!")
    print("Elige la pieza a la que deseas promover:")
    print("1. Reina.")
    print("2. Torre.")
    print("3. Alfil.")
    print("4. Caballo.")
    while True:
        opcion = input("Opción: ")
        if opcion == "1":
            Tablero[d][c] = "♕" if pieza == "♙" else "♛"
            pieza = Tablero[d][c]
            break
        elif opcion == "2":
            Tablero[d][c] = "♖" if pieza == "♙" else "♜"
            pieza = Tablero[d][c]
            break
        elif opcion == "3":
            Tablero[d][c] = "♗" if pieza == "♙" else "♝"
            pieza = Tablero[d][c]
            break
        elif opcion == "4":
            Tablero[d][c] = "♘" if pieza == "♙" else "♞"
            pieza = Tablero[d][c]
            break
        else:
            print("Opción inválida. Elija un numero del 1 al 4.")

def mov_valido(pieza, a, b, c, d, destino): # Verifica si el movimiento es valido
    #Peones
    if pieza == "♙":
        if (a == c and b==1) and (d==b+1 or d==b+2) and destino == "    ":
            return True
        elif a == c and d == b + 1 and destino == "    ":
            return True
        elif (c==(a+1) or c==(a-1)) and d==b+1 and destino != "    ":                
            return True
        else:
            return False
    elif pieza == "♟":
        if (a == c and b==6) and (d==b-1 or d==b-2) and destino == "    ":
            return True
        elif a == c and d == b - 1 and destino == "    ":
            return True
        elif (c==(a+1) or c==(a-1)) and d==b-1 and destino != "    ":                
            return True
        else:
            return False
    #Torres 
    if pieza == "♖" or pieza == "♜":
        if a==c and b!=d:
            return True
        elif b==d and a!=c:
            return True
        else:
            return False
    #Caballos
    if pieza == "♘" or pieza == "♞":
        if (abs(a-c)==2 and abs(b-d)==1) or (abs(a-c)==1 and abs(b-d)==2):
            return True
        else:
            return False
    #Alfiles
    if pieza == "♗" or pieza == "♝":
        if abs(a-c)==abs(b-d):
            return True
        else:
            return False
    #Reinas
    if pieza == "♕" or pieza == "♛":
        if a==c and b!=d:
            return True
        elif b==d and a!=c:
            return True
        elif abs(a-c)==abs(b-d):
            return True
        else:
            return False
    #Reyes
    if pieza == "♔" or pieza == "♚":
        if abs(a-c)<=1 and abs(b-d)<=1:
            return True
        else:
            return False
    
def Mov(a,b,c,d,T): # Función para mover las piezas
    mov=a.upper()+b.upper()+"-"+c.upper()+d.upper()   
    a = ord(a.upper()) - ord('A')
    c = ord(c.upper()) - ord('A')

    b = int(b)-1
    d = int(d)-1
    if(a < 0 or a > 7) or (b < 0 or b > 7) or (c < 0 or c > 7) or (d < 0 or d > 7):
        print("¡Movimiento fuera de rango!")
        return T

    pieza = Tablero[b][a]
    if pieza == "    ":
        print("¡No hay pieza en esa posición!")
        return T
    
    if Turnos % 2 == 1:
        if pieza not in piezas_blancas:
            print("¡No puedes mover piezas negras en el turno de blancas!")
            return T
    else:
        if pieza not in piezas_negras:
            print("¡No puedes mover piezas blancas en el turno de negras!")
            return T
        
    if mov_valido(pieza, a, b, c, d, Tablero[d][c]):
        if Tablero[d][c] in piezas_blancas and Turnos % 2 == 1:
            print("¡No puedes comer tu propia pieza!")
            return T
        
        elif Tablero[d][c] in piezas_negras and Turnos % 2 == 0:
            print("¡No puedes comer tu propia pieza!")
            return T
        
        else:
            if (pieza == "♙" and d == 0) or (pieza == "♟" and d == 7):
                promocion(pieza, c, d)
            Move_list.append(mov)    
            Tablero[d][c] = pieza
            Tablero[b][a] = "    "
            return T+1
    else:
        print("¡Movimiento inválido!")
        return T
    
def show_tablero(): # Función para mostrar el tablero
    print("    " + "+------" * 8 + "+")
    for i in range(8):
        print(f" {8 - i} ", end=" |")
        for j in range(8):
            print(f" {Tablero[7 - i][j]:^4} |", end="")
        print()
        print("    " + "+------" * 8 + "+")
    print("     ", end="")
    for letra in "ABCDEFGH":
        print(f"  {letra}    ", end="")
    print("\n")

show_tablero()

print('\nIngrese su movimiento de manera que quede claro \nla casilla de inicio de la pieza y la casilla final\n(Ej.: E2-E4) \n')

while True:    
    print(f"Turno N°{Turnos}")
    if Turnos%2==1:
        print("Turno de las blancas: ")
    else:
        print("Turno de las negras: ")
    Move= input()
    Turnos=Mov(Move[0],Move[1],Move[3],Move[4], Turnos)
    
    show_tablero()
    
    piezas = sum(Tablero, [])  
    if "♔" not in piezas:
        print("¡Las negras han ganado!")
        for i in range(len(Move_list)):
            print(f"Turno N°{i+1}: " , Move_list[i])
        break
    elif "♚" not in piezas:
        print("¡Las blancas han ganado!")
        for i in range(len(Move_list)):
            print(f"Turno N°{i+1}: " , Move_list[i])
        break
    