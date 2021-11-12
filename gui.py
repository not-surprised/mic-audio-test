import PySimpleGUI as sg

num_displays = 1
num_audio = 2

font = "Helvetica"
header_size = "60"
body_size = "36"

full_size = (800, 500)
col_size = (375, 400)


left_col = [[sg.Text("Displays", font=(font + "," +header_size))]]
for i in range(num_displays):
    left_col.append([sg.Image(sg.EMOJI_BASE64_SAD)])
    left_col.append([sg.Text("Display", font=(font + "," +body_size))])
    left_col.append([sg.Checkbox("Enable !surprised", font=(font + "," +body_size))])

right_col = [[sg.Text("Audio", font=(font + "," +header_size))]]
for i in range(num_audio):
    right_col.append([sg.Text("Audio Device", font=(font + "," +body_size))])
    right_col.append([sg.Checkbox("Enable !surprised", font=(font + "," +body_size))])

calibrate_button = [sg.Button("Calibrate", font=(font + "," +body_size))]
is_headphones = [sg.Checkbox("Using headphones", font=(font + "," +body_size))]

button_container = [calibrate_button, is_headphones]


layout = [[sg.Column(left_col, element_justification='c', size=col_size), sg.Column(right_col, element_justification='c', size=col_size)],
          [sg.Column(button_container, element_justification='r', size = (75, 50))]]

window = sg.Window("!surprised", layout, size=full_size)

while True:
    event = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Calibrate" or event == sg.WIN_CLOSED:
        break

