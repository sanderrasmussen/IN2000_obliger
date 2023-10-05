
import java.util.PriorityQueue;

public class oppgaveB {
    
    public static PriorityQueue<Integer> skrivUt(PriorityQueue<Integer> queue){
        
        if (queue == null){
            return null;
        }
        if (queue.size()<=2){
            for (int i = 0; i < queue.size();i++){
                System.out.println(queue.poll());
            }
            return queue;    
        }
        
        else if (queue.size()>=3){ //splitter array i to og printer ut midterste element

            int middle= (int) Math.floor(queue.size()/2) ;
            

            PriorityQueue<Integer> venstreSubTre = new PriorityQueue<Integer> ();

            for (int i = 0; i< middle;i++){
                venstreSubTre.offer(queue.poll());
            }
            System.out.println(queue.poll());//popper og skriver ut midterste element

            PriorityQueue<Integer> hoyreSubTre = queue;

            skrivUt(venstreSubTre);
            skrivUt(hoyreSubTre);

            return null;
        }   
        return null;
    }
}
