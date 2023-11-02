from alberi.alberibinari import AlberoBin

#TRACCIA
#   Si deve realizzare una funzione ricorsiva
#
#       def twoSum(a:AlberoBin, z:int)->bool
#
#   che restituisce true se e solo se esiste in a almeno un nodo non foglia p tale che il sottoalbero destro
#   di p contiene almeno un nodo foglia q e valga che p.val() + q.val() = z

def twoSum(a:AlberoBin, z:int)->bool:
    if a is None:
        return False
    if a.sin is None or a.des is None:
        return False
    
    if a.sin is not None and a.des is not None:
        return controllo(a, z, a.val)

    return twoSum(a.sin, z) or twoSum(a.des, z)

def controllo(a:AlberoBin, z:int, p:int)->bool:
    if a is None:
        return False
    
    if a.des is None:
        return p + a.des.val == z
    
    return controllo(a.sin, z, p) or controllo(a.des, z, p)

#Complessità:
#   CTM(n)= Theta(n) nel miglior caso dobbiamo visitare sempre e comunque tutto l'albero in modo da verificare se la condizione è rispettata
#   CTP(n)= Theta(n) 
#   CSM(n)= Theta(log n) solo se l'albero è bilanciato 
#   CSP(n)= Theta(n) albero degenere