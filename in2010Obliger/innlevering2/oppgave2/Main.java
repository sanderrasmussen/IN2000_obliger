import java.util.ArrayList;
import java.util.Arrays;
import java.util.PriorityQueue;


public class Main {

    public static void main(String[] args){

        ArrayList<Integer> array = new ArrayList<>(Arrays.asList(0,1,2,3,4,5,6,7,8,9,10));

        ArrayList<Integer> sekvens = new ArrayList<>();

        PriorityQueue<Integer> tall = new PriorityQueue<Integer>();
        for (int i = 0; i< args.length; i++){
            sekvens.add((Integer.parseInt(args[i])));
        }
            oppgaveA.skrivUt(sekvens);
            //oppgaveB.skrivUt(tall);
    }
}
