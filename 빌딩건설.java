package org.opentutorials.javatutorial.eclipse;
import java.util.Scanner;
public class ºôµù°Ç¼³ {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int [] dx= {-1,0, 1, -1,1,-1,0,1};
		int [] dy= {-1,-1,-1, 0,0,1,1,1};
		
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		
		for (int i=0;i<t;i++) {
			
			int n=sc.nextInt();
			char [][] block=new char [n][n];
			int [][] count=new int[n][n];
			for (int j=0;j<n;j++) {
				for (int k=0;k<n;k++) {
					char c=sc.next().charAt(0);
					block[j][k]=c;
				}
			}
			int max=0;
			for (int l=0;l<n;l++) {
				for(int m=0;m<n;m++) {
					
					if (block[l][m]=='G') {
						continue;
					}
					for(int x=0;x<dx.length;x++) {
						int tmp_x=m+dx[x];
						int tmp_y=l+dy[x];
						
						if(tmp_x>-1 && tmp_y>-1 &&tmp_x<n &&tmp_y<n) {
							char tmp_char=block[tmp_y][tmp_x];
							if(tmp_char=='G') {
								count[l][m]=2;
								if(max<2) max=2;
							}
						}
						
					}
					if(count[l][m]==0) {
						int b_count=0;
						for (int z=0;z<n;z++) {
							if(block[l][z]=='B') b_count+=1;
							if(block[z][m]=='B') b_count+=1;
						}
						if(b_count-1>max) {max=b_count-1; count[l][m]=b_count-1;}
					}
				}
			}
			System.out.println("#"+(i+1)+" "+max);
			
		}
		
	}

}
