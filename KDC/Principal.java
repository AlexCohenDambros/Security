package KDC;

import java.io.UnsupportedEncodingException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

import javax.crypto.BadPaddingException;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;

public class Principal {

	public static void main(String[] args) throws InvalidKeyException, IllegalBlockSizeException, BadPaddingException, NoSuchAlgorithmException, NoSuchPaddingException, UnsupportedEncodingException {
		
		Pessoa bob = new Pessoa("bob", "bolabolabolabola");
		Pessoa ana = new Pessoa("ana", "patopatopatopato");
		KDC kdc = new KDC(bob, ana);
		
		String parametro1 = bob.getID();
		byte[] parametro2 = AES.cifra(bob.getID(), bob.getChaveMestre());
		byte[] parametro3 = AES.cifra(ana.getID(), bob.getChaveMestre());
		
		kdc.GerarChaveSessao(parametro1, parametro2, parametro3);
		
		byte[] chaveSbob= kdc.getChaveSessaoBob();
		byte[] chaveSana= kdc.getChaveSessaoAna();
		
		String ChaveDeciBob = AES.decifra(chaveSbob, bob.getChaveMestre());
		String ChaveDeciAna = AES.decifra(chaveSana, ana.getChaveMestre());
		
		
		int noncef = ana.setGeradorNonce();
		
		byte[] NonceAna = AES.cifra(Integer.toString(noncef), ChaveDeciAna);
		String NonceBob = AES.decifra(NonceAna, ChaveDeciBob);
		
		int NewNonce = FuncaoAutenticacao.funcaoBobAna(Integer.parseInt(NonceBob));
		
		byte[] NewNonceBob = AES.cifra(Integer.toString(NewNonce), ChaveDeciBob);
		
		System.out.println("Nonce: " + noncef);
		System.out.println("Nonce Criptografado por Ana: " + new String(NonceAna));
		System.out.println("NewNonce feito pelo Bob: " + NewNonce);
		System.out.println("NewNonce Criptografado por Bob: " + new String(NewNonceBob));
		
		
		}
		
}

