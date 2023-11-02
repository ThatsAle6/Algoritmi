from alberi.alberibinari import AlberoBin

#TRACCIA:
#   Si deve realizzare una funzione ricorsiva che restituisce True se e solo se tutti i nodi non foglia di A al livello l sono contenuti
#   in almeno un nodo nel sottoalbero destro di B al livello l+1

def verifica(a:AlberoBin, b:AlberoBin, l:int)->bool:
    if a.sin is not None and a.des is not None:
        return livello(a,b,l,0)
    
    return verifica(a.sin, b, l) and verifica(a.des, b, l)

def livello(a:AlberoBin, b:AlberoBin, l:int, livA:int)->bool:
    if a is None or b is None:
        return False
    
    if l==livA:
        return controllaB(b,l,0,a.val)
    
    return livello(a.sin, b, l, livA+1) or livello(a.des, b, l, livA+1)

def controllaB(b:AlberoBin, l:int, livB:int, nodoA:int)->bool:
    if b is None:
        return False
    
    if b.des is None:
        return True if b.des.val==nodoA and livB==l+1
    
    return False
