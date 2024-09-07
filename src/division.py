def evaluar(dividendo, divisor):
     cociente = dividendo // divisor
     residuo = dividendo % divisor
     if residuo == 0:
        return "La división es exacta. \n" \
            "Cociente: " + str(int(cociente)) + "\n" \
            "Residuo: " + str(residuo)
     else:
        #calculo los de division con residuo
        return "La división no es exacta. \n" \
            "Cociente: " + str(cociente) + "\n" \
            "Residuo: " + str(residuo)
     
if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
