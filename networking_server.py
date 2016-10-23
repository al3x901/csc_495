#!/usr/bin/python           # This is server.py file

import socket               # Import socket module

class server:
	def __init__(self):
		s = socket.socket()         # Create a socket object
		host = socket.gethostname() # Get local machine name
		port = 12345                # Reserve a port for your service.
		s.bind(('192.168.1.109', port))        # Bind to the port
		print 'Listening for clients'
		s.listen(5)                 # Now wait for client connection.
		self.c, addr = s.accept()     # Establish connection with client.
		print 'Got connection from', addr
		c.send('You are now connected to kit!')

	def send_map(map):
		self.c.send(map)
		print 'map sent!'
