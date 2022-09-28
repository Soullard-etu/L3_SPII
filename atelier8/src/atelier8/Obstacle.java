package atelier8;

public class Obstacle {
	private int penlite; //caractérise l’obstacle c’est-à-dire le nombre de points à retrancher au joueur qui le rencontre

	/*
	 * constructeur avec un
	 * @para de type integer pour definir la pénalité
	 */
	public Obstacle(int penlite) {
		this.penlite = penlite;
	}

	/*
	 *methode pour recuperer la  
	 * @return pénalité
	 */
	public int getPenlite() {
		return penlite;
	}
}
