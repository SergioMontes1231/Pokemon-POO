#======== Clases Abstractas ========
"""
Agregar clases que se usan como bases para otras
"""

from abc import ABC, abstractmethod
class PokemonBase(ABC):
    """
    Representa la plantilla para los pokemones 
        Atributos:
            -nombre(str): Nombre del pokemon
            -descripcion(str): Descripcion del pokemon
            -vida(int): Vida del pokemon
            -nivel(int): Nivel del pokemon
            -evolucion(int): En que "nivel" de evolucion va
            -ataque(int): El daño que puede causar el pokemon
            -defensa(int): La cantidad de daño que puede evitar el pokemon
            -atrapado(bool): Indica si ya se atrapo al pokemon

        Metodos:
            -hablar() -> None: Metodo con el que hablar del pokemon
            -detallesPokemon() -> None: Despliega los atributos del pokemon
            -actualizar() -> None: Ni bombardera idea de que hace xd
            -entrenar() -> None: Hacer entrenar al pokemon y subir stats
    """

    def __init__(self, nombre = "Sin nombre", descripcion = "Sin descripcion", vida = 0,
     nivel = 0, evolucion = 1, ataque = 0, defensa = 0, atrapado = False ):
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
    """
    Representa la plantilla de tipos de acciones que puede realizar un pokemon para subir sus stats
    """

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
class Pokemon(PokemonBase):
    """
    Representa la base para pokemones utilizables con la logica basica
        Atributos:
            -nombre(str): Nombre del pokemon
            -descripcion(str): Descripcion del pokemon
            -vida(int): Vida del pokemon
            -nivel(int): Nivel del pokemon
            -evolucion(int): En que "nivel" de evolucion va
            -ataque(int): El daño que puede causar el pokemon
            -defensa(int): La cantidad de daño que puede evitar el pokemon
            -atrapado(bool): Indica si ya se atrapo al pokemon

        Metodos:
            -hablar() -> None: Metodo con el que hablar del pokemon
            -detalles() -> None: Despliega los atributos del pokemon
            -actualizar() -> None: Ni bombardera idea de que hace xd
            -entrenar() -> None: Hacer entrenar al pokemon y subir stats a la par
            -subirVida() -> None: Sube stat de vida
            -subirAtaque() -> None: Sube stat de Ataque
            -sburDefensa() -> None: Sube stat de defensa

    
    """
    def __init__(self, nombre: str, descripcion: str, vida: int , nivel: int , evolucion: int , ataque: int, defensa: int, atrapado: bool):
        super().__init__(nombre, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado)

    def hablar(self):
        print(f"i {self.nombre} !")

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
        self.defensa +=10
        self.nivel += 10
        self.vida += 10

        if self.nivel >= 100:
            self.evolucion  += 1
            print("="*55)
            print(f"¡El Pokémon ha evolucionado! Ahora es: {self.nombre}")
            print("="*55)
            self.nivel = 0


    def subirAtaque(self):
        boost_ataque = 20
        self.ataque = self.ataque + boost_ataque

    def subirDefensa(self):
        boost_defensa = 20
        self.defensa = self.defensa + boost_defensa

    def subirVida(self):
        boost_vida = 20
        self.vida = self.vida + boost_vida


    def actualizar(self):
        boost_ataque = 20
        boost_defensa = 20
        boost_vida = 20

        self.ataque =  self.ataque + boost_ataque
        self.defensa = self.defensa + boost_defensa
        self.vida = self.vida + boost_vida

class PokemonConEntrenamiento(Pokemon, Entrenamiento):
    """
    Representa la union de los metodos y atributos de clase Pokemon y clase Entrenamiento, para ser usados en una sola herencia
        Atributos:
            -nombre(str): Nombre del pokemon
            -descripcion(str): Descripcion del pokemon
            -vida(int): Vida del pokemon
            -nivel(int): Nivel del pokemon
            -evolucion(int): En que "nivel" de evolucion va
            -ataque(int): El daño que puede causar el pokemon
            -defensa(int): La cantidad de daño que puede evitar el pokemon
            -atrapado(bool): Indica si ya se atrapo al pokemon

        Metodos:
            -hablar() -> None: Metodo con el que hablar del pokemon
            -detalles() -> None: Despliega los atributos del pokemon
            -actualizar() -> None: Ni bombardera idea de que hace xd
            -entrenar() -> None: Hacer entrenar al pokemon y subir stats
    """
    def __init__(self, nombre: str, descripcion: str, vida: int, nivel: int, evolucion: int, ataque: int, defensa: int, atrapado: bool):
        super().__init__(nombre, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado)


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
