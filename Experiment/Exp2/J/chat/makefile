all:server client clean

server:Server_main.o server.o
	g++ -g -o server Server_main.o server.o
client:Client_main.o client.o
	g++ -g -o client Client_main.o client.o
Server_main.o:Server_main.cc
	g++ -g -c Server_main.cc
Client_main.o:Client_main.cc
	g++ -g -c Client_main.cc
server.o:server.cc
	g++ -g -c server.cc
client.o:client.cc
	g++ -g -c client.cc

clean:
	rm  server.o
	rm Server_main.o
	rm client.o
	rm Client_main.o