package org.opentutorials.javatutorial.eclipse;
import java.util.Scanner;
public class islandtravel {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String maps=sc.next();
		String[] tmp_map=maps.split(",");
		int len= tmp_map.length;
		char[][]map=new char[len][len];
		int i=0;
		int j=0;
		for(char c: maps.toCharArray()) {
			if(c!='"' && c!='[' && c!=']' &&c!='"'&&c!=',') {
				map[i][j]=c;
				if(j<len-1) {
					j+=1;
				}
				else {
					i+=1;
					j=0;
				}
			}
		}
		
	}

}
