import java.util.*;
import java.lang.Math;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("Please enter a number between 1 and 379434:");
		int input = Integer.parseInt(scanner.nextLine());
		int win = (int)(Math.random()*(379434-1+1)+1);
		if (input == win){
			System.out.println("\nCongrats! you won. Take this: flag{GkwAhSnD3eBhHvsV1xSYUwsUE48WzG9Z}");
		} else {
			System.out.println("\nlol try again");
		}
	}
}