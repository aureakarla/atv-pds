class Dog(Animal):
    def __init__(self, nome, breed):
        super().__init__(nome)
        self.breed = breed

    def bark(self):
        return f"{self.nome} diga au!"


if __name__ == "__main__":
    dog = Dog("pingo", "golden retriever")
    dog.set_idade(5)
    dog.set_especies("canino")
    print(dog.nome)         
    print(dog.get_idade())    
    print(dog.get_especies())
    print(dog.bark())