import math

class Teque:

    def __init__(self):
        self.liste = []
        
    def push_back(self, x):
        self.liste.append(x)
    
    def push_front(self, x):
        self.liste.insert(x,0)

    def push_middle(self, x):
        k = len(self.liste)
        midt_i = math.floor((k+1)/2)
        self.liste.insert(midt_i, x)
        
    def get_i(self,i):
        return self.liste[i]
    
    def printListe(self):
        print(self.liste)
    
teque = Teque()

teque.push_front(1)
teque.push_back(3)
teque.push_middle(2)
teque.push_middle(5)
teque.push_middle(6)
teque.printListe()
