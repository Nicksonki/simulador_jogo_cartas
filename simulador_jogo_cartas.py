"""
Simulador de jogo de Blackjack.
O objetivo é chegar o mais perto de 21 pontos sem ultrapassar.
O jogo é jogado contra o dealer.
"""

import random

# Classe representando uma carta
class Carta:
    """
    Representa uma carta de baralho com um naipe e valor.
    """
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

    def __repr__(self):
        return f'{self.valor} de {self.naipe}'

# Classe representando o baralho
class Baralho:
    """
    Classe que gera um baralho de cartas e embaralha automaticamente.
    """
    naipes = ['Copas', 'Ouros', 'Espadas', 'Paus']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei', 'Ás']

    def __init__(self):
        self.cartas = [Carta(naipe, valor) for naipe in self.naipes for valor in self.valores]
        random.shuffle(self.cartas)

    def puxar_carta(self):
        """
        Retira e retorna a última carta do baralho.
        """
        return self.cartas.pop()

# Função para calcular a pontuação de uma mão
def calcular_pontos(mao):
    """
    Calcula a pontuação de uma mão de cartas.
    Ás pode valer 11 ou 1, dependendo do contexto para evitar estouro.
    """
    pontos = 0
    ases = 0
    valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
               'Valete': 10, 'Dama': 10, 'Rei': 10, 'Ás': 11}

    for carta in mao:
        pontos += valores[carta.valor]
        if carta.valor == 'Ás':
            ases += 1

    # Ajuste do valor do Ás para 1 se a pontuação ultrapassar 21
    while pontos > 21 and ases:
        pontos -= 10
        ases -= 1

    return pontos

# Função principal para simular o jogo de Blackjack
def blackjack():
    """
    Simula uma partida de Blackjack entre o jogador e o dealer.
    """
    print("Bem-vindo ao Blackjack!\n")

    baralho = Baralho()

    # Mão do jogador e do dealer
    mao_jogador = [baralho.puxar_carta(), baralho.puxar_carta()]
    mao_dealer = [baralho.puxar_carta(), baralho.puxar_carta()]

    # Loop principal do jogo
    while True:
        pontos_jogador = calcular_pontos(mao_jogador)
        pontos_dealer = calcular_pontos(mao_dealer)
        print(f"Suas cartas: {mao_jogador} (pontuação: {pontos_jogador})")
        print(f"Dealer mostra: {mao_dealer[0]}")

        if pontos_jogador == 21:
            print("Blackjack! Você ganhou!")
            return

        escolha = input("Deseja [P]uxar mais uma carta ou [F]icar? ").lower()

        if escolha == 'p':
            mao_jogador.append(baralho.puxar_carta())
            pontos_jogador = calcular_pontos(mao_jogador)
            if pontos_jogador > 21:
                print(f"Suas cartas: {mao_jogador} (pontuação: {pontos_jogador})")
                print("Você estourou! Dealer vence.")
                return
        elif escolha == 'f':
            break

    # Turno do dealer
    while pontos_dealer < 17:
        mao_dealer.append(baralho.puxar_carta())
        pontos_dealer = calcular_pontos(mao_dealer)

    print(f"Dealer revela as cartas: {mao_dealer} (pontuação: {pontos_dealer})")

    if pontos_dealer > 21:
        print("Dealer estourou! Você ganhou!")
    elif pontos_jogador > pontos_dealer:
        print("Você ganhou!")
    else:
        print("Dealer venceu!")

# Executa o jogo
if __name__ == "__main__":
    blackjack()
