class WrongNumberOfPlayersError(Exception):
    """Проверка количества игроков"""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'{self.message}.'


class NoSuchStrategyError(WrongNumberOfPlayersError):
    '''Проверка на корректность хода'''


def rps_game_winner(arr):
    p1 = arr[0][1]
    p2 = arr[1][1]
    WIN_P1 = ['RS', 'SP', 'PR']
    if len(arr) > 2:
        raise WrongNumberOfPlayersError('Игроков должно быть 2')
    elif p1 not in ['R', 'P', 'S'] or p2 not in ['R', 'P', 'S']:
        raise NoSuchStrategyError('Введенное значение одного из игроков некорректное')
    else:
        if p1 == p2 or p1 + p2 in WIN_P1:
            return ' '.join(i for i in arr[0])
        else:
            return ' '.join(i for i in arr[1])

