#include <iostream>
#include <ctime>
#include <thread>
#include <vector>
#include <telebot.h>

int main() {
    std::string token = "7006992799:AAH19FiYzQcuIDRi_MRiN92ZfT8Ol20HuE8";
    Telebot bot(token);
    int myUsername = 1111655025;

    bot.sendMessage(myUsername, "bot started");

    double startedTime = std::time(nullptr);
    std::vector<int> timer(99, 1);

    std::cout << timer[0] << ", " << timer[1] << std::endl;
    int multiplier = 0;
    int times = 1;
    int hour = 1;
    int breaktime = 3;

    while (true) {
        std::this_thread::sleep_for(std::chrono::seconds(1));

        if (static_cast<int>(std::time(nullptr)) == static_cast<int>(startedTime + (hour * 3) * times)) {
            bot.sendMessage(myUsername, "1zaidite za nagardoy @1111655025, u vas est 5 minut");
            times++;
            std::this_thread::sleep_for(std::chrono::seconds(breaktime));
            bot.sendMessage(myUsername, "vremya vishlo");
        }
    }

    return 0;
}