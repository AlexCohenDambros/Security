import java.lang.String;

public class CifradeCesar {
	
	   public static String cifrar(String original, int k) {
	        String alfabeto = "abcdefghijklmnopqrstuvwxyz";

	        // deslocar de k
	        StringBuilder resultado = new StringBuilder();
	        for (char ch : original.toLowerCase().toCharArray())
	        {
	            if (ch == ' ') {
	                resultado.append(' ');
	                continue;
	            }

	            int chr = ch - alfabeto.charAt(0);
	            chr = (chr + k) % alfabeto.length();
	            if (chr < 0)
	                chr += alfabeto.length();
	            chr += alfabeto.charAt(0);
	            resultado.append((char)chr);
	        }
	        return resultado.toString();
	    }

	    public static void main(String [] args)
	    {
	    	
	    	//Texto original
	        String texto = "Ola mundo";
	        System.out.println("-------------------------------");
	        System.out.println("Texto Original: " + texto);

	        String resultado = cifrar(texto, 3);
	        
	        //Texto Criptografado
	        System.out.println("-------------------------------");
	        System.out.println("Texto Criptografado: " + resultado);
	        
	        
	        //FORÇA BRUTA
	        System.out.println("-------------------------------");
	        System.out.println("Tentando Descriptografar com força bruta: \n");

	        for (int i = 0; i<27; i++) {
	            System.out.println("Tentativa: " + cifrar(resultado, -i));
	        }

	    }
	}
