//#include <iostream>
//#include <string>
//#include <cstdlib>
//
//using namespace std;
//
//struct Node
//{
//	int Value;
//	Node* Next; // ������ ��������� � ���������
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
//		int* arr = new int[times]; // ���� � ��� ������ ������ ������������ � ����� ����������� ��� ������� �� ��� ����� ���
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
#include <locale>	// ����� ��� ������� ����
using namespace std;

struct Node// ���������
{
	int Value;
	Node* Next;
};

Node* add_node(Node* second, int Value)// ��� ���� ����� ��������� ���������� ���������� �������
{
	Node* head = new Node;// ��������� head � ��������� node
	head->Value = Value;// ������ ����� ��������� head ����� int Value
	head->Next = second;// ������ ����� �������� head ����� ����� ��������� second

	return head;// ���������� �� ���� �������, ��������� head
}

int main()
{
	locale::global(locale("ru_RU.UTF-8"));// ����� ��� ������� ����
	int times, times2 = 0;
	int value, value1, value2;
	bool new_data_exist = false;

	wcout << L"������� ���������� ���������: ";// ���������� ��������� ����� ��� �������, ������� �� ��������
	cin >> times;

	// ������ ������, ������ ��������� node, ����� ���������� ������ ����� � ���������� ������, 
	// ��� ���� ������ �� ����� ����������� �� ������ for
	Node* arr2 = new Node[times];
	
	wcout << L"������� ���� �����, ����� ������� enter: " << endl;// ��������� ���������� � ���������� ������ � ������
	for (int i = 0; i < times; i++)
	{
		cin >> value;
		arr2[i].Value = value;
	}

	wcout << L"������ ��������..." << endl;
	wcout << endl;
	wcout << L"����� ���������� � ����" << endl;
	
	do 
	{
		system("cls");

		int i = 1;
		wcout << L"����" << endl;
		wcout << i++ << L". ���������� ������" << endl;
		wcout << i++ << L". �����" << endl;
		wcout << i++ << L". �������� ������������� ������" << endl;
		wcout << L"��� �� ������ �������?" << endl;

		cin >> i;
		system("cls");
		
		switch (i) {
		case 1:
			wcout << L"����" << endl;
			wcout << L"1. ���������� ������" << endl << endl;

			if(new_data_exist != true)
				for (int i = 0; i < times; i++)
				{
					cout << arr2[i].Value << endl;
				}
			else
				for (int i = 0; i < times+times2; i++)
				{
					cout << new_data[i].Value << endl;
				}

			break;
		case 2:
			wcout << L"����" << endl << endl;
			wcout << L"2. �����" << endl << endl;
			exit(0);
			break;
		case 3:
			wcout << L"����" << endl << endl << endl;
			wcout << L"3. �������� ������������� ������" << endl << endl;
			
			wcout << L"������� ���������� ���������: ";

			cin >> times2;

			Node* arr3 = new Node[times2];

			Node* new_data = new Node[times + times2];

			system("cls");

			/*cout << times << endl;
			cout << times2 << endl;*/
			for (int i = 0; i < times2; i++)
				cin >> arr3[i].Value;

			system("cls");

			int i = 0, j = 0;
			while (i < times) 
			{
				cout << arr2[i].Value << endl; i++;
				new_data[i].Value = arr2[i].Value;

				if(i == times-1)
					while (j < times2) 
					{
						cout << arr3[j].Value << endl; j++;
						new_data[j].Value = arr3[j].Value;
					}
			}
			new_data_exist = true;
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
		system("pause");
	} while (true);

	//wcout << L"������� �� ������, ������������� �����e" << endl;

	//for (int i = 0; i < times; i++)
	//{
	//	int value;
	//	cin >> value;

	//	arr2[i].Value = value;
	//}

	//// ������� �������
	//system("cls");

	//// ����� ��, ��� ������� � ������ 
	//for (int i = 0; i < times; i++)
	//{
	//	cout << arr2[i].Value << endl;
	//}

	return 0;
}

