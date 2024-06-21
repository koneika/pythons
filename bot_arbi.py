import subprocess
import time
import urllib.request

url = "https://www.geckoterminal.com/ru/ton/pools/EQCCsJOGdUdSGq0ambJFgSptdHfDPkaQlKlLIKTqtazhhcps"
word = 'leading-none\"><span>'

while True:
    time.sleep(10)
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    source_code = response.read().decode('utf-8')

    make_sure_its_digit = True
    while make_sure_its_digit == True:
        # тут проблема жёсткая, найти не может, причина по которой, программа после с десятого раза запуска, это надо исправить, чтоб
        # запускалось и работало с одного раза
        letter = source_code.find(word)
        fixated = source_code[letter + len(word) : letter + len(word) + 6]
        print(fixated)
        for i in range(0, len( fixated)):
            if ( fixated[i] == '0' or  fixated[i] == '1' or  fixated[i] == '2' or  fixated[i] == '3' or  fixated[i] == '4' or 
                fixated[i] == '5' or  fixated[i] == '6' or  fixated[i] == '7' or  fixated[i] == '8' or  fixated[i] == '9' or 
                fixated[i] == ','):
                make_sure_its_digit = False
            else:
                make_sure_its_digit = True

    ############################################################################
    char_temp = [''] *  len( fixated)
    for i in range(0, len( fixated)):   
        char_temp[i] = fixated[i]
        if char_temp[i] == ',':
            char_temp[i] = '.'

    ###
    array_to_variable = ''.join(char_temp)

    print(make_sure_its_digit, fixated, array_to_variable)

    # for i in range(0, len( fixated)):
    #     print(make_sure_its_digit, fixated, char_temp)
    ############################################################################
    #make_sure_its_digit = False
    #time.sleep(60)
    #for i in range(0, len(completed)): # попозже добавить защиту  
    make_sure_its_digit = True
    while make_sure_its_digit == True:
        letter = source_code.find(word)
        completed = source_code[letter + len(word) : letter + len(word) + 6]
        for i in range(0, len(completed)):
            if (completed[i] == '0' or completed[i] == '1' or completed[i] == '2' or completed[i] == '3' or completed[i] == '4' or 
                completed[i] == '5' or completed[i] == '6' or completed[i] == '7' or completed[i] == '8' or completed[i] == '9' or 
                completed[i] == ','):
                make_sure_its_digit = False
            else:
                make_sure_its_digit = True
        

    ############################################################################
    char_temp = [''] *  len( completed)
    for i in range(0, len( completed)):   
        char_temp[i] = completed[i]
        if char_temp[i] == ',':
            char_temp[i] = '.'
        
        ###
    array_to_variable2 = ''.join(char_temp)

        #print(make_sure_its_digit, completed, array_to_variable2)

        # for i in range(0, len( completed)):
        #     print(make_sure_its_digit, completed, char_temp)
    ############################################################################
        #make_sure_its_digit = False
        
    if (letter != -1):
            #print(make_sure_its_digit, float(array_to_variable), float(array_to_variable2))
            # switcher = True
            # while (switcher == True):
            #     for i in range(0, len(completed)):
            #         if (completed[i] == '0' or completed[i] == '1' or completed[i] == '2' or completed[i] == '3' or completed[i] == '4' or 
            #         completed[i] == '5' or completed[i] == '6' or completed[i] == '7' or completed[i] == '8' or completed[i] == '9' or 
            #         completed[i] == '.'):
            #             switcher = False
            #print(array_to_variable, array_to_variable2)
        if (float(array_to_variable) != float(array_to_variable2)):
            if (float(array_to_variable) < float(array_to_variable2)):
                print("sell it", ('+', (float(array_to_variable) / float(array_to_variable2))* 100 ) - 100, "%")
            else:
                print("buy it", ('-', (float(array_to_variable) / float(array_to_variable2))* 100 ) - 100, "%")
    else:
        print("cant find word")

       