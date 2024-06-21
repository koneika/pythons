import subprocess
import time
import urllib.request
import re



switcher = True

while switcher == True:
    print("1 or 2?")
    choise = int(input())
    if choise == 1:
        url = "https://www.geckoterminal.com/ru/ton/pools/EQCCsJOGdUdSGq0ambJFgSptdHfDPkaQlKlLIKTqtazhhcps"
        switcher = False
    elif choise == 2:
        print("input link of geckoterminal of price")
        url = str(input())
        switcher = False
    else:
        print("choose only 1 or 2")
        switcher = True

print("\n", subprocess.run(['curl', url], capture_output=True))

word = str(input())



"""for time"""
# staked_time = 0
# def staked_time_def(staked_time):

staked_time = time.time()

while True:
    if (int(time.time()) != int(staked_time)):
        staked_time += 1
        result = subprocess.run(['curl', url], capture_output=True)

        #print("\n",result)
        


        # time.sleep(10)
        index_chatgpt = str(result).find(word)

        xz = int(index_chatgpt)-len(word) + len(word)-len(word)
        print(index_chatgpt-xz)

        print(str(result)[index_chatgpt + len(word) - 8: index_chatgpt + len(word) + 8])




# print(word)
# if str(input()) in str(result):
#     print("good")
# else:
#     print('bad')

