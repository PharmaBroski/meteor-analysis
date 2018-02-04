import socket
import sys
from _thread import *

host = ''
port = 5555
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



try:
	socket.bind((host, port))
except socket.error as e:
	print(str(e)) #error handling

socket.listen(5)
print('Waiting for a connection.')
def threaded_client(conn):
	ref = 0 #this ref variable keeps track of the user's progress through the terminal interface
	conn.send(str.encode('Welcome, to proceed please enter your password\nPassword: '))

	while True:
		data = conn.recv(2048) #2048 is buffer rate
		reply = "Command not recognized. Type 'help' if you need assistance\n"

		#PASSWORD PROTECTION#
		#	ONCE A USER CONNECTS TO THE SERVER, THEY WILL BE PROMPTED TO ENTER IN A PASSWORD.
		#	THE USER CAN ONLY ACCESS FEATURES ONCE THE CORRECT PASSWORD IS ENTERED
		if data == b'research\r\n' and ref == 0: #(utf-8 encoding)
			reply = "SERVER: You now have access to this server. Type 'help' for assistance or 'exit' to end this session\n"
			ref = 1
		if data != b'research\r\n' and ref == 0: #(utf-8 encoding)
			#if password is incorrect
			reply = "SERVER: Password incorrect.\nPassword: "
			ref = 0

		#HELP HANDLING
		#	IF THE USER TYPES IN 'help' INTO THE TERMINAL, A SERIES OF COMMANDS AND THEIR FUNCTIONS WILL BE DISPLAYED
		#	THE HELP SCREEN CAN ONLY BE ACCESSED IF THE USER DOES NOT
		if data == b'help\r\n' and ref != 0:
			reply = "SERVER: The following commands are available for your use:\n	start-detector:		can be entered to start the motion detector on the host machine\n"

		#EXIT HANDLING
		#	IF THE USER TYPES 'exit' THEIR SESSION WILL END.
		if data == b'exit\r\n': #(utf-8 encoding)
			reply = "SERVER: Session ending\n"
			conn.close()

		#RUN MOTION DETECTOR FROM TERMINAL
		if data == b'start-detector\r\n' and ref != 0:
			reply = "SERVER: Starting motion detector\n"
			exec(open('motion_detector.py').read())


		if not data:
			break
		conn.sendall(str.encode(reply))




	conn.close()
	print ('connection lost: ' +addr[0]+':'+str(addr[1]))
while True:
	conn, addr = socket.accept()
	print('connected to: '+addr[0]+':'+str(addr[1]))
	start_new_thread(threaded_client, (conn,))
