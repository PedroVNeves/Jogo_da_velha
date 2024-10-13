from abc import ABC, abstractmethod
from random import random
import time as time
from tabulate import tabulate

class JogoVelha():
    """Classe principal do jogo da velha, responsável por gerenciar o fluxo do jogo.

    Atributos:
        tabuleiro (Tabuleiro): Instância da classe Tabuleiro que mantém o estado do jogo.
        jogador1 (Jogador): Instância de JogadorHumano ou JogadorComputador representando o primeiro jogador.
        jogador2 (Jogador): Instância de JogadorHumano ou JogadorComputador representando o segundo jogador.
        turno (int): Contador de turnos.
    """
    def __init__(self):
        """Inicializa o jogo com as configurações do jogador e do computador."""
        print('''
                ***********************************************
                 Bem vindo ao Jogo da Velha!
                ***********************************************
                ''')
        Nome = input("Qual seu nome? ")

        Simbolo = input("Você gostaria de ser o 'X' ou 'O'? ")

        estrategia = 'aleatório'

        # Define os jogadores com base no símbolo escolhido
        if Simbolo == 'X':
            jogador1 = JogadorHumano(Nome, 'X')
            jogador2 = JogadorComputador('Bot', 'O', estrategia)
        elif Simbolo == 'O':
            jogador1 = JogadorComputador('Bot', 'O', estrategia)
            jogador2 = JogadorHumano(Nome, 'X')
        else:
            raise ValueError('Simbolo inválido. Use "X" ou "O".')
        
        self.tabuleiro = Tabuleiro()
        self.jogador1 = jogador1
        self.jogador2 = jogador2
        self.turno = 0        

    def Jogar(self):
        """Executa o loop principal do jogo, alternando entre os jogadores até que haja um vencedor ou empate."""
        while True:
            jogador_atual = self.jogador_atual(self.jogador1, self.jogador2)
            self.tabuleiro.imprimir_tabuleiro()
            jogador_atual.fazer_jogada(self.tabuleiro)
            
            # Verifica se há um vencedor ou empate
            resultado = self.verificar_tabuleiro()
            if resultado is not None and resultado != 'empate':
                self.tabuleiro.imprimir_tabuleiro()
                print(f"O jogador {jogador_atual.nome} ganhou!")
                break
            if self.turno == 9:
                print("Empate")
                break

            self.turno += 1

    def verificar_tabuleiro(self):
        """Verifica se há um vencedor ou empate no tabuleiro.

        Returns:
            str: Retorna 'empate' em caso de empate, ou o símbolo do vencedor.
        """
        if self.turno == 9:
            return 'empate'
        
        # Verifica linhas e colunas
        for i in range(3):
            if self.tabuleiro.casas[i][0] == self.tabuleiro.casas[i][1] == self.tabuleiro.casas[i][2] != '':
                return self.tabuleiro.casas[i][0]
            if self.tabuleiro.casas[0][i] == self.tabuleiro.casas[1][i] == self.tabuleiro.casas[2][i] != '':
                return self.tabuleiro.casas[0][i]
        
        # Verifica diagonais
        if self.tabuleiro.casas[0][0] == self.tabuleiro.casas[1][1] == self.tabuleiro.casas[2][2] != '':
            return self.tabuleiro.casas[0][0]
        if self.tabuleiro.casas[0][2] == self.tabuleiro.casas[1][1] == self.tabuleiro.casas[2][0] != '':
            return self.tabuleiro.casas[0][2]

        return None

    def jogador_atual(self, jogador1, jogador2):
        """Determina de quem é o turno atual com base na contagem de turnos.

        Args:
            jogador1 (Jogador): Primeiro jogador.
            jogador2 (Jogador): Segundo jogador.

        Returns:
            Jogador: O jogador que deve fazer a próxima jogada.
        """
        jogadores = (jogador1, jogador2)
        indice = self.turno % 2
        return jogadores[indice]


class Tabuleiro():
    """Classe que representa o tabuleiro do jogo da velha.

    Atributos:
        casas (list): Uma matriz 3x3 representando as casas do tabuleiro.
    """
    def __init__(self):
        """Inicializa o tabuleiro vazio."""
        self.casas = [['', '', ''],
                      ['', '', ''],
                      ['', '', '']]

    def pegar_tabuleiro(self):
        """Retorna o estado atual do tabuleiro.

        Returns:
            list: Matriz 3x3 representando o tabuleiro.
        """
        return self.casas
    
    def preencher_casa(self, simbolo, linha, coluna):
        """Preenche uma casa no tabuleiro com o símbolo do jogador.

        Args:
            simbolo (str): O símbolo do jogador ('X' ou 'O').
            linha (int): Índice da linha da casa.
            coluna (int): Índice da coluna da casa.
        """
        self.casas[linha][coluna] = simbolo

    def imprimir_tabuleiro(self):
        """Imprime o tabuleiro formatado na tela, com cabeçalhos de linha e coluna numerados."""
        headers = ["#", "1", "2", "3"]
        tabuleiro_formatado = [[str(i + 1)] + [self.casas[i][j] if self.casas[i][j] != '' else ' ' for j in range(3)] for i in range(3)]
        print('\n\n\n' + tabulate(tabuleiro_formatado, headers=headers, tablefmt="grid"))


class Jogador(ABC):
    """Classe abstrata para representar um jogador.

    Atributos:
        nome (str): Nome do jogador.
        simbolo (str): Símbolo do jogador ('X' ou 'O').
    """
    def __init__(self, nome, simbolo):
        """Inicializa o jogador.

        Args:
            nome (str): Nome do jogador.
            simbolo (str): Símbolo do jogador ('X' ou 'O').
        """
        self.nome = nome
        self.simbolo = simbolo

    @abstractmethod
    def fazer_jogada(self, Tabuleiro):
        """Método abstrato para fazer uma jogada."""
        pass


class JogadorHumano(Jogador):
    """Classe que representa um jogador humano."""
    def __init__(self, nome, simbolo):
        """Inicializa o jogador humano.

        Args:
            nome (str): Nome do jogador.
            simbolo (str): Símbolo do jogador ('X' ou 'O').
        """
        super().__init__(nome, simbolo)

    def fazer_jogada(self, Tabuleiro):
        """Permite que o jogador humano faça uma jogada.

        Args:
            Tabuleiro (Tabuleiro): O tabuleiro atual do jogo.
        """
        tabuleiro = Tabuleiro.pegar_tabuleiro()
        while True:
            coordenadas = input(f"\nVez do jogador {self.nome} ({self.simbolo}).\nEscolha a casa a ser marcada (linha,coluna): ")
            coordenadas = coordenadas.replace(" ", "")
            linha, coluna = map(int, coordenadas.split(','))
            if tabuleiro[linha - 1][coluna - 1] == '':
                Tabuleiro.preencher_casa(self.simbolo, linha - 1, coluna - 1)
                break
            else:
                print(f"\nA casa {(linha, coluna)} está ocupada. Escolha outra.\n")


class JogadorComputador(Jogador):
    """Classe que representa um jogador computador."""
    def __init__(self, nome, simbolo, estrategia):
        """Inicializa o jogador computador.

        Args:
            nome (str): Nome do jogador.
            simbolo (str): Símbolo do jogador ('X' ou 'O').
            estrategia (str): Estratégia do computador.
        """
        super().__init__(nome, simbolo)
        self.estrategia = estrategia

    def fazer_jogada(self, Tabuleiro):
        """Faz uma jogada com base na estratégia do computador.

        Args:
            Tabuleiro (Tabuleiro): O tabuleiro atual do jogo.
        """
        print('\nBot pensando...\n')
        time.sleep(2)

        if self.estrategia == 'aleatório':
            while True:
                linha = int(random() * 3)
                coluna = int(random() * 3)
                if Tabuleiro.casas[linha][coluna] == '':
                    Tabuleiro.preencher_casa(self.simbolo, linha, coluna)
                    break
                
        # Outras estratégias podem ser implementadas futuramente.
