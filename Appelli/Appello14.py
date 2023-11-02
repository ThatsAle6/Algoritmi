
from alberi.alberibinari import AlberoBin


#TRACCIA: 
#   realizzare un metodo corsivo verifica(a:AlberoBinario)->bool :che resistuisce True se e solo se l'albero a contiene almeno un nodo foglia con valore negativo 
#   i cui antenati contengono tutti un valore positivo

def verifica(a:AlberoBin)->bool:
    if a is None: 
        return False
    if a.sin is None and a.des is None:         #controllo se è una foglia e richiamo il metodo controllo
        return controllo(a,a.val)               #gli passo l'albero e il valore della foglia
    return verifica(a.sin) or verifica(a.des)

def controllo(a:AlberoBin, antenato:int)->bool:
    if a is None: 
        return False
    if a.sin is None and a.des is None: 
        return a.val < 0                        #controllo se il valore della foglia è minore di zero
    if a.val < 0:                               #se è minore controllo a questo punto gli antenati
        return True if antenato > 0 else False
    return controllo(a.sin, antenato) and controllo(a.des, antenato)



# CTM(n) = Theta(1) il primo nodo dell'albero è una foglia con valore negativo
# CSM(n) = Theta(1)
# CTP(n)= Theta(n) l'albero è sbilanciato e deve controllare ogni nodo
# CSP(n)= Theta(n)