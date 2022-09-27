package exo1;

public class DePipes extends De{
	private int borneMin;

	public DePipes(String nom, int nbrFaces, int borneMin) {
		super(nom, nbrFaces);
		if(borneMin<nbrFaces)
			this.borneMin = borneMin;
		else
			this.borneMin=0;
	}
	
	public int lancer() {
		return r.nextInt(this.nbrFaces + 1 - this.borneMin) + this.borneMin;
	}
}
