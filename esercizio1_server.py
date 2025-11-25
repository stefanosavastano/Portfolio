import socket
import threading

def calcola_operazione(op, a, b):
    try:
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
    except Exception as e:
        return f"Errore: {e}"

def gestisci_client(conn, addr):
    print(f"Connessione da {addr}")
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        parti = data.split()
        if len(parti) == 3:
            op, a, b = parti
            risultato = calcola_operazione(op, a, b)
        else:
            risultato = "Formato non valido. Usa: op num1 num2"
        conn.sendall(risultato.encode())
    conn.close()

def server():
    HOST = "127.0.0.1"
    PORT = 65432
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print("Server in ascolto...")
    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=gestisci_client, args=(conn, addr))
        t.start()

if __name__ == "__main__":
    server()