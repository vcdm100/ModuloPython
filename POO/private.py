class MinhaClasse:
    def __init__(self):
        self.__atributo_private = 42;
        
    def __metodo_private(self):
        print("Esse método é private!"); 
        
    def aceesarMetodoPRivate(self):
        self.__metodo_private();

objeto = MinhaClasse();
#objeto.__metodo_private(); - Acesso não permitido

objeto.aceesarMetodoPRivate();

""" RESULTADO (TERMINAL)

Esse método é private!

"""