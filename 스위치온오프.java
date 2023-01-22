package org.opentutorials.javatutorial.eclipse;
import java.util.Scanner;
public class 스위치온오프 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		
		int n=sc.nextInt();
		int m=sc.nextInt();
		int [] button=new int [n];
		int [] push=new int[m];
		for(int i=0;i<m;i++) {
			int x=sc.nextInt();
			push[i]=x;
		}
		
		for (int j=0;j<m;j++) {
			int toggle=push[j];
			for(int k=1;k*toggle<=n;k++) {
				if(button[(toggle*k)-1]==0) button[(toggle*k)-1]=1;
				else if (button[(toggle*k)-1]==1) button[(toggle*k)-1]=0;
			}
		}
		
		for (int x:button) {
			System.out.print(x + " ");
		}
		
	}
}