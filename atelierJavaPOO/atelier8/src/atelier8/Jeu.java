package atelier8;

import java.util.ArrayList;
import java.util.Random;

public class Jeu {
	private String titre;	//titre
	private int NB_JOUEUR_MAX = 6;	// nombre maximum de joueur pouvant être inscrit à un jou
	private int NB_CASES = 50;	//nombre de cases du tableau sur lequel se déplacent les personnage
	private ArrayList<Joueur> listeJoueurs = new ArrayList<Joueur>();	//liste des joueurs inscits au jeu
	private Case cases[] = new Case[NB_CASES];	//tableau de Case représentant la liste des cases du jeu
	private int nbEtapes;	//correspondant au nombre de déplacements à réaliser par chacun des personnages au cours du déroulement du jeu
	private int nbObstacles;	//correspondant au nombre maximum d’obstacles présents dans le tableau des cases (il s’agit d’un nombre maximum car comme les obstacles sont générés de manière aléatoire, il n’est pas certain que ce nombre soit atteint lors de l’initialisation des cases).
	private int scoreMax;	//représentant le score maximum obtenu sur l’ensemble des lancements de jeux
	private boolean fistGame = true;
	private static Random r = new Random();
	
	/**
	 * constructeur de la classe
	 * @param titre
	 * @param nbEtapes
	 * @param nbObstacles
	 */
	public Jeu(String titre, int nbEtapes, int nbObstacles) {
		this.titre = titre;
		this.nbEtapes = nbEtapes;
		this.nbObstacles = nbObstacles;
	}

	/**
	 * ajoute le joueur  
	 * @param j
	 * à la liste des joueurs inscrits au jeu
	 */
	public void ajouterJoueur(Joueur j) {
		listeJoueurs.add(j);
	}

	/**
	 * renvoie un ArrayList de Personnage contenant la liste de tous les 
	 * personnages de tous les joueurs. Cet arrayList est construit en parcourant les listes de 
	 * personnages de chacun des joueurs du jeu
	 * @return
	 */
	public ArrayList<Personnage> tousLesPersos(){
		ArrayList<Personnage> listePersonnage = new ArrayList<Personnage>();
		listeJoueurs.forEach((jou) -> {
			jou.getArrayListePersonnages().forEach((per) -> {
				listePersonnage.add(per);
			});
		});
		return listePersonnage;
	}
	
	/**
	 * methode qui initialise le tableau de case selont moulte conditions provenent de lenonce
	 */
	public void initialiserCases() {
		int aleatoir;
		int nbCasesCree = 0;
		
		for (int i=0; i<NB_CASES;i++) {
			aleatoir = r.nextInt(NB_CASES+1);
			if((aleatoir%5 == 0) && (nbCasesCree < this.nbObstacles)) {
				Obstacle o = new Obstacle(aleatoir*2);
				cases[i] = new Case(aleatoir, o);
				nbCasesCree ++;
			}
			else
				cases[i] = new Case(aleatoir);
		}
	}
	
	public void lancerJeu() {
		int i = 0;
		int etap = 0;
		
		this.initialiserCases();

		for (Personnage per : this.tousLesPersos()) {
			if(cases[i].sansObstacle()) {
				cases[i].placerPersonnage(per);
				i++;
			}
			else {
				while(!cases[i].sansObstacle()) 
					i++;
				cases[i].placerPersonnage(per);
			}
		}
		
		while(etap < this.nbEtapes) {
			this.tousLesPersos().forEach((per) -> {
				int posSouh = per.positionSouhaitee();
				
				if(!(posSouh<this.NB_CASES)) {
					posSouh = this.NB_CASES-1;
				}
				if(cases[posSouh].estLibre()) {
					//eleve perso de la case precedent
					cases[per.getPosition()].enleverPersonnage();
					//perso se deplace
					per.deplacer(posSouh, cases[posSouh].getGain());
					//enregistre dans la case le nouveau perso
					cases[posSouh].placerPersonnage(per);
				}
				else{
					per.penaliser(cases[per.getPosition()].getGain());
				}
				
			});
			etap++;
			System.out.println(this.afficherCases());
		}
	}
	
	/**
	 * affiche le tableau des cases
	 */
	public String afficherCases() {
		String chaineRetour = "\n";
		for(int i = 0; i < this.NB_CASES; i++) {
			chaineRetour += "\nCase " + i + " : " + cases[i] + ")";
		}
		return chaineRetour;
	}
	
	/*
	 * affiche la liste des joueurs inscrits au jeu
	 */
	public String afficherParticipants() {
		String chaineRetour = "\nLISTE DES JOUEURS";
		
		for (Joueur jou : this.listeJoueurs )
			chaineRetour += "\n--------------------------\n" + jou;
		
		return chaineRetour;
	}
	
	/**
	 * @return le resultat de la partie
	 */
	public String afficherResultats() {
		Joueur gagnant = new Joueur("");
		String chaineRetour = "";
		
		gagnant.modifierPoints(-100000000);
		
		for (Joueur jou : this.listeJoueurs) {
			if(gagnant.getNbPoints() < jou.getNbPoints()) 
				gagnant = jou;
		}
		
		chaineRetour = "\nJEU AtelierPOO\n**********************************************\nRESULTATS\nLe gagnant est " + gagnant.getNom() + " avec " + Integer.toString(gagnant.getNbPoints()) + " points";
		
		if(!this.fistGame) {
			if(gagnant.getNbPoints()>this.scoreMax) {
				chaineRetour += "\nRecord battu : Ancien score maximun : " + this.scoreMax;
				this.scoreMax = gagnant.getNbPoints();
			}
			else
				chaineRetour += "\nRecord non battu : Score maximun : " + this.scoreMax;
		}
		else {
			chaineRetour += "\nRecord ettabli : Score maximun : " + gagnant.getNbPoints();
			this.scoreMax = gagnant.getNbPoints();
		}
			
		
		return chaineRetour;
	}
}

























