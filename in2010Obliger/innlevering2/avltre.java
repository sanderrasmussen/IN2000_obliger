

public class avltre<T> extends tre<T> {


    int hoyde = 0;

    //dersom treet er venstretungt 
    public node<T> hoyreRotasjon(node<T> node){
      
        node<T> x = node.hentVenstre();
        node<T> y = x.hentHoyre();

        x.settHoyreBarn(node);
        node.settVenstreBarn(y);

        node.settHoyde(hoyde(node));
        x.settHoyde(hoyde(x));

          if (node.equals(rot)){
            rot=x;
        }
        return x;
    }

    public node<T> venstreRotasjon(node<T> z){
        node<T> y = z.hentHoyre();
        node<T> T = y.hentVenstre();

        y.settVenstreBarn(z);
        z.settHoyreBarn(T);

        z.settHoyde(hoyde(z));
        y.settHoyde(hoyde(y));

        if (z.equals(rot)){
            rot=y;
        }
        return y;
    }
    public int balanseFactor(node<T> node){
        if(node==null){
            return 0;
        }
        //retur forteller oss om treet er venstre eller hopyretungt, evt balandert
        return (hoyde(node.hentVenstre()) - hoyde(node.hentHoyre()));
    }
        
    public node<T> balanser(node<T> node){ //denne inneholder feil

        if (balanseFactor(node)< -1){
            if (balanseFactor(node.hentHoyre())>0){
                node.settHoyreBarn(hoyreRotasjon(node.hentHoyre()));
            }
            return venstreRotasjon(node);
        }
        if (balanseFactor(node)> 1){
            if (balanseFactor(node.hentVenstre()) <0){
                node.settVenstreBarn(venstreRotasjon(node.hentVenstre()));
            }
            return hoyreRotasjon(node);
        }
        return node;
    }

    
    public node<T> settInn(node<T> node,T x){
        
        if (node==null){
            node = new node<T>(x);    
            if (rot==null){
                rot = node;
            }
        }
        
        else if (node.erStorre(x)){
            node.settVenstreBarn(settInn(node.hentVenstre(),x));
            node.hentVenstre().settForelder(node);

        }
        else if (node.erMindre(x)){
            node.settHoyreBarn(settInn(node.hentHoyre(), x));
            node.hentHoyre().settForelder(node);
        }
        node.settHoyde(hoyde(node));  
        size = calcSize(this.rot); 
        return balanser(node);
    }
    

    @Override
    public node<T> remove(node<T> startnode, T element){
        if (startnode==null){
            return null;
        }
        //dersom rotnoden er den som skal fjernes
        if(rot.hentInnhold().equals(element)){
            rot = fjernRotNode();
            
        }
        if (startnode.erStorre(element)){
            startnode.settVenstreBarn(remove(startnode.hentVenstre(), element));
          
        }
        else if (startnode.erMindre(element)){
            startnode.settHoyreBarn(remove(startnode.hentHoyre(), element));;
         
        }
        else if (startnode.hentVenstre()== null){
            startnode = startnode.hentHoyre();
            
        }
        else if (startnode.hentHoyre()==null){
            startnode = startnode.hentVenstre();
          
        }
        else {
            node <T> u = finnMinste(startnode.hentHoyre());
            startnode.settInnhold(u.hentInnhold());
            startnode.settHoyreBarn(remove(startnode.hentHoyre(), u.hentInnhold()));;
        }
        if (startnode!=null){
            startnode.settHoyde(hoyde(startnode));
        }
        
        return balanser(startnode);
    }
}
