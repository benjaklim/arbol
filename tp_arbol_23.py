class NodoArbol:
    def __init__(self, nombre, derrotado_por=None, capturado_por=None, descripcion=None):
        self.nombre = nombre
        self.derrotado_por = derrotado_por
        self.capturado_por = capturado_por
        self.descripcion = descripcion
        self.izquierdo = None
        self.derecho = None

class ArbolCriaturas:
    def __init__(self):
        self.raiz = None

    def insertar(self, nombre, derrotado_por=None, capturado_por=None, descripcion=None):
        nuevo_nodo = NodoArbol(nombre, derrotado_por, capturado_por, descripcion)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar_nodo(self.raiz, nuevo_nodo)

    def _insertar_nodo(self, actual, nuevo_nodo):
        if nuevo_nodo.nombre < actual.nombre:
            if actual.izquierdo is None:
                actual.izquierdo = nuevo_nodo
            else:
                self._insertar_nodo(actual.izquierdo, nuevo_nodo)
        else:
            if actual.derecho is None:
                actual.derecho = nuevo_nodo
            else:
                self._insertar_nodo(actual.derecho, nuevo_nodo)


    def inorden(self):
        def recorrer_inorden(nodo):
            if nodo is not None:
                recorrer_inorden(nodo.izquierdo)
                print(f"Criatura: {nodo.nombre}, Derrotado por: {nodo.derrotado_por}")
                recorrer_inorden(nodo.derecho)
        recorrer_inorden(self.raiz)

    def agregar_descripcion(self, nombre, descripcion):
        nodo = self.buscar_nodo(nombre)
        if nodo:
            nodo.descripcion = descripcion


    def mostrar_informacion(self, nombre):
        nodo = self.buscar_nodo(nombre)
        if nodo:
            print(f"Nombre: {nodo.nombre}, Derrotado por: {nodo.derrotado_por}, Capturado por: {nodo.capturado_por}, Descripción: {nodo.descripcion}")
        else:
            print("Criatura no encontrada.")


    def buscar_nodo(self, nombre):
        return self._buscar_nodo_recursivo(self.raiz, nombre)

    def _buscar_nodo_recursivo(self, actual, nombre):
        if actual is None or actual.nombre == nombre:
            return actual
        if nombre < actual.nombre:
            return self._buscar_nodo_recursivo(actual.izquierdo, nombre)
        else:
            return self._buscar_nodo_recursivo(actual.derecho, nombre)

    def listar_derrotadas_por(self, heroe):
        def recorrer(nodo):
            if nodo is not None:
                recorrer(nodo.izquierdo)
                if nodo.derrotado_por == heroe:
                    print(nodo.nombre)
                recorrer(nodo.derecho)
        recorrer(self.raiz)

    def listar_no_derrotadas(self):
        def recorrer(nodo):
            if nodo is not None:
                recorrer(nodo.izquierdo)
                if nodo.derrotado_por is None:
                    print(nodo.nombre)
                recorrer(nodo.derecho)
        recorrer(self.raiz)

    def modificar_captura_heracles(self, criaturas):
        for criatura in criaturas:
            nodo = self.buscar_nodo(criatura)
            if nodo:
                nodo.capturado_por = "Heracles"

    def buscar_coincidencia(self, cadena):
        resultados = []
        def recorrer(nodo):
            if nodo is not None:
                recorrer(nodo.izquierdo)
                if cadena.lower() in nodo.nombre.lower():
                    resultados.append(nodo.nombre)
                recorrer(nodo.derecho)
        recorrer(self.raiz)
        return resultados
    
    def eliminar(self, nombre):
        self.raiz = self._eliminar_nodo(self.raiz, nombre)

    def _eliminar_nodo(self, actual, nombre):
        if actual is None:
            return actual
        if nombre < actual.nombre:
            actual.izquierdo = self._eliminar_nodo(actual.izquierdo, nombre)
        elif nombre > actual.nombre:
            actual.derecho = self._eliminar_nodo(actual.derecho, nombre)
        else:
            if actual.izquierdo is None:
                return actual.derecho
            elif actual.derecho is None:
                return actual.izquierdo

            sucesor = self._minimo_valor(actual.derecho)
            actual.nombre = sucesor.nombre
            actual.derrotado_por = sucesor.derrotado_por
            actual.capturado_por = sucesor.capturado_por
            actual.derecho = self._eliminar_nodo(actual.derecho, sucesor.nombre)

        return actual

    def _minimo_valor(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

arbol = ArbolCriaturas()
arbol.insertar("Cerbero")
arbol.insertar("Toro de Creta", derrotado_por="Teseo")
arbol.insertar("Hidra de Lerna", derrotado_por="Heracles")
arbol.insertar("Quimera", derrotado_por="Belerofonte")
arbol.insertar("Ladón", derrotado_por="Heracles")

# a) 
arbol.inorden()

# c) 
arbol.mostrar_informacion("Quimera")

# e)
arbol.listar_derrotadas_por("Heracles")

# f) 
arbol.listar_no_derrotadas()

# h) 
arbol.modificar_captura_heracles(["Cerbero", "Toro de Creta"])

# i) 
print(arbol.buscar_coincidencia("Creta"))

# j) 
arbol.eliminar("Basilisco")
arbol.eliminar("Sirenas")
