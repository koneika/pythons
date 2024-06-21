#include <iostream>
using namespace std;

struct Node
{
	int Value;
	Node* Next;
};

Node* add_node(Node* second, int Value)
{
	Node* head = new Node;
	head->Value = Value;
	head->Next = second;

	return head;
}

void for_view(bool &new_data_exist, int times, Node* arr2, Node* new_data, int times2)
{
	if (new_data_exist != true)
	{
		for (int i = 0; i < times; i++)
		{
			cout << arr2[i].Value << " ";
		}
	}
	else
	{
		



			
		new_data[3].Value = arr2[0].Value;
		for (int i = 0; i < times + times2; i++)
		{
			
			cout << new_data[i].Value << " ";

		}


	}
	cout << endl;
}

int main()
{
	int times = 0, times2 = 0;
	int value, value1, value2;
	bool new_data_exist = false;

	cout << "write amount of elements: ";
	cin >> times;


	Node* arr2 = new Node[times];
	Node* new_data = nullptr;

	cout << "write only one digit, then 'enter': " << endl;
	for (int i = 0; i < times; i++)
	{
		cin >> value;
		arr2[i].Value = value;
	}

	cout << "data saved..." << endl;
	cout << endl;
	cout << "welcome to the menu" << endl;
	
	do 
	{
		


		system("cls");

		int i = 1;
		cout << "Menu" << endl;
		cout << i++ << ". show data" << endl;
		cout << i++ << ". exit" << endl;
		cout << i++ << ". add data between before end and end" << endl;
		cout << i++ << ". change data" << endl << endl;
		cout << "what do you want to choose?" << endl;

		cin >> i;
		system("cls");

		switch (i) {
			case 1:
			{
				cout << "Menu" << endl;
				cout << "1. show data" << endl << endl;

				for_view(new_data_exist, times, arr2, new_data, times2);

				break;
			}
			case 2:
			{
				cout << "Menu" << endl << endl;
				cout << "2. exit" << endl << endl;
				exit(0);
				break;
			}
			case 3:
			{
				cout << "Menu" << endl << endl << endl;
				cout << "3. add data between before end and end" << endl << endl;

				cout << "write amount of elements: ";

				cin >> times2;

				system("cls");

				Node* arr3 = new Node[times2];
				new_data = new Node[times + times2];

				/*cout << times << endl;
				cout << times2 << endl;*/

				int j = 0, k = 0;
				while (k < times2)
				{
					cin >> arr3[k].Value; k++;
				}


				system("cls");

				j = 0, k = 0;
				while (j < times)
				{
					new_data[j].Value = arr2[j].Value;				
					new_data[j + k].Value = arr2[j].Value;

					cout << arr2[j].Value << " ";
					j++;


					if (j == times - 1)
						while (k < times2)
						{
							new_data[k].Value = arr3[k].Value;
							new_data[j + k].Value = arr3[k].Value;

							cout << arr3[k].Value << " ";
							k++;
						}
				}
				new_data_exist = true;

				break;
			}
			case 4:
			{
				cout << "Menu" << endl << endl << endl << endl;
				cout << "4. change data" << endl << endl;
				for_view(new_data_exist, times, arr2, new_data, times2);

				cout << "choose 1-" << times+times2 << endl;
				int i, value3;

				cin >> i;
				cout << "Enter the new value: ";

				cin >> value3;

				if (new_data_exist)
					new_data[i-1].Value = value3;
				else 
					arr2[i-1].Value = value3;
				break;
			}
			


		}
		system("pause");
	} while (true);



	return 0;
}

