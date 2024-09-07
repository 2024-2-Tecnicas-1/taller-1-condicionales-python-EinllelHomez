def evaluar(anno):
    if anno < 1582:
        if anno % 4 == 0:
            return f"{anno} es bisiesto"
        else:
            return f"{anno} no es bisiesto"
    else:
        if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0):
            return f"{anno} es bisiesto"
        else:
            return f"{anno} no es bisiesto"
    return "";

if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(respuesta)
