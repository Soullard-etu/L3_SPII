package exo1;

import java.util.Random;

public class De {
	private String nom;
	int nbrFaces;	//min=3 max=120
	private static int nbrDe = 0;
	protected static Random r = new Random();
	private static int BORNE_MIN = 3;
	private static int BORNE_MAX = 120;
	
	public De(String nom, int nbrFaces) {
		if(nom!="")
			this.nom = nom;
		else
			this.nom = "De n°" + (nbrDe+1);
		this.nbrFaces = nbrFaces;
		nbrDe++;
	}

	public De(int nbrFaces) {
		this("De n°" + (nbrDe+1), nbrFaces);
	}

	public De(String nom) {
		this(nom, 6);
	}
	
	public De() {
		this("De n°" + nbrDe, 6);
	}

	public int getNbrFaces() {
		return nbrFaces;
	}
	
	public void setNbrFaces(int nbrFaces) {
		if((BORNE_MIN <= nbrFaces) && (nbrFaces <= BORNE_MAX)) 
			this.nbrFaces = nbrFaces;
			
		else 
			System.out.println("Hors des limite");
	}

	public String getNom() {
		return nom;
	}
	
	public int lancer() {
		return r.nextInt(this.nbrFaces + 1);
	}
	
	public int lancer(int nb) {
		int res=0;
		int test=0;
		for (int i=0; i < nb; i++) {
			test = lancer();
			if(res < test)
				res = test;
		}
		return res;
	}

	public String toString() {
		return "De [nom=" + nom + ", nbrFaces=" + nbrFaces + "]";
	}
	
	public boolean equals(De anotherObject) {
		if(this == anotherObject)
			return true;
		return ((this.nom == anotherObject.nom) && (this.nbrFaces == anotherObject.nbrFaces));  //true si De equal
	}
}
