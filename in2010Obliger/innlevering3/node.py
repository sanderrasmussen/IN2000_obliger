class node:

    #Lager variabler for baade film og skuespiller slik at vi senere kan velge aa kun bruke en av de alt etter hva noden holder paa
    
    #film vaariabler
    tt_id = None
    tittel = None
    rating = None
    antallStemmer=None

    #actor variabler
    nm_id= None
    navn = None
    tt_id_list = []

    #type er actor eller movie
    type=""
    edgesAmount= 0


    def insertActor(self,nm_id,navn, tt_id_list):
        self.type="actor"
        self.nm_id = nm_id
        self.navn = navn
        self.tt_id_list = tt_id_list

    def get_tt_id_list(self):
        return self.tt_id_list
    
    def get_rating(self):
        return self.rating

    def insertMovie(self, tt_id , tittel, rating, antallStemmer):
        self.type = "movie"
        self.tt_id = tt_id
        self.tittel = tittel
        self.rating = rating 
        self.antallStemmer= antallStemmer

    def get_tt_id(self):
        return self.tt_id

    def isActor(self):
        if self.type=="actor":
            return True
        return False
    
    def isMovie(self):
        if self.type=="movie":
            return True
        return False


    