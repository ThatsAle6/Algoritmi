def Prim(self):
    key = [sys.maxsize] * self.V    #Array per memorizzare il peso minimo dell'arco per ciascun nodo. Viene inizializzato con un valore massimo.
    parent = [None] * self.V        #Array per memorizzare il genitore di ciascun nodo nell'MST. Viene inizializzato come None per tutti i vertici.

    key[0] = 0
    mstSet = [False] * self.V       #Array booleano per tenere traccia dei nodi inclusi nell'MST (con il fine di evitare cicli). Viene inizializzato come False per tutti i nodi.

    parent[0] = -1

    for count in range(self.V):         #controlliamo tutti i nodi

        u = self.minKey(key, mstSet)    #'u' variabile utilizzata per indicare il nodo di partenza, cambia dinamicamente durante l'esecuzione dell'algoritmo
                                        #minKey è responsabile di trovare il prossimo nodo da aggiungere al MST, selezionando il nodo con il peso minimo tra quelli dispobibili

        mstSet[u] = True

        for v in range(self.V):         #analizziamo tutti i nodi adiacenti al nodo 'u' e identifichiamo i nodi che possono essere aggiunti al MST

            if self.graph[u][v] > 0 and mstSet[V] == False and key[v] > self.graph[u][v]:   #controlliamo se un nodo 'v' può essere aggiunto all'MST

                key[v] = self.graph[u][v]
                parent[v] = u
    
    return parent