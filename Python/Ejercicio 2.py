class CuentaBancaria:
    """Representa una cuenta bancaria."""

    def __init__(self, nombre, saldo):
        """Inicializa la cuenta bancaria."""
        self.nombre = nombre
        self.saldo = saldo

    def depositar(self, cantidad):
        """Deposita una cantidad en la cuenta."""
        self.saldo += cantidad

    def retirar(self, cantidad):
        """Retira una cantidad de la cuenta."""
        if cantidad > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= cantidad

    def __str__(self):
        """Devuelve una cadena con la información de la cuenta."""
        return f"Cuenta bancaria de {self.nombre} con saldo de {self.saldo} €"


cuenta1 = CuentaBancaria("Juan Pérez", 1000)
cuenta2 = CuentaBancaria("Xavier Barriga", 2000)
cuenta3 = CuentaBancaria("Franner Vega", 500)

cuenta1.depositar(500) 
print(f"\nJuan Pérez depositó dinero: {cuenta1}")

cuenta2.retirar(300) 
print(f"\nXavier Barriga retiró dinero: {cuenta2}")

cuenta3.depositar(200)  
print(f"\nFranner Vega depositó dinero: {cuenta3}")  

cuenta3.retirar(100)   
print(f"\nFranner Vega retiró dinero: {cuenta3}")  

