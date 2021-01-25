# SnakesAndLadders
### Descrição
O jogo de tabuleiro Snakes and Ladders foi implementado neste projeto para se realizar o estudo das probabilidades envolvidas com este jogo. Para tal foi feito a simulação de 10.000 jogos e a partir dos dados coletados se torna possível a sua análise. O principal interesse foi responder as quatro perguntas listadas abaixo: 

1. Em um jogo com dois jogadores, qual a probabilidade do jogador inicial ganhar o jogo?
2. Em média, quantas cobras são usadas em cada jogo?
3. Se cada vez que um jogador parasse em uma escada e tivesse somente 50% de chance de usa-la, qual seria o número de rodadas para se completar o jogo?
4. Começando com um jogo base, você decide que quer que o jogo tenha aproximadamente chances iguais. Você faz isso ao mudar a casa de ínicio. Em qual casa o segundo jogador deve começar para se ter chances iguais para ambos os jogadores?
5. Em uma tentativa diferente de mudar as probabilidades, em vez do segundo jogador começar o jogo em uma casa diferente, você decide dar ao Jogador 2 imunidade para a primeira cobra que ele parar. Qual é a probabilidade aproximada de que o Jogador 1 ganhe?

Para a implementação do jogo, foi usado um tabuleiro com 35 casas, sendo 5 delas cobras e 5 delas escadas. A configuração do boardgame pode ser vista na imagem abaixo. A tabela mostra a posição das cobras e das escadas bem como o local final em que o jogador é levado por elas.

<center><img src= "https://github.com/Eloiza/SnakesAndLadders/blob/main/board_game.png"></center>


| Cobras  | Escadas |
|---------|---------|
|12 -> 2  | 3 -> 16 |
|14 -> 11 | 5 -> 7  |
|17 -> 4  | 15 -> 25|
|31 -> 19 | 18 -> 20|
|35 -> 22 | 21 -> 32|


### Executando o código
Para executar o projeto basta clonar o repositório e digitar o comando abaixo:

```
python3 game_analysis.py
```