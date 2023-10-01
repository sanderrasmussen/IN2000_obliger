package innlevering2;

public class Main{
    public static void main (String[] args){
    
        tre<Integer> treet= new tre<Integer>();
        treet.settInn(treet.hentRot(),1);
        treet.settInn(treet.hentRot(),2);
        treet.settInn(treet.hentRot(),4);
        treet.settInn(treet.hentRot(),3);
        
        treet.remove(treet.hentRot(), 3);//denne metoden fungerer ikke på forste element?
       
        System.out.println("rot: "+ treet.rot.innhold);
        System.out.println("hoyre" + treet.hentRot().hoyreBarn.innhold);
        //System.out.println("venstre" +treet.hentRot().venstreBarn.innhold);
        //System.out.println("hoyre, hoyre" +treet.hentRot().hoyreBarn.hoyreBarn.innhold);
        //System.out.println("hoyre, venstre" +treet.hentRot().hoyreBarn.venstreBarn.innhold);
        //System.out.println(treet.hentRot().hoyreBarn.venstreBarn.innhold);
        //System.out.println(treet.hentRot().innhold);
               
        //System.out.println("rot: "+ treet.rot.innhold);
        System.out.println("stoerrelse" + treet.size(treet.hentRot()));
        //System.out.println(treet.hentRot().hentVenstre().hentInnhold());

        System.out.println(treet.contains(treet.hentRot(), 1));
        System.out.println(treet.contains(treet.hentRot(), 2));
        System.out.println(treet.contains(treet.hentRot(), 3));
        System.out.println(treet.contains(treet.hentRot(), 4));
    }
}
