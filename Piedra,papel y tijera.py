# Importamos el modulo random
import random

# Inicializamos los dos contadores 
Human_c = 0
Maquina_c = 0

# Lista de seleccion para humano y maquina
h_game = ["Papel","Piedra","Tijera"]
m_game = ["Papel","Piedra","Tijera"]

# Variable de juego, mientras sea True el juego se inicia. 
jugar = True

print ("empieza el juego: ")
print (" \n -------------------------- \n ")

#Iniciamos el juego. 
while jugar: 

    h_choice = random.choice(h_game)
    m_choice = random.choice(m_game)


    if ((h_choice == "Papel" and m_choice == "Piedra") or 
        (h_choice == "Piedra" and m_choice == "Tijera") or 
        (h_choice == "Tijera" and m_choice == "Papel")):

        print (f"Humano eligio {h_choice}, Maquina eligio {m_choice}, Humano gana 1 punto.")
        Human_c += 1
        print (Human_c, "puntos acumulados.")
        print (" \n -------------------------- \n ")

    elif h_choice == m_choice:
        print ("Empate, no gana ninguno de los dos.\n","\bHumano pts ->", Human_c,"\nMaquina pts ->", Maquina_c)
        print (" \n -------------------------- \n ")
    
    else:
        print (f"Maquina eligio {m_choice}, Humano eligio {h_choice}.")
        Maquina_c += 1
        print (Maquina_c, "puntos acumulados.")
        print (" \n -------------------------- \n ")
    
    while Human_c == 3 or Maquina_c == 3:
        
        print (f"""
        Juego terminado.
        Score: 
        Humano = {Human_c},
        Maquina = {Maquina_c}       
        """)

        mensaje = "Gana humano."
        print (mensaje.upper() if Human_c == 3 else "GANA MAQUINA.")
        jugar = False
        break
 

