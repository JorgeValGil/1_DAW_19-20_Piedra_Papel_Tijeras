#Imports. Random para calcular aleatoriamente a elección ordenador. Time para facer unha simulación de procesamento de datos.
import random
import time

#función animacion_carga, a cal usa time para facer unha animación de proceso
def animacion_carga():
    print("Procesando os datos, agarde por favor")
    for i in range(1,4):
        print("------------------")
        time.sleep(1)

#función puntuacións, a cal mostra as puntuacións
def puntuacions():
    print("Puntuacións:")
    print("Usuario:", puntuacion_usuario, "puntos")
    print("Ordenador:", puntuacion_ordenador, "puntos")

#función nova liña, creo un string coas puntuacions da partida actual e gardo nunha liña dun nun ficherio de texto
def nova_lina():
    ficheiro = open("historico.txt", "a")
    puntos_ordenador = str(puntuacion_ordenador)
    puntos_usuario = str(puntuacion_usuario)
    lina = 'Ordenador ' + puntos_ordenador + " - " + puntos_usuario + " Usuario"
    ficheiro.write(lina+'\n')
    ficheiro.close()

#funcion historico mostro todas as liñas do ficheiro historico ficheiro no cal se gardar as puntuacións das partidas
def historico():
    print("Histórico de partidas:")
    ficheiro = open("historico.txt","r")
    for lina in ficheiro.readlines():
        print(lina)
    ficheiro.close()

#creo e inicializo unha variable que se usará o rematar a partida, para ver se quere comezar outra partida ou saír do bucle
nova_partida = ""
#bucle mentres nova partida non sexa igual a n
while nova_partida != "n":

    #inicializo as puntuacións de ambos a 0
    puntuacion_ordenador = 0
    puntuacion_usuario = 0

    #creo un bucle ata unha das dúas puntuacións chegue a 3 puntos
    while puntuacion_ordenador < 3 and puntuacion_usuario < 3:

        #con Random xeramos un número ao azar entre 0 e 2, co cal escolleremos a elección do ordenador
        numero_ordenador = random.randrange(0, 3)
        #creo e inicializo a variable da eleccion do ordenador
        eleccion_ordenador = ""
        #dependendo do numero random escollo a eleccion do ordenador
        if numero_ordenador == 0:
            eleccion_ordenador = "pedra"
        elif numero_ordenador == 1:
            eleccion_ordenador = "papel"
        elif numero_ordenador == 2:
            eleccion_ordenador = "tesoiras"

        #creo e inicializo a variable da eleccion do usuario
        eleccion_usuario = ""
        eleccions_posibles_usuario = ["pedra", "papel", "tesoiras"]
        #Presento o xogo e as opcións
        print("Benvido ao xogo 'Pedra, papel, tesoiras'")
        print("Introduce a túa elección:")
        print("1 - Pedra")
        print("2 - Papel")
        print("3 - Tesoiras")
        eleccion = int(input())
        #dependendo do numero introducido escollo a eleccion do usuario
        if eleccion == 1:
            eleccion_usuario = eleccions_posibles_usuario[0]
        elif eleccion == 2:
            eleccion_usuario = eleccions_posibles_usuario[1]
        elif eleccion == 3:
            eleccion_usuario = eleccions_posibles_usuario[2]
        else:
            print("Erro na entrada de datos! Debes introducir 1, 2 ou 3!")

        #se a entrada do usuario foi correcta sigo executando o xogo, senón mostro as puntuacións e volvería a comezar
        if eleccion_usuario == "pedra" or eleccion_usuario == "papel" or eleccion_usuario == "tesoiras":
            #mostro as 2 eleccións
            print("Ti elixiche:", eleccion_usuario)
            print("O ordenador elixiu: ", eleccion_ordenador)
            #uso a función animación carga
            animacion_carga()
            #posibles resultados
            if eleccion_ordenador == "pedra" and eleccion_usuario == "papel":
                #se o usuario xa ten 2 puntos o papel perderá contra a pedra, o usuario non conseguirá nunca o terceiro punto, se non ten os 2 puntos o xogo funcionará coma sempre
                if puntuacion_usuario == 2:
                    print("Meu deus! A pedra aplastou ao papel e fixoo anacos! Punto para o ordenador")
                    puntuacion_ordenador += 1
                else:
                    print("Punto para o usuario! O papel envolve á pedra")
                    puntuacion_usuario += 1
            elif eleccion_ordenador == "papel" and eleccion_usuario == "tesoiras":
                #se o usuario xa ten 2 puntos as tesoiras perderán contra o papel, o usuario non conseguirá nunca o terceiro punto, se non ten os 2 puntos o xogo funcionará coma sempre
                if puntuacion_usuario == 2:
                    print("Meu deus! O papel envolveu as tesoiras e non pode cortar! Punto para o ordenador")
                    puntuacion_ordenador += 1
                else:
                    print("Punto para o usuario, As tesoiras cortan o papel")
                    puntuacion_usuario += 1
            elif eleccion_ordenador == "tesoiras" and eleccion_usuario == "pedra":
                #se o usuario xa ten 2 puntos a pedra perderá contra as tesoiras, o usuario non conseguirá nunca o terceiro punto, se non ten os 2 puntos o xogo funcionará coma sempre
                if puntuacion_usuario == 2:
                    print("Meu deus! As tesoiras afíanse coa pedra e conseguen cortar á pedra! Punto para o ordenador")
                    puntuacion_ordenador += 1
                else:
                    print("Punto para o usuario! A pedra aplasta as tesoiras")
                    puntuacion_usuario += 1
            if eleccion_ordenador == "papel" and eleccion_usuario == "pedra":
                print("Punto para o ordenador! O papel envolve á pedra")
                puntuacion_ordenador += 1
            elif eleccion_ordenador == "tesoiras" and eleccion_usuario == "papel":
                print("Punto para o ordenador! As tesoiras cortan o papel")
                puntuacion_ordenador += 1
            elif eleccion_ordenador == "pedra" and eleccion_usuario == "tesoiras":
                print("Punto para o ordenador! A pedra aplasta as tesoiras")
                puntuacion_ordenador += 1
            elif eleccion_ordenador == eleccion_usuario:
                print("Empate! Ámbolos dous elixístedes o mesmo")
        #uso a función puntuación
        puntuacions()
    #Unha vez que algúen consiga 3 puntos e saian do bucle, comparo as puntuacións e mostro quen gañou
    print("Fin do xogo, temos un gañador!")
    #uso a función nova liña
    nova_lina()
    if puntuacion_ordenador < puntuacion_usuario:
        print("O usuario proclámase vencedor do xogo!")
    else:
        print("O ordenador proclámase vencedor do xogo!")
    #uso a función historico
    historico()
    #pregunto se quee xogar outra partida e fago uso de nova_partida
    print("Queres xogar outra partida? (s/n)")
    nova_partida = input()
#se non xoga outra partida o xogo remata
print("Fin do xogo")