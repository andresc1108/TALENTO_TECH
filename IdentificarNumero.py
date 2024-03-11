def IdentificarNumero(numero):
    
    
    # Verificar si el numero es par, impar o 0 
    if numero == 0:
        print ("El numero es 0.")
    elif numero % 2 == 0:
        print ("El numero es par.")
    else:
        print ("El numero es impar.")
        if numero % 3 == 0:
            print ("El numero es impar y es divisible entre 3.")
        else:
            print("El numero es impar pero no es divisible entre 3.")
