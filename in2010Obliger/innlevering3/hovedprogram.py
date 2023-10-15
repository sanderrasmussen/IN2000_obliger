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

graf.countNodesAndEdges()