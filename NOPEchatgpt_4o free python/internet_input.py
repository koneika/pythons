import socket

# Создаем сокет
while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_address = ('10.0.2.15', 12345)
    s.connect(server_address)
# Соединяемся с сервером

    
    


    message = "123"
    s.sendall(message.encode('utf-8')) #.encode('utf-8')


# s.close()
