package atelier8;

public class Case {
	private int gain;	//correspondant au nombre de points à ajouter au joueur propriétaire du personnage lorsque celui-ci se place sur la case. Ce nombre représente également le nombre de points à retrancher au joueur si son personnage tente de se placer sur la case alors qu’elle est déjà occupée par un autre personnage
	private Personnage perso;	//représentant le personnage présent sur la case. Cet attribut a la valeur null si aucun personnage n’est présent sur la case
	private Obstacle obs;	//représentant l’obstacle présent sur la case. Cet attribut a la valeur null si aucun obstacle n’est présent sur la case
	
	/**
	 * constructeur de la classe a deux parametres
	 * @param gain
	 * @param obs
	 */
	public Case(int gain, Obstacle obs) {
		this.gain = gain;
		this.obs = obs;
		this.perso = null;
	}
	
	/**
	 * constructeur a un seul parametre
	 * @param gain
	 */
	public Case(int gain) {
		this(gain, null);
	}
	
	/**
	 * retourne la penaliter de l'obstacle lier a case
	 * @return
	 */
	public int getPenalite() {
		if(this.obs != null)
			return this.obs.getPenlite();
		return 0;
	}
	
	public int getGain() {
		return this.gain;
	}
	
	/**
	 * positionement du Personnage 
	 * @param perso
	 */
	public void placerPersonnage(Personnage perso) {
		this.perso = perso;
	}
	
	/**
	 * positionement de l'Obstacle
	 * @param obs
	 */
	public void placerObstacle(Obstacle obs) {
		this.obs = obs;
	}
	
	/**
	 * affecte la valeur null au personnage perso associé à la case
	 */
	public void enleverPersonnage() {
		if(this.perso != null)
			this.perso = null;
	}
	
	/**
	 * si this.obs == null
	 * @return true 
	 */
	public boolean sansObstacle() {
		return this.obs == null;
	}
	
	/**
	 * si this.perso == null
	 * @return true
	 */
	public boolean sansPerso() {
		return this.perso == null;
	}
	
	/**
	 * si this.obs == null && this.perso == null
	 * @return true
	 */
	public boolean estLibre() {
		return sansObstacle() && sansPerso();
	}

	@Override
	public String toString() {
		if(this.estLibre())
			return "Libre (gain = " + this.gain;
		else if(!this.sansObstacle())
			return "Obstacle (penalite = " + this.obs.getPenlite();
		else
			return this.perso + " (penalite = -" + this.gain;
	}
}


























