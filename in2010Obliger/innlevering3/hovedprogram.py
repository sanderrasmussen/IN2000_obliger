from graf import graf
from node import node
from pathlib import Path

#marvel test data
pathMovieMarvel= Path("six-degrees-of-imdb-ressursside-main/marvel_movies.tsv")
pathActorMarvel = Path("six-degrees-of-imdb-ressursside-main/marvel_actors.tsv")

pathMovie = Path("six-degrees-of-imdb-ressursside-main/movies.tsv")
pathActor = Path("six-degrees-of-imdb-ressursside-main/actors.tsv")

graf = graf()

inputData = graf.readFiles(pathMovie,pathActor)

G = graf.buildGraph(inputData)
#print(list(graf.V)[0].tt_id)
#print(list(graf.V)[0].tittel)
#print(list(graf.V)[0].isMovie())
graf.countNodesAndEdges()
#for v in list(graf.E[graf.idTilNode["nm2255973"]]):
#    print(v.isActor())

#print(graf.idTilNode["nm0001859"].navn)
""" 
print("\n")
print(" ---     shortest path     --- ")
print("\n")
print(graf.shortest_path("nm2255973" , "nm0000460"))
print("\n")
print(graf.shortest_path("nm0424060" , "nm8076281"))
print("\n")
print(graf.shortest_path("nm4689420" , "nm0000365"))
print("\n")
print(graf.shortest_path("nm0000288" , "nm2143282"))
print("\n")
print(graf.shortest_path("nm0637259" , "nm0931324"))
print("\n")
print(" ---     chillest path     --- ")
print("\n")
print(graf.chillest_path("nm2255973" , "nm0000460"))
print("\n")
print(graf.chillest_path("nm0424060" , "nm8076281"))
print("\n")
print(graf.chillest_path("nm4689420" , "nm0000365"))
print("\n")
print(graf.chillest_path("nm0000288" , "nm2143282"))
print("\n")
print(graf.chillest_path("nm0637259" , "nm0931324"))
"""

graf.find_Components(graf.G)