#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {	
	char board[11][11];
	int i = 0, j = 0;
	for(i = 0; i < 11; i++) {
		for(j = 0; j < 11; j++) {
			scanf("%s", &(board[i][j]));
		}
	}
	
	int x, y;

	// Edit following code with your code.
	srand((unsigned)time(0));
	
	x = rand() % 11;
	y = rand() % 11;
	while(board[x][y] != 'U') {
		x = rand() % 11;
		y = rand() % 11;
	}

	printf("%d %d", x, y);
	return 0;
}