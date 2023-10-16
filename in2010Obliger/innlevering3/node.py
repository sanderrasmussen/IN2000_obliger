class node:

    #Lager variabler for baade film og skuespiller slik at vi senere kan velge aa kun bruke en av de alt etter hva noden holder paa
    
    #film vaariabler
    tt_id = ""
    tittel = ""
    rating = None
    antallStemmer=None

    #actor variabler
    nm_id= ""
    navn = ""
    tt_id_list = []

    #type er actor eller movie
    type=""
    edgesAmount= 0


    def insertActor(self,nm_id_in,navn_in, tt_id_list_input):
        self.type="actor"
        self.nm_id = nm_id_in
        self.navn = navn_in
        self.tt_id_list = tt_id_list_input

    def get_tt_id_list(self):
        return self.tt_id_list
    
    def get_rating(self):
        return self.rating

    def insertMovie(self, tt_id_in , tittel_in, rating_in, antallStemmer_in):
        self.type = "movie"
        self.tt_id = tt_id_in
        self.tittel = tittel_in
        self.rating = rating_in
        self.antallStemmer= antallStemmer_in

    def get_tt_id(self):
        return self.tt_id

    def get_nm_id(self):
        return self.nm_id

    def isActor(self):
        if self.type=="actor":
            return True
        return False
    
    def isMovie(self):
        if self.type=="movie":
            return True
        return False


    def __lt__(self, other):
        return True