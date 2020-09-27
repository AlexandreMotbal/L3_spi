package atelier1;

public class TestDe {
	public static void main(String args[]) {
		De de1 = new De(119, "dédé");
		De de2 = new De(70, "paul-fé");
		De de3 = new De(6, "gégé");
		System.out.println(de1.toString());
		// test lancer de dé
		System.out.println(de3.nb_lancer(6));
	}
}
