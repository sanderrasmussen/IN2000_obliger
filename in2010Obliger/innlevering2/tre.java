

public class tre<T> {
    node<T> rot; //startnode
    int size= 0;
    //metoder som skal være med:
    //settInn 
    //inneHolder
    //slett
    //størrelse

   public int calcSize(node<T> startNode){
    if (startNode==null){
        return 0;
    }
    int hoyreSubTre= calcSize(startNode.hoyreBarn);
    int venstreSubTre = calcSize(startNode.venstreBarn);
    
    return hoyreSubTre +venstreSubTre +1;
   }
   public int size(){
    return size;
   }

    //hjelpemetode
    public node<T> finnNode(node<T> startNode, T element){
        if (startNode == null){
            return null; 
        }
        if (startNode.hentInnhold().equals(element)){//basisteg
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
        //System.out.println(node.innhold);
        //System.out.println("minste: " + node.hentInnhold());
        return node;
    }

   //hjelpemetode for aa slette rotnoden, skrevet som seperat funksjon for aa vaere lettere aa lese
    public node<T> fjernRotNode(){
        if (rot.loevNode()){
            rot=null;
            size = calcSize(this.rot); 
            return rot;
        }
        if(rot.hoyreBarn!=null){
            node<T> minste= finnMinste(rot.hentHoyre());
            rot.innhold = minste.innhold;
            
            //naa skal minste noden slettes
            //to cases: 
            //1: dersom noden som skal slettes er hoyrebarn
            if (!minste.hentForelder().equals(rot)){
                minste.hentForelder().settVenstreBarn(minste.hentHoyre());
                size = calcSize(this.rot); 
            }
            //2: dersom noden som skal slettes er hoyrebarn.venstrebarn
            //da er ikke forelderen til minste null
            else{
                minste.hentForelder().settHoyreBarn(minste.hentHoyre());
            }
            size = calcSize(this.rot); 
            return rot;
        }
        //her vet vi at venste barn maa bli rotnoten, fordi det ikke er noen root.hoyre
        rot = rot.venstreBarn;
        size = calcSize(this.rot); 
        return rot;
    }


    public node<T> remove(node<T> startNode, T element){ //siden jeg bare har referanse fra forelder til barn og ikke tilbake saa endrer jeg bare innhold i nodene istedenfor å endre pekere
       
        if (startNode==null){
            return null;
        }
        //dersom rotnoden er den som skal fjernes
        if(rot.hentInnhold().equals(element)){
            fjernRotNode();
        }

        if ((Integer)startNode.hentInnhold()> (Integer)element){
            startNode.venstreBarn= remove(startNode.venstreBarn, element);
            size = calcSize(this.rot); 
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
        size = calcSize(startNode); //size blir fortsatt o(1) fordi calcSize() er o(logn) men er i insert og remove som også er o(logn)
        return startNode;
    }

    

    public boolean contains(node<T> startNode, T maalElement){
        if (startNode == null){
            return false; //da maa treet vaere tomt 
        }
        if (startNode.hentInnhold().equals(maalElement)){
            return true;
        }
        if (startNode.erStorre(maalElement)){
            return contains(startNode.hentVenstre(), maalElement);
        }
        if (startNode.erMindre(maalElement)){
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
        else if (forelderNode.erMindre(x)){
            forelderNode.settHoyreBarn(settInn(forelderNode.hentHoyre(), x));
            forelderNode.hentHoyre().settForelder(forelderNode);
        }
        size = calcSize(this.rot); 
        return forelderNode;
    }

    public int hoyde(node<T> node){ //her hadde jeg stor feil men rettet opp naa?
        
        if (node == null){
            if(rot==null){
                return -1;
            }
            return 0;
        }
        node.hoyde = Math.max(hoyde(node.hentHoyre()), hoyde(node.hentVenstre()) +1 );
        return node.hoyde;
    }
   
    //hjelpemetode
    public node<T> hentRot(){
        if (rot == null){
            return null;
        }
        return this.rot;
    }
}
