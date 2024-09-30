class NodoArbol:
    def __init__(self, nombre, es_heroe):
        self.nombre = nombre
        self.es_heroe = es_heroe
        self.izquierdo = None
        self.derecho = None

class ArbolMarvel:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, es_heroe):
        nuevo_nodo = NodoArbol(nombre, es_heroe)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, nodo_actual, nuevo_nodo):
        if nuevo_nodo.nombre < nodo_actual.nombre:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, nuevo_nodo)
        else:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = nuevo_nodo
            else:
                self._insertar_recursivo(nodo_actual.derecho, nuevo_nodo)

    # b) 
    def listar_villanos(self):
        villanos = []
        self._listar_villanos_recursivo(self.raiz, villanos)
        return villanos

    def _listar_villanos_recursivo(self, nodo, villanos):
        if nodo:
            self._listar_villanos_recursivo(nodo.izquierdo, villanos)
            if not nodo.es_heroe:  # Es villano
                villanos.append(nodo.nombre)
            self._listar_villanos_recursivo(nodo.derecho, villanos)

    # c)
    def listar_superheroes_con_C(self):
        heroes_con_C = []
        self._listar_superheroes_con_C_recursivo(self.raiz, heroes_con_C)
        return heroes_con_C

    def _listar_superheroes_con_C_recursivo(self, nodo, heroes_con_C):
        if nodo:
            self._listar_superheroes_con_C_recursivo(nodo.izquierdo, heroes_con_C)
            if nodo.es_heroe and nodo.nombre.startswith('C'):
                heroes_con_C.append(nodo.nombre)
            self._listar_superheroes_con_C_recursivo(nodo.derecho, heroes_con_C)

    # d) 
    def contar_superheroes(self):
        return self._contar_superheroes_recursivo(self.raiz)

    def _contar_superheroes_recursivo(self, nodo):
        if nodo is None:
            return 0
        conteo = 1 if nodo.es_heroe else 0
        return conteo + self._contar_superheroes_recursivo(nodo.izquierdo) + self._contar_superheroes_recursivo(nodo.derecho)

    # e) 
    def corregir_doctor_strange(self):
        self._corregir_doctor_strange_recursivo(self.raiz)

    def _corregir_doctor_strange_recursivo(self, nodo):
        if nodo is None:
            return
        if "Strange" in nodo.nombre:
            print(f"Nombre incorrecto encontrado: {nodo.nombre}. Corrigiendo a 'Doctor Strange'.")
            nodo.nombre = "Doctor Strange"
        self._corregir_doctor_strange_recursivo(nodo.izquierdo)
        self._corregir_doctor_strange_recursivo(nodo.derecho)

    # f) 
    def listar_superheroes_descendente(self):
        heroes = []
        self._listar_superheroes_descendente_recursivo(self.raiz, heroes)
        return heroes

    def _listar_superheroes_descendente_recursivo(self, nodo, heroes):
        if nodo:
            self._listar_superheroes_descendente_recursivo(nodo.derecho, heroes)
            if nodo.es_heroe:
                heroes.append(nodo.nombre)
            self._listar_superheroes_descendente_recursivo(nodo.izquierdo, heroes)

    # g)
    def generar_bosque(self):
        arbol_heroes = ArbolMarvel()
        arbol_villanos = ArbolMarvel()
        self._generar_bosque_recursivo(self.raiz, arbol_heroes, arbol_villanos)
        return arbol_heroes, arbol_villanos

    def _generar_bosque_recursivo(self, nodo, arbol_heroes, arbol_villanos):
        if nodo:
            if nodo.es_heroe:
                arbol_heroes.insertar(nodo.nombre, nodo.es_heroe)
            else:
                arbol_villanos.insertar(nodo.nombre, nodo.es_heroe)
            self._generar_bosque_recursivo(nodo.izquierdo, arbol_heroes, arbol_villanos)
            self._generar_bosque_recursivo(nodo.derecho, arbol_heroes, arbol_villanos)

    # g.I)
    def contar_nodos(self):
        return self._contar_nodos_recursivo(self.raiz)

    def _contar_nodos_recursivo(self, nodo):
        if nodo is None:
            return 0
        return 1 + self._contar_nodos_recursivo(nodo.izquierdo) + self._contar_nodos_recursivo(nodo.derecho)

    # g.II) 
    def barrido_alfabetico(self):
        elementos = []
        self._barrido_alfabetico_recursivo(self.raiz, elementos)
        return elementos

    def _barrido_alfabetico_recursivo(self, nodo, elementos):
        if nodo:
            self._barrido_alfabetico_recursivo(nodo.izquierdo, elementos)
            elementos.append(nodo.nombre)
            self._barrido_alfabetico_recursivo(nodo.derecho, elementos)


arbol_mcu = ArbolMarvel()
arbol_mcu.insertar("Iron Man", True)
arbol_mcu.insertar("Thanos", False)
arbol_mcu.insertar("Captain America", True)
arbol_mcu.insertar("Loki", False)
arbol_mcu.insertar("Spider-Man", True)
arbol_mcu.insertar("Doctor Stranger", True)  
arbol_mcu.insertar("Black Widow", True)
arbol_mcu.insertar("Ultron", False)

# b) 
villanos = arbol_mcu.listar_villanos()
print("Villanos ordenados alfabéticamente:", villanos)

# c)
heroes_con_C = arbol_mcu.listar_superheroes_con_C()
print("Superhéroes que empiezan con C:", heroes_con_C)

# d) 
cantidad_heroes = arbol_mcu.contar_superheroes()
print(f"Cantidad de superhéroes: {cantidad_heroes}")

# e) 
arbol_mcu.corregir_doctor_strange()

# f) 
heroes_descendentes = arbol_mcu.listar_superheroes_descendente()
print("Superhéroes ordenados de manera descendente:", heroes_descendentes)

# g) 
arbol_heroes, arbol_villanos = arbol_mcu.generar_bosque()

# g.I) 
nodos_heroes = arbol_heroes.contar_nodos()
nodos_villanos = arbol_villanos.contar_nodos()
print(f"El árbol de superhéroes tiene {nodos_heroes} nodos.")
print(f"El árbol de villanos tiene {nodos_villanos} nodos.")

# g.II)
heroes_alfabetico = arbol_heroes.barrido_alfabetico()
villanos_alfabetico = arbol_villanos.barrido_alfabetico()
print("Superhéroes en orden alfabético:", heroes_alfabetico)
print("Villanos en orden alfabético:", villanos_alfabetico)
