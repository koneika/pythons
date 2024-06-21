import socket

# Создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к порту
server_address = ('localhost', 12345)
s.bind(server_address)

# Слушаем входящие соединения
s.listen(1)

while True:
    # Ждем соединения
    print('Ожидание соединения...')
    connection, client_address = s.accept()

    try:
        print('Соединение с', client_address)

        # Получаем данные и отправляем их обратно
        data = connection.recv(1024)
        message = data.decode('utf-8')  # Декодируем данные
        print('Получено', message)

    finally:
        # Закрываем соединение
        connection.close()
