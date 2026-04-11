#======== Clases Abstractas ========
"""
Agregar clases que se usan como bases para otras
"""

from abc import ABC, abstractmethod

class PokemonBase(ABC):
    def __init__(self, nombre = "Sin pokemon", descripcion = "Sin descripcion", ataque = 0, defensa = 0, vida = 0, nivel = 0, evolucion = 1, atrapado = False) -> None:
        self.nombre = nombre
        self.descripcion = descripcion
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        self.nivel = nivel
        self.evolucion = evolucion
        self.atrapado = atrapado

    @abstractmethod
    def hablar(self):
        pass

    @abstractmethod
    def actualizar(self):
        pass

    @abstractmethod
    def detallesPokemon(self):
        pass

    @abstractmethod
    def entrenar(self):
        pass


class Entrenamiento(ABC):
    @abstractmethod
    def subirAtaque(self):
        pass

    @abstractmethod
    def subirDefensa(self):
        pass

    @abstractmethod
    def subirVida(self):
        pass
#======== Pokemon ========
"""
"""
from clases_abstractas import Entrenamiento, PokemonBase

class Pokemon(PokemonBase):
    def __init__(self, nombre, descripcion, ataque, defensa, vida, nivel, evolucion, atrapado ) -> None:
        super().__init__(nombre, descripcion, ataque, defensa, vida, nivel, evolucion, atrapado)

    def hablar(self):
        print(f"{self.nombre} !!")

    def actualizar(self):
        self.ataque
        self.defensa += 20
        self.vida += 20


    def subirAtaque(self):
        boost_ataque = 20
        self.ataque = self.ataque + boost_ataque


    def subirDefensa(self):
        boost_defensa = 20
        self.defensa = self.defensa + boost_defensa

    def subirVida(self):
        boost_vida = 20
        self.vida = self.vida + boost_vida

    def entrenar(self):
        self.ataque = self.ataque + 10
        self.defensa = self.defensa + 10
        self.nivel = self.nivel + 10
        self.vida = self.vida + 10
        if self.nivel >= 100:
            print("!El Pokemon ha evolucionado! Ahora es: {self.nombre}")

    def detallesPokemon(self):
        detalles =f"""Nombre: {self.nombre}
        Descripcion:{self.descripcion}
        Ataque: {self.ataque}
        Defensa: {self.defensa}
        Vida: {self.vida}
        Nivel: {self.nivel}
        Evolucion: {self.evolucion}
        atrapado: {self.atrapado}
        """
        print(detalles)
#======== Especializados ========
"""
Clases de los pokemones con tipo
"""
#======== Combate ========
"""
Logica de combate, creacion de enemigos
"""
#======== Utilidades ========
"""
Funciones extras para menus, ciclos fijos, etc.
"""
#======== Main ========
"""
Ejecucion del progama
"""
