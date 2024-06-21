import socket

# Создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Соединяемся с сервером
server_address = ('localhost', 12345)
s.connect(server_address)

try:
    # Отправляем данные
    message = "hello"
    s.sendall(message.encode('utf-8')) #.encode('utf-8')

finally:
    # Закрываем соединение
    s.close()
