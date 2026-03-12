# 35. Crea la clase UsuarioBanco
    # - Representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente.
    # - Métodos: retirar_dinero, transferir_dinero, agregar_dinero.
    # - Código a seguir:
    #     1. Inicializar un usuario con nombre, saldo y un indicador (True o False) de cuenta corriente.
    #     2. Implementar retirar_dinero para sustraer dinero del saldo, lanzando un error si no es posible.
    #     3. Implementar transferir_dinero para transferir dinero desde otro usuario, lanzando un error en caso de fallo.
    #     4. Implementar agregar_dinero para aumentar el saldo del usuario.
    # - Caso de uso:
    #   - a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
    #   - b. Agregar 20 unidades al saldo de Bob.
    #   - c. Transferir 80 unidades de Bob a Alicia.
    #   - d. Retirar 50 unidades del saldo de Alicia.

# Creación de excepciones
class SaldoNoDisponible(Exception):
    pass
   
# Creación de la clase y de sus métodos
class UsuarioBanco:
    def __init__(self, nombre, saldo, tieneCuenta):
        """Método constructor de la clase.

        Args:
            nombre (str): atributo 1.
            saldo (int): atributo 2.
            tieneCuenta (bool): atributo 3.
        """
        self.nombre = nombre
        self.saldo = saldo
        self.tieneCuenta = tieneCuenta
        
    def retirar_dinero(self, cantidad):
        """Si hay suficiente saldo, sustrae la cantidad indicada.

        Args:
            cantidad (int): Cantidad a retirar.

        Raises:
            SaldoNoDisponible: Excepción en el caso de que el saldo no haya suficiente saldo.
        """
        if self.saldo >= cantidad:
            self.saldo -= cantidad
        else:
            raise SaldoNoDisponible("Saldo insuficiente")
    
    def transferir_dinero(self, cantidad, usuarioDestino):
        """Transfiere una cantidad de dinero desde un usuario a otro.

        Args:
            cantidad (int): cantidad a transferir.
            usuarioDestino (UsuarioBanco): usuario destino.
        """
        self.retirar_dinero(cantidad)
        usuarioDestino.agregar_dinero(cantidad)
        
    def agregar_dinero(self, cantidad):
        """Agrega la cantidad indicada de dinero.

        Args:
            cantidad (int): Cantidad a ingresar.
        """
        self.saldo += cantidad

# - Caso de uso:
    #   - a. Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
usuario1 = UsuarioBanco("Alicia", 100, True)
usuario2 = UsuarioBanco("Bob", 50, True)

    #   - b. Agregar 20 unidades al saldo de Bob.
usuario2.agregar_dinero(20)
    
    #   - c. Transferir 80 unidades de Bob a Alicia.
try:
    usuario2.transferir_dinero(80, usuario1)
except SaldoNoDisponible:
    print("Saldo no Disponible")
    
    #   - d. Retirar 50 unidades del saldo de Alicia.
usuario1.retirar_dinero(50)