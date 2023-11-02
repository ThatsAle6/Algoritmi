def Kruscal(self):
    result = []     #lista che conterrà gli  archi del MST (Minimum Spanning Tree)
    i = 0   #variabile utlizzata per attraversare gli archi ordinati, in ordine crescente di peso
    e = 0   #variabile di conteggio, tiene traccia del numero di archi aggiunti al MST
    
    self.graph = (sorted(self.graph, key=lambda item:item[2]))  #ordino in ordine crescente di peso, Key = ecc.. specifica il criterio di ordinamento
    
    parent = []     #rappresenta i set dei nodi nel grafo
    rank = []   #raprresenta  il rango di ciascun set

    for node in range(self.V):
        parent.append(node)
        rank.append(0)

    while e < self.V-1:     #il ciclo continua finchè non vengono aggiunti V-1 archi al MST
        u, v, w = self.graph[i]     #u: una estremità del grafo,   v: l'altra espremità,     w: peso
        i = i+1

        x = self.find(parent, u)    #rappresenta la radice del set a cui appartiene il nodo u
        y = self.find(parent, v)    #rappresenta la radice del set a cui appartiene il nodo v
        
        #L'obiettivo principale di x e y è verificare se i nodi u e v sono già nello stesso set
        #se sono uguali significa che appartengo allo stesso set e quindi creerebero dei cicli
        #se sono diversi significa che appartengo a set diversi e quindi non creano cicli

        if x!=y:
            e = e+1
            result.append([u,v,w])
            self.union(parent, rank, x, y)
    
    return result

    #find cerca la radice di un insieme a cui appartiene un nodo specifico.
    #union unisce due insiemi in base al loro rango, collegando la radice di un insieme all'altro.