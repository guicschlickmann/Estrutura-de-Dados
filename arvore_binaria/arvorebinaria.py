class Elemento:
    def __init__(self, valor):
        self.__valor = valor
        self.__filhoesq = None
        self.__filhodir = None

    @property
    def valor(self):
        return self.__valor
    
    @property
    def filhoesq(self):
        return self.__filhoesq
    
    @property
    def filhodir(self):
        return self.__filhodir
    
    @filhoesq.setter
    def filhoesq(self,filhoesq):
        self.__filhoesq = filhoesq

    @filhodir.setter
    def filhodir(self,filhodir):
        self.__filhodir = filhodir


class ArvoreBinaria:
    def __init__(self):
        self.__raiz = None
        self.__lista = []
        self.__cursor = None

    @property
    def lista(self):
        return self.__lista
    
    @lista.setter
    def lista(self,lista):
        self.__lista = lista

    @property
    def raiz(self):
        return self.__raiz
    
    @raiz.setter
    def raiz(self,raiz):
        self.__raiz = raiz

    def busca(self, chavebusca):
        if self.raiz != None:
            self._busca(self.raiz, chavebusca)
        else:
            return False
        
    def _busca(self, raiz, chavebusca):
        if raiz != None:
            if raiz.valor == chavebusca:
                return chavebusca #ou dados 
            else:
                if chavebusca < raiz.valor:
                    return self._busca(raiz.filhoesq,chavebusca)
                else:
                    return self._busca(raiz.filhodir,chavebusca)
        else:
            return False

    def inserir(self,valor):
        if self.raiz != None:
            self._inserir(self.raiz, valor)
        else:
            self.raiz = Elemento(valor)
            
    
    def _inserir(self,raiz,chave):
        if raiz != None:
            if chave < raiz.valor:
                if raiz.filhoesq != None:
                    return self._inserir(raiz.filhoesq, chave)
                else:
                    raiz.filhoesq = Elemento(chave)
            else:
                if raiz.filhodir != None:
                    return self._inserir(raiz.filhodir, chave)
                else:
                    raiz.filhodir = Elemento(chave)

    def excluir(self,valor):
        if self.raiz != None:
            self._excluir(self.raiz,valor)
        else:
            return False
    

    def excluir(self, valor):
        if self.raiz is None:
            return False
        else:
            if self.raiz.valor == valor:
                if self.raiz.filhoesq is None and self.raiz.filhodir is None:
                    self.raiz = None
                elif self.raiz.filhoesq is None:
                    self.raiz = self.raiz.filhodir
                elif self.raiz.filhodir is None:
                    self.raiz = self.raiz.filhoesq
                else:
                    self.raiz.valor = self._encontrar_minimo(self.raiz.filhodir)
                    self._excluir(self.raiz.filhodir, self.raiz.valor)
                return True
            elif valor < self.raiz.valor:
                return self._excluir(self.raiz.filhoesq, valor)
            else:
                return self._excluir(self.raiz.filhodir, valor)

    def _encontrar_minimo(self, raiz):
        while raiz.filhoesq is not None:
            raiz = raiz.filhoesq
        return raiz.valor

    def _excluir(self, raiz, valor):
        if raiz is None:
            return False
        if valor == raiz.valor:
            if raiz.filhoesq is None and raiz.filhodir is None:
                raiz = None
            elif raiz.filhoesq is None:
                raiz = raiz.filhodir
            elif raiz.filhodir is None:
                raiz = raiz.filhoesq
            else:
                raiz.valor = self._encontrar_minimo(raiz.filhodir)
                self._excluir(raiz.filhodir, raiz.valor)
            return True
        elif valor < raiz.valor:
            return self._excluir(raiz.filhoesq, valor)
        else:
            return self._excluir(raiz.filhodir, valor)
            




    def inorder(self):
        if self.raiz != None:
            self._inorder(self.raiz)
        else:
            return False
        
        
    def _inorder(self,raiz):
        if raiz != None:
            self._inorder(raiz.filhoesq)
            self.lista.append(raiz.valor)
            self._inorder(raiz.filhodir)
    
    def preorder(self):
        if self.raiz != None:
            self._preorder(self.raiz)
        else:
            return False
        
    def _preorder(self,raiz):
        if raiz != None:
            self.lista.append(raiz.valor)
            self._preorder(raiz.filhoesq)
            self._preorder(raiz.filhodir)

    def posorder(self):
        if self.raiz != None:
            self._posorder(self.raiz)
        else:
            return False
    
    def _posorder(self,raiz):
        if raiz != None:
            self._posorder(raiz.filhoesq)
            self._posorder(raiz.filhodir)
            self.lista.append(raiz.valor)

a1 = ArvoreBinaria()
a1.inserir(10)
a1.inserir(5)
a1.inserir(20)
a1.inserir(4)
a1.inserir(6)
a1.inserir(12)
#a1.inorder()
a1.posorder()        
print(a1.lista)
print(a1.raiz.filhoesq.valor) #5
print(a1.raiz.filhodir.valor) #20
print(a1.raiz.filhodir.filhoesq.valor) #12
print(a1.raiz.filhoesq.filhoesq.valor) #4
print(a1.raiz.filhoesq.filhodir.valor) #6



    