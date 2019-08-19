import socket
import threading
#指明协议，socket.AF_INET服务器之间网络通信，SOCK_STREAM流式socket，for TCP
#创建TCP Socket：s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#创建UDP Socket：s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定IP地址和端口
server.bind(('0.0.0.0',8000))
server.listen() #监听


def handle_sock(sock, addr):
	while True:
		data= sock.recv(1024) #获取从客户端获取的数据,1次获取1k的数据
		if (data.decode('utf8')=='q!'):
			break
		print(data.decode('utf8')) #打印返回数据
		re_data = input()
		sock.send(re_data.encode('utf8'))
	sock.close()

while True:
	sock, addr = server.accept()  #接收

	client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
	client_thread.start()
#server.close()  #关闭
#sock.close()
