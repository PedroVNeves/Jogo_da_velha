# Jogo da Velha 

Este é um simples jogo da velha em Python, jogável contra o computador. O jogador pode escolher entre os símbolos "X" e "O", e o computador jogará com o símbolo oposto. Na versão atual o computador joga de forma aleatória.

## Funcionalidades

- O jogador humano escolhe seu símbolo ("X" ou "O").
- O tabuleiro é exibido de forma clara e interativa, com marcações de linhas e colunas.
- Na versão atual, o computador joga usando uma estratégia de jogada aleatória.
- O jogo detecta vitórias, derrotas e empates.
- Suporte para rodadas alternadas entre jogador humano e o computador.

---

## Requisitos

- **Python 3.x**
- **Biblioteca `tabulate`** (para formatar o tabuleiro de jogo na tela)
- **Biblioteca `random`** (para o bot escolher as cassa onde irá jogar)

---

## Instalação

## Como Jogar

1. Ao iniciar o jogo, o usuário será solicitado a digitar seu nome.
2. Escolha entre ser o jogador "X" ou "O".
3. O jogo irá começar, e você pode escolher a posição para sua jogada com as coordenadas no formato linha,coluna (por exemplo, 1,2 para marcar a primeira linha e segunda coluna).
4. O computador jogará de forma aleatória.
5. O jogo terminará quando houver um vencedor ou quando todas as casas forem preenchidas, resultando em empate.

## Estrutura do código

- **JogoVelha**: Responsável por gerenciar o jogo, alternar entre jogadores e verificar o estado do tabuleiro. Esta classe controla o fluxo principal do jogo e valida se há um vencedor ou empate.
- **Tabuleiro**: Controla o estado do tabuleiro e imprime o layout formatado na tela. Ele armazena a configuração atual das casas e lida com a lógica de preenchimento e impressão.
- **Jogador (Abstract Base Class)**: Classe abstrata para representar jogadores. Define a interface de jogada a ser implementada tanto pelo jogador humano quanto pelo jogador computador.
- **JogadorHumano**: Implementa a lógica de jogada para o jogador humano, solicitando que o usuário escolha as coordenadas da jogada no formato linha,coluna.
- **JogadorComputador**: Implementa a lógica de jogada para o jogador computador. Atualmente, a estratégia utilizada pelo computador é aleatória, mas o código foi projetado para suportar outras estratégias (como jogadas em linha, coluna ou diagonal).


## Fluxo de jogo

1. Inicialização: O jogador escolhe seu símbolo e o jogo é inicializado com o tabuleiro vazio.
2. Jogada: O jogador humano e o computador se alternam em fazer jogadas, até que um deles vença ou o tabuleiro fique completamente preenchido.
3. Verificação de Vencedor: A cada jogada, o jogo verifica se há um vencedor com base nas linhas, colunas ou diagonais preenchidas.
4. Fim de Jogo: O jogo termina quando há um vencedor ou um empate (quando todas as casas são preenchidas sem um vencedor).


## Melhorias futuras

- Implementação de diferentes estratégias para o computador (como tentar vencer em linha, coluna ou diagonal).
- Adicionar níveis de dificuldade para o jogador computador.


## Licensa

Este projeto está licenciado sob a licença MIT - consulte o arquivo LICENSE para mais detalhes.