import random

class Dealer:

    def __init__(self, dinero: int):
        self.dineroDealer = dinero
        self.cartasDealer = []
        self.valorMano = 0
        self.rondasGanadas = 0

    def valorCartasDealer(self) -> int:
        self.valorMano = 0
        self.cartasDealer.sort(key=lambda carta: carta.ValorReal, reverse=True)
        for carta in self.cartasDealer:
            if carta.ValorReal ==1:
                valorAux1=self.valorMano+carta.ValorReal
                valorAux2=self.valorMano+11
                if valorAux2 <=21:
                     self.valorMano=valorAux2
                else:
                    self.valorMano= valorAux1
            else:
                self.valorMano= self.valorMano+carta.ValorReal

        return self.valorMano

    def cogerCarta(self,carta):
        self.cartasDealer.append(carta)

    def viableCogerCarta(self, numcartasPlayer)-> bool:
        return self.valorMano <17 and self.valorMano<numcartasPlayer


    def printCartasDealer(self):
        for carta in self.cartasDealer:
            print(carta.Valor, carta.Palo)

    def dealerBlackjack(self):
        return self.valorMano==21

    def victoriaDealer(self, apuesta):
        self.dineroDealer=self.dineroDealer+apuesta
        self.rondasGanadas=self.rondasGanadas+1
        self.cartasDealer.clear()
        self.valorMano=0

    def derrotaDealer(self,apuesta):
        self.dineroDealer=self.dineroDealer-apuesta*2
        self.cartasDealer.clear()
        self.valorMano=0

    def empateDealer(self):
        self.cartasDealer.clear()
        self.valorMano = 0





class Jugador:

    def __init__(self, nombreJugador, dineroJugador):
        self.nombreJugador = nombreJugador
        self.dineroJugador = dineroJugador
        self.cartasJugador = []
        self.valorMano = 0
        self.apuesta = 0
        self.rondasGanadas = 0

    def calcularMano(self)->int:
        print("")
        print("Calculando el valor de tu mano...")
        self.valorMano = 0
        self.cartasJugador.sort(key=lambda carta: carta.ValorReal, reverse=True)
        for carta in self.cartasJugador:
            if carta.ValorReal ==1:
                valorAux1 = self.valorMano + carta.ValorReal
                valorAux2 = self.valorMano + 11
                print("")
                print("Escoge lo que quieres que valga tu AS:")
                print("Si tu AS vale 1 se te queda la mano en: ", valorAux1)
                print("Si tu AS vale 11 se te queda la mano en: ", valorAux2)
                decision=0
                while(decision !=11 and decision != 1):
                    print("")
                    decision=int(input("Escribe lo que quieres que valga tu AS: "))
                if decision == 1:
                    print("Tu mano vale ahora: ", valorAux1)
                    self.valorMano = valorAux1
                else:
                    print("Tu mano vale ahora: ", valorAux2)
                    self.valorMano = valorAux2

            else:
                self.valorMano= self.valorMano+carta.ValorReal

        print(self.nombreJugador,"tu mano vale finalmente: ", self.valorMano)
        return self.valorMano


    def valorCartasJugador(self) -> int:
        valorManoAux=0
        copiaCartas=self.cartasJugador.copy()
        copiaCartas.sort(key=lambda carta: carta.ValorReal, reverse=True)
        for carta in copiaCartas:
            if carta.ValorReal ==1:
                valorAux1=valorManoAux+carta.ValorReal
                valorAux2=valorManoAux+11
                if valorAux2 <=21:
                     valorManoAux=valorAux2
                else:
                    valorManoAux= valorAux1
            else:
                valorManoAux= valorManoAux+carta.ValorReal

        return valorManoAux

    def printCartasJugador(self):
        for carta in self.cartasJugador:
            print(carta.Valor, carta.Palo)

    def printValorReal(self):
        print("Con estas cartas tendrías: ",self.valorMano)

    def cogerCarta(self, carta):
        self.cartasJugador.append(carta)

    def playerBlackjack(self):
        print("Player Blackjack")

    def victoriaPlayer(self):
        self.dineroJugador=self.dineroJugador+self.apuesta*2
        self.rondasGanadas=self.rondasGanadas+1
        print("--------------------------------------------")
        print("VICTORIA, del jugador ", self.nombreJugador)
        print("+",self.apuesta*2)
        print("Tu saldo actual es: ",self.dineroJugador)
        self.cartasJugador.clear()
        self.valorMano=0

    def derrotaPlayer(self):
        self.dineroJugador=self.dineroJugador-self.apuesta
        print("--------------------------------------------")
        print("DERROTA, del jugador ", self.nombreJugador)
        print("-", self.apuesta)
        print("Tu saldo actual es: ", self.dineroJugador)
        self.cartasJugador.clear()
        self.valorMano = 0

    def empatePlayer(self):
        self.cartasJugador.clear()
        self.valorMano = 0



class Baraja:

    def __init__(self):
        self.palos = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]
        self.valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
        self.mazo = []
        self.rellenaMazo()
        self.remueveMazo()

    def rellenaMazo(self):
        for palo in self.palos:
            for valor in self.valores:
                aux = Carta(valor, palo)
                self.mazo.append(aux)

    def remueveMazo(self):
        random.shuffle(self.mazo)

    def sacaCarta(self):
        carta=self.mazo.pop()
        return carta



class Carta :

    def __init__(self, Valor, Palo):
        self.Valor = Valor
        self.Palo = Palo
        self.ValorReal=self.setValorReal()


    def setValorReal(self)->int:
        if isinstance(self.Valor, int) ==True:
            return  self.Valor
        else:
            return  10

    def printCarta(self):
        s = f"{self.Valor} {self.Palo}"
        print(s)
        return s



class Ronda:

    def __init__(self,numero,player,dealer):
        self.numero=numero
        self.player=player
        self.dealer=dealer
        self.baraja=Baraja()
        self.cartaVisible=None


    def evalucionResultados(self):

       apuesta=self.player.apuesta
       if self.dealer.valorMano>21:
           self.dealer.derrotaDealer(apuesta)
           self.player.victoriaPlayer()
       elif self.player.valorMano >21:
           self.dealer.victoriaDealer(apuesta)
           self.player.derrotaPlayer()
       elif self.dealer.valorMano==self.player.valorMano:
           print("-------------------------------")
           print("EMPATE!! ")
           print("Las apuestas son devueltas")
           self.player.empatePlayer()
           self.dealer.empateDealer()

       elif self.dealer.valorMano>self.player.valorMano:
           self.dealer.victoriaDealer(apuesta)
           self.player.derrotaPlayer()

       elif self.dealer.valorMano<self.player.valorMano:
           self.dealer.derrotaDealer(apuesta)
           self.player.victoriaPlayer()

    def turnoDealer(self):
        print("")
        print("LE TOCA AL DEALER:")
        print(".....................")
        print("")
        print("Cartas del Dealer:")
        self.dealer.printCartasDealer()
        self.dealer.valorCartasDealer()
        print("Su mano vale:",self.dealer.valorMano)
        while self.dealer.viableCogerCarta(self.player.valorMano)==True:
            print("")
            print("El dealer ha decidido coger una carta más.")
            cartaDealer = self.baraja.sacaCarta()
            self.dealer.cogerCarta(cartaDealer)
            cartaDealer.printCarta()
            print("La mano del dealer vale ahora: ", self.dealer.valorCartasDealer())
            print("")


    def nuevaRonda(self):
        stop=False
        print("--------------------------------")
        print("--------------------------------")
        print("RONDA ", self.numero)
        print("")
        print(self.player.nombreJugador,"tienes este saldo: ",self.player.dineroJugador)

        apuesta = -1
        while apuesta <= 0 or apuesta > self.player.dineroJugador:
            apuesta=int(input("Introduce tu apuesta: "))
        self.player.apuesta = apuesta

        print("")
        print("COMENCEMOS!!!!")

        for i in range(2):
            cartaPlayer= self.baraja.sacaCarta()
            cartaDealer= self.baraja.sacaCarta()
            if i ==0:
                self.cartaVisible=cartaDealer

            self.player.cogerCarta(cartaPlayer)
            self.dealer.cogerCarta(cartaDealer)

        print("CARTAS DEL DEALER:")
        print("La primera carta del dealer es: ",end="")
        self.cartaVisible.printCarta()
        print("")

        print("TUS CARTAS SON:")
        self.player.printCartasJugador()
        self.player.calcularMano()
        print("")
        decision=-1
        while decision!=1 and decision!=2:
            decision = int(input("¿Te plantas o pides otra carta?: 1-> TE PLANTAS, 2-> PIDES CARTA:  "))
            print("")

        if decision == 2:

            while self.player.valorCartasJugador()<21 and stop==False:
                cartaPlayer = self.baraja.sacaCarta()
                self.player.cogerCarta(cartaPlayer)
                print("Te ha tocado: ",end="" )
                cartaPlayer.printCarta()
                print("")
                print("Tus cartas actuales son:")
                self.player.printCartasJugador()
                self.player.calcularMano()
                if self.player.valorMano==21:
                    self.player.playerBlackjack()
                elif self.player.valorMano>21:
                    print("")
                    print("-------------------------------")
                    print("DERROTA, TE PASASTE DE 21...")
                    print("")
                    print("Cartas del Dealer:")
                    self.dealer.printCartasDealer()
                    self.dealer.valorCartasDealer()
                    print("Su mano valía:", self.dealer.valorMano)
                    self.dealer.victoriaDealer(self.player.apuesta)
                    self.player.derrotaPlayer()
                    return
                else:
                    decision=-1
                    while decision!=1 and decision!=2:
                        decision = int(input("¿Te plantas o pides otra carta?: 1-> TE PLANTAS, 2-> PIDES CARTA :    "))
                        print("")
                    if decision == 1:
                        stop=True

            self.turnoDealer()
            self.evalucionResultados()
        else:
            self.turnoDealer()
            self.evalucionResultados()















































