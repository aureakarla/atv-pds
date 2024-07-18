class Animal:
    def __init__(self, nome):
        self.nome = nome      
        self._idade = None          
        self.__especies = None 

    def get_especies(self):
        return self.__especies

    def set_especies(self, especies):
        self.__especies = especies

    def get_idade(self):
        return self._idade

    def set_idade(self, idade):
        if idade > 0:
            self._idade = idade
            