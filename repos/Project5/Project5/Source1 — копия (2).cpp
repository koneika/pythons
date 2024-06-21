//#include <iostream>
//#include <string>
//#include <cstdlib>
//
//using namespace std;
//
//struct Node
//{
//	int Value;
//	Node* Next; // создаёт структуру в структуре
//};
//
//Node* add_node(Node* second, int Value, int arr[], int N) 
//{
//	Node* head = new Node;
//	int* arr = new int[N];
//
//	head->Value = arr[N];
//	head->Next = second;
//
//	return head;
//	delete head;
//	delete[]arr;
//
//}
//
//int main(Node* head, Node* second)
//{
//	int Value, unkn, N, * arr;
//	Value = 0;
//	unkn = 0;
//	N = 0;
//
//	add_node(second, Value, arr, N);
//}










//#include <iostream>
//
//using namespace std;
//
//struct Node
//{
//	int Value;
//	Node* Next;
//};
//
//Node* add_node(Node* second, int Value)
//{
//	Node* head = new Node;
//	head->Value = Value;
//	head->Next = second;
//
//	return head;
//}
//
//int main()
//{
//	Node* head = nullptr;
//	Node* second = nullptr;
//
//	int Value = 0, times;
//	
//	
//
//	cin >> times;
//
//	for(int i = 0; i < times; i++)
//	{
//		int* N = new int[];
//		cin >> N[times];
//		head = add_node(second, N[times]);
//
//		for (int i = 0; i < times; i++) 
//		{
//			cout << add_node(second, N[times])-Value << endl;
//		}
//	}
//	
//
//	
//
//
//
//	// delete head;s
//
//	system("pause");
//	return 0;
//}\


















//#include <iostream>
//
//using namespace std;
//
//struct Node
//{
//	int Value;
//	Node* Next;
//};
//
//Node* add_node(Node* second, int Value)
//{
//	Node* head = new Node;
//	head->Value = Value;
//	head->Next = second;
//
//	return head;
//}
//
//int main()
//{
//	Node* head = nullptr;
//	int times;
//	Node* head = new Node[times];
//
//	cin >> times;
//
//	for (int i = 0; i < times; i++)
//	{
//		int value;
//		int* arr = new int[times]; // типо у нас теперь массив динамический с тримя количеством или сколько ты там задал фак
//
//
//		cin >> arr[times];
//
//		
//		head[times] = add_node(head, arr[times]);
//	}
//
//	return 0;
//}









#include <iostream>
using namespace std;

struct Node// структура
{
	int Value;
	Node* Next;
};

Node* add_node(Node* second, int Value)// для того чтобы создавать беконечное количество функций
{
	Node* head = new Node;// структура head в структуре node
	head->Value = Value;// внутри новой структуры head будет int Value
	head->Next = second;// внутри новой струтуры head будет новая структура second

	return head;// возвращаем по этой функции, структуру head
}

void for_view(bool &new_data_exist, int times, Node* arr2, Node* new_data, int times2)
{
	if (new_data_exist != true)
		for (int i = 0; i < times; i++)
		{
			cout << arr2[i].Value << " ";
		}
	else
	{
		int j = 0, k = 0;
		/*int* temp = new int[times + times2];

		for (int i = 0; i < times + times2; i++)
			temp[i] = 0;

		for (int i = 0; i < times + times2; i++)
			cout << temp[i] << " ";*/



		/*system("pause");*/

		while (j < times)
		{
			

			/*new_data[j].Value = temp[j];*/
			/*cout << temp << " ";*/
			cout << new_data[j].Value << " "; j++;

			/*cout << k << " == " << times - 1 << endl;*/
			if (j == times - 1)
				while (k < times2)
				{
					/*new_data[k].Value = temp[k];*/
					cout << new_data[k].Value << " "; k++;
				}
		}

		//rework
		/*for (int i = 0; i < times + times2; i++)
			new_data[i].Value = temp[i];*/


	}


	



}

int main()
{
	int times = 0, times2 = 0;
	int value, value1, value2;
	bool new_data_exist = false;

	cout << "write amount of elements: ";// количество елементов будет вот столько, сколько ты захочешь
	cin >> times;

	// создаём массив, внутри структуры node, чтобы запоминать данные ввода с клавиатуры данных, 
	// без него данные не будут запоминатся во втором for
	Node* arr2 = new Node[times];
	Node* new_data = nullptr;

	cout << "write only one digit, then 'enter': " << endl;// постоянно записываем с клавиатуры данные в массив
	for (int i = 0; i < times; i++)
	{
		cin >> value;
		arr2[i].Value = value;
	}

	cout << "data saved..." << endl;
	wcout << endl;
	cout << "welcome to the menu" << endl;
	
	do 
	{
		


		system("cls");

		int i = 1;
		cout << "Menu" << endl;
		wcout << i++ << L". show data" << endl;
		wcout << i++ << L". exit" << endl;
		wcout << i++ << L". add data between before end and end" << endl;
		wcout << i++ << L". change data" << endl << endl;
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

				system("pause");

				j = 0, k = 0;
				while (j < times + times2)
				{
					cout << new_data[i].Value << " ";
					j++;
				}
				//for (int i = 0; i < times + times2; i++)
				//{

				//	//if(i == times - 1)
				//	//{
				//	/*cout << arr2[i].Value << endl;*/
				//	
				//	if (i == times - 1) 
				//	{
				//		for (int i = 0; i < times2; i++)
				//		{
				//			int value2;

				//			cin >> value2;
				//			arr3[i].Value = value2;
				//		}
				//		
				//		/*for (int i = 0; i < times2; i++)
				//		{

				//			cout << arr3[i].Value << endl;
				//		}*/

				//	}
				//	
				//		/*}*/

				//	
				//}

				//system("cls");
				//
				///*for (int i = 0; i < times2; i++)
				//{

				//	cout << arr2[i].Value << endl;
				//}
				//for (int i = 0; i < times2; i++)
				//{

				//	cout << arr3[i].Value << endl;
				//}*/

				//for (int i = 0; i < times; i++)
				//{
				//	cout << arr2[i].Value << endl;
				//	/*cout << i << "==" << times - 1 << " debug" << endl;*/
				//	if (i == times-2)
				//	{
				//		/*cout << i << "==" << times2 - 1 << " debug" << endl;*/
				//		for (int i = 0; i < times2; i++)
				//			cout << arr3[i].Value << endl;
				//	}

				//}


				//int i = 0, j = 0;
				//while(i < times-1)
				//{

				//	new_data[i+j].Value = arr2[i].Value; 
				//	i++;

				//	if (i == times - 2)
				//	{

				//		while (j < times-1)
				//			new_data[i+j].Value = arr3[i].Value;
				//			j++;
				//	}

				//}
				break;
			}
			case 4:
			{
				cout << "Menu" << endl << endl << endl << endl;
				cout << "4. change data" << endl << endl;

				for_view(new_data_exist, times, arr2, new_data, times2);

				system("pause");

				int j = 0, k = 0; 
				while (j < times)
				{
					cout << new_data[i + j].Value << " ";
					j++;
					if(i == times-1)
						while (k < times2)
						{
							cout << new_data[i + j].Value << " ";
							k++;
						}

				}
					
					

				break;
			}

			//	cout << "4. заменить данные" << endl << endl;

			//	if (new_data_exist != true)
			//		for (int i = 0; i < times; i++)
			//		{
			//			cout << arr2[i].Value << endl;
			//		}
			//	else
			//	{
			//		int j = 0, k = 0;
			//		while (j < times)
			//		{
			//			cout << new_data[j].Value << endl; j++;

			//			/*cout << k << " == " << times - 1 << endl;*/
			//			if (j == times - 1)
			//				while (k < times2)
			//				{
			//					cout << new_data[k].Value << endl; k++;
			//				}
			//		}
			//	}

			//	break;

		}
		system("pause");
	} while (true);

	//cout << "сколько вы хотите, промежуточных данныe" << endl;

	//for (int i = 0; i < times; i++)
	//{
	//	int value;
	//	cin >> value;

	//	arr2[i].Value = value;
	//}

	//// очистка консоли
	//system("cls");

	//// вывод то, что вводили в массив 
	//for (int i = 0; i < times; i++)
	//{
	//	cout << arr2[i].Value << endl;
	//}

	return 0;
}

