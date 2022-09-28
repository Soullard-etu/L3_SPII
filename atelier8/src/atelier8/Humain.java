package atelier8;

public class Humain extends Personnage {
	private int nbDeplacements;	//nombre de deplacement de l'humain durant la partie
	private int niveau;	//niveau de l'humain selon le nombre de deplacement

	/**
	 * constructeur de la classe
	 * @param nom
	 * @param age
	 */
	public Humain(String nom, int age) {
		super(nom, age);
		this.nbDeplacements = 0;
		this.niveau = 1;
	}
	
	/**
	 * redefinition de la methode deplacer(int destination, int gain)
	 */
	public void deplacer(int destination, int gain) {
		super.deplacer(destination, gain);
		this.nbDeplacements ++;
		if(this.nbDeplacements == 4)
			this.niveau = 2;
		else if(this.nbDeplacements == 6)
			this.niveau = 3;
	}	
	
	/**
	 * renvoie un entier représentant la position que souhaite 
	 * atteindre le personnage. Cette position est calculée en ajoutant à la position actuelle du 
	 * personnage, le niveau multiplié par le nombre de déplacements
	 */
	public int positionSouhaitee() {
		return this.position + this.niveau * this.nbDeplacements;
	}

	/**
	 * redefinition de toString()
	 */
	public String toString() {
		return "Humain " + this.nom;
	}
}
