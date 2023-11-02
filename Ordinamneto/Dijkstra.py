def Dijkstra(self, src):

    dist = [float('inf')] * self.V      #è una lista che tiene traccia delle distanze minime dai nodi di origine a tutti gli altri nodi del grafo.
                                        #tutti gli elementi sono impostati su un valore molto grande o infinito
    dist[src] = 0
    sptSet = [False] * self.V   #è una lista booleana utilizzata per tenere traccia dei vertici inclusi nell'albero del percorso più breve

    for cout in range(self.V):  #itera tutti i nodi del grafo

        u = self.minDistance(dist, sptSet)  #cerca il nodo con distanza minima non ancora incluso nell'albero del percorso più breve.

        sptSet[u] = True    #contrassegna il nodo rappresentato da 'u' come inserito 

        for v in range(self.V):

            #verifica se è possibile ottenere una distanza più breve da 'src' a 'v' passando da 'u', se lo è aggiorna la distanza minima.
            if (self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]):
                dist[v] = dist[u] + self.graph[u][v]

    return dist
