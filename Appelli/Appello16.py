from alberi.alberibinari import AlberoBin

#TRACCIA:
#   Si deve realizzare un metodo ricorsivo
#	    public static boolean verificaAlmenoUnNodo(AlberoBinario a, int l) {…}
#   che restituisce True se e solo se esiste in a al livello l almeno un nodo foglia n che è figlio unico e tale che n.val() 
#   è contenuto in almeno un altro nodo che si trova a un qualsiasi livello l1 tale che l1 != l.

def verificaAlmenoUnNodo(a:AlberoBin, l:int)->bool:
    if a is None:
        return False
    return livello(a,l,0)

def livello(a:AlberoBin, l:int, livA:int)->bool:
    if a is None:
        return False
    if l == livA:
        return contenuto(a, l, livA)
    return livello(a.sin, l, livA+1) or livello(a.des, l, livA+1)
    

def contenuto(a:AlberoBin, l:int, livA:int)->bool:
    if a is None:
        return False
    if a.sin is None and a.des is None and livA != l:
        return unico(a, a.val, 0) == l
    return contenuto(a.sin, l, livA+1) or contenuto(a.des, l, livA+1)

def unico(a:AlberoBin, nodo: int, cnt:int)->int:
    if a is None:
        return 0
    cnt = 0
    if a.val == nodo:
        cnt+=1
        return 1 + unico(a.sin, nodo, cnt) + unico(a.des, nodo, cnt)
    return unico(a.sin, nodo, cnt) + unico(a.des, nodo, cnt)