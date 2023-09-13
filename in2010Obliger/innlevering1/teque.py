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

        while True:
            inp = input()
        
            match inp:
                case "":
                    break

                case None:
                    break
            
            kommando=inp.split(" ")[0]
            argument = int(inp.split(" ")[1])
            
            match kommando:
                case "push_front":
                    teque.push_front(argument)
                case "push_middle":
                    teque.push_middle(argument)
                case "push_back":
                    teque.push_back(argument)
                case "get_i":
                    teque.get_i(argument)


program = hovedprogram()
program.kjor()