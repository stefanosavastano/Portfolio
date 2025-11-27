import socket
import tkinter as tk



def client(richiesta):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(("127.0.0.1", 65432))  # stesso host e porta del server
        client.sendall(richiesta.encode())
        risposta = client.recv(1024).decode()
        client.close()
        risultato_label.config(text=f"Risultato: {risposta}")


def invia_richiesta():
        op = operazione.get()
        a = entry_a.get()
        b = entry_b.get()
        richiesta = f"{op} {a} {b}"
        client(richiesta)
      

# Interfaccia grafica
root = tk.Tk()
root.title("Client Calcolatrice")

tk.Label(root, text="Numero A:").grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)

tk.Label(root, text="Numero B:").grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)

tk.Label(root, text="Operazione:").grid(row=2, column=0)
operazione = tk.StringVar(value="add")
tk.OptionMenu(root, operazione, "add", "sub", "mul", "div").grid(row=2, column=1)

tk.Button(root, text="Calcola", command=invia_richiesta).grid(row=3, column=0, columnspan=2)

risultato_label = tk.Label(root, text="Risultato: ")
risultato_label.grid(row=4, column=0, columnspan=2)

root.mainloop()