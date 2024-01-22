import PySimpleGUI as sg

layout = [
    [sg.Text('Koks tavo vardas?')],
    [sg.Input(key = "-NAME-")],
    [
        sg.Button('Pasisveikinti', key = "-HELLO-"),
        sg.Button('Atsisveikinti', key = "-BYE-"),
    ],
    [sg.Text(size=(40, 1), key ='-OUTPUT-')]
]

window = sg.Window('LABAS', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == '-HELLO-':
        window['-OUTPUT-'].update(f'Sveiki {values["-NAME-"]}')
    elif event == '-BYE-':
        window['-OUTPUT-'].update(f'Viso gero {values["-NAME-"]}')

    window.close