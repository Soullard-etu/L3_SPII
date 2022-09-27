package exo1;

public class DeMemoire extends De {
	private int dernierLancer;
	private int res;
	
	public int lancer() {
		do {
			res = r.nextInt(this.nbrFaces)+1 ;
		}while(dernierLancer == res);
		
		dernierLancer = res;
		
		return res;
	}
}
