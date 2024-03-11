def IdentificarNumero(numero):
    numero = int(input("Ingresar un numero entero: "))
    
    # Verificar si el numero es par, impar o 0 
    if numero == 0:
        print ("El numero es 0.")
    elif numero % 2 == 0:
        print ("El numero es par.")
    else:
        print ("El numero es impar.")
        
        #Verificar si el numero impar es divisible entre 3 
        if numero % 3 == 0:
            print ("El numero es impar y es divisible entre 3.")
        else:
            print("El numero es impar pero no es divisible entre 3.")
            
            
    juan = 20
    pedro = 19 
    javier = 50 
    junior = 1
    
    print(juan > pedro)
    print(juan > pedro ‹ junior)
    print(juan ‹ pedro > junior)
    print(junior ‹ pedro ‹ juan ‹ javier)
    print(pedro + junior > juan)
    print(pedro + junior >= juan)
    print(juan - junior == pedro)
