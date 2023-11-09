from collections import defaultdict

#testlinjer
# python3 katt.py < inputs/eksempel_input | cmp - outputs/eksempel_output
# python3 katt.py < inputs/input_1 | cmp - outputs/output_1
# python3 katt.py < inputs/input_2 | cmp - outputs/output_2
# python3 katt.py < inputs/input_3 | cmp - outputs/output_3
# python3 katt.py < inputs/input_4 | cmp - outputs/output_4
# python3 katt.py < inputs/input_5 | cmp - outputs/output_5

#python3 katt.py < inputs/eksempel_input

# jeg bruker innebygd hashmap for aa lose denne oppgaven da jeg gaar utifra at jeg ikke trenger aa implementere dette paa nytt

def lagTre():
    noder = defaultdict(None)
    sitterFast = input()
    sitterFast=int(sitterFast)


    while True:
        inp = input()
        if inp == "-1":
            break
        inp = inp.split(" ")

       

        forelder= int(inp[0])
        barn = inp[1:]

        for node in barn:
            node = int(node)
            noder[node] = forelder
        
    #finner veien
    node = sitterFast
    vei = str(sitterFast)
 
    while node!=None:
        #print(node)
        if noder[node] not in noder:
            break
        node = noder[node] #endrer peker til foreldrenoden
        vei+= " " + str(node)
    #print(noder[node])
    vei+= " " +str(noder[node])
    print(vei)

lagTre()