from blackjack_models import Jugador, Dealer, Ronda

def BlackJack():
   miDealer = Dealer(10000)
   round = 0

   stopPartida = False
   modoEspecial = False

   print("¡¡Bienvenido a Blackjack!!")
   name = input("Introduce tu nombre: ")

   print("De acuerdo", name, ", hora de decidir los parámetros de la partida")
   print("El dealer tiene: ", miDealer.dineroDealer, " euros")
   dineroPlayer = -1
   while dineroPlayer < 1:
      dineroPlayer = int(input("Introduce con cuánto dinero vas a jugar tú:  "))

   if dineroPlayer * 10 == miDealer.dineroDealer:
      modoEspecial = True
      print("")
      print("MODO ESPECIAL: ACTIVADO")
   mijugador = Jugador(name, dineroPlayer)

   print("")
   print("")
   while stopPartida == False:
      round = round + 1
      ronda = Ronda(round, mijugador, miDealer)
      ronda.nuevaRonda()
      if mijugador.dineroJugador == 0:
         stopPartida = True
         print("")
         print("Se acabo la partida: TE QUEDASTE SIN DINERO")
         if modoEspecial == True:
            print("")
            print("Estaba activado el MODO ESPECIAL.")
            print("El dealer gano: ", miDealer.rondasGanadas, "RONDAS")
            print("El player gano: ", mijugador.rondasGanadas, "RONDAS")
            if mijugador.rondasGanadas > miDealer.rondasGanadas:
               print("")
               print("JUGADOR", mijugador.nombreJugador, " , HAS GANADO!!")
            else:
               print("")
               print("PERDISTE... el dealer te gano, ", mijugador.nombreJugador)
      else:
         respuesta = -1
         while respuesta != 1 and respuesta != 2:
            print("")
            respuesta = int(input("¿Quieres jugar otra ronda?:  1->SI ,  2->NO :  "))
         if respuesta == 2:
            print("")
            print("Adios!!! Hasta pronto ", mijugador.nombreJugador, "!!!!!")
            stopPartida = True
         else:
            print("")
            print("De acuerdo, sigamos jugando!! Mucha suerte ", mijugador.nombreJugador, "!!!")

      print("")
      print("")


if __name__=='__main__':

   BlackJack()





