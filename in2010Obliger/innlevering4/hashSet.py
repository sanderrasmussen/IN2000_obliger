import math

class hashSet():
    def __init__(self) -> None:
        self.REHASH_LIMIT = 0.75
        self.n = 0
        self.N = 1
        self.Array = [None] *self.N

    def REHASH_FACTOR(self):
        return self.n/self.N
    
    def Hash_function(self, number):
        hash =int(int(number) * 31) % self.N
        return hash
    
    def ensure_size(self):
        if self.REHASH_FACTOR()>= self.REHASH_LIMIT:
            self.reHash()

    def reHash(self):
        oldArray = self.Array

        self.n = 0
        self.N = self.N * 2
        self.Array = [None] * self.N

        for i in range(len(oldArray)):
            if oldArray[i] != None:
                self.insert(oldArray[i])

    def insert(self, numb):
        if numb == None:
            return
        
        self.ensure_size()

        i = self.Hash_function(numb)

        if self.contains(numb): 
            while self.Array[i]!= None:
                i = (i +1) % self.N

        self.Array[i] = numb
        self.n += 1

    def contains(self, n):
        i = self.Hash_function(n)

        if self.Array[i]!=None:

            while self.Array[i]!= None:
                if self.Array[i] == n:
                    return True
                i = (i+1) % self.N
                
        return False
    
    def remove(self, int):
        i = self.Hash_function(int)

        while self.Array[i] != int and self.Array[i]!=None:
            i = (i+1) % self.N

        if self.Array[i]== int:
            self.n -= 1
            self.Array[i] = None
            # fyll hull
            self.fill_gap(i)
            
    def fill_gap(self, i):
        j = i +1

        while self.Array[j%self.N] != None or self.Hash_function(j%self.N)!=i:
            el = self.Array[j%self.N]
            hash = self.Hash_function(el)
            if not (0 < (j-i) % self.N <= j):
                self.Array[i] = el
                self.Array[j%self.N] = None
                self.fill_gap(j% self.N)
                return 
            j +=1

    def size(self):
        return self.n