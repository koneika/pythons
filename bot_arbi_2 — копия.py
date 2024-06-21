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


result = subprocess.run(['curl', url], capture_output=True)

word = 'leading-none\"><span>'

index_chatgpt = str(result).find(word)

print(index_chatgpt)

print(int(index_chatgpt)-len(word) + len(word)-len(word))

print(str(result)[int(index_chatgpt)-len(word) + len(word)-len(word)-30 : index_chatgpt+30])




# print(word)
# if str(input()) in str(result):
#     print("good")
# else:
#     print('bad')

