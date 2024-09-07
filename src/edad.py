def evaluar(dia, mes, anno):
    from time import localtime
    t = localtime()
    diaAc = t.tm_mday
    mesAc = t.tm_mon
    annoAc = t.tm_year
    edad = (anno - annoAc) * -1

    if(mes > mesAc) or (mes == mesAc and dia > diaAc):
        edad -= 1
    return f"Usted tiene {edad} años"

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
