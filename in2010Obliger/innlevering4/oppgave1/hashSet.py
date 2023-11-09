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
        hash =(number * 31) % self.N
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

        #print("rehash------")

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

        d = 1

        while self.Array[(i+d)%self.N] != None:
            
            el = self.Array[(i+d)%self.N]
            hash = self.Hash_function(el)

            if not (0<(hash-i)%self.N<=d):

                self.Array[i] =  el
                self.Array[(i+d)%self.N] = None
                self.fill_gap((i+d)%self.N)
                
                return
            d+=1
        return
      

    
        

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