# -*- encoding=utf-8 -*-


import socket,threading

def server():
    # 1. 创建套接字
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2. 绑定
    HOST = '0.0.0.0'
    PORT = 6666
    s.bind((HOST, PORT))
    # 3. 监听
    s.listen(10)
    # 4. 处理
    while True:
        c, addr = s.accept()
        t1=threading.Thread(target=Server_thread,args=(c, addr))
        t1.start()

    s.close()
    pass
    
def Server_thread(c, addr):
    print('Connect client: ', addr)
    while True:
        msg = c.recv(1024)
        if not msg:
            print('Disconnect client: ', addr)
            break;
        print('From client: ', addr,msg.decode())
        c.sendall(msg)
    pass    

if __name__ == '__main__':
    server()
