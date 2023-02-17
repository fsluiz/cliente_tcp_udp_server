import socket # chama api soket inteface entre placa de rede e os
import sys #

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e: 
        print("A conexão falhou!")
        print("Erro: {}".format(e)) #imprime o erro
        sys.exit()#sai da aplicação
    
    print("Socket criado com sucesso")

    HostAlvo = input("Digite o Host ou Ip a ser conectado: ")
    PortaAlvo = input("Digite a porta a ser conectada: ")

    try:
        s.connect((HostAlvo, int(PortaAlvo))) #faz a conexão
        print("Cliente TCP conectado com Sucesso no Host: " + HostAlvo + " e na porta " + PortaAlvo)
        s.shutdown(2)

    execpt socket.error as e
        print("Não foi possivel conectar no Host: " + HostAlvo + " - Porta: " + PortaAlva)
        print("Erro: {}".format(e))
        sys.exit()

if __name__=="__main__":
    main()