package atelier1;

public class TestDe {
	public static void main(String args[]) {
		De de1 = new De(119, "d�d�");
		De de2 = new De(70, "paul-f�");
		De de3 = new De(6, "g�g�");
		System.out.println(de1.toString());
		// test lancer de d�
		System.out.println(de3.nb_lancer(6));
	}
}
