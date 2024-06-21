# import win32api
# import win32con
# import time


# import docker

# client = docker.from_env()

# def get_or_create_container(image_name, command):
#     containers = client.containers.list(all=True, filters={"ancestor": image_name})

#     for container in containers:
#         if container.status == 'exited':
#             container.start()
#             return container

#     return client.containers.run(image_name, command, detach=True)

# while True:
#     a = str(input())
#     container = get_or_create_container("ubuntu", a)
#     print(container.logs().decode('utf-8'))

import docker

# Создаем клиента Docker
client = docker.from_env()

# Запускаем контейнер с Firefox

container = client.containers.run(
    "jlesage/firefox", 
    detach=True, 
    ports={'5800/tcp': 5800}, 
    environment=['DISPLAY_WIDTH=400', 'DISPLAY_HEIGHT=300'],
    mem_limit='800m'
)
container2 = client.containers.run(
    "jlesage/firefox2", 
    detach=True, 
    ports={'5801/tcp': 5801}, 
    environment=['DISPLAY_WIDTH=400', 'DISPLAY_HEIGHT=300'],
    mem_limit='800m'
)

print("Firefox запущен в Docker контейнере. Вы можете получить доступ к нему по адресу http://localhost:5800 в вашем веб-браузере.")




# same_time = 0.1

# time.sleep(2)

# word = "chatgpt.com"
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







# def chatgpt_writer(letter, slow_time):

#     writer(slow_time)

# chatgpt_writer(0.01)
# win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
# win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)

# win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
# win32api.keybd_event(ord('S'), 0, 0, 0)
# time.sleep(0.5)

# win32api.keybd_event(ord('S'), 0, win32con.KEYEVENTF_KEYUP, 0)
# win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
# time.sleep(same_time)

# win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
# win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)
# time.sleep(same_time)

# win32api.keybd_event(win32con.VK_TAB, 0, 0, 0)
# win32api.keybd_event(win32con.VK_TAB, 0, win32con.KEYEVENTF_KEYUP, 0)
# time.sleep(same_time)

# win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
# win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)










# import docker
# client = docker.from_env()

# container = client.containers.run(
#     "jlesage/firefox", 
#     detach=True, 
#     ports={'5800/tcp': 5800}, 
#     environment=['DISPLAY_WIDTH=400', 'DISPLAY_HEIGHT=300'],
#     mem_limit='800m'
# )

# print(client.containers.list())


# container = client.containers.get('45e6d2de7c54')