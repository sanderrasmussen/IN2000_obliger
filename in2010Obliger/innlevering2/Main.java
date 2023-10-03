
//notater
//OOPS husk å fikse size metoden og optdatere variabler istendenfor å hele tiden loope igjennom treet
import java.util.ArrayList;

public class Main{

    public static void main (String[] args){
        //java Main inputFiler/eksempel_input.txt outputFiler/eksempel_output.txt
       //java Main inputFiler/input_10.txt outputFiler/output_10.txt 
        //java Main inputFiler/input_100.txt outputFiler/output_100.txt
        //java Main inputFiler/input_1000.txt outputFiler/output_1000.txt
        tre<Integer> treet= new tre<Integer>();
        avltre<Integer> avlTre = new avltre<Integer>();
        
        inputLeser inputs= new inputLeser();
        //forste argument = input fil, andre argument = output fil
        ArrayList<String[]> input_data = inputs.lesInputFraFil(args[0]);
        ArrayList<String[]> output_data = inputs.lesInputFraFil(args[1]);

        //kjorProgam(input_data, output_data,treet);
        //OOPS AVL TRE GJØR INGEN ROTASJONER
        //avlTre.settInn(avlTre.hentRot(), 2);
       // avlTre.settInn(avlTre.hentRot(), 4);
        // avlTre.settInn(avlTre.hentRot(), 3);
       // avlTre.settInn(avlTre.hentRot(), 5);
        // avlTre.settInn(avlTre.hentRot(), 6);
      
       // avlTre.venstreRotasjon(avlTre.hentRot());// har teori om at feil ligger i rotasjonsmetodene ved at de sletter pekere , --oppdaterte rot pekeren
        //avlTre.settInn(avlTre.hentRot(), 2);
        //avlTre.settInn(avlTre.hentRot(), 2);
        //avlTre.settInn(avlTre.hentRot(), 6);
        //avlTre.settInn(avlTre.hentRot(), 1);
        //avlTre.settInn(avlTre.hentRot(), 7);
       // System.out.println(avlTre.contains(avlTre.hentRot(), 4));
       //System.out.println(avlTre.hentRot().hentInnhold());
       // System.out.println(" " + avlTre.hentRot().hentVenstre().hentInnhold() + " " + avlTre.hentRot().hentHoyre().hentInnhold());
        //System.out.println(avlTre.hentRot().venstreBarn.venstreBarn.hentInnhold());
       //System.out.println(avlTre.hentRot().hoyreBarn.hoyreBarn.hentInnhold());
        //System.out.println(avlTre.hoyde(avlTre.hentRot()));
        //System.out.println(avlTre.size());
        //System.out.println("kjør");
        kjorProgam(input_data, output_data, avlTre);
        //kjorProgam(input_data, output_data, treet);

    }

    public static void kjorProgam(ArrayList<String[]> input_data, ArrayList<String[]> output_data, tre<Integer> tre){
        int outputLinje=0; //for aa telle hvilken ouput vi er paa
        int antallFeil=0;
        //System.out.println("kjører");
        for (int i = 0; i< input_data.size(); i++){
            //lager forst tre fra input data
       
            String kommando = input_data.get(i)[0];
       
            if (input_data.get(i).length==2){ //dersom vi har f.eks bare size uten noe argument etter
                Integer tallArg = Integer.valueOf(input_data.get(i)[1]);

                if (kommando.equals("insert")){
                    tre.settInn(tre.hentRot(), tallArg);
                   // System.out.println("setter inn: "+ tallArg);
                }

                else if (kommando.equals("contains")){
                    //System.out.println("inneholder : " + tallArg + " : " + tre.contains(tre.hentRot(), tallArg));
                    System.out.println(tre.contains(tre.hentRot(), tallArg));
                    String output = output_data.get(outputLinje)[0];
                    outputLinje+=1;
                    
                    //sammenligner med output
                    if (tre.contains(tre.hentRot(), tallArg)!=Boolean.parseBoolean(output)){
                        System.out.println("input og output ikke like");
                        antallFeil+=1;
                    }
                }

                else if (kommando.equals("remove")){
                    //System.out.println("fjerner: "+ tallArg);
                    tre.remove(tre.hentRot(), tallArg);
                }
            }
            else {//dersom bare ett arg

                if (kommando.equals("size")){
                    //System.out.println("storrelse: "+ tre.calcSize(tre.hentRot()));
                    System.out.println(tre.calcSize(tre.hentRot()));
                    String output = output_data.get(outputLinje)[0];
                    outputLinje+=1;
                    if (tre.calcSize(tre.hentRot())!=Integer.parseInt(output)){
                        System.out.println("input og output ikke like");
                        antallFeil+=1;
                    }
                }
            }
        }
        //System.out.println("ferdig");
        //for testing
        //System.out.println(tre.hoyde(tre.hentRot()));
        System.out.println("Antall feil : "+ antallFeil);
    }
}
