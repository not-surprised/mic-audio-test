import PySimpleGUIQt as sg

num_displays = 3
num_audio = 2

font = "Helvetica"
header_size = "36"
body_size = "14"

sg.theme("Dark")

full_size = (800, 500)
col_size = (375, 400)

monitor_image = "monitor_image.png"

left_col = [[sg.Text("Displays", font=(font + " " +header_size))]]
for i in range(num_displays):
    left_col.append([sg.Image(monitor_image, size=(50, 50))])
    left_col.append([sg.Text("Display", font=(font + " " +body_size))])
    left_col.append([sg.Checkbox("Enable !surprised", font=(font + " " +body_size))])

right_col = [[sg.Text("Audio", font=(font + " " +header_size))]]
for i in range(num_audio):
    right_col.append([sg.Text("Audio Device", font=(font + " " +body_size))])
    right_col.append([sg.Checkbox("Using headphones", font=(font + " " +body_size))])
    right_col.append([sg.Checkbox("Enable !surprised", font=(font + " " +body_size))])

calibrate_button = [sg.Button('Calibrate', font=(font + " " +body_size), pad=(25, 25))]


button_container = [calibrate_button]




layout = [[sg.Column(left_col, element_justification='l', size=col_size), sg.Column(right_col, element_justification='r', size=col_size)],
          [sg.Column(button_container, element_justification='r', size = (75, 50))]]

window = sg.Window("!surprised", layout, size=full_size)

while True:
    event, values  = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Calibrate" or event == sg.WIN_CLOSED:
        break

