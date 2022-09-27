package exo2;

public class MainEx2 {

	public static void main(String[] args) {
		Vecteur3D v1 = new Vecteur3D(2,3,4);
		Vecteur3D v2 = new Vecteur3D(1,2,3);
//		Vecteur3D v3 = Vecteur3D.Somme(v1, v2);
		Vecteur3D v3 = v1.Somme(v2);
		
		System.out.println(v3);
	}

}
