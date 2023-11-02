from alberi.alberibinari import AlberoBin

#TRACCIA:
#   Si deve realizzare un metodo ricorsivo
#	public static boolean verifica(AlberoBinario a) {…}
#   che restituisce true se e solo se esiste un nodo non foglia n di a tale che tutti i nodi foglia 
#   che appaiono nel sottoalbero radicato in n hanno lo stesso valore. 

#TIPS: quando abbiamo un sottoalbero radicato non dobbiamo fare il confronto da un nodo a caso bensi partiamo dalla radice

def verifica(a:AlberoBin)->bool:
    if a is None:
        return False
    if a.sin is not None and a.des is not None:
        return analizzaValore(a,a.val)
    return verifica(a.sin) or verifica(a.des)

def analizzaValore(a:AlberoBin, radice:int)->bool:
    if a is None:
        return False
    if a.sin is None and a.des is None:
        return True if a.val == radice else False
    return analizzaValore(a.sin,radice) and analizzaValore(a.des,radice)




#CTM(n) = Theta(n) questo perchè in ogni caso devo controllare sia i nodi foglia che quelli non foglia     

#CTP(n) = Theta(n^2) seguono chiamate ricorsive su entrambi i sottoalberi sx e dx

#CSM(n) = Theta(n) perchè ogni chiamata ricorsiva aggiunge uno strato di frame di chiamata alla pila, e la pila delle chiamate 
#può contenere fino a n frame nel caso peggiore

#CSP(n) = Theta(n) albero degenere