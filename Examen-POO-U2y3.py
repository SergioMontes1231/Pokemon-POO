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
