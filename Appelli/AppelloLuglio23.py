
from alberi.alberibinari import AlberoBin

#TRACCIA:
    #Realizzare un metodo verifica(a:AB, b:AB, k:int)->bool chw restiruisce True se e solo se per ogni nodo foglia x di a esistono
    #almeno k nodi non foglia y nel sotto albero destro di b tali che x.val == y.val

    #per ogni nodo foglia x di a eisitonono almeno k nodi non foglia y nel sottoalbero dx di b tale che la foglia di a = non foglia di y

def verifica(a:AlberoBin, b:AlberoBin, k=int)->bool:
    if a is None or b is None:
        return False
    if a.sin is None and a.des is None:
        return nonFogliaB(a.val, b) >= k
    
    return verifica(a.sin, b, k) and verifica(a.des, b, k)

def nonFogliaB(b:AlberoBin, radice:int)->int:
    if b is None:
        return False
    if b.sin is not None and b.des is not None: #verifico che non sia un nodo foglia
        return conta(b, radice, 0)
    
    return nonFogliaB(b.sin, radice) and nonFogliaB(b.des, radice)

def conta(b:AlberoBin, radice:int, cnt:int)->int:
    if b is None:
        return 0
    if b.des.val == radice:
        cnt+=1
        return 1+conta(b.sin, radice, cnt)+conta(b.des, radice, cnt)
    
    return conta(b.sin, radice, cnt)+conta(b.des, radice, cnt)