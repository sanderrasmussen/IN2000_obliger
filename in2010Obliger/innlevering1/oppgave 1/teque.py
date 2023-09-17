import math

class Teque:

    def __init__(self):
        self.liste = []
        
    def push_back(self, x):
        self.liste.append(x)
    
    def push_front(self, x):
        self.liste.insert(0,x)

    def push_middle(self, x):
        k = len(self.liste)
        midt_i = math.floor((k+1)/2)
        self.liste.insert(midt_i, x)
        
    def get_i(self,i):
        print(self.liste[i])
    
    def printListe(self):
        print(self.liste)
    

class hovedprogram():

    def kjor(self):
        teque = Teque()
        antallOperasjoner = int(input())
        operasjoner = []

        for i in range(0,antallOperasjoner): #o(n)
            inp = input()
            operasjoner.append(inp)


        for i in range(0, len(operasjoner)): #o(n)
        
            inp = operasjoner[i]
        
            if inp== "":
                break

            elif inp== None:
                break
            
            kommando=inp.split(" ")[0]
            argument = int(inp.split(" ")[1])
            
            if kommando== "push_front":
                teque.push_front(argument)
            if kommando== "push_middle":
                teque.push_middle(argument)
            if kommando== "push_back":
                teque.push_back(argument)
            if kommando== "get":
                teque.get_i(argument)
        
program = hovedprogram()
program.kjor()