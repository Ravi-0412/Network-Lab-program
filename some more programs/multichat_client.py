import threading
import socket

host = '127.0.0.1'
port = 5559
nickname = input("Enter your name: ")

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((socket.gethostname(),port))

def recieve():
	try:
		message = client.recv(1024).encode()
		if message == 'Nick':  # means client has to send the nickname
			client.send(nickname.encode())
		else :
			print(message)
	except:
		print("An error Occured!")
		client.close()
        # break
		
def write():
	message = f'{nickname}: {input("")}' 
	client.send(message.encode())
	
recieve_thread = threading.Thread(target = recieve)
recieve_thread.start()

write_thread = threading.Thread(target = write)
write_thread.start()
