from alberi.alberibinari import AlberoBin


#MIA VERSIONE, poco ottimizzata
def dueNodiLivello(a:AlberoBin, l:int)->bool:
    if a is None:
        return False
    return verifica(a, 0, l)

def verifica(a:AlberoBin, livA:int, l:int)->bool:
    if a is None:
        return False
    if livA!=l:
        return False
    if confronto(a):
        return True
    return verifica(a.sin, livA+1, l) and verifica(a.des, livA+1, l)

def confronto(a:AlberoBin)->bool:
    if a is None:
        return False
    if a.sin.val != a.des.val:
        return False
    return confronto(a.sin) and confronto(a.des)


#VERSIONE di ALE, ben ottimizzata
def dueNodiLivello2(a:AlberoBin, l:int)->bool:
    if a is None:
        return False
    if livello(a, 0, l):
        return a.sin.val == a.des.val if a.sin is not None and a.des is not None else False
    if a.sin is None and a.des is None:
        return False
    return dueNodiLivello2(a.sin, l) and dueNodiLivello2(a.des, l)

def livello(a:AlberoBin, livA:int, l:int)->bool:
    if a is None:
        return False
    return livello(a.sin, livA+1,l) and livello(a.des, livA+1,l)