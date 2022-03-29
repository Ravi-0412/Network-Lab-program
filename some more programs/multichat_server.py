import threading
import socket

port= 5559

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), port))
server.listen()

clients= [] 
nicknames= []

def broadcast(message):
    for client in clients:
        client.send(message)
    
def handle(client):
    while True:
        try:  #as long as client doesn't give any exceptional error
            message= client.recv(1024)
            broadcast(message)   # after receiving the message broadcast this message
                                # to all other clients
        except:  # if get any error then remove that client and terminate the conn with that client
            index= clients.index(client)
            clients.remove(client)
            client.close()
            nickname= nicknames[index]  # also remove the nickname of that client
            # boradacast to all that somenone has left
            broadcast(f'(nickname) left the chat!'.encode())
             # also remove the nickname of that client
            nicknames.remove(nickname)
            break

def recieve():
    client,address = server.accept()
    print(f'Connected to the {str(address)}')
    client.send("Nick".encode())   # 'nick' will tell client to send their nickname
    nickname = client.recv(1024).decode()
    clients.append(client)
    nicknames.append(nickname)
    print(f'nickname of the client is : {nickname}!')
    broadcast(f'{nickname} joined the chat'.encode())
    client.send('connected to the server!'.encode())

    thread = threading.thread(target =  handle, args = (client,))  # one thread for eac client
    thread.start()

print("server is listening....")
recieve()


