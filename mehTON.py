import telebot
from selenium import webdriver
import time
import socket

ascii_table = [ ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '/', ':', ';', '<', '=', '>', '?', '@',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z',
            '[', '\\', ']', '^', '_', '`',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z',
            '{', '|', '}', '~']
            #normal_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'] #len()
url = "https://www.geckoterminal.com/ton/pools/EQANjvfeRYoFunO606gTR00CyqbPU8Np2aVo0vmbPPE4BJOz"
myUsername = 1111655025
token = '7053594101:AAE2ZaCg_i6rt7dALqC6ixmkZKpIyQRpLDU'
bot = telebot.TeleBot(token)
find_this_word = 'leading-none\"><span>$'
#find_this_word_2 = '</span></span></div><span class=\"line-clamp-'
# switcher = False

driver = webdriver.Firefox() # ANY BROWSER HERE
driver.get(url) # FOR WORK
#
index_of_dollar = driver.page_source.find(find_this_word)
#index_of_dollar_2 = driver.page_source.find(find_this_word_2)
#
print("UBEDITELNAYA PROSBA, PROVER INTENET PREZDE CHEM TI BUDESH VKLUCHAT BOTA \nUBEDITELNAYA PROSBA, PROVER INTENET PREZDE CHEM TI BUDESH VKLUCHAT BOTA \nUBEDITELNAYA PROSBA, PROVER INTENET PREZDE CHEM TI BUDESH VKLUCHAT BOTA \n")
# print(len(find_this_word))

# print(driver.page_source.find(find_this_word))

#print(index_of_dollar + len(find_this_word) , index_of_dollar + len(find_this_word) + 8)
target = driver.page_source[index_of_dollar + len(find_this_word):index_of_dollar + len(find_this_word) + 8]
while(True):
    
    def check_internet_connection(host="8.8.8.8", port=53, timeout=3):
        try:
            socket.setdefaulttimeout(timeout)
            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
            return True
        except socket.error:
            return False

    if check_internet_connection():
        #
        ###- (index_of_dollar_2-index_of_dollar)
        if(index_of_dollar != -1):
            # for i in range(len(ascii_table)):
            #     if not str(ascii_table[i]) in str(driver.page_source):
            #         switcher = True
            #     else:
            #         switcher = False
            #print(list(target) ,len(list(target)))

            

            # def switcher():
            #     for i in range(0, len(list(target))):
            #         for j in range(len(list(ascii_table))):
            #             if (ascii_table[j] != target[i]):# bad word != word - true
            #                 # switcher = True
            #                 return True
            #             # else:
            #             #     # switcher = False
            #             #     return
            #             else:
            #                 return False
            
            # print(index_of_dollar_2-index_of_dollar)
            
            # print(target)

            # if switcher():
            #     for i in range(0, len(list(target))):
            #         for j in range(len(list(ascii_table))):
            #             if (ascii_table[j] != target[i]):# bad word != word - true
                            
                            #   if not("<" in target or ">" in target or "n" in target or "$>" in target or "</" in target):
                            #seven_chars_after_dollar = driver.page_source[index_of_dollar + len(find_this_word):index_of_dollar + len(find_this_word) + 8]
            fix_it = str("$") + str(target)
                            #if "$" in seven_chars_after_dollar:
            bot.send_message(myUsername, fix_it)# print(bot.send.message())
                
            time.sleep(10) # SUPER IMPORTANT, CHANGE TO BIGGER TIME THAN IT WAS IF YOU HAVE A BREAK PROGRAM AFTER 40-60 MINUTS OR MORE
                
            # else:
            #     print("Error, cant find a word")
                
    else:
        print("Нет интернета")
        time.sleep(10)

    
# Закрытие браузера
driver.quit()

#######################################################почистить зубы
#######################################################почистить зубыы
#######################################################почистить зубы



