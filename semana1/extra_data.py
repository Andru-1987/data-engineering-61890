class Calculadora:
    def __init__(self, nombre: str) -> None:
        self.nombre: str =  nombre
    
    def calculo(self, n1:int, n2:int, cb:callable) -> any:
        return cb(n1, n2)



def main():
    iteracion:list = [ x for x in [1,2,3,4,5] if x%2 != 0 ]
    print(iteracion)

    iteracion_dos:list = [ _ for _ in [1,2,3,4,5] if _%2 != 0 ]
    print(iteracion_dos)


    def suma(n:int , n2:int) -> int:
        return n + n2
    
    calculin = Calculadora("data-engineer")

    print("El calculo es: suma, resultado: ",calculin.calculo(2,3,suma))
    print("El calculo es: resta, resultado: ",calculin.calculo(2,3, lambda x,y : x - y))
    print("El calculo es: multiplicacion, resultado: ",calculin.calculo(2,3, lambda x,y : x * y))
    print("El calculo es: division, resultado: ",calculin.calculo(2,3, lambda x,y : x / y))

    print(id(suma))

if __name__ == "__main__":
    main()