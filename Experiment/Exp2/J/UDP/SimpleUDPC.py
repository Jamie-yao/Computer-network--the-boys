# -*- encoding=utf-8 -*-


import socket


def client():
    HOST=input('请输入IP地址：')
    PORT=input('请输入port端口号：')
    print("键入 exit 以结束程序")
    # 1. 创建套接字
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    while True:
        msg=input('$')
        if not msg: continue
        elif msg.strip() == 'exit': break
        s.sendto(msg.encode(),(HOST,int(PORT)))
        back_msg,addr=s.recvfrom(1024)
        print('From server: %s' % back_msg.decode())


if __name__ == '__main__':
    client()