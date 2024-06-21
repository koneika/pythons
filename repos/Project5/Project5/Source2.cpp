#include <iostream>
using namespace std;

struct Node 
{
	int Value;
	Node* Next;
};

Node* add_node(Node* second, int value) 
{
	Node* head = new Node;
	head->Value = value;
	head->Next = second;

	return head;
}

void for_view(bool new_data_exist, int times, Node* arr2, Node* new_data, int times2) 
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
	int value;
	bool new_data_exist = false;

	cout << "Enter the number of elements: ";
	cin >> times;

	Node* arr2 = new Node[times];
	Node* new_data = nullptr;

	cout << "Enter the elements: " << endl;
	for (int i = 0; i < times; i++) {
		cin >> value;
		arr2[i].Value = value;
	}

	cout << "Data saved..." << endl;

	int choice;
	do {
		system("cls");
		cout << "Menu" << endl;
		cout << "1. Show data" << endl;
		cout << "2. Exit" << endl;
		cout << "3. Add data before the end" << endl;
		cout << "4. Change data" << endl;
		cout << "What do you want to choose? ";
		cin >> choice;
		system("cls");

		switch (choice) {
			case 1:
			{
				cout << "Menu - Show data" << endl;
				for_view(new_data_exist, times, arr2, new_data, times2);
				break;
			}
			case 2:
			{
				cout << "Exiting..." << endl;
				exit(0);
				break;
			}
			case 3:
			{
				cout << "Menu - Add data before the end" << endl;
				cout << "Enter the number of new elements: ";
				cin >> times2;

				Node* arr3 = new Node[times2];
				new_data = new Node[times + times2];

				cout << "Enter the new elements: " << endl;
				for (int i = 0; i < times2; i++) {
					cin >> arr3[i].Value;
				}

				for (int i = 0; i < times; i++) {
					new_data[i].Value = arr2[i].Value;
				}
				for (int i = 0; i < times2; i++) {
					new_data[times + i].Value = arr3[i].Value;
				}

				new_data_exist = true;

				delete[] arr3;
				break;
			}
			case 4:
			{
				cout << "Menu - Change data" << endl;
				for_view(new_data_exist, times, arr2, new_data, times2);

				cout << "Enter the index to change (0 to " << times+times2-1 << "): ";
				int index;
				cin >> index;
				cout << "Enter the new value: ";
				int newValue;
				cin >> newValue;

				if (new_data_exist) {
					new_data[index].Value = newValue;
				}
				else {
					arr2[index].Value = newValue;
				}
				break;
			}
			/*default:
				cout << "Invalid choice, please try again." << endl;*/
		}

		system("pause");
	} while (true);

	delete[] arr2;
	if (new_data_exist) {
		delete[] new_data;
	}

	return 0;
}
