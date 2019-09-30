import java.util.*;

public class main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        char[] ID = "stanle".toCharArray();

        prt("Introduzca la cadena de texto: ");
        String txtInput = sc.nextLine();

        List<Integer> m = matching(txtInput.toLowerCase(), ID);
        prt(m);
        prt("\n");
        String aux = "";
        for(int x : m){
            aux += txtInput.charAt(x);
        }
        prt("\n");
        prt(aux);
    }
 
    private static List<Integer> matching(String s, char[] ID){
        List<Integer> pos = new ArrayList<Integer>(); 

        for(int i = 0; i < s.length(); i++){
            for(char x : ID){
                if(s.charAt(i) == x){
                    pos.add(i);
                }
            }
        }
        return pos;
    }
       
    private static void prt(Object s){
        System.out.println(s);
    }
}