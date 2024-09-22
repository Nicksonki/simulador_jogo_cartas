import tkinter as tk
import random

class Carta:
    def __init__(self, naipe, valor):
        self.naipe = naipe
        self.valor = valor

    def __repr__(self):
        return f'{self.valor} de {self.naipe}'

class Baralho:
    naipes = ['Copas', 'Ouros', 'Espadas', 'Paus']
    valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei', 'Ás']

    def __init__(self):
        self.cartas = [Carta(naipe, valor) for naipe in self.naipes for valor in self.valores]
        random.shuffle(self.cartas)

    def puxar_carta(self):
        return self.cartas.pop()

def calcular_pontos(mao):
    pontos = 0
    ases = 0
    valores = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
               'Valete': 10, 'Dama': 10, 'Rei': 10, 'Ás': 11}

    for carta in mao:
        pontos += valores[carta.valor]
        if carta.valor == 'Ás':
            ases += 1

    while pontos > 21 and ases:
        pontos -= 10
        ases -= 1

    return pontos

class BlackjackApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Blackjack")

        self.baralho = Baralho()
        self.mao_jogador = [self.baralho.puxar_carta(), self.baralho.puxar_carta()]
        self.mao_dealer = [self.baralho.puxar_carta(), self.baralho.puxar_carta()]

        self.label_info = tk.Label(master, text="Bem-vindo ao Blackjack!")
        self.label_info.pack()

        self.botao_puxar = tk.Button(master, text="Puxar carta", command=self.puxar_carta)
        self.botao_puxar.pack()

        self.botao_ficar = tk.Button(master, text="Ficar", command=self.ficar)
        self.botao_ficar.pack()

        self.label_resultado = tk.Label(master, text="")
        self.label_resultado.pack()

        self.atualizar_jogo()

    def atualizar_jogo(self):
        pontos_jogador = calcular_pontos(self.mao_jogador)
        self.label_info.config(text=f"Suas cartas: {self.mao_jogador} (pontuação: {pontos_jogador})")
        self.label_resultado.config(text="")

    def puxar_carta(self):
        self.mao_jogador.append(self.baralho.puxar_carta())
        pontos_jogador = calcular_pontos(self.mao_jogador)

        if pontos_jogador > 21:
            self.label_resultado.config(text="Você estourou! Dealer vence.")
            self.botao_puxar.config(state=tk.DISABLED)
            self.botao_ficar.config(state=tk.DISABLED)
        else:
            self.atualizar_jogo()

    def ficar(self):
        pontos_jogador = calcular_pontos(self.mao_jogador)
        pontos_dealer = calcular_pontos(self.mao_dealer)

        while pontos_dealer < 17:
            self.mao_dealer.append(self.baralho.puxar_carta())
            pontos_dealer = calcular_pontos(self.mao_dealer)

        resultado = f"Dealer mostra: {self.mao_dealer} (pontuação: {pontos_dealer})"
        if pontos_dealer > 21 or pontos_jogador > pontos_dealer:
            resultado += "\nVocê ganhou!"
        else:
            resultado += "\nDealer venceu!"
        
        self.label_resultado.config(text=resultado)
        self.botao_puxar.config(state=tk.DISABLED)
        self.botao_ficar.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackApp(root)
    root.mainloop()
