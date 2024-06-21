# import win32api
# import win32con
import time
import socket

# print("write your ask: ")
# message = input()

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




# same_time = 0.1

# time.sleep(2)

# word = message

# letter = ''
# slow_time = 0.0


# # def conventer(word):
# #     for i in range(len(word)):
# #         if word == '.'


# def chatgpt_writer(slow_time):
#     for i in range(len(word)):
#         if word[i] == '.':
#             win32api.keybd_event(win32con.VK_DECIMAL, 0, 0, 0)
#             win32api.keybd_event(win32con.VK_DECIMAL, 0, win32con.KEYEVENTF_KEYUP, 0)
#         else:
#             letter = word[i].upper()
#             win32api.keybd_event(ord(letter), 0, 0, 0)
#             win32api.keybd_event(ord(letter), 0, win32con.KEYEVENTF_KEYUP, 0)
#             time.sleep(slow_time)

# def writer(letter, slow_time):
    
#         light_click(letter, slow_time)


# chatgpt_writer(0.01)