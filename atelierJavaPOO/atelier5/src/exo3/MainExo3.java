package exo3;

import java.util.Random;

public class MainExo3 {
	public static void main(String[] args) {

		System.out.println(Math.PI);

		Random r = new Random();
        double n = r.nextDouble(1);
        System.out.println(n);
		
        Random j = new Random();
        int in = j.nextInt(3);
        System.out.println(in+1);
		
        int x1 = j.nextInt(3);
        int x2 = j.nextInt(3);
        System.out.println(Math.max(x1, x2));
        
        String n1 = "yaya";
        String n2 = "mais non";
        if (n1.compareTo(n2) > 0)
        	System.out.println(n2);
        else
        	System.out.println(n1);
        
   
	}
}
