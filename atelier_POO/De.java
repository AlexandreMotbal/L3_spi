package atelier1;

//zone des imports
import java.util.*;

public class De {
	// static final = constante de classe
	// static = de classe
	// final constant
	public static final int NB_MIN_FACES = 3;
	public static final int NB_MAX_FACES = 120;
	private static final int NB_DEFAULT_FACES = 6;
	private static final String DEFAULT_NAME = "titi";

	// Variable de classe
	public static Random rand = new Random();

	// Variable d'instances
	private int nbFaces;
	private String nom;

//-----------Constructeur par defaut----------
	public De() {
		this(NB_DEFAULT_FACES);
		nom = DEFAULT_NAME;
	}

	public De(int nFaces) {
		this.setNbFaces(nFaces);
		nom = DEFAULT_NAME;
	}

	public De(int nFaces, String inputNom) {
		this.setNbFaces(nFaces);
		this.setNom(inputNom);
	}

//----------To string---------
	public String toString() {
		return "le dé possède" + nbFaces + "et s'appelle " + nom;
	}

//acesseurs et modificateurs : getter et setter
	public int getNbFaces() {
		return nbFaces;
	}

	public void setNbFaces(int nvNbFaces) {
		if ((nvNbFaces > NB_MIN_FACES) && (nvNbFaces <= NB_MAX_FACES)) {
			nbFaces = nvNbFaces;
		} else {
			System.err.println(
					"Attention le nombre de faces doit être compris entre" + NB_MIN_FACES + "et" + NB_MAX_FACES);
		}
	}

	public String getNom() {
		return nom;
	}

	private void setNom(String nvNom) {
		if (nvNom != "" && nvNom != null) {
			nom = nvNom;
		} else {
			System.err.println("Attentino le nom n'est pas valide");
		}
	}

// méthodes d'instances

	public int lancer() {
		int result;
		result = 1 + rand.nextInt(nbFaces);
		return result;
	}

	public int nb_lancer(int nombre_lancer) {
		int meilleur_lancer = 0;
		int nbr_lancer = nombre_lancer;
		for (int n = 0; n < nbr_lancer; n++) {
			if (meilleur_lancer < this.lancer()) {
				meilleur_lancer = this.lancer();
			}
		}
		return meilleur_lancer;
	}

	public String show() {
		result = "Le lancé du "+nom_instance+ "donne" this.lancer();
	}
}

public class Depipe extends De {
	public int lancer_pipe(int score_minimum) {
		private int result = 0;
		while (result < score_minimum) {
			result = this.lancer();
		}

		return result;
	}
}
