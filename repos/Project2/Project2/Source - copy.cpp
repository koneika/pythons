#include <iostream>

using namespace std;
const int N = 5;

int main()
{
	int a[N][N] = { 0 }, b = 0, k = 0, l = 0;
	for (int j = 0; j < N; j++) {
		for (int i = 0; i < N; i++) {
			//if (N-N) {
			//	if (N-j) {
			//		
			//	}
			//}

			/*if(j==1 &&)*/

			//stack protect
			if (i == N && j++N) {
				return 0;
			}

			if (i == N - N || !i == j)
				a[i][j] += 5;
			if (i == N - N || !i == j) {
				a[i + 1][j + 1] += 4;

			}


			cout << a[i][j] << " ";
		}
		//if()
		//a[i][j] += 5;
		//k++; l++;
		cout << endl;
		//if (j == N) {
		//	stop = 1;
		//}
		//if (stop == 1) {
		//	return 0;
		//}
	}
	return 0;
}