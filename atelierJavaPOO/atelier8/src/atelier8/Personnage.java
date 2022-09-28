package atelier8;

abstract class Personnage {
	protected String nom;	//nom 
	private int age;	//age
	protected int position;	//position (numéro de case) du personnage dans le tableau des cases du jeu
	private Joueur proprietaire;	//Joueur proprietaire du personnage
	
	/**
	 * constructeur de la classe
	 * @param nom
	 * @param age
	 */
	public Personnage(String nom, int age) {
		this.nom = nom;
		this.age = age;
	}
	
	/**
	 * modifie la position du personnage en lui 
	 * attribuant la valeur du paramètre destination et augmente le nombre de points de son joueur 
	 * propriétaire de la valeur du paramètre gain
	 * @param destination
	 * @param gain
	 */
	public void deplacer(int destination, int gain) {
		this.position = destination;
		this.proprietaire.modifierPoints(gain);
	}
	
	/**
	 * set le proprio
	 * @param proprietaire
	 */
	public void setProprietaire(Joueur proprietaire) {
		this.proprietaire = proprietaire;
	}

	/**
	 * diminue le nombre de points de son joueur propriétaire 
	 * de la valeur du paramètre penalite
	 * @param penaliter
	 */
	public void penaliser(int penaliter) {
		this.proprietaire.modifierPoints(-penaliter);
	}
	
	/**
	 * 
	 * @return position du perso
	 */
	public int getPosition() {
		return this.position;
	}
 
	/**
	 * redefinition de toString()
	 */
	public String toString() {
		return nom;
	}
	
	/**
	 * methode abstraite qui oblige une definition de la methode dans les classe de specification
	 * @return
	 */
	abstract int positionSouhaitee();
}
