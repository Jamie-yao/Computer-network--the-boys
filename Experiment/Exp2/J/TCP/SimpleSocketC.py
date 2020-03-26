# -*- encoding=utf-8 -*-


import socket


def client():
    HOST=input('请输入IP地址：')
    PORT=input('请输入port端口号：')
    # 1. 创建套接字
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2. 连接
#     HOST = '127.0.0.1'
#     PORT = 6666
    s.connect((HOST, int(PORT)))
    # 3. 处理信息
    while True:
        str=input("请输入:")
        s.sendall(str.encode())
        msg = s.recv(1024)
        print('From server: %s' % msg.decode())


if __name__ == '__main__':
    client()