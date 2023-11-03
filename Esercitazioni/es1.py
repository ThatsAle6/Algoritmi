from alberi.alberibinari import AlberoBin

#Realizzare una funzione che restituisce True se la parte informativa di tutti i nodi foglia di a è maggiore di k

def analizzaFoglia(a:AlberoBin, k:int) -> bool:

    if a is None:
        return False
    
    if a.sin is None or a.des is None: #mi trovo su un nodo foglia
        return a.val > k
    
    return analizzaFoglia(a.sin, k) and analizzaFoglia(a.des,k)

#CTM(n) = theta(1) la prima foglia che visitiamo ha un valore < k 

#CTP(n) = theta(n) visitiamo tutto l'albero, tutti i nodi foglia hanno valore > k

#CSM(n) = theta(1)

#CSP(n) theta(n) nel caso di albero degene