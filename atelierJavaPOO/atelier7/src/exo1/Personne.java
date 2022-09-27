package exo1;

import java.util.GregorianCalendar;
import java.util.Objects;
import java.util.Calendar;
//import java.util.LocalDate;

public class Personne{
    private static final Adresse ADRESSE_INCONNUE = null;
    private String nom;
    private String prenom;
    private final GregorianCalendar dateNaissance;
    private Adresse adresse=ADRESSE_INCONNUE;
    private static int nbrPersonnes=0;
	
	/**
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le pr�nom de la personne
	 * @param laDate la date de naissance de la personne
	 * @param lAdresse l'adresse de la personne
	 */
	public Personne(String leNom,String lePrenom, GregorianCalendar laDate, Adresse lAdresse){
		nom = leNom.toUpperCase();
		prenom=lePrenom;
		dateNaissance=laDate;
		adresse=lAdresse;
		nbrPersonnes++;
	}
	
	/** 
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le pr�nom de la personne
	 * @param j le jour de naissance
	 * @param m le mois de naissance
	 * @param a l'ann�e de naissance
	 * @param numero le n� de la rue
	 * @param rue la rue
	 * @param code_postal le code postal de l'adresse
	 * @param ville la ville ou la personne habite
	 */
	public Personne(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville){
		this(leNom, lePrenom, new GregorianCalendar(a,m,j),new Adresse(numero,rue,code_postal,ville));
	}

	/**
	 * Accesseur
	 * @return retourne le nom
	 */
	public String getNom(){
		return nom;
	}
	/**
	 * Accesseur
	 * @return retourne le pr�nom
	 */
	public String getPrenom(){
		return prenom;
	}
	/**
	 * Accesseur
	 * @return retourne la date de naissance	 
	 */
	public GregorianCalendar getDateNaissance() {
		return dateNaissance;
	}
	/**
	 * Accesseur
	 * @return retourne l'adresse	 
	 */
	public Adresse getAdresse() {
		return adresse;
	}
	/**
	 * Modificateur
	 * @param retourne l'adresse	 
	 */
	public void setAdresse(Adresse a) {
		adresse=a;
	}
		
	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	public String toString(){
		String result="\nNom : "+nom+"\n"
		+"Pr�nom : "+prenom+"\n"+
		"N�(e) le : "+dateNaissance.get(Calendar.DAY_OF_MONTH)+
		"-"+dateNaissance.get(Calendar.MONTH)+
		"-"+dateNaissance.get(Calendar.YEAR)+"\n"+
		"Adresse : "+
		adresse.toString();
		return result;
	}

	public static int getNbrPersonnes() {
		return nbrPersonnes;
	}
	
	public static boolean plusAgee(Personne p1, Personne p2) {
		boolean retour = false;
		
		if (p1.dateNaissance.get(Calendar.YEAR)<p2.dateNaissance.get(Calendar.YEAR))
			retour = true;
		else if (p1.dateNaissance.get(Calendar.YEAR)>p2.dateNaissance.get(Calendar.YEAR))
			retour = false;
		else if(p1.dateNaissance.get(Calendar.MONTH)<p2.dateNaissance.get(Calendar.MONTH))
			retour = true;
		else if (p1.dateNaissance.get(Calendar.MONTH)>p2.dateNaissance.get(Calendar.MONTH))
			retour = false;
		else if (p1.dateNaissance.get(Calendar.DAY_OF_MONTH)<p2.dateNaissance.get(Calendar.DAY_OF_MONTH))
			retour = true;
		
		return retour;
	}
	
	public boolean plusAgee(Personne p2) {
		boolean retour = false;
		
		if (this.dateNaissance.get(Calendar.YEAR)<p2.dateNaissance.get(Calendar.YEAR))
			retour = true;
		else if (this.dateNaissance.get(Calendar.YEAR)>p2.dateNaissance.get(Calendar.YEAR))
			retour = false;
		else if(this.dateNaissance.get(Calendar.MONTH)<p2.dateNaissance.get(Calendar.MONTH))
			retour = true;
		else if (this.dateNaissance.get(Calendar.MONTH)>p2.dateNaissance.get(Calendar.MONTH))
			retour = true;
		else if (this.dateNaissance.get(Calendar.DAY_OF_MONTH)<p2.dateNaissance.get(Calendar.DAY_OF_MONTH))
			retour = true;
		
		return retour;
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		else if (obj == null)
			return false;
		else if (getClass() != obj.getClass())
			return false;
		Personne other = (Personne) obj;
		return Objects.equals(dateNaissance, other.dateNaissance) && Objects.equals(nom, other.nom)
				&& Objects.equals(prenom, other.prenom);
	}
	
}

    
   
   