import java.util.Random;
import java.util.Scanner;

public class Play {
	
    // Edit this function with your code.
    static int[] play(char board[][]) {
        Random random= new Random();
        int x = random.nextInt(11);
        int y = random.nextInt(11);
        while(board[x][y] != 'U') {
            x = random.nextInt(11);
            y = random.nextInt(11);
        }
        
        int result[] = new int[2];
        result[0] = x;
        result[1] = y;
        return result;
    }

	public static void main(String[] args) {
        
		Scanner s=new Scanner(System.in);
		char board[][]= new char[11][11];
		char color;
		for(int i=0; i < 11; i++) {
            for(int j=0;j<11;j++) {
                board[i][j]= s.next().charAt(0);
            }
        }
        color = s.next().charAt(0);

        int xy[] = play(board);
        System.out.print(xy[0] + " " + xy[1]);

		s.close();
	}
}