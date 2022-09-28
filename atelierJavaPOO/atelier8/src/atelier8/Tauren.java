package atelier8;

import java.util.Random;

public class Tauren extends Personnage {
	private int taille;	//représente la taille du Tauren exprimée en mètres
	private static Random r = new Random();
	
	/**
	 * constructeur de la classe
	 * @param nom
	 * @param age
	 * @param taille
	 */
	public Tauren(String nom, int age, int taille) {
		super(nom, age);
		this.taille = taille;
	}
	
	/**
	 * renvoie un entier représentant la position que souhaite 
	 * atteindre le personnage. Cette position est calculée en ajoutant à la position actuelle du 
	 * personnage un nombre aléatoire compris entre 1 et la valeur de l’attribut taille.
	 */
	public int positionSouhaitee() {
		return this.position + 1 + r.nextInt(this.taille);
	}

	/**
	 * redefinition de toString()
	 */
	public String toString() {
		return "Tauren " + nom;
	}
}
