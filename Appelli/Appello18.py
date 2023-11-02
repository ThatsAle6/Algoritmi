from alberi.alberibinari import AlberoBin

#TRACCIA:
#   Si deve realizzare una funzione
#       def livelloSomma(a:AlberoBin, l:int, soglia:int)->bool
#   che restituisce True se e solo se esiste almeno un nodo al livello l in a e la somma dei valori 
#   dei nodi che si trovano al livello l in a sia maggiore di soglia

def livelloSomma(a:AlberoBin, l:int, soglia:int)->bool:
    if a is None:
        return False
    return livello(a,l,soglia,0)

def livello(a:AlberoBin, l:int, soglia:int, livA:int)->bool:
    if a is None:
        return False
    if l==livA:
        return somma(a, 0) > soglia
    return livello(a.sin, l, soglia, livA+1) or livello(a.des, l , soglia, livA+1)

def somma(a:AlberoBin, sum:int)->int:
    if a is None:
        return 0
    sum=0
    if a.sin is not None and a.des is not None:
        sum=a.sin.val + a.des.val
    return somma(a.sin, sum) + somma(a.des, sum)


#Complessità:
#   CTM(n)= Theta(n)  
#   CTP(n)= Theta(n)

#   CSM(n)= Theta(log n) solo se l'albero è bilanciato 
#   CSP(n)= Theta(n) albero degenere
    