class CalculadoraRaiz:
    def __init__(self, a):
        self.a = a
        self.x = 1.0

    def calcular_raiz(self, iteraciones):
        for k in range(1, iteraciones + 1):
            self.x = (self.x + self.a / self.x) / 2
            print(f"La raíz después de {k} iteraciones es {self.x}")

# Uso de la clase
def main():
    a = float(input("Dame el valor de a:\n"))
    iteraciones = 10  # Número de iteraciones a realizar
    calculadora = CalculadoraRaiz(a)
    calculadora.calcular_raiz(iteraciones)

if __name__ == "__main__":
    main()
