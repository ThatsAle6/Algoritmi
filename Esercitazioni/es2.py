#Realizzare una funzione python che restituisce il costo del cammino (da radice a foglia) di costo massimo,
#dove il costo di un cammino è dato dalla somma dei valori dei nodi che si incontrani lungo il cammino.

from alberi.alberibinari import AlberoBin

def camminoMax(a:AlberoBin) -> int:
    if a is None:
        return 0
    
    return a.val + max(camminoMax(a.sin), camminoMax(a.des))

#CTM(n) = CTP(n) = theta(n) in qualunque caso si deve comunque visitare tutto l'albero

#CSM(n) = theta(log n) nel caso di albero bilanciato

#CSP(n) = theta(n) nel caso di albero degenere 




#CTM(n) = theta()

#CTP(n) = theta()

#CSM(n) = theta()

#CSP(n) = theta() 