package org.opentutorials.javatutorial.eclipse;

import java.util.Scanner;

public class Bridge_P {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		
		// n * n ũ�� �迭 ���� ( ���� )
		int[][] map = new int[n][n];
		
		// ���� ���� �Է� �ޱ�
		for ( int i=0 ; i<n ; i++ ) {
			for ( int j=0 ; j<n ;j++ ) {
				map[i][j] = sc.nextInt();
			}
		}
		
		// �ִ밪 ����
		int maxDistance = 0;
		
		for ( int i=0 ; i<n ; i++) {
			for ( int j=0 ; j<n ; j++ ) {
				
				// ���� ��ġ�� ������ �˻�
				if ( map[i][j]==1 ) {
					
					// ���̸� ���� ��ġ�κ��� ���Ž�� �Ͽ� ���� �Ǵ� ���ο� �ִ� ���� �Ÿ� ����, �ִ밪 ����				  
					//**nt [] dx= {0,0,1,-1};
					//int [] dy= {1,-1,0,0};

					//for (int k=0;k<dx.lenth;k++){
					//	int tmp_x=j+dx[k];
					//	int tmp_y=i+dy[k];
					//	if(tmp_x>-1 && tmp_y>-1 && tmp_x<n &&tmp_y<n) {
					//		int tmp_num=island[tmp_x][tmp_y];
					//		maxDistance+=1;
					//}
					//**//
					
					// ������ 1���� �˻�
					for (int d = 1; j+d<n ; d++) {
						if ( map[i][j+d]==1 ) {
							maxDistance = Math.max( maxDistance , d );
							break;
						}
					}
					
					// ������ 1���� �˻�
					for (int d = 1; j-d>-1 ; d++) {
						if ( map[i][j-d]==1) {
							maxDistance = Math.max(maxDistance , d );
							break;
						}
					}
					
					// ������ 1���� �˻�
					for (int d = 1; i-d>-1 ; d++) {
						if ( map[i-d][j]==1 ) {
							maxDistance = Math.max(maxDistance , d);
							break;
						}
					}
					
					// ������ 1���� �˻�
					for (int d = 1; d+i<n ; d++) {
						if ( map[i+d][j]==1 ) {
							maxDistance = Math.max(maxDistance , d);
							break;
						}
					}
				}
			}
		}
		
		System.out.println(maxDistance);

	}
}
