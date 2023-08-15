import random

# los dos contadores 
Human_c = 0
Maquina_c = 0

h_game = ["Papel","Piedra","Tijera"]
m_game = ["Papel","Piedra","Tijera"]


jugar = True

while jugar:

    h_choice = random.choice(h_game)
    m_choice = random.choice(m_game)

    print ("empieza el juego: ")
    print (" \n -------------------------- \n ")

    if (h_choice == "Papel" and m_choice == "Piedra") or (h_choice == "Piedra" and m_choice == "Tijera") or (h_choice == "Tijera" and m_choice == "Papel"):
        print (f"Humano eligio {h_choice}, Maquina eligio {m_choice}")
        Human_c += 1

    elif h_choice == m_choice:
        print ("Empate")
    
    else:
        print (f"Maquina eligio {m_choice}, Humano eligio {h_choice}")
        Maquina_c += 1
    
    while Human_c == 3 or Maquina_c == 3:
        continuar = input(print ("Desea continuar jugando ? "))
        
        if continuar == "Y" or continuar == "y":
            print ("Continuamos")
        elif continuar == "N" or continuar =="n":
            print ("Temrinamos")
            jugar = False
        continue
 

