from alberi.alberibinari import AlberoBin

#TRACCIA:
#   Si deve realizzare una funzione ricorsiva che restituisce True se e solo se esiste un nodo che si trova al livello l
#   nell'albero a che ha valore 0 e i cui discendenti (compresi i figli) hanno tutti valore 0

def verificaCammini(a:AlberoBin, l:int)->bool:
    if a is None:
        return False
    return verifica(a,l,0)

def verifica(a:AlberoBin, l:int, livA:int)->bool:
    if a is None:
        return False
    
    if livA == l:
        return a.val==0
    
    if discendenti(a):
        return True
    
    return verifica(a.sin, l, livA+1) and verifica(a.des, l, livA+1)

def discendenti(a:AlberoBin)->bool:
    if a is None:
        return True
    if a.val != 0:
        return False
    
    return discendenti(a.sin) and discendenti(a.des)


#Complessità:
#
#CTM(n) = Theta(n) anche nel caso in cui trovo subito un nodo uguale a 0 dovrò comunque visitare tutto l'albero per controllare i suoi discendenti     
#CTP(n) = Theta(n)

#CSM(n) = 

#CSP(n) = Theta(n) albero degenere