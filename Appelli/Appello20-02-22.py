
from alberi.abr import AlberoBin

def verificaValori(a:AlberoBin) -> bool:
    if a is None:
        return False
    if a.sin is None or a.des is None:
        return False
    return verifica(a,a)

def verifica(a: AlberoBin, radice:AlberoBin)-> bool:
    if a is None:
        return True
    if a.sin is not None or a.des is not None:
        return True if radice.sin.val > a.val and radice.des.val < a.val else False
    return verifica(a.sin, radice) and verifica(a.des, radice) 