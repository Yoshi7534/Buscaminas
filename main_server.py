import socket
import random

HOST = "127.0.0.1"
PORT = 65432
buffer_size = 1024


def colocar_numeros(tam,matriz):
    i = 0
    for i in range(tam):
        j = 0
        for j in range(tam):
            pass


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TPCServerSocket:
    TPCServerSocket.bind((HOST, PORT))
    TPCServerSocket.listen()
    print("El servidor TCP está disponible y en espera de solicitudes.")

    Client_conn, Client_addr = TPCServerSocket.accept()
    with Client_conn:
        print("Conectado a", Client_addr)
        while True:
            print("Esperando a recibir la dificultad...")
            data = str(Client_conn.recv(buffer_size), "utf-8")
            print("Recibi la dificultad:"+ data, end="\n")
            if not data:
                break
            elif data == "0":  # facil
                tam = "4"
                matriz = [['' for j in range(4)] for i in range(4)]  # inicializar matriz de 4 x 4 con 9 minas
                minas = 0
                casillas_vacias = 0
                i = 0
                for i in range(4):
                    j = 0
                    for j in range(4):
                        num = random.randint(0, 1)
                        if num == 1 and minas < 9:
                            matriz[i][j] = "X"
                            minas += 1
                        elif 0 == num:
                            matriz[i][j] = str(num)
                            casillas_vacias += 1
                        elif num == 1 and minas >= 9:
                            num = 0
                            casillas_vacias += 1
                            matriz[i][j] = str(num)
                        print(matriz[i][j], end=" ")
                    print()
            elif data == "1":  # medio
                tam = "6"
                matriz = [['' for j in range(6)] for i in range(6)]  # inicializar matriz de 6 x 6 con 15
                minas = 0
                casillas_vacias = 0
                i = 0
                for i in range(6):
                    j = 0
                    for j in range(6):
                        num = random.randint(0, 1)
                        if num == 1 and minas < 15:
                            matriz[i][j] = "X"
                            minas += 1
                        elif 0 <= num <= 8:
                            matriz[i][j] = str(num)
                            casillas_vacias += 1
                        elif num == 1 and minas >= 15:
                            num = 0
                            casillas_vacias += 1
                            matriz[i][j] = str(num)
                        print(matriz[i][j], end=" ")
                    print()
            elif data == "2":  # dificil
                tam = "9"
                matriz = [['' for j in range(9)] for i in range(9)]  # inicializar matriz de 9 x 9 con 40 minas
                minas = 0
                casillas_vacias =0
                i = 0
                for i in range(9):
                    j = 0
                    for j in range(9):
                        num = random.randint(0, 1)
                        if num == 1 and minas < 40:
                            matriz[i][j] = "X"
                            minas += 1
                        elif 0 <= num <= 8:
                            matriz[i][j] = str(num)
                            casillas_vacias += 1
                        elif num == 1 and minas >= 40:
                            num = 0
                            casillas_vacias += 1
                            matriz[i][j] = str(num)
                        print(matriz[i][j], end=" ")
                    print()
            else:
                print("El caracter ingresado no es valido")
                Client_conn.sendall(bytes("No valido", "utf-8"))
                break
            Client_conn.sendall(bytes("Juego iniciado", "utf-8"))
            # Client_conn.sendall(bytes(tam, "utf-8"))
            Client_conn.sendall(bytes("Por favor ingrese donde no hay una mina", "utf-8"))
            bandera = 0
            bomba = ""
            while bandera == 0 and casillas_vacias > 0:
                respuesta = str(Client_conn.recv(buffer_size), "utf-8")
                if respuesta == "salir":
                    break
                fil = int(respuesta[0])
                col = int(respuesta[2])
                if matriz[fil][col] == "X":
                    print("Piso una mina, se acaba el juego :(")
                    bomba = "X"
                    bandera = 1
                    casillas_vacias = -1
                elif matriz[fil][col] == "0":
                    print("No piso nada, sigue...")
                    bomba = matriz[fil][col]
                    bandera = 0
                    casillas_vacias -= 1

                if casillas_vacias == 0:
                    print("Gano :)")
                    Client_conn.sendall(bytes("Gano", "utf-8"))
                elif casillas_vacias == -1:
                    Client_conn.sendall(bytes("X","utf-8"))
                else:
                    c_v = str(casillas_vacias)
                    Client_conn.sendall(bytes(c_v, "utf-8"))