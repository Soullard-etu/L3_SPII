package exo2;

import java.util.Objects;

public class Entier {
	private int borneMin;
	private int borneMax;
	protected int lentier;
	
	public Entier(int borneMin, int borneMax) {
		this.borneMin = borneMin;
		this.borneMax = borneMax;
		lentier=0;
	}

	public void setLentier(int lentier) {
		if(lentier>=this.borneMin && lentier <= this.borneMax)
				this.lentier = lentier;
	}
	
	public void increment() {
		this.setLentier(lentier+1);
	}

	public String toString() {
		return "" + this.lentier;
	}

	public boolean equals(Object obj) {
		if (this == obj)
			return true;
		if (obj == null)
			return false;
		if (getClass() != obj.getClass())
			return false;
		Entier other = (Entier) obj;
		return borneMax == other.borneMax && borneMin == other.borneMin && lentier == other.lentier;
	}


}
