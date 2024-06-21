my_string = "**🚀 Rocket-чек на 117.5 USDT (117.5$)****Внутри чека:** 4700 активация(й) по 0.02 USDT (0.02$) с реферальной наградой 0.005 USDT (0.005$)[**🔥П__олучить🔥__**](https://t.me/xrocket?start=mci_vaw5eSj0YP0pthC)__Надоело сливать деньги на пустых сигналах? Лучшие сигналы здесь - ____https://t.me/xrocket?start=sb_v__NMn2321hEya67NСамые сочные чеки на просторах телеграма https://t.me/xrocket?start=sb_VlNY26QvQ4qKOHx"
word_to_find = "https://t.me/xrocket?start="
index = my_string.find(word_to_find)
if index != -1:
    
    print(my_string[index : index+len(word_to_find)+19])
