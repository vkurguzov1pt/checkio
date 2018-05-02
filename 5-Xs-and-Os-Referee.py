'''
You are given a result of a game and you must determine
if the game ends in a win or a draw as well as who will be the winner.
Make sure to return "X" if the X-player wins and "O" if the O-player wins.
If the game is a draw, return "D".
'''

def checkio(game_result):
    result_dict = {'XXX':'X', 'OOO':'O'}
    result = ''
    # Define length of a row
    theLength = len(game_result[0])
    for row in game_result:
        result = result_dict[row] if row in result_dict else ''
    # If no result reverse the rows
    if result == '':
        sReversed = ''
        for i in range(theLength):
            for row in game_result:
                sReversed += row[i]
                if 'XXX' in sReversed:
                    result = 'X'
                elif 'OOO' in sReversed:
                    result = 'O'
            else:
                sReversed = ''
    # If still no result check diagonal
    if result == '':
        sDiag = ''
        for i in range(theLength):
            sDiag += game_result[i][i]
        if 'XXX' in sDiag:
            result = 'X'
        elif 'OOO' in sDiag:
            result = 'O'
    # Finally check another diagonal
    if result == '':
        sDiagAnother = ''
        for i in range(theLength):
            sDiagAnother += game_result[i][theLength - 1 - i]
        if 'XXX' in sDiagAnother:
            result = 'X'
        elif 'OOO' in sDiagAnother:
            result = 'O'
    # If still no result it means draw
    if result == '':
        result = 'D'

    return result


if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check'")
