#Algoritmo di Floyd-Warshall
def floyd(graph):
    n = len(graph)
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i==j:
                dist[i][j]=0   #imposta la diagonale a 0, poichè la distanza di un nodo a se stesso è ovviamente 0
            elif graph[i][j]!=0:    
                dist[i][j]=graph[i][j]  #vengono aggiornate le distanza con valori reali del grafo
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:        
                    dist[i][j] = dist[i][k] + dist[k][j]
                                    #viene verificata per ciascuna coppia di nodi (i, j). Se la somma della distanza tra il nodo sorgente i e il nodo intermedio k, 
                                    #insieme alla distanza tra il nodo intermedio k e il nodo destinazione j, è minore della distanza attualmente nota 
                                    #tra i nodi sorgente e destinazione, allora l'algoritmo aggiorna la distanza tra i nodi sorgente e destinazione 
                                    #con la nuova distanza calcolata tramite il nodo intermedio k.
    return dist