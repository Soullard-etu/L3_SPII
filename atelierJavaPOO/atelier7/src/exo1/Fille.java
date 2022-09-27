package exo1;

import java.util.GregorianCalendar;

public class Fille extends Personne {
	private double salaire;
    private final GregorianCalendar dateDEmbauche;
    
	public Fille(String leNom, String lePrenom, GregorianCalendar laDate, Adresse lAdresse, double salaire,
			GregorianCalendar dateDEmbauche) {
		super(leNom, lePrenom, laDate, lAdresse);
		this.salaire = salaire;
		this.dateDEmbauche = dateDEmbauche;
	}
    
	
    
 
}
