

import java.util.ArrayList;

public class Main{

    public static void main (String[] args){
        //java Main inputFiler/eksempel_input.txt outputFiler/eksempel_output.txt
        //java Main inputFiler/input_10.txt outputFiler/output_10.txt
        tre<Integer> treet= new tre<Integer>();
        
        
        inputLeser inputs= new inputLeser();
        //forste argument = input fil, andre argument = output fil
        ArrayList<String[]> input_data = inputs.lesInputFraFil(args[0]);
        ArrayList<String[]> output_data = inputs.lesInputFraFil(args[1]);

        kjorProgam(input_data, output_data,treet);
   

    }

    public static void kjorProgam(ArrayList<String[]> input_data, ArrayList<String[]> output_data, tre<Integer> tre){
        int outputLinje=0; //for aa telle hvilken ouput vi er paa
        int antallFeil=0;
        System.out.println("kjører");
        for (int i = 0; i< input_data.size(); i++){
            //lager forst tre fra input data
       
            String kommando = input_data.get(i)[0];
       

            if (input_data.get(i).length==2){ //dersom vi har f.eks bare size uten noe argument etter
                Integer tallArg = Integer.valueOf(input_data.get(i)[1]);

                if (kommando.equals("insert")){
                    tre.settInn(tre.hentRot(), tallArg);
                    System.out.println("setter inn: "+ tallArg);
                }

                else if (kommando.equals("contains")){
                    System.out.println("inneholder : " + tallArg + " : " + tre.contains(tre.hentRot(), tallArg));
                    String output = output_data.get(outputLinje)[0];
                    outputLinje+=1;
                    
                    //sammenligner med output
                    if (tre.contains(tre.hentRot(), tallArg)!=Boolean.parseBoolean(output)){
                        System.out.println("input og output ikke like");
                        antallFeil+=1;
                    }
                }

                else if (kommando.equals("remove")){
                    System.out.println("fjerner: "+ tallArg);
                    tre.remove(tre.hentRot(), tallArg);
                }
            }
            else {//dersom bare ett arg

                if (kommando.equals("size")){
                    System.out.println("storrelse: "+ tre.size(tre.hentRot()));
                    String output = output_data.get(outputLinje)[0];
                    outputLinje+=1;
                    if (tre.size(tre.hentRot())!=Integer.parseInt(output)){
                        System.out.println("input og output ikke like");
                        antallFeil+=1;
                    }
                }
            }
        }
        System.out.println("ferdig");
        System.out.println("Antall feil : "+ antallFeil);
    }
}
