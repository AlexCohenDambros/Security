package KDC;
import java.util.Random;

public class Pessoa {
	private String id;
	private String k_mestre;
	private int nonce;
	

	public Pessoa(String id, String k_mestre){
		this.id = id;
		this.k_mestre = k_mestre;
	}	
	public String getID(){
		return this.id;
	}	
	public String getChaveMestre(){
		return this.k_mestre;
	}
	
	public int setGeradorNonce() {
		
		double ale= Math.random();
		this.nonce = (int) (100 + ale * (1000 - 100));
		return this.nonce;

		
	
	}
	
}
