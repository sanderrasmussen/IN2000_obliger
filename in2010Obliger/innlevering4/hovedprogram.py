import sys
from hashSet import *
import random
#python3 hashSet.py < inputs/eksempel_input
#python3 hovedprogram.py input_10.txt output_10.txt

#python3 hovedprogram.py input_10 output_10 
#python3 hovedprogram.py input_100 output_100
#python3 hovedprogram.py input_1000 output_1000
#python3 hovedprogram.py input_10000 output_10000 
#python3 hovedprogram.py < inputs/input_100000 | cmp - outputs/output_100000
#python3 hovedprogram.py < inputs/input_10000 | cmp - outputs/output_10000
#python3 hovedprogram.py < inputs/input_1000 | cmp - outputs/output_1000
#python3 hovedprogram.py < inputs/input_100 | cmp - outputs/output_100
#python3 hovedprogram.py < inputs/input_10 | cmp - outputs/output_10

#python3 hovedprogram.py < inputs/eksempel_input 

def main(): 
    inpFile = open("inputs/"+str(sys.argv[1]), "r")
    outFile = open("outputs/"+str(sys.argv[2]), "r")

    results =[]
    outFileSolutions = []
    errors = 0
    insertions=0
    hashset = hashSet()

    for line in outFile:
        line.strip()
        outFileSolutions.append(line)

    

    for line in inpFile:
        splited= line.split(" ")
    

        if "insert" == splited[0].strip():
            inp = int(splited[1].strip())
            insertions+=1
            hashset.insert(inp)
            
        elif "size" == splited[0].strip():
            print(str(hashset.size()))
            results.append(str(hashset.size()))

        elif "contains" == splited[0].strip():
            print(str(hashset.contains(int(splited[1]))))
            results.append(str(hashset.contains(int(splited[1]))))

        elif "remove" == splited[0].strip():
            hashset.remove(int(splited[1].strip()))

    for i in range(len(results)):
        
        if results[i].lower().strip() != outFileSolutions[i].lower().strip():
            print("wrong output")
            print(results[i])
            print("skal vere: " + outFileSolutions[i])
            errors+=1
            


    print("errors: " + str(errors))
    print("plasser i array "+ str(hashset.size()))

    print("plasser i array "+ str(len(hashset.Array)))
     #finn duplikat
    besokt= set()
    duplikater=set()
    for n in hashset.Array:
        if n not in besokt and n!=None:
            besokt.add(n)
        elif n in besokt:
            print("duplikat: " + str(n))
            print(hashset.contains(n))
            duplikater.add(n)
            
    print( "antall elementer " + str(hashset.size()))
    print("plasser i array "+ str(hashset.n))
    print("plasser i array "+ str(len(hashset.Array)))
    print("faktiske elementer som ikke er None: " + str(len(besokt)))

def test():
    
    hashset = hashSet()
    for i in range(0,1000):
        hashset.insert(i)
    print(hashset.size())
    for i in range(0,50):
        hashset.remove(i*3)
    print(hashset.size())
    for i in range(0,1000):
        hashset.insert(i)
    for i in range(0,50):
        hashset.remove(i*2)
    print(hashset.size())
    for i in range(0,1000):
        hashset.insert(i)
    for i in range(0,50):
        hashset.remove(i*3)
    
    print(hashset.contains(3))
    print(hashset.size())

    #finn duplikat
    besokt= []
    duplikater=[]
    for n in hashset.Array:
        if n not in besokt and n!=None:
            besokt.append(n)
            
        elif n in besokt:
            print("duplikat: " + str(n))
            print(hashset.contains(n))
            duplikater.append(n)


antallLinjer = int(input())
hashset=hashSet()
besokt = []

for i in range(antallLinjer):
    inn = input()
    inn = inn.split()

    if "insert" == inn[0].strip():
        tall = int(inn[1].strip())
        hashset.insert(tall)
        
    elif "size" == inn[0].strip():
        print(str(hashset.size()))
    

    elif "contains" == inn[0].strip():
        print(str(hashset.contains(int(inn[1]))).lower())


    elif "remove" == inn[0].strip():
        hashset.remove(int(inn[1].strip()))

for i in hashset.hentDuplikater():
    print("duplikater:")
    print(i)
