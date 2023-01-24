package org.opentutorials.javatutorial.eclipse;
import java.util.Scanner;
public class blackqueen {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int t = sc.nextInt();
		int [] answer= new int[t];
		
		int [] dx = {};
		int [] dy = {};
		
		for (int j =0 ;j<t;j++) {
			
			int n = sc.nextInt();
			int [] loc = new int[4];
			for (int i=0; i<4;i++) {
				loc[i]=sc.nextInt();
			}
			int w_x = loc[0];
			int w_y = loc[1];
			int b_x = loc[2];
			int b_y = loc[3];
			
			if ((w_x-b_x)==0 || (w_y-b_y)==0) {
				answer[j]=1;
			}
			else if ((w_x-b_x)==(w_y-b_y)) {
				answer[j]=1;
			}
			else {
				answer[j]=0;
			}
			
			
			
		}
		for(int k =0; k<answer.length;k++) {
			System.out.println(answer[k]);
		}

	}

}
