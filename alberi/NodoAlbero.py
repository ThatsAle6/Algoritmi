class NodoAlbero:
    def _init_(self, chiave):
        self.chiave = chiave
        self.sinistro = None
        self.destro = None

class AlberoBinario:
    def _init_(self):
        self.radice = None

    def inserisci(self, chiave):
        if self.radice is None:
            self.radice = NodoAlbero(chiave)
        else:
            self._inserisci_ricorsivo(chiave, self.radice)

    def _inserisci_ricorsivo(self, chiave, nodo):
        if chiave < nodo.chiave:
            if nodo.sinistro is None:
                nodo.sinistro = NodoAlbero(chiave)
            else:
                self._inserisci_ricorsivo(chiave, nodo.sinistro)
        else:
            if nodo.destro is None:
                nodo.destro = NodoAlbero(chiave)
            else:
                self._inserisci_ricorsivo(chiave, nodo.destro)

    def cerca(self, chiave):
        return self._cerca_ricorsivo(chiave, self.radice)

    def _cerca_ricorsivo(self, chiave, nodo):
        if nodo is None or nodo.chiave == chiave:
            return nodo
        if chiave < nodo.chiave:
            return self._cerca_ricorsivo(chiave, nodo.sinistro)
        return self._cerca_ricorsivo(chiave, nodo.destro)

    def visita_in_ordine(self):
        self._visita_in_ordine_ricorsivo(self.radice)

    def _visita_in_ordine_ricorsivo(self, nodo):
        if nodo is not None:
            self._visita_in_ordine_ricorsivo(nodo.sinistro)
            print(nodo.chiave)
            self._visita_in_ordine_ricorsivo(nodo.destro)