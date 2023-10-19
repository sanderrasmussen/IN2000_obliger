from collections import defaultdict
import csv
import heapq
from node import node
from collections import deque
import sys

class graf:
   
    V = set()  #noder
    E = defaultdict(set) #kanter
    w = dict() #vekt
    idTilNode = dict()# for a sla opp id og nodereferasne i konstanttid
    G = V, E, w
    
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


    def buildGraph(self, inputLines):
        V = set()  #noder
        E = defaultdict(set) #kanter
        w = dict() #vekt
        self.idTilNode = dict()# for a sla opp id og nodereferasne i konstanttid

        # inne i loopen lager vi og legger inn noder i grafen
        for dataList in inputLines:

            if "tt" in dataList[0]: #dersom forste argument er tt id saa vet vi at det er en film
                #film har rigide forutsigbare inndata, altsaa antall argumenter er altid lik 4
                filmNode = node()
                filmNode.insertMovie(str(dataList[0]), str(dataList[1]), float(dataList[2]), int(dataList[3]))
                V.add(filmNode)

                #LEGGER TIL FILMNODEN SOM NOKKEL I KANTER 
                E[filmNode].add(None)#noen filmer har ikke actors i databasen
                self.idTilNode[filmNode.get_tt_id()] = filmNode

            elif "nm" in dataList[0]:
                #her vet vi at det er actor sine data
                #som sagt, INVARIANT: gaar utifra at alle filmnoder allerede er lagt til
                actorNode = node()
                actorNode.insertActor(str(dataList[0]), str(dataList[1]), list(dataList[2:len(dataList)])) #OOPS HUSK Å SJEKKE OM DETTE ER GYLDIG INDEX
                V.add(actorNode)
                self.idTilNode[actorNode.get_nm_id()]= actorNode

                #looper igjennom actor sine filmer
                filmListe= actorNode.get_tt_id_list()
                for i in range(0, len(filmListe)):
                   
                    if filmListe[i] in self.idTilNode: # om det ikke er lagret data om filmen i tsv fil så skal den ignoreres
                        movie = self.idTilNode[filmListe[i]]
                        E[movie].add(actorNode) 
                        E[actorNode].add(movie)
                    
                        w[(movie, actorNode)] = float(movie.get_rating())
                        w[(actorNode, movie)] = float(movie.get_rating())

        self.V = V
        self.E = E
        self.w = w
        self.G = V, E, w

        return V, E , w
    



    def countNodesAndEdges(self):
        edges = 0
        # må telle alle indexer i E.values
        for node in self.V:
            if node.isActor():
                edges+= len(self.E[node])

        print("Nodes: " + str(len(self.E)))
        print("Edges: " + str(edges))



    # tar utgangspunkt i koden fra grafnotatet publisert av faglærer på emnesiden
    def dijkstra(self, G, s):
        V, E ,w = G
        queue = []
        heapq._heapify_max(queue)

        heapq.heappush(queue, (0,s))
        dist = defaultdict(lambda: float("inf"))
        dist[s] = 0
        parents = {s:None}

        while queue: # nå skal distansen til alle andre noder i grafen beregnes og lagres

            cost , u = heapq.heappop(queue)
            if cost != dist[u]:
                    continue
            
            for v in E[u]: # for alle kanter fra v
                if v!=None:
                    c = cost + (10-w[(u,v)])
                    if c < dist[v]:
                        dist[v] = c
                        heapq.heappush(queue, (c,v))
                        parents[v] = u

        return dist, parents
    
    def shortest_path(self, FromId, ToId):
        #må finne node av navnene som er inputs
        FromNode = self.idTilNode[FromId]
        ToNode = self.idTilNode[ToId]

        parents = self.shortest_pathBFS( self.G, FromNode, ToNode)

        #print(dist[ToNode])
        Node =ToNode
        
        output = ToNode.navn
        while parents[Node]!=None:
            Node = parents[Node]
            if Node.isMovie():
                output = "[ " + Node.tittel  +  " ("+ str(Node.rating) +") " + "]" + "\n" +"===>" + output
            else:
                output =  Node.navn  + "==="+ output
        #output= FromNode.navn + output
        return output
    
    def shortest_pathBFS(self, G,s, target):
        #gjør bfs
        queue = deque([s])
        visited = set()
        parents= {s: None}
        visited.add(s)
        
        V, E, w = G
        while queue:
            k = queue.popleft()
            
            for u in E[k]:
                if u not in visited and u!=None:
                    visited.add(u)
                    queue.append(u)
                    parents[u]=k
                if u==(target):
                    print("target found " + u.navn)
                    return parents
                
        return parents

    def chillest_path(self, FromId, ToId):
        #må finne node av navnene som er inputs
        FromNode = self.idTilNode[FromId]
        ToNode = self.idTilNode[ToId]

        dist, parents = self.dijkstra( self.G, FromNode)

        print(dist[ToNode])
        Node =ToNode
        
        output = ToNode.navn
        while parents[Node]:
            Node = parents[Node]
            if Node.isMovie():
                output = "[ " + Node.tittel  +  " ("+ str(Node.rating) +") " + "]" + "\n" +"===>" + output
            else:
                output =  Node.navn  + "==="+ output
        #output= FromNode.navn + output
        return output


    #oppgave 4
    # bruker breddesøk for å finne ut om graf er sammenhengende, deretter så gjør jeg det samme på alle noder som ikke var med i det forgje breddesøket

    def find_Components(self, G):
        V,E,w = G
        # lager en metode som returnerer set med nodene til en komponent

        def DFSvisitRecursive(self, G, visit, visited): #denne metoden funer bare på mindre grafer pga at python har lav recursion limit
            V ,E ,w = G
            if visited==None:
                visited = set()

            for v in E[visit]:
                if v not in visited:
                    visited.add(v)
                    DFSvisitRecursive(self, G, v, visited)
            return visited
        
        def DFSvisitCallStack(self, G, s):
            V, E, w = G
            visited = set()
            stack = [s]
        
            while stack:
                u = stack.pop()

                if u not in visited:
                    visited.add(u)
        
                    for v in E[u]:
                        stack.append(v)
            return visited



        #går igjennom alle komonenter
        componenter = []
        masterSet = V
        visited = set()
        sizes = defaultdict(int)

        while masterSet:
         
            visit = masterSet.pop()
        
            resultSet = DFSvisitCallStack(self, G, visit)

            sizes[len(resultSet)] += 1

            componenter.append(resultSet)
            visited = resultSet | visited
            masterSet = masterSet - visited
            print(len(masterSet))
            print(len(componenter))#testing
        
        for key,value in sizes.items():
            print("det er " + str(value) + " componenter av storrelse: "+  str(key) + " : " )

    def count_Components(self, G):
        V,E,w = G
        visited = set()

        components = 0
            



  





















    
    def DFSvisit(self, u, visited):
        visited.add(u)
        for (u,v) in self.E:
            if v not in visited:
                self.DFSvisit(v, visited)
        return visited

    def DFSfull(self, u):
        visited = []
        for (u, v) in self.E:
            if v not in visited:
                self.DFSvisit(v, visited)   
        return visited

    def DFSrecursive(self, v , visited=None):
        if visited== None:
            visited = set()
        for (v, u) in self.E:
            if u not in visited:
                self.DFSrecursive(u, visited)
        return visited
        
    def BFSvisit(self, u, visited=None):
        if visited == None:
            visited =set()
        queue = [u]
        while queue:
            u = queue.pop()
            for (u, v) in self.E:
                if v not in visited:
                    queue.append(v)
                    visited.append(v)

    def BFSfull(self):
        visited= set()
        for node in self.V:
            if node not in visited:
                self.BFSvisit(node, visited)





            


        
    
