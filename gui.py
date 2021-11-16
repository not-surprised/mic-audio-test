import PySimpleGUIQt as sg

num_displays = 3
num_audio = 4

font = "Helvetica"
header_size = "24"
body_size = "13"
small_body_size = "9"

sg.theme("Dark")

full_size = (1400, 1000) # width, height
col_size = (600, 450)

monitor_image = "monitor_image.png"
speaker_image = "speaker_image.png"

padding = [[sg.Stretch()]]

left_col = [[sg.Text("\nDisplays\n", font=(font + " " +header_size))]]

for i in range(num_displays):
    left_col.append([sg.Image(monitor_image, size=(50, 50))])
    left_col.append([sg.Text("\nDisplay", font=(font + " " +body_size))])
    left_col.append([sg.Text("\n", font=(font + " " + "2"))])
    left_col.append([sg.Checkbox("Enable !surprised", font=(font + " " +small_body_size))])
    left_col.append([sg.Text("\n\n", font=(font + " " + body_size))])


right_col = [[sg.Text("\nAudio\n", font=(font + " " +header_size))]]

for i in range(num_audio):
    right_col.append([sg.Image(speaker_image, size=(50, 50))])
    right_col.append([sg.Text("\nAudio Device", font=(font + " " +body_size))])
    left_col.append([sg.Text("\n", font=(font + " " + "2"))])
    right_col.append([sg.Checkbox("Using headphones", font=(font + " " +small_body_size))])
    right_col.append([sg.Checkbox("Enable !surprised", font=(font + " " +small_body_size))])
    right_col.append([sg.Text("\n", font=(font + " " + body_size))])


calibrate_button = [sg.Button('Calibrate', font=(font + " " + body_size), size=(140, 60), button_color=("#bac6d4", "#3f618a"))]


button_container = [calibrate_button]

padding = [[sg.Stretch()]]

layout = [[sg.Stretch(), sg.Column(left_col, element_justification='l'), sg.Stretch(), sg.Stretch(), sg.Column(right_col, element_justification='l'), sg.Stretch()],
          [sg.Column(button_container, element_justification='r')]]
scrollable = [[sg.Column(layout, size=full_size, scrollable=True)]]
window = sg.Window("!surprised", scrollable, size=full_size, resizable=False)




while True:
    event, values  = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Calibrate" or event == sg.WIN_CLOSED:
        break

