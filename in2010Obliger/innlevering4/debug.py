import hashSet

antallLinjer = int(input())
hashset=hashSet()

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
