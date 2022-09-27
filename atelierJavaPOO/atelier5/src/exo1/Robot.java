package exo1;

public class Robot {
	private
		String nom;
		String reference;
		int x;
		int y;
		int orientation;					// 1=Nord 2=Est 3=Sud 4=Ouest
		static int nbrRobot = 0;
	
	public Robot(String nom, int x, int y, int orientation) {
		super();
		this.setNom(nom);
		this.x = x;
		this.y = y;
		this.orientation = orientation;
		nbrRobot ++;
		this.reference = "ROB" + Integer.toString(nbrRobot);
	}

	public Robot(String nom, int x, int y) {
		super();
		this.setNom(nom);
		this.x = x;
		this.y = y;
		this.orientation = 1;
		nbrRobot ++;
		this.reference = "ROB" + Integer.toString(nbrRobot);
	}

	public int getOrientation() {
		return orientation;
	}

	public void setOrientation(int orientation) {
		this.orientation = orientation;
	}

	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	}
	
	public int deplace(int i) {
		int ereur = 1;
		switch(orientation) {
			case 1:
				x += i;
				
			case 2:
				y += i;
				
			case 3:
				if (0 < x)
					x-= i;
				else 
					ereur = 0;
				
			case 4:
				if (0 < y)
					y -= i;
				else
					ereur = 0;
		}
		
		return ereur; // 0 = limite depace  1 = ok
		
	}
	
	public String afficheToi() {
//		System.out.printf(string);
//		System.out.printf(format, arguments);
		String chaine;
		//System.out.printf("Nom: %s, reference: %s\nx: %d\ny: %d\norientation: ", this.nom, this.reference, this.x, this.y);
		chaine = "Nom: " + this.nom + ", reference: " + this.reference + "\nx: " + this.x + "\ny: " + this.y + "\norientation: ";

		if (this.orientation == 1)
			chaine += "Nord\n";
		else if (this.orientation == 2)
			chaine += "Est\n";
		else if (this.orientation == 3)
			chaine += "Sud\n";
		else if (this.orientation == 4)
			chaine += "Ouest\n";
		
		return chaine;
	}
	
	public String toString(){
		return this.afficheToi();
	}
	
}
