from alberi.alberibinari import AlberoBin

def verificaCammini(a:AlberoBin, l:int) -> bool:
    if a is None:
        return False
    return verifica(a, 0, l)

def verifica(a:AlberoBin, livA:int, l:int)->bool:
    if a is None:
        return True
    if livA==l:
        return a.val==0
    if discendenti(a):
        return True
    return verifica(a.sin, livA+1, l) and verifica(a.des, livA+1, l)

def discendenti(a:AlberoBin)->bool:
    if a is None:
        return True
    if a.val !=0:
        return False
    return discendenti(a.sin) and discendenti(a.des)