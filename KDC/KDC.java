package KDC;

import java.io.UnsupportedEncodingException;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Random;

import javax.crypto.BadPaddingException;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.NoSuchPaddingException;

public class KDC {
	
	private Pessoa bob;
	private Pessoa ana;
	private byte[] k_s_bob;
	private byte[] k_s_ana;
		
	public KDC(Pessoa bob, Pessoa ana)
	{
		this.bob = bob;
		this.ana = ana;
	}
	
	public String getChaveSessao()
	{
		int qtdeMaximaCaracteres = 16;
	    String[] caracteres = { "0", "1", "b", "2", "4", "5", "6", "7", "8",
	                "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
	                "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
	                "x", "y", "z"};
	    
		StringBuilder senha = new StringBuilder();

        for (int i = 0; i < qtdeMaximaCaracteres; i++) {
            int posicao = (int) (Math.random() * caracteres.length);
            senha.append(caracteres[posicao]);
        }
        return senha.toString();
        
	}
	
	public void GerarChaveSessao(String id, byte[] idCifrado, byte[] destinatarioCifrado) throws InvalidKeyException, IllegalBlockSizeException, BadPaddingException, NoSuchAlgorithmException, NoSuchPaddingException, UnsupportedEncodingException
	{
		String novoID = AES.decifra(idCifrado, bob.getChaveMestre());
		
		if( id.equals(novoID) )
		{
			System.out.println("Autenticação realizada com sucesso");
			String destinatario = AES.decifra(destinatarioCifrado, bob.getChaveMestre());
			
			if( destinatario.equals(ana.getID()) )
			{
				String chaveSessao = getChaveSessao();
				k_s_bob = AES.cifra(chaveSessao, bob.getChaveMestre());
				k_s_ana = AES.cifra(chaveSessao, ana.getChaveMestre());	
			}			
		}
		else
		{
			System.out.println("Autenticação invalida");
		}
	}
	
	public byte[] getChaveSessaoBob() {
		return this.k_s_bob;
	}
	
	public byte[] getChaveSessaoAna() {
		return this.k_s_ana;
	}
	
	
}
