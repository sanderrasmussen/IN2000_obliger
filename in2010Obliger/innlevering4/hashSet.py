import math

class hashSet():
    def __init__(self) -> None:
        self.REHASH_LIMIT = 0.75
        self.n = 0
        self.N = 1
        self.Array = [None] *self.N

    def REHASH_FACTOR(self):
        return self.n /self.N
    
    def Hash_function(self, number):
        hash =(number * 2654435761) % self.N
        return hash
    
    def ensure_size(self):
        if self.REHASH_FACTOR() >= self.REHASH_LIMIT:
            self.reHash()

    def reHash(self):
        oldArray = self.Array.copy()

        self.n = 0
        self.N = self.N * 2
        self.Array = [None] * self.N

        for i in range(len(oldArray)):
                if oldArray[i]!=None and oldArray[i] not in self.Array:
                    self.insert(oldArray[i])



    def insert(self, numb):
        if numb==None:
            return
        
        self.ensure_size()
        
        i = self.Hash_function(numb)

        if self.contains(numb) == False:
                
            while self.Array[i]!= None:
                
                i = (i +1) % self.N
                
            self.Array[i] = numb
            self.n += 1

    def contains(self, n):
        
        if n in self.Array:
            return True
        return False
        
        i = self.Hash_function(n)

        while self.Array[i]!= None:
            
            if self.Array[i] == n:
                return True
            i = (i+1) % self.N
        
        return False
    
    def remove(self, int):
        i = self.Hash_function(int) % self.N

      
        
        while self.Array[i]!=None:
            
            if self.Array[i] == int:
                
                self.Array[i] = None
                self.n -=1
                # fyll hull
                self.fill_gap(i)
                
                return
            i = (i+1) % self.N

    def fill_gap(self, i):

        s = 1

        while self.Array[(i+s)%self.N] != None:
        
            hash = self.Hash_function((i+s)%self.N)

            if hash <= i:

                self.Array[i] =  self.Array[(i+s) %self.N]    
                self.Array[(i+s)%self.N] = None
                self.fill_gap((i+s)%self.N)
              
                return
            s+=1


    def size(self):
        return self.n
    
    def hentDuplikater(self):
        besokt=set()
        duplikater=set()
        for el in self.Array:
            if el == None:
                continue
            if el not in besokt:
                besokt.add(el)
            elif el in besokt:
                duplikater.add(el)
        return duplikater