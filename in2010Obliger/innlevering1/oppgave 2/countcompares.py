from functools import total_ordering
# her lar jeg filen stå uendret slik jeg lastet den ned fra resurssiden 
@total_ordering
class CountCompares:
    def __init__(self, elem):
        self.elem = elem
        self.compares = 0

    def reset(self):
        self.compares = 0

    def __eq__(self, other):
        return self.elem == other.elem

    def __lt__(self, other):
        self.compares += 1
        return self.elem < other.elem

    def __repr__(self):
        return self.elem.__repr__()
    
    # denne metoden skrev jeg selv
    def compared(self):
        self.compares +=1
