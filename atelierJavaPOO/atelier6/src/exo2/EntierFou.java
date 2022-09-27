package exo2;

import java.util.Random;

public class EntierFou extends Entier{
	private int niveauDeFolie;
	private static Random r = new Random();

	public EntierFou(int borneMin, int borneMax, int niveauDeFolie) {
		super(borneMin, borneMax);
		this.niveauDeFolie = niveauDeFolie;
	}

	@Override
	public void increment() {
//		super.increment();
		this.setLentier(lentier+r.nextInt(this.niveauDeFolie));
	}
	
	
}
