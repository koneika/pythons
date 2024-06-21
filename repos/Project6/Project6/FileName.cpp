#include <iostream>
#include <fstream>
#include <string>

using namespace std;

struct function
{
	string& new_times;
	char& time_unit;
};

string function1(string &new_times) 
{
	

	return new_times;
}

char function2(char& time_unit) 
{


	return time_unit;
}

int main() 
{
	setlocale(LC_ALL, "Russian");

	do
	{
		short choose;
		string times;
		string new_times;
		int i = 0;
        char time_unit = '\0';

		cout << "меню" << endl;
		cout << "1. ѕосчитать врем€" << endl;

		cin >> choose;

		switch (choose)
		{
		case 1:

			cout << "сколько уже прошло времени? напишите например как то так 2s или 5m или 10h или 20d" << endl;
			
			cin >> times;

            for (int i = 0; i < times.length(); i++)
            {
                if (isdigit(times[i]))
                {
                    new_times += times[i];
                }
                else
                {
                    time_unit = times[i];
                    break; // ќстанавливаемс€, как только встретили символ времени
                }

            }

			cout << function1(new_times) << endl;
			cout << function2(time_unit) << endl;


			break;

		default:
			break;
		}



	} while (true);
	



	return 0;
}