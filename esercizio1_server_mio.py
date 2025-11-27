import socket
import threading

def calcola_operazione(op, a, b):
    a, b = float(a), float(b)
    if op == "add":
        return str(a + b)
    elif op == "sub":
        return str(a - b)
    elif op == "mul":
        return str(a * b)
    elif op == "div":
        if b == 0:
            return "Errore: divisione per zero"
        return str(a / b)
    else:
        return "Operazione non riconosciuta"


def ricevi_calcola(conn):
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        parti = data.split()
        op, a, b = parti
        risultato = calcola_operazione(op, a, b)
        conn.sendall(risultato.encode())
    conn.close()

def server():
    HOST = "127.0.0.1"
    PORT = 65432
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=ricevi_calcola, args=(conn,))
        t.start()


TT=threading.Thread(target=server)
TT.daemon=True
TT.start()

# while True:
#     pass

input("Premi INVIO per chiudere il server...")