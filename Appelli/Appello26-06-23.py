from alberi.alberibinari import AlberoBin

#TRACCIA
#   Si deve realizzare una funzione ricorsiva:
#       def twoSum(a:AlberoBin, k:int)->bool
#   che restituisce True se e solo se esistano in a almeno due nodi non foglia x e y, tali che x.val() + y.val() = k
 
def twoSum(a:AlberoBin, k:int)->bool:
    if a is None:
        return False
    if a.sin is None and a.des is None:
        return False
    if a.sin is not None and a.des is not None:
        return True if a.sin.val + a.des.val == k else False
    return twoSum(a.sin, k) and twoSum(a.des, k)

#Complessità:
#   CTM(n)= Theta(1) trova subito un nodo non foglia che rispettano la proprietà 
#   CTP(n)= Theta(n) dobbiamo visitare tutto l'albero o comunque tutto l'albero tranne l'ultimo nodo più a destra

#   CSM(n)= Theta(log n) solo se l'albero è bilanciato 
#   CSP(n)= Theta(n) albero degenere

#Version 2
def twoSum2(a:AlberoBin, k:int)->bool:
    if a is None:
        return False
    if a.sin is None and a.des is None:
        return False
    if a.sin is not None and a.des is not None:
        return controlla(a, k, 0) >=2
    return twoSum2(a.sin, k) and twoSum2(a.des, k)

def controlla(a:AlberoBin, k: int, cnt: int)->int:
    if a is None:
        return 0
    cnt = 0
    if a.sin is not None and a.des is not None:
        cnt+=1
        return 1+controlla(a.sin, k, cnt) + controlla(a.des, k, cnt) if a.sin.val + a.des.val == k else 0
    return controlla(a.sin, k, cnt) + controlla(a.des, k, cnt)
