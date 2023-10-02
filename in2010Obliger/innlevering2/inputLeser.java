
import java.io.File; 
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner; 

public class inputLeser {

    //returnerer array med commandoer fra input fil


    //
    public ArrayList<String[]> lesInputFraFil(String Path){
        try{
            ArrayList<String[]> kommandoer= new ArrayList<String[]>();

            File fil = new File(Path);
            Scanner scanner = new Scanner(fil);
            while (scanner.hasNextLine()){
                String linje = scanner.nextLine();
                //splitter string så vi faar matrise med kommando etterfulgt av argument
                String[] kommando_argument = linje.split(" ");
                kommandoer.add(kommando_argument);
            }
            scanner.close();
            return kommandoer;
        }
        catch(FileNotFoundException e){
            System.out.println(e);
            return null;
        }
    }
    
}
