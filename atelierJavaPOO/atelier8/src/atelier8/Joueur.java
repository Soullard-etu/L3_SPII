package atelier8;

import java.util.ArrayList;

public class Joueur {
	private String nom;		//nom du joueurs
	private String code;	//de la forme J suivi d’un numéro correspondant au numéro d’ordre de création du joueur (par exemple : J1 pour le premier joueur, J2 , ..ect…). Il est généré automatiquement lors de la création d’un joueur
	private static int nbJoueurs = 0;	//represente le nombre de joueurs créés
	private int nbPoints;	//represente le nombre de points gagnés
	private ArrayList<Personnage> listePersos = new ArrayList<Personnage>();	//liste des personnages appartenant au joueur
	
	/**
	 * constructeur de la classe
	 * @param nom
	 */
	public Joueur(String nom) {
		this.nom = nom;
		this.code = "J" + (nbJoueurs + 1);
		nbPoints = 0;
		nbJoueurs ++;
	}

	/*
	 * methode qui ajoute un personnage a la liste des personnages du joueur
	 */
	public void ajouterPersonnage(Personnage p) {
		listePersos.add(p);
		p.setProprietaire(this);
	}

	/*
	 * modifi les points du joueur
	 */
	public void modifierPoints(int nb) {
		if((this.nbPoints += nb) >= 0)
			this.nbPoints += nb;
		else
			this.nbPoints = 0;
	}
	
	/**
	 * test si le joueur possed au moins un personnage
	 * @return true si oui, false si non
	 */
	public boolean peutJouer() {
		boolean retour = false;
		
		if(this.listePersos != null)
			retour = true;
		
		return retour;
	}
	
	/**
	 * 
	 * @return liste des personnages du joueur
	 */
	public ArrayList<Personnage> getArrayListePersonnages(){
		return this.listePersos;
	}

	/**
	 * redefinition de toString()
	 */
	public String toString() {
		if(this.peutJouer())
			return code + " " + nom + "(" + this.nbPoints + " points) avec " + this.listePersos.size() + " personnage(s)";
		else
			return code + " " + nom + "(" + this.nbPoints + " points) avec aucun personnage(s)";
	}

	/**
	 * @return le nombre de points du joueur
	 */
	public int getNbPoints() {
		return this.nbPoints;
	}

	/**
	 * @return nom du joueur
	 */
	public String getNom() {
		return this.nom;
	}
}
