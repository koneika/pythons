#include <iostream>
#include <fstream>
#include <string>

using namespace std;

fstream f;
fstream f2;

int main() 
{
	string a;
	f.open("����� ��������� ��������.txt", ios::in);
	f2.open("����� ��������� ��������2.txt", ios::out);

	while(f >> a)
	{
		
		for(int i = 0; i < a.length(); i++)
		{
			
			if (a[i] == '<')
			{
				f2 << endl;
				cout << endl;
			}

			if (a[i] == '{')
			{
				f2 << endl;
				cout << endl;
			}

			if (a[i] == ',')
			{
				f2 << endl;
				cout << endl;
			}

			f2 << a[i];
			cout << a[i];

		}

		f2 << " ";
		cout << " ";

		
	}
		
		
	f2.close();
	f.close();


	return 0;
}