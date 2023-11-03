#Realizzare una funzione che restituisce true se esiste almeno un nodo n in a tale che x appare nel sottoalbero sx e dx di n

from alberi.alberibinari import AlberoBin

def verifica(a:AlberoBin, x:int) -> bool:
    if a is None:
        return False
    
    if a.sin is not None and a.des is not None:
        return presente(a, x)
    
    return verifica(a.sin, x) or verifica(a.des, x)

def presente(a:AlberoBin, x:int) -> bool:
    if a is None:
        return False
    
    if a.val == x:
        return True
    
    return presente(a.sin, x) or presente(a.des, x)

#CTM(n) = theta(1) il primo nodo che visitiamo è uguale al valore x

#CTP(n) = theta(n) dobbiamo visitare tutto l'albero  

#CSM(n) = theta(n) nel caso di albero degenere 

#CSP(n) = theta(1) corrisponde a CTM, effettuiamo quindi una sola chiamata 