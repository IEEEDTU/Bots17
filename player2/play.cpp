#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
using namespace std;

// Edit this function with your code.
vector<int> play(vector<vector<char > > board) 
{
	srand(unsigned(time(0)));
	
	int x = rand() % 11;
	int y = rand() % 11;
	
	while(board[x][y] != 'U') {
		x = rand() % 11;
		y = rand() % 11;
	}
	
	vector<int> result;
	result.push_back(x);
	result.push_back(y);
	return result;
}

int main() 
{	
	vector<vector<char> > board(11, vector<char>(11));
	for (int i = 0; i < 11; i++) {
		for (int j = 0; j < 11; j++) {
			cin >> board[i][j];
		}
	}
	
	vector<int> xy = play(board);
	cout << xy[0] << ' ' << xy[1];
	return 0;
}