# 34. Crea la clase Arbol
    # - Define un árbol genérico con un tronco y ramas como atributos.
    # - Métodos disponibles: crecer_tronco, nueva_rama, crecer_ramas, quitar_rama, info_arbol.
    # - Código a seguir:
    #     1. Inicializar un árbol con un tronco de longitud 1 y una lista vacía de ramas.
    #     2. Implementar el método crecer_tronco para aumentar la longitud del tronco en una unidad.
    #     3. Implementar el método nueva_rama para agregar una nueva rama de longitud 1 a la lista de ramas.
    #     4. Implementar el método crecer_ramas para aumentar en una unidad la longitud de todas las ramas existentes.
    #     5. Implementar el método quitar_rama para eliminar una rama en una posición específica.
    #     6. Implementar el método info_arbol para devolver información sobre la longitud del tronco, el número de ramas y sus longitudes.
    # - Caso de uso:
    #     - a. Crear un árbol.
    #     - b. Hacer crecer el tronco una unidad.
    #     - c. Añadir una nueva rama.
    #     - d. Hacer crecer todas las ramas una unidad.
    #     - e. Añadir dos nuevas ramas.
    #     - f. Retirar la rama situada en la posición 2.
    #     - g. Obtener información sobre el árbol.
    
# Creación de la clase con sus respectivos métodos
class Arbol:
    def __init__(self):
        """Método constructor de la clase.

        Args:
            tronco (int): establece la longitud del tronco.
            ramas (list): lista de ramas existentes en el árbol.
        """
        self.tronco = 1
        self.ramas = []
        
    def crecer_tronco(self):
        """Aumenta la longitud del tronco en una unidad.
        """
        self.tronco +=1
        
    def nueva_rama(self):
        """Agrega una nueva rama con longitud 1 unidad a la lista de ramas.
        """
        self.ramas.append(1)
              
    def crecer_ramas(self):
        """Aumentar en una unidad la longitud de todas las ramas existentes.
        """
        for i in range(len(self.ramas)):
            self.ramas[i] += 1
        
    def quitar_rama(self, posicion):
        """Elimina una rama en una posición específica.
        """
        self.ramas.pop(posicion)
         
    def info_arbol(self):
        """Devuelve información sobre la longitud del tronco, el número de ramas y sus longitudes.
        """
        
        print(f"La longitud del tronco es de {self.tronco} unidades")
        print(f"El número de ramas es de {len(self.ramas)} y las longitudes son de {self.ramas}")
             
# Caso de uso
    #     - a. Crear un árbol.
arbol = Arbol()
    #     - b. Hacer crecer el tronco una unidad.
arbol.crecer_tronco()
    #     - c. Añadir una nueva rama.
arbol.nueva_rama()
    #     - d. Hacer crecer todas las ramas una unidad.
arbol.crecer_ramas()
    #     - e. Añadir dos nuevas ramas.
arbol.nueva_rama()
arbol.nueva_rama()
    #     - f. Retirar la rama situada en la posición 2.
arbol.quitar_rama(2)
    #     - g. Obtener información sobre el árbol.
arbol.info_arbol()