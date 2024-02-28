import random
user_win = 0
computer_win = 0

choices = ("piedra", "papel", "tijera")

contador_user_wins = 0
contador_computer_wins = 0

bandera = True
while bandera: 
    print("*"*20, "Bienvenido a Piedra, Papel o Tijera", "*" *20)
    print("Porfavor, elija una opcion: \n1. Piedra \n2. Papel \n3. Tijera")
    
    user_option = input().lower()
    computer_option = random.choice(choices)
    
    print("=" * 10, "Datos del juego", "=" * 10)
   
    print("Computadora: ",computer_option, "\nUsuario:", user_option)
    print("=" * 40)
    
    if computer_option == user_option:
        print("Hay un empate!")
        contador_user_wins += 1
        contador_computer_wins += 1
    elif computer_option == "piedra":
        if user_option == "papel":
            print("Papel le gana a piedra. \nHas ganado!!")
            contador_user_wins +=1
        else:
            print("Piedra le gana a tijera. \nHas perdido!!")
            contador_computer_wins += 1
    elif computer_option == "papel":
        if user_option == "tijera":
            print("Tijera le gana a papel. \nHas ganado!!")
            contador_user_wins +=1
        else: 
            print("Papel le gana a piedra. \nHas perdido!!")
            contador_computer_wins +=1
    elif computer_option == "tijera":
        if user_option == "piedra":
            print("Piedra le gana a tijera. \nHas ganado!!")
            contador_user_wins +=1
        else:
            print("Tijera le gana a papel. \nHas perdido!!")
            contador_computer_wins +=1
    else:
        print("No has elegido una opcion correcta!! Intentalo nuevamente :)")        
    
    print("*" * 4, "M A R C A D O R  G L O B A L", "*" * 4)
    print("COMPUTADORA: ", contador_computer_wins, "\nUSER: ", contador_user_wins)
    bandera = False
    
    desicion_continue = 0
    
    print("->¿Desea continuar?<-\n1. SI\n2. NO")
    desicion_continue = int(input(""))
    
    if desicion_continue == 1:
        bandera = True
    else: 
        bandera = False
    