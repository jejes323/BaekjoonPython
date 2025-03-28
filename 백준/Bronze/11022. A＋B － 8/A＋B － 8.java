import java.util.*;

public class Main {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		
		int tcase = input.nextInt();
		int[] a = new int[tcase];
		int[] b = new int[tcase];
		int[] sum = new int[tcase];
		
		for(int i =0; i < tcase; i++) {
			a[i] = input.nextInt();
			b[i] = input.nextInt();
			sum[i] = a[i] + b[i];
		}
		
		for(int i = 0; i < tcase; i++) {
			System.out.printf("Case #%d: %d + %d = %d\n", i + 1, a[i], b[i], sum[i]);
		}
		
		input.close();
	}

}
