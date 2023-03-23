import socket

HOST = "127.0.0.1"
PORT = 65432
buffer_size = 1024
matriz = ""


def matriz_inicial(tam):
    if tam == "0":
        tama = 4
    elif tam == "1":
        tama = 6
    elif tam == "2":
        tama = 9
    matriz = [['' for j in range(tama)] for i in range(tama)]
    i = 0
    for i in range(tama):
        j = 0
        for j in range(tama):
            matriz[i][j] = "-"
            print(matriz[i][j], end=" ")
        print()
    return matriz


def imprimir_matriz(fila, col, valor, tam, matriz):
    if tam == "0":
        tama = 4
    elif tam == "1":
        tama = 6
    elif tam == "2":
        tama = 9
    matriz[fila][col] = valor
    for i in range(tama):
        j = 0
        for j in range(tama):
            print(matriz[i][j], end=" ")
        print()


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT))
    intentar = 0
    while intentar == 0:
        print("Selccionar dificultad:\n"
              "0.Fácil\n"
              "1.Intermedio\n"
              "2.Dificil\n"
              "Entrada:", end=" ")
        data = input()
        TCPClientSocket.sendall(bytes(data, "utf-8"))
        print(str(TCPClientSocket.recv(buffer_size), "utf-8", "<end>"))
        # print(str(TCPClientSocket.recv(buffer_size), "utf-8", "<end>"))
        print(str(TCPClientSocket.recv(buffer_size), "utf-8", "<end>"))
        bandera = 0
        mina = ""
        valor = ""
        print("Ingresar columna y fila donde no haya mina:\n"
              "ej. 2,2\n")
        matriz = matriz_inicial(data)
        while bandera == 0:
            punto = input("fila, columna:")
            fila = int(punto[0])
            col = int(punto[2])
            TCPClientSocket.sendall(bytes(punto, "utf-8"))
            mina = str(TCPClientSocket.recv(buffer_size), "utf-8")
            print(mina)
            if mina == "X":
                bandera = 1
                valor = "X"
                print("Perdiste :( \nPisaste una mina X(")
            elif mina == "Gano":
                print("Ganaste :)")
                bandera = 1
            elif int(mina) >= 0:
                bandera = 0
                valor = "0"
                print("Muy bien, no pisaste una mina")
                print(mina)
            imprimir_matriz(fila, col, valor, data, matriz)
        volver = input("Quieres volver a intentarlo? Si o No: ")
        if volver == "Si" or volver == "si":
            intentar = 0
        elif volver == "No" or volver == "no":
            intentar = 1
