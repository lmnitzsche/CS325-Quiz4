from abc import ABC, abstractmethod

class Jedi(ABC):
    @abstractmethod
    def use_lightsaber(self):
        pass

    @abstractmethod
    def use_force(self):
        pass

class LukeSkywalker(Jedi):
    def use_lightsaber(self):
        print("Luke Skywalker uses his lightsaber.")

    def use_force(self):
        print("Luke Skywalker uses the Force.")

class Yoda(Jedi):
    def use_lightsaber(self):
        print("Uses Lightsaber with great skill, Yoda does.")

    def use_force(self):
        print("Expells the force, Yoda does.")
