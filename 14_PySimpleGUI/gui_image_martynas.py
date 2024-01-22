from PIL import Image
import PySimpleGUI as sg
import io
import base64

image = Image.open('PTU20_live/ai_guy.webp')
with io.BytesIO() as bio:
    image.save('PTU20_live/ai_guy.png', format='PNG')
    image_data = bio.getvalue()

layout = [
    #[sg.Image(data=image.convert())] #expand_x=True, expand_y=True)],
    [sg.Button(image_source='PTU20_live/ai_guy.png')]
]

window = sg.Window("AI GUY", layout, resizable=True)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break