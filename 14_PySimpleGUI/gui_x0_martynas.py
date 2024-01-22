import PySimpleGUI as sg

def get_player(turn):
    if turn % 2 == 0:
        return "X"
    return "0"

def check_winning(game):
    winning_combos = [
        ['1x1', '1x2', '1x3'],
        ['2x1', '2x2', '2x3'],
        ['3x1', '3x2', '3x3'],
        ['1x1', '2x1', '3x1'],
        ['2x1', '2x2', '3x2'],
        ['1x3', '2x3', '3x3'],
        ['1x1', '2x2', '3x3'],
        ['1x3', '2x2', '3x1']
    ]
    for combo in winning_combos:
        if combo[0] in game and combo[1] in game and combo[2] in game \
            and game[combo[0]] == game[combo[1]] and game[combo[0]] == game[combo[2]]:
            return True
    return False
    
def reset_game(window: sg.Window):
    window['-CURRENT-'].update('Current Player: X')
    for row in range(1, 4):
        for col in range(1, 4):
            window[f'{row} x {col}'].update('  ', disabled = False)
    window['-RESET-'].update(visible = False)
    return 0, {}



coordinates = []
rows = []
for row in range(1, 4):
    columns = []
    for col in range(1, 4):
        columns.append(sg.Button("  ", key=f'{row} x {col}', font="Terminal 20"))
        coordinates.append(f'{row}x{col}')
    rows.append(columns)

layout = [
    [sg.Text('Current player: X', key='-CURRENT-')],
    rows,
]

window = sg.Window("X's and 0's", layout)

turn = 0
game = {}

while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in coordinates:
        window[event].Update(get_player(turn), disabled = True)
        game[event] = get_player(turn)
        is_game_winner = check_winning(game)
        if is_game_winner or turn >= 8:
            if is_game_winner: 
                window['-CURRENT-'].update(f'WINNER: {get_player(turn)}')
            else:
                window['-CURRENT-'].update('DRAW')
            window['-RESET-'].update(visible = True)
        else:
            turn += 1 
            window['-CURRENT-'].Update(f'Current player: {get_player(turn)}')