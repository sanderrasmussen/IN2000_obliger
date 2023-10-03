

public class node<T> implements Comparable<T> {
    T innhold;
    node<T> venstreBarn;
    node<T> hoyreBarn;
    node<T> forelder;
    int hoyde=0;

    public node(T innhold){
        this.innhold= innhold;
    }
    public void settHoyde(int hoyde){
        this.hoyde= hoyde;
        
    }
    public int hentHoyde(){
        return this.hoyde;
    }
    public void settForelder(node<T> forelder){
        this.forelder= forelder;
    }
    public node<T> hentForelder(){
        return forelder;
    }

    public int dybde(node<T> node){
        if (node==null){
            return -1;
        }
        return 1+ dybde(node.forelder);
    }

    public void settVenstreBarn(node<T> node){
        venstreBarn= node;
    }
    public node<T> hentVenstre(){
        return this.venstreBarn;
    }
    public node<T> hentHoyre(){
        return this.hoyreBarn;
    }


    public void settHoyreBarn(node <T> node){
        hoyreBarn= node;
    }

    //hjelpemetode 
    public void settInnhold(T nyttInnhold){
        this.innhold= nyttInnhold;
    }

    //hjelpemetode
    public T hentInnhold(){
        return innhold;
    }

    @Override
    public int compareTo(T annen) {
        //går altid ut ifra at jeg får tall
        //derfor returnerer jeg bare -1 om det ikke er tall,
        //men forventer som sagt altid gyldig input
        //denne metoden kan utvides senere om noe annet enn int skal settes inn i treet
            int thisTall = (int) this.innhold;
            int annenTall = (int) annen;

            if (thisTall> annenTall){
                return 1;
            }
            else if (thisTall<annenTall){
                return -1;
            }
           return 0; //dersom de er like  
    }
    public boolean erStorre(T annen){ //hjelpemetode
        return (this.compareTo(annen)==1);
    }
    public boolean erMindre(T annen){
        return (this.compareTo(annen)==-1);
    }

    public boolean loevNode(){ //hjelpemetode
        return (venstreBarn==null && hoyreBarn==null);
    }
}
