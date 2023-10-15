from collections import defaultdict
import csv
from node import node

class graf:

    V = set()  #noder
    E = defaultdict(set) #kanter
    w = dict() #vekt
    idTilNode = defaultdict# for a sla opp id og nodereferasne i konstanttid

    inputLines = ""

    def readFiles(self, movieFile, actorsFile):

        dataList=[]

        with open(movieFile) as mv:
            data = csv.reader(mv, delimiter="\t")
            for row in data:
                dataList.append(row)

        with open(actorsFile) as ac:
            data = csv.reader(ac, delimiter="\t")
            for row in data:
                dataList.append(row)
  
        return dataList


        movieData = open(movieFile, "r")
        actorData = open(actorsFile, "r")
        alldata = movieData.read()  + actorData.read()
        self.inputLines = alldata
        #print(alldata)
        return alldata





    def buildGraph(self, inputLines):
        V = set()  #noder
        E = defaultdict(set) #kanter
        w = dict() #vekt
        idTilNode = dict()# for a sla opp id og nodereferasne i konstanttid

        # inne i loopen lager vi og legger inn noder i grafen
        for dataList in inputLines:

            if "tt" in dataList[0]: #dersom forste argument er tt id saa vet vi at det er en film
                #film har rigide forutsigbare inndata, altsaa antall argumenter er altid lik 4
                filmNode = node()
                filmNode.insertMovie(dataList[0], dataList[1], dataList[2], dataList[3])
                V.add(filmNode)

                #LEGGER TIL FILMNODEN SOM NOKKEL I KANTER 
                E[filmNode].add(None)#noen filmer har ikke actors i databasen
                idTilNode[filmNode.get_tt_id()] = filmNode

            elif "nm" in dataList[0]:
                #her vet vi at det er actor sine data
                #som sagt, INVARIANT: gaar utifra at alle filmnoder allerede er lagt til
                actorNode = node()
                actorNode.insertActor(dataList[0], dataList[1], dataList[2:len(dataList)]) #OOPS HUSK Å SJEKKE OM DETTE ER GYLDIG INDEX
                V.add(actorNode)

                #looper igjennom actor sine filmer
                filmListe= actorNode.get_tt_id_list()
                for i in range(0, len(filmListe)):
                   
                    if filmListe[i] in idTilNode: # om det ikke er lagret data om filmen i tsv fil så skal den ignoreres
                        movie = idTilNode[filmListe[i]]
                        E[movie].add(actorNode) 
                        E[actorNode].add(movie)
                    
                        w[(movie, actorNode)] = float(movie.get_rating())
                        w[(actorNode, movie)] = float(movie.get_rating())

        self.V = V
        self.E = E
        self.w = w
        self.idTilNode = idTilNode

        return V, E , w, idTilNode
    



    def countNodesAndEdges(self):
        edges = 0
        # må telle alle indexer i E.values
        for node in self.V:
            if node.isActor():
                edges+= len(self.E[node])
                
          
          

        print("Nodes: " + str(len(self.E)))
        print("Edges: " + str(edges))

    



        
    
