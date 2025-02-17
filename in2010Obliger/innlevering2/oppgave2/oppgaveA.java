import java.util.ArrayList;


public class oppgaveA{

    public static void main(String[] args){
        ArrayList<Integer> sekvens = new ArrayList<>();
        for (int i = 0; i< args.length; i++){
            sekvens.add((Integer.parseInt(args[i])));
        }
            skrivUt(sekvens);
    }



    public static ArrayList<Integer> skrivUt(ArrayList<Integer> array){
        
        if (array == null){
            return null;
        }
        if (array.size()<=2){
            for (int i = 0; i < array.size();i++){
                System.out.println(array.get(i));
            }
            return array;    
        }

        else if (array.size()>=3){ //splitter array i to og printer ut midterste element

            int middle= (int) Math.floor(array.size()/2) ;
           
            System.out.println(array.get(middle));

            ArrayList<Integer> venstreSubTre = new ArrayList<Integer> (array.subList(0, middle));
            ArrayList<Integer> hoyreSubTre = new ArrayList<Integer> (array.subList(middle +1 , array.size()));

            skrivUt(venstreSubTre);
            skrivUt(hoyreSubTre);

            return null;
        }   
        return null;
    }
}