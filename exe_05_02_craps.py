"""Jogo de Craps

Faça um programa que implemente um jogo de Craps. O jogador lança um
par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada,
você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou
12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na
primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10, este é seu "ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número
novamente. Você perde, no entanto, se tirar um 7 antes de tirar este
Ponto novamente.
"""

from random import randint


def game_status(value: int, point: int, round: int) -> int:
    """Verifica o estado do jogo.
    
    @return:
        -1: o jogador perdeu
         0: o jogo continua
         1: o jogador ganhou
    """
    if (round == 1) and (value in [7, 11]):     # natural
        return 1
    if (round == 1) and (value in [2, 3, 12]):  # craps
        return -1
    if (value == 7):
        return -1
    if value == point:
        return 1
    return 0

def rollDice() -> None:
    """Retorna a soma dos dois dados"""
    return randint(2, 12)

if __name__ == '__main__':
    while True:
        input('\nPressiona ENTER para jogar e CTR+C para sair...')
        point = 0
        round = 1
        while True:
            value = rollDice()
            print(f'Ronda {round:>2}: {value}')
            status = game_status(value, point, round)
            if status == -1:
                print("Game Over! :'(")
                break
            if status == 1:
                print('Você ganhou! :D')
                break
            if not point:
                point = value 
            round += 1

