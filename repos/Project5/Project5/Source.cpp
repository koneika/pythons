#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

struct Node
{
	int Value;
	Node* Next; // создаёт структуру в структуре
};

Node* add_node(Node* second, int &Value, int arr[], int N)
{
	Node* head = new Node;		// [head]

								// we creating th first node 

	head->Value = arr[N];			// in the first node we put '1' in Value variable
	head->Next = second;		// and it connect first with second node

	return head;

	delete head;
}


int main(Node* head, Node* second, Node* third, Node* unknown, Node* fourth, Node* p, Node* q, Node* p1)
{
	int unkn, N;
	int* Value;
	unkn = 0;
	N = 0;




	while (true/*isdigit(N)*/)
	{
		cin >> N;
		int* arr = new int[N];
		for (int i = 0; i < N; i++)
		{
			cin >> arr[N];
			add_node(second, arr[N], arr[N], N);
		}
		for (int i = 0; i < N; i++)
		{
			cout << add_node(second, arr[N])->Value << endl;
		}
	}

	cout << "write any digit: ";
	cin >> unkn;
	cout << endl;

	/*cout << first_node(second, Value)->Value << endl;
	cout << second_node(third, Value)->Value << endl;
	cout << third_node(Value, unknown)->Value << endl;
	cout << unknown_node(third, fourth, Value, p, q, p1, unkn)->Value << " <- your is here digit" << endl;
	cout << fourth_node(Value, p, q, p1)->Value << endl;*/

	system("pause");
	return 0;
}