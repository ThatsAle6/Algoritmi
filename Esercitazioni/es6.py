#Realizzare una funzione che restituisce True se esiste un nodo in a al livello 'liv' che compare in b a un livello > liv

from alberi.alberibinari import AlberoBin

def verifica(a:AlberoBin, b:AlberoBin) -> bool:
    if a is None or b is None:
        return False
    
    return verificaA(a, b, 0)

def verificaA(a:AlberoBin, b:AlberoBin, livA:int) -> bool:
    if a is None:
        return False
    
    if esiste(b, a.val, livA, 0):
        return True
    
    return verificaA(a.sin, b, livA+1) or verifica(a.des, b, livA+1)

def esiste(b:AlberoBin, infoA: int, livA:int, livB:int) ->bool:
    if b is None:
        return False
    
    if b.val == infoA and livB > livA:
        return True
    
    return esiste(b.sin, infoA, livA, livB+1) or esiste(b.des, infoA, livA, livB+1)

#CTM(n,m) = theta()

#CTP(n,m) = theta(n * m) 

#CSM(n,m) = theta()

#CSP(n,m) = theta() 
