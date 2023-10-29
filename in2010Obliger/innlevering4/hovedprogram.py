import sys
from hashSet import *
#python3 hashSet.py < inputs/eksempel_input
#python3 hovedprogram.py input_10.txt output_10.txt
#python3 hovedprogram.py input_10 output_10 
inpFile = open("inputs/"+str(sys.argv[1]), "r")
outFile = open("outputs/"+sys.argv[2], "r")
inpCommands=[]
sysoutResults =[]
outFileSolutions = []
errors = 0

for line in outFile:
    outFileSolutions.append(line)

hashSet = hashSet()

for line in inpFile:
    splited= line.split(" ")
    for el in splited:
        el.strip()

    if splited[0]== "insert" and len(splited)>1:
        inp = int(splited[1].strip())
        print(inp)
        hashSet.insert(inp)
        
    elif splited[0] == "size":
        sys.stdout(hashSet.size())
        print(str(hashSet.size()))
        sysoutResults.append(str(hashSet.size()))

    elif splited[0] == "contains":
        sys.stdout(hashSet.contains(splited[1]))
        sysoutResults.append(str(hashSet.contains(splited[1])))
        print(str(hashSet.contains(splited[1])))

    elif splited[0] == "remove":
        hashSet.remove(int(splited[1]))


for i in range(len(outFileSolutions)):
    print(sysoutResults[i])

    if sysoutResults[i] != [i]:
        print("wrong output")
        print(sysoutResults[i])
        errors+=1


print("errors: " + str(errors))