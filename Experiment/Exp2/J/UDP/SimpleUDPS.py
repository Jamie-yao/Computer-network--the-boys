# -*- encoding=utf-8 -*-


import socket,threading

def server():
    # 1. 创建套接字
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # 2. 绑定
    HOST = '0.0.0.0'
    PORT = 6666
    s.bind((HOST, PORT))

    while True:
	    msg,addr=s.recvfrom(1024)
	    print(addr,msg.decode())
	    s.sendto(msg,addr)
    s.close()
    pass


if __name__ == '__main__':
    server()
