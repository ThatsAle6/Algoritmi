#Realizzare una funzione che restituisce True se e solo se tutti i nodi foglia di a hanno un valore uguale a quello della radice

from alberi.alberibinari import AlberoBin

def analizzaFoglie(a:AlberoBin)->bool:
    if a is None:
        return True
    
    return analizza(a, a.val)

def analizza(a:AlberoBin, radice: int)->bool:
    if a is None:
        return True
    if a.sin is None and a.des is None:
        return a.val >= radice
    
    return analizza(a.sin, radice) and analizza(a.des, radice)


#CTM(n) = theta(1) il primo nodo visitato ha un valore differente da dalla radice

#CTP(n) = theta(n) tutti i nodi hanno valore uguale alla radice, oppure tutti tranne l'ultima foglia più a dx

#CSM(n) = theta(1) coincide con CTM

#CSP(n) = theta(n) nel caso di un albero degenere 