import threading
import socket


def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect(('localhost', 1236))
    except:
        return print('\n Nao foi possvel acessar o servidor\n')

    atendente = input("Digite o Usuario")


    print('\n Logado')

    thread1 = threading.Thread(target=receberPedido, args=[cliente])
    thread2 = threading.Thread(target=enviarPedido, args=[cliente, atendente])

    thread1.start()
    thread2.start()


def receberPedido(cliente):
    while True:
        try:
            msg = cliente.recv(2048).decode('utf-8')
            print(msg + '\n')
        except:
            print("\n Voce foi deslogado do sevridor \n")
            print("Pressione enter para continuar")
            cliente.close()
            break


def enviarPedido(cliente, atendente):
    while True:
        try:
            NomeCliente = input('Digite o nome de quem efetuou o pedido: \n')
            Comida = input('Digite o que foi pedido pelo cliente: \n')
            Mesa = int(input('Digite o numero da mesa do cliente: \n'))
            pedido = ["Atendente: "+atendente ,"Cliente: "+NomeCliente,"Comida: "+Comida,"Numero da mesa: "+str(Mesa)]
            msg = pedido
            cliente.send(f'{msg}'.encode('utf-8'))
        except:
            return


main()