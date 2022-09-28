package atelier8;

public class TestJeu {

	public static void main(String[] args) {
		int REPETITION = 5;
		int ETAPES = 4;
		int OBSTACLES = 10;
		Jeu AtelierPOO = new Jeu("AtelierPOO", ETAPES, OBSTACLES);
		
		Joueur Paul = new Joueur("Paul");
		Paul.ajouterPersonnage(new Tauren("Hector", 15, 10));
		Paul.ajouterPersonnage(new Humain("Jean", 10));
		
		Joueur Lucien = new Joueur("Lucien");
		Lucien.ajouterPersonnage(new Tauren("Hercule", 20, 5));
		Lucien.ajouterPersonnage(new Humain("Marie", 10));
	
		AtelierPOO.ajouterJoueur(Paul);
		AtelierPOO.ajouterJoueur(Lucien);
		
		for(int i = 0; i < REPETITION; i++) {
			AtelierPOO.lancerJeu();
			
			System.out.println(AtelierPOO.afficherParticipants());
			System.out.println(AtelierPOO.afficherResultats());
		}

	}

}
