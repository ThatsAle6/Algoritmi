from alberi.alberibinari import AlberoBin

#TRACCIA:
#   Si deve realizzare un metodo ricorsivo
#       public static boolean verifica(AlberoBinario a) {…}
#   che restituisce true se e solo se almeno una delle foglie più profonde dell’albero contiene 
#   un valore maggiore o uguale a zero.

def verifica(a:AlberoBin)->bool:
    if a is None:
        return False
    return controlla(a,0,0)

def controlla(a:AlberoBin, profonditaFoglia: int, maxProfondita:int)->bool:
    if a is None:
        return False
    if a.sin is None and a.des is None and profonditaFoglia > maxProfondita:
        return a.val >= 0
    return controlla(a.sin, profonditaFoglia+1, maxProfondita) or controlla(a.des, profonditaFoglia+1, maxProfondita)

#Complessità:
#   CTM(n)= Theta(1) 
#   CTP(n)= Theta

#   CSM(n)= Theta
#   CSP(n)= Theta