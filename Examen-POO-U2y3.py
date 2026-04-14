# CLASES ABSTRACTA
from abc import ABC, abstractmethod
from typing import List

class PokemonBase(ABC):
    def __init__(self, nombre = "Sin nombre", descripcion = "Sin descripcion", vida = 0,
        nivel = 0, evolucion = 1, ataque = 0, defensa = 0, atrapado = False) :
        self.nombre = nombre
        self.descripcion = descripcion
        self.vida = vida
        self.nivel = nivel
        self.evolucion = evolucion
        self.ataque = ataque
        self.defensa = defensa
        self.atrapado = atrapado

    @abstractmethod
    def hablar(self):
        pass

    @abstractmethod
    def detallesPokemon(self):
        pass

    @abstractmethod
    def actualizar(self):
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


# Pokemon
class Pokemon(PokemonBase):
    def __init__(self, evoluciones, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado):
        super().__init__(evoluciones[0], descripcion, vida, nivel, evolucion, ataque, defensa, atrapado)
        self.evoluciones = evoluciones

    def hablar(self):
        print(f"{self.nombre}!")

    def detallesPokemon(self):
        print (f""" ==== {self.nombre} =====
Despcripcion: {self.descripcion}
Vida: {self.vida}
Nivel: {self.nivel}
Evolucion: {self.evolucion}
Ataque: {self.ataque}
Defensa: {self.defensa}
Atrapado: {self.atrapado}
================\n""")

    def entrenar(self):
        self.ataque += 10 
        self.defensa += 10
        self.nivel += 10
        self.vida += 10

        if self.nivel >= 100:
            if self.evolucion < len(self.evoluciones):
                self.evolucion += 1
                self.nombre = self.evoluciones[self.evolucion-1]
                print(f"¡Evolucionó! Ahora es {self.nombre}")
            else:
                print("Ya no puede evolucionar más")

            self.nivel = 1

        self.limitar_stats()

    def subirAtaque(self):
        self.ataque += 20
        self.limitar_stats()

    def subirDefensa(self):
        self.defensa += 20
        self.limitar_stats()

    def subirVida(self):
        self.vida += 20
        self.limitar_stats()

    def actualizar(self):
        self.ataque += 20
        self.defensa += 20
        self.vida += 20
        self.limitar_stats()

    def limitar_stats(self):
        self.ataque = max(1, min(self.ataque, 1000))
        self.defensa = max(1, min(self.defensa, 1000))
        self.vida = max(1, min(self.vida, 1000))
        self.nivel = max(1, min(self.nivel, 100))


# Clase de union
class PokemonConEntrenamiento(Pokemon, Entrenamiento):
    def __init__(self, evoluciones, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado):
        super().__init__(evoluciones, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado)


# Pokemon con especializacion
class PokemonAgua(PokemonConEntrenamiento):
    def __init__(self, evoluciones, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado):
        super().__init__(evoluciones, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado)
        self.atribto_especial = "Hidrobomba"

    def actualizar(self):
        self.ataque += 10
        self.defensa += 20
        self.vida += 10
        self.limitar_stats()


class PokemonFuego(PokemonConEntrenamiento):
    def __init__(self, evoluciones, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado):
        super().__init__(evoluciones, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado)
        self.atribto_especial = "Lanzallamas"

    def actualizar(self):
        self.ataque += 30
        self.defensa += 10
        self.vida += 10
        self.limitar_stats()


class PokemonElectrico(PokemonConEntrenamiento):
    def __init__(self, evoluciones, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado):
        super().__init__(evoluciones, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado)
        self.atribto_especial = "Impactrueno" 

    def actualizar(self):
        self.ataque += 25
        self.defensa += 5
        self.vida += 10
        self.limitar_stats()


class PokemonHierba(PokemonConEntrenamiento):
    def __init__(self, evoluciones, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado):
        super().__init__(evoluciones, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado)
        self.atribto_especial = "Látigo Cepa"

    def actualizar(self):
        self.ataque += 10
        self.defensa += 15
        self.vida += 25
        self.limitar_stats()
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
