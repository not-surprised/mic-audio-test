import PySimpleGUIQt as sg


def make_window():
    num_displays = 10
    num_audio = 10

    font = 'Consolas'
    header_font = font + ' 24'
    body_font = font + ' 14'
    small_body_font = font + ' 10'

    sg.theme("Dark")

    full_size = (800, 600)  # width, height

    monitor_image = "monitor_image.png"
    speaker_image = "speaker_image.png"

    left_col = [[sg.Image(monitor_image)], [sg.Text("\nDisplays\n", font=header_font)]]

    for i in range(num_displays):
        layout = [[sg.Text("\nDisplay", font=body_font)],
                  [sg.Text("\n", font=(font + " " + "2"))],
                  [sg.Checkbox("Enable !surprised", font=small_body_font)],
                  [sg.Text("\n", font=body_font)]]
        left_col.append([sg.Column(layout)])

    right_col = [[sg.Image(speaker_image)], [sg.Text("\nAudio\n", font=header_font)]]

    for i in range(num_audio):
        layout = [[sg.Text("\nAudio", font=body_font)],
                  [sg.Text("\n", font=(font + " " + "2"))],
                  [sg.Checkbox("Enable !surprised", font=small_body_font)],
                  [sg.Checkbox("Is speaker", font=small_body_font)],
                  [sg.Text("\n", font=body_font)]]
        right_col.append([sg.Column(layout)])

    calibrate_button = [sg.Button('Calibrate', font=body_font, size=(140, 60), button_color=("#bac6d4", "#3f618a"))]

    button_container = [calibrate_button]

    layout = [[sg.Stretch(),
               sg.Column(left_col, element_justification='l'),
               sg.Stretch(),
               sg.Stretch(),
               sg.Column(right_col, element_justification='l'),
               sg.Stretch()],
              [sg.Column(button_container, element_justification='c')]]
    scrollable = [[sg.Column(layout, size=full_size, scrollable=True)]]
    return sg.Window("!surprised", scrollable, size=full_size, resizable=False)


def run():
    window = make_window()
    while True:
        event, values  = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Calibrate" or event == sg.WIN_CLOSED:
            break


if __name__ == "__main__":
    run()
