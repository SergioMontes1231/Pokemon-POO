from abc import ABC, abstractmethod
import random

class PokemonBase(ABC):
    def __init__(self, nombre = "Sin Pokemon", descripcion = "Sin descripcion", vida = 0,
        nivel = 0, evolucion = 1, ataque = 0, defensa = 0, atrapado = False):
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


class Pokemon(PokemonBase):
    def __init__(self, nombre, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado, evoluciones):
        super().__init__(nombre, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado)
        self.evoluciones = evoluciones

    def hablar(self):
        print(f"{self.nombre}!")

    def detallesPokemon(self):
        print(f"""
===== {self.nombre} =====
Descripcion: {self.descripcion}
Vida: {self.vida}
Nivel: {self.nivel}
Evolucion: {self.evolucion}
Ataque: {self.ataque}
Defensa: {self.defensa}
Atrapado: {self.atrapado}
================
""")
    
    
    def limitar_stats(self):
        if self.ataque < 1:
            self.ataque = 1
        if self.ataque > 1000:
            self.ataque = 1000
        if self.defensa < 1:
            self.defensa = 1
        if self.defensa > 1000:
            self.defensa = 1000
        if self.vida < 1:
            self.vida = 1
        if self.vida > 1000:
            self.vida = 1000
        if self.nivel < 0:
            self.nivel = 0
        if self.nivel > 100:
            self.nivel = 100
    
    def entrenar(self):
        self.ataque += 10
        self.defensa += 10
        self.nivel += 10
        self.vida += 10
        self.limitar_stats()
        
        if self.nivel >= 100:
            if self.evolucion < len(self.evoluciones):
                self.evolucion += 1
                self.nombre = self.evoluciones[self.evolucion - 1]
                print(f"¡El Pokemon ha evolucionado! Ahora es: {self.nombre}")
                self.nivel = 0
            else:
                print("Ya no puede evolucionar mas")
                self.nivel = 100

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


class PokemonConEntrenamiento(Pokemon, Entrenamiento):
    def __init__(self, nombre, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado, evoluciones):
        super().__init__(nombre, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado, evoluciones)


class PokemonAgua(PokemonConEntrenamiento):
    def __init__(self, nombre, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado, evoluciones):
        super().__init__(nombre, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado, evoluciones)
        self.ataque_especial = "Hidrobomba"

    def actualizar(self):
        self.ataque += 10
        self.defensa += 20
        self.vida += 10
        self.limitar_stats()


class PokemonFuego(PokemonConEntrenamiento):
    def __init__(self, nombre, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado, evoluciones):
        super().__init__(nombre, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado, evoluciones)
        self.ataque_especial = "Lanzallamas"

    def actualizar(self):
        self.ataque += 30
        self.defensa += 10
        self.vida += 10
        self.limitar_stats()


class PokemonElectrico(PokemonConEntrenamiento):
    def __init__(self, nombre, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado, evoluciones):
        super().__init__(nombre, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado, evoluciones)
        self.ataque_especial = "Impactrueno"

    def actualizar(self):
        self.ataque += 25
        self.defensa += 5
        self.vida += 10
        self.limitar_stats()


class PokemonHierba(PokemonConEntrenamiento):
    def __init__(self, nombre, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado, evoluciones):
        super().__init__(nombre, descripcion, vida, nivel, evolucion, ataque, defensa, atrapado, evoluciones)
        self.ataque_especial = "Latigo Cepa"

    def actualizar(self):
        self.ataque += 10
        self.defensa += 15
        self.vida += 25
        self.limitar_stats()


enemigos = []
pokemons_atrapados = []
pokemon_jugador = None


def crear_pokemon_enemigo(nombre, descripcion, vida, ataque, defensa, nivel, ataque_especial):
    class Enemigo(PokemonConEntrenamiento):
        def __init__(self):
            super().__init__(nombre, descripcion, vida, nivel, 1, ataque, defensa, False, [nombre])
            self.ataque_especial = ataque_especial
        
        def actualizar(self):
            self.ataque += 10
            self.defensa += 10
            self.vida += 10
            self.limitar_stats()
    
    return Enemigo()


def inicializar_enemigos():
    global enemigos
    enemigos = [
        crear_pokemon_enemigo("Magikarp", "Pokemon bajo", 50, 10, 30, 1, "Salpicadura"),
        crear_pokemon_enemigo("Rattata", "Pokemon bajo", 60, 25, 35, 2, "Mordisco"),
        crear_pokemon_enemigo("Gyarados", "Pokemon alto", 200, 80, 60, 30, "Hidrobomba"),
        crear_pokemon_enemigo("Dragonite", "Pokemon alto", 250, 90, 70, 40, "Dracoataque")
    ]
    
def combate():
    global pokemon_jugador, pokemons_atrapados, enemigos
    
    if pokemon_jugador is None:
        print("\nPrimero debes elegir un Pokemon")
        return
    
    enemigo = random.choice(enemigos)
    
    print(f"\n===== INICIO DE COMBATE =====")
    print(f"Un {enemigo.nombre} salvaje aparecio")
    
    enemigo_original_vida = enemigo.vida
    enemigo_original_defensa = enemigo.defensa
    
    while pokemon_jugador.vida > 0 and enemigo.vida > 0:
        print(f"\n----- TURNO -----")
        print(f"\nTU POKEMON:")
        print(f"Nombre: {pokemon_jugador.nombre}")
        print(f"Ataque: {pokemon_jugador.ataque}")
        print(f"Defensa: {pokemon_jugador.defensa}")
        print(f"Vida: {pokemon_jugador.vida}")
        
        print(f"\nENEMIGO:")
        print(f"Nombre: {enemigo.nombre}")
        print(f"Ataque: {enemigo.ataque}")
        print(f"Defensa: {enemigo.defensa}")
        print(f"Vida: {enemigo.vida}")
        
        print(f"\nOpciones:")
        print("1. Pasar turno")
        print("2. Ataque normal")
        print("3. Ataque especial")
        print("4. Huir")
        
        opcion = input("\nElige una opcion: ")
        
        if opcion == "1":
            print("\nDecidiste pasar el turno")
        elif opcion == "2":
            danio = pokemon_jugador.ataque
            if danio >= enemigo.defensa:
                danio_restante = danio - enemigo.defensa
                enemigo.defensa = 0
                enemigo.vida -= danio_restante
                if enemigo.vida < 0:
                    enemigo.vida = 0
                print(f"\n¡Atacaste! Causaste {danio} de danio")
            else:
                enemigo.defensa -= danio
                print(f"\n¡Atacaste! La defensa del enemigo disminuyo a {enemigo.defensa}")
        elif opcion == "3":
            danio = pokemon_jugador.ataque * 2
            if danio >= enemigo.defensa:
                danio_restante = danio - enemigo.defensa
                enemigo.defensa = 0
                enemigo.vida -= danio_restante
                if enemigo.vida < 0:
                    enemigo.vida = 0
                print(f"\n¡Usaste {pokemon_jugador.ataque_especial}! Causaste {danio} de daño")
            else:
                enemigo.defensa -= danio
                print(f"\n¡Usaste {pokemon_jugador.ataque_especial}! La defensa del enemigo disminuyo a {enemigo.defensa}")
        elif opcion == "4":
            print("\n¡Huiste del combate!")
            enemigo.vida = enemigo_original_vida
            enemigo.defensa = enemigo_original_defensa
            return
        else:
            print("\nOpcion invalida")
            continue
        
        if enemigo.vida <= 0:
            print(f"\n¡Derrotaste a {enemigo.nombre}!")
            resultado_atrapado = random.choice([True, False])
            if resultado_atrapado:
                enemigo.atrapado = True
                pokemons_atrapados.append(enemigo)
                print(f"¡Atrapaste a {enemigo.nombre}!")
            else:
                print(f"{enemigo.nombre} logro escapar")
            break
        
        accion_enemigo = random.choice([1, 2, 3])
        if accion_enemigo == 1:
            print(f"\n{enemigo.nombre} decidio pasar el turno")
        elif accion_enemigo == 2:
            danio = enemigo.ataque
            if danio >= pokemon_jugador.defensa:
                danio_restante = danio - pokemon_jugador.defensa
                pokemon_jugador.defensa = 0
                pokemon_jugador.vida -= danio_restante
                if pokemon_jugador.vida < 0:
                    pokemon_jugador.vida = 0
                print(f"\n{enemigo.nombre} te ataco! Recibiste {danio} de daño")
            else:
                pokemon_jugador.defensa -= danio
                print(f"\n{enemigo.nombre} te ataco! Tu defensa disminuyo a {pokemon_jugador.defensa}")
        elif accion_enemigo == 3:
            danio = enemigo.ataque * 2
            if danio >= pokemon_jugador.defensa:
                danio_restante = danio - pokemon_jugador.defensa
                pokemon_jugador.defensa = 0
                pokemon_jugador.vida -= danio_restante
                if pokemon_jugador.vida < 0:
                    pokemon_jugador.vida = 0
                print(f"\n{enemigo.nombre} uso ataque especial! Recibiste {danio} de daño")
            else:
                pokemon_jugador.defensa -= danio
                print(f"\n{enemigo.nombre} uso ataque especial! Tu defensa disminuyo a {pokemon_jugador.defensa}")
        
        if pokemon_jugador.vida <= 0:
            print("\n¡Tu Pokemon fue derrotado!")
            pokemon_jugador.vida = 1
            break
    
    enemigo.vida = enemigo_original_vida
    enemigo.defensa = enemigo_original_defensa

def ver_pokemons_atrapados():
    if len(pokemons_atrapados) == 0:
        print("\nNo hay pokemons atrapados")
    else:
        print("\n===== POKEMONS ATRAPADOS =====")
        for i, p in enumerate(pokemons_atrapados, 1):
            print(f"{i}. {p.nombre}")


def main():
    global pokemon_jugador
    
    print("===== BIENVENIDO A LA POKEDEX =====")
    nombre_entrenador = input("Ingresa tu nombre: ")
    print(f"\n¡Hola {nombre_entrenador}!")
    print("No tienes un Pokemon aun.")
    
    print("\nElige tu Pokemon inicial:")
    print("1. Pokemon Agua - Squirtle")
    print("2. Pokemon Fuego - Charmander")
    print("3. Pokemon Electrico - Pichu")
    print("4. Pokemon Hierba - Bulbasaur")
    
    opcion_inicial = input("\nElige una opcion: ")
    
    if opcion_inicial == "1":
        evoluciones = ["Squirtle", "Wartortle", "Blastoise"]
        pokemon_jugador = PokemonAgua("Squirtle", "Pokemon tortuga agua", 100, 1, 1, 50, 50, True, evoluciones)
    elif opcion_inicial == "2":
        evoluciones = ["Charmander", "Charmeleon", "Charizard"]
        pokemon_jugador = PokemonFuego("Charmander", "Pokemon lagartija fuego", 100, 1, 1, 55, 45, True, evoluciones)
    elif opcion_inicial == "3":
        evoluciones = ["Pichu", "Pikachu", "Raichu"]
        pokemon_jugador = PokemonElectrico("Pichu", "Pokemon raton electrico", 100, 1, 1, 55, 40, True, evoluciones)
    elif opcion_inicial == "4":
        evoluciones = ["Bulbasaur", "Ivysaur", "Venusaur"]
        pokemon_jugador = PokemonHierba("Bulbasaur", "Pokemon semilla planta", 100, 1, 1, 50, 50, True, evoluciones)
    else:
        print("Opcion invalida, se asignara Squirtle")
        evoluciones = ["Squirtle", "Wartortle", "Blastoise"]
        pokemon_jugador = PokemonAgua("Squirtle", "Pokemon tortuga agua", 100, 1, 1, 50, 50, True, evoluciones)
    
    print("\n¡Has elegido a tu Pokemon!")
    pokemon_jugador.detallesPokemon()
    
    inicializar_enemigos()
    
    while True:
        print(f"\n===== MENU PRINCIPAL =====")
        print("1. Detalles de mi Pokemon")
        print("2. Hablar Pokemon")
        print("3. Entrenamiento")
        print("4. Combatir")
        print("5. Ver Pokemon Atrapados")
        print("6. Crear Pokemon Enemigo")
        print("7. Salir")
        
        opcion = input("\nElige una opcion: ")
        
        if opcion == "1":
            pokemon_jugador.detallesPokemon()
        elif opcion == "2":
            pokemon_jugador.hablar()
        elif opcion == "3":
            menu_entrenamiento()
        elif opcion == "4":
            combate()
        elif opcion == "5":
            ver_pokemons_atrapados()
        elif opcion == "6":
            crear_enemigo_personalizado()
        elif opcion == "7":
            print("\n¡Gracias por jugar!")
            break
        else:
            print("Opcion invalida")


def menu_entrenamiento():
    global pokemon_jugador
    while True:
        print(f"\n===== ENTRENAMIENTO DE {pokemon_jugador.nombre} =====")
        print("1. Entrenamiento Normal")
        print("2. Entrenamiento Individual")
        print("3. Entrenamiento Intensivo")
        print("4. Entrenamiento Personalizado")
        print("5. Volver al menu principal")
        
        opcion = input("\nElige una opcion: ")
        
        if opcion == "1":
            pokemon_jugador.entrenar()
            print("\n¡Entrenamiento completado!")
            pokemon_jugador.detallesPokemon()
        elif opcion == "2":
            print("\n1. Subir ataque +20")
            print("2. Subir defensa +20")
            print("3. Subir vida +20")
            sub_opcion = input("Elige que mejorar: ")
            if sub_opcion == "1":
                pokemon_jugador.subirAtaque()
                print("\n¡Ataque aumentado!")
            elif sub_opcion == "2":
                pokemon_jugador.subirDefensa()
                print("\n¡Defensa aumentada!")
            elif sub_opcion == "3":
                pokemon_jugador.subirVida()
                print("\n¡Vida aumentada!")
            else:
                print("Opcion invalida")
                continue
            pokemon_jugador.detallesPokemon()
        elif opcion == "3":
            pokemon_jugador.actualizar()
            print("\n¡Entrenamiento intensivo completado!")
            pokemon_jugador.detallesPokemon()
        elif opcion == "4":
            print("\nIngresa los nuevos valores:")
            nuevo_ataque = int(input(f"Ataque actual: {pokemon_jugador.ataque}. Nuevo ataque: "))
            nueva_defensa = int(input(f"Defensa actual: {pokemon_jugador.defensa}. Nueva defensa: "))
            nueva_vida = int(input(f"Vida actual: {pokemon_jugador.vida}. Nueva vida: "))
            nuevo_nivel = int(input(f"Nivel actual: {pokemon_jugador.nivel}. Nuevo nivel: "))
            
            pokemon_jugador.ataque = nuevo_ataque
            pokemon_jugador.defensa = nueva_defensa
            pokemon_jugador.vida = nueva_vida
            pokemon_jugador.nivel = nuevo_nivel
            pokemon_jugador.limitar_stats()
            print("\n¡Entrenamiento personalizado completado!")
            pokemon_jugador.detallesPokemon()
        elif opcion == "5":
            break
        else:
            print("Opcion invalida")

def crear_enemigo_personalizado():
    global enemigos
    print("\n===== CREAR POKEMON ENEMIGO =====")
    nombre = input("Nombre del Pokemon: ")
    descripcion = input("Descripcion: ")
    vida = int(input("Vida del 1 al 1000: "))
    ataque = int(input("Ataque del 1 al 1000: "))
    defensa = int(input("Defensa del 1 al 1000: "))
    nivel = int(input("Nivel del 1 al 100: "))
    ataque_especial = input("Ataque especial: ")
    
    nuevo_enemigo = crear_pokemon_enemigo(nombre, descripcion, vida, ataque, defensa, nivel, ataque_especial)
    nuevo_enemigo.limitar_stats()
    enemigos.append(nuevo_enemigo)
    print(f"\n¡{nombre} ha sido creado y agregado a la lista de enemigos!")


main()
