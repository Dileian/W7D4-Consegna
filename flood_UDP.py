File Edit Options Buffers Tools Python Help                                                                         
import socket
import random

def crea_socket(): #Crea e restituisce un socket UDP                                                                
    return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def dati_input():
    ip_target = input("Inserisci IP target: ")
    porta_target = int(input("Inserisci la porta target: "))
    numero_pacchetti = int(input("Quanti pacchetti vuoi inviare? "))
    return ip_target, porta_target, numero_pacchetti

def invio_pacchetti(sock, ip_target, porta_target, numero_pacchetti):
    pacchetto = random.randbytes(1024) #Crea un pacchetto di 1 KB usando bytes casuali                              
    print("Inizio invio dei pacchetti...")
  
    for _ in range(numero_pacchetti): #Ripete il blocco n volte quanti sono i pacchetti che l'utente decide di inviare
        try: #Tenta di inviare un pacchetto di dati                                                                 
            sock.sendto(pacchetto, (ip_target, porta_target))
        except Exception as e: #Stampa eventuale errore se ci sono problemi nell'invio                              
            print(f"Errore durante l'invio dei pacchetti: {e}")
    print("Invio pacchetti completato.")

def main():
    sock = crea_socket()
    ip_target, porta_target, numero_pacchetti = dati_input()
    invio_pacchetti(sock, ip_target, porta_target, numero_pacchetti)
    sock.close()

if __name__ == "__main__":
    main()

