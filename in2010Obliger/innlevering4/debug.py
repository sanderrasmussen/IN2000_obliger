from hashSet import *

#python3 debug.py < inputs/input_1000 | cmp - outputs/output_1000
#python3 hovedprogram.py < inputs/input_100 | cmp - outputs/output_100
#python3 hovedprogram.py < inputs/input_10 | cmp - outputs/output_10


antallLinjer = int(input())
hashset=hashSet()

outLine = 0

for i in range(antallLinjer):
    inn = input()
    inn = inn.split()

    if "insert" == inn[0].strip():
        tall = int(inn[1].strip())
        if outLine >=10 and outLine <= 12:
            print("outline: "+str(outLine)+", inserting "+str(tall))
            print(hashset.Array)
        hashset.insert(tall)
        
    elif "size" == inn[0].strip():
        outLine+=1
        print(str(hashset.size()))
    

    elif "contains" == inn[0].strip():
        outLine+=1
        print(str(hashset.contains(int(inn[1]))).lower())


    elif "remove" == inn[0].strip():
        if outLine >=10 and outLine <= 12:
            print("outline: "+str(outLine)+", removing "+str(tall))
        hashset.remove(int(inn[1].strip()))
    if outLine >=10 and outLine <=12:
        print(hashset.size())

