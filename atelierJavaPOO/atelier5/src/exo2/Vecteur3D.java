package exo2;

public class Vecteur3D {
		int x;
		int y;
		int z;
		
	public Vecteur3D(int x, int y, int z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}

	public Vecteur3D() {
		this(0, 0, 0);
	}
	
	public double Norme() {
		return Math.sqrt(x*x + y*y + z*z);
	}
	
	public double produitScalaire(Vecteur3D V) {		
		return this.x*V.x + this.y*V.y + this.z*V.z;
	}
	
	public static double produitScalaire(Vecteur3D V1, Vecteur3D V2) {		
		return V1.x*V2.x + V1.y*V2.y + V1.z*V2.z;
	}

	public Vecteur3D Somme(Vecteur3D V) {		
		return new Vecteur3D(this.x+V.x, this.y+V.y, this.z+V.z);
	}
	
	public static Vecteur3D Somme(Vecteur3D V1, Vecteur3D V2) {		
		return new Vecteur3D(V1.x+V2.x, V1.y+V2.y, V1.z+V2.z);
	}
	
	@Override
	public String toString() {
		return "<" + x + ", " + y + ", " + z + ">";
	}
		
	

}
