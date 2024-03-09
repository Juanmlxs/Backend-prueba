import random

#el juego del casino nuevo
juego = []
while True: 
    print("Bienvanidos al casino")
    jugador = random.randint(2,26)
    dealer = random.randint(2,26)
    
    while True:
        print(f"el jugador tiene {jugador} y el dealer tiene {dealer}")
        quiere_cartas = input("Quiere mas cartas? s/n")
        if quiere_cartas == "s": 
            jugador = jugador + random.randint(1,13)
        else: 
            if jugador == dealer:
                print("gano el dealer")
                juego.append("dealer")
                break
            elif jugador == 21 or (jugador > dealer and jugador < 21):
                print("Gano el jugador")
                juego.append("jugador")
                break
            else: 
                print("gano dealer")
                juego.append("dealer")
                break  
            
    pregunta = input("desea salir del juego? s/n")
    if pregunta == "s": 
        print("Adios, Gracias por dejar el dinero")
        break
    else: 
        print('\n'*20)      
print(juego)
