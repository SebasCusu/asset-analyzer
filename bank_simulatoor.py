
# Creating Class User
class User:
    def __init__(self, saldo):
        self.saldo = saldo
        
        #Deposit method
    def depositar(self, cantidad_deposito: int|float) -> int|float:
        if cantidad_deposito <= 0:#If amount is same or lower than 0, reject
            print("Deposito Invalido")
            return self.saldo
        
        else:#else deposit amount
            self.saldo += cantidad_deposito
            print(f"Deposito Exitoso de {cantidad_deposito}")
            return self.saldo
        
        #withdraw method
    def retirar(self, cantidad_retiro: int|float) -> int|float:
        if cantidad_retiro > self.saldo:#If withdraw higher than balance, reject
            print("Fondos Insuficientes")
            return self.saldo
            
        elif cantidad_retiro <= 0:#If amount is same or lower than 0, reject
            print("Retiro Invalido")
            return self.saldo
        
        else:# else:
            self.saldo -= cantidad_retiro
            print(f"Retiro Exitoso de {cantidad_retiro}")
            return self.saldo
        
user1 = User(4500)


#Principal Menu
print("1: Depositar")
print("2: Retirar")
print("3: Salir")

#Make the program stay still with a while loop
while True:
    try:
        opcion = int(input("Selecciona Una Opcion: "))
        if opcion == 1:
            cantidad_deposito = float(input("Cuanto dinero quieres depositar: "))
            print(user1.depositar(cantidad_deposito))
        
        elif opcion == 2:
            cantidad_retiro = float(input("Cuanto Dinero quieres Retirar: "))
            print(user1.retirar(cantidad_retiro))
            
            
        elif opcion == 3:
            break
    except ValueError:
        print("Opcion Invalida")