def recursividad(numero):
    if numero == 1:
        return 1
    else:
        return numero + (numero - 1)
print(recursividad(6))