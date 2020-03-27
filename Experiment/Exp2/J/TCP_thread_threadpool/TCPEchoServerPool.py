# -*- encoding=utf-8 -*-


import socket,threading
from queue import Queue

def Server_thread(q):
    c,addr=q.get()
    print('Connect client: ', addr)
    while True:
        msg = c.recv(1024)
        if not msg:
            print('Disconnect client: ', addr)
            break;
        print('From client: ', addr,msg.decode())
        c.sendall(msg)
    pass    


def server(nworkers):
    q=Queue()	#任务队列
    for n in range(nworkers):
        t=threading.Thread(target=Server_thread,args=(q,))
        t.daemon=True    #守护线程
        t.start()
		
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
        q.put((c,addr))

    s.close()
    pass
    


if __name__ == '__main__':
    server(99)
