import threading
import socket

pedido = []


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(("localhost", 1236))
        server.listen()
    except:
        return print('\n O servidor nao pode ser acessado \n')

    while True:
        client, addr = server.accept()
        thread = threading.Thread(target=PedidoFeito, args=[client])
        thread.start()



def PedidoFeito(cliente):
    while True:
        try:
            msg = cliente.recv(2048)
            pedido.append(eval(msg.decode('utf-8')))
            print(pedido)
        except:
            break


main()