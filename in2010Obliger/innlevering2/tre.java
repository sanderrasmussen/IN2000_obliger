package innlevering2;

public class tre<T> {
    node<T> rot; //startnode

    //metoder som skal være med:
    //settInn 
    //inneHolder
    //slett
    //størrelse

   public int size(node<T> startNode){
    if (startNode==null){
        return 0;
    }
    int hoyreSubTre= size(startNode.hoyreBarn);
    int venstreSubTre = size(startNode.venstreBarn);
    
    return hoyreSubTre +venstreSubTre +1;
   }

    //hjelpemetode
    public node<T> finnNode(node<T> startNode, T element){
        if (startNode == null){
            return null; 
        }
        if (startNode.hentInnhold()==element){//basisteg
            return startNode;
        }
        if (startNode.erStorre(element)){
            return finnNode(this.rot.hentVenstre(), element);
        }
        if (!startNode.erStorre(element)){
            return finnNode(startNode.hentHoyre(), element);
        }
        return null;
    }

     //hjelpemetode for slett node funksjonen
    public node<T> finnMinste(node<T> startNode){
        if (startNode==null){
            return null;
        }
        if (startNode.hentVenstre()==null){
            return startNode;
        }
        node<T> node = startNode;
        while (node.hentVenstre()!=null){
            node =node.hentVenstre();
        }
        System.out.println(node.innhold);
        System.out.println("minste: " + node.hentInnhold());
        return node;
    }

   //hjelpemetode for aa slette rotnoden, skrevet som seperat funksjon for aa vaere lettere aa lese
    public node<T> fjernRotNode(){
        if (rot.loevNode()){
            rot=null;
            return rot;
        }
        if(rot.hoyreBarn!=null){
            node<T> minste= finnMinste(rot.hentHoyre());
            rot.innhold = minste.innhold;
            
            //naa skal minste noden slettes
            //to cases: 
            //1: dersom noden som skal slettes er hoyrebarn
            if (minste.hentForelder()!=rot){
                minste.hentForelder().settVenstreBarn(minste.hentHoyre());
            }
            //2: dersom noden som skal slettes er hoyrebarn.venstrebarn
            //da er ikke forelderen til minste null
            else{
                minste.hentForelder().settHoyreBarn(minste.hentHoyre());
            }
            return rot;
        }
        //her vet vi at venste barn maa bli rotnoten, fordi det ikke er noen root.hoyre
        rot = rot.venstreBarn;
        return rot;
    }


    public node<T> remove(node<T> startNode, T element){ //siden jeg bare har referanse fra forelder til barn og ikke tilbake saa endrer jeg bare innhold i nodene istedenfor å endre pekere
       
        if (startNode==null){
            return null;
        }
        //dersom rotnoden er den som skal fjernes
        if(rot.hentInnhold()==element){
            fjernRotNode();
        }

        if ((Integer)startNode.hentInnhold()> (Integer)element){
            startNode.venstreBarn= remove(startNode.venstreBarn, element);
            return startNode;
        }
        if ((Integer)startNode.hentInnhold()< (Integer)element){
            startNode.hoyreBarn= remove(startNode.hoyreBarn, element);
            return startNode;
        }
        if (startNode.venstreBarn==null){
            return startNode.hoyreBarn;
        }
        if (startNode.hoyreBarn==null){
            return startNode.venstreBarn;
        }
        node<T> u= finnMinste(startNode.hentHoyre());
        startNode.innhold = u.innhold;
        startNode.hoyreBarn=remove(startNode.hoyreBarn, u.innhold);
        return startNode;

    }

    

    public boolean contains(node<T> startNode, T maalElement){
        if (startNode == null){
            return false; //da maa treet vaere tomt
        }
        if (startNode.hentInnhold()==maalElement){
            return true;
        }
        if (startNode.erStorre(maalElement)){
            return contains(startNode.hentVenstre(), maalElement);
        }
        if (!startNode.erStorre(maalElement)){
            return contains(startNode.hentHoyre(), maalElement);
        }
        return false;
    }

    public node<T> settInn(node<T> forelderNode,T x){
        if (this.rot==null){
            this.rot = new node<T>(x); 
        }
        if (forelderNode==null){
            forelderNode = new node<T>(x); 
        }
        else if (forelderNode.erStorre(x)){
           forelderNode.settVenstreBarn(settInn(forelderNode.hentVenstre(),x));
           forelderNode.hentVenstre().settForelder(forelderNode);
        }
        else if (!forelderNode.erStorre(x)){
            forelderNode.settHoyreBarn(settInn(forelderNode.hentHoyre(), x));
            forelderNode.hentHoyre().settForelder(forelderNode);
        }
        return forelderNode;

    }
    //hjelpemetode
    public node<T> hentRot(){
        return this.rot;
    }
}
