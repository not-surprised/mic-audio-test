import PySimpleGUIQt as sg
import screen_brightness_control as sbc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume



devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


num_displays = 3
num_audio = 2

font = "Verdana"
header_size = "24"
body_size = "14"
small_body_size = "10"

sg.theme("Dark")

full_size = (1400, 1000) # width, height
col_size = (600, 450)

monitor_image = "monitor_image.png"
speaker_image = "speaker_image.png"

padding = [[sg.Stretch()]]

left_col = [[sg.Text("\nDisplays\n", font=(font + " " + header_size))]]


for i in range(num_displays):

    image_col = [[sg.Image(monitor_image)], [sg.Text("\n", font=(font + " " + "2"))],
                 [sg.Text("Display\n", font=(font + " " + body_size))]]
    settings_col = [[sg.Text("\n", font=(font + " 6"))],
                [sg.Slider(range=(0, 100), default_value=sbc.get_brightness() * 100, orientation='h', key='display' + str(i), disabled=True)],
                [sg.Checkbox("Enable !surprised", font=(font + " " + small_body_size), size=(20, 1.75))]]
    device_unit = [[sg.Column(image_col, element_justification='c'), sg.Column(settings_col)]]

    left_col.append([sg.Column(device_unit)])


right_col = [[sg.Text("\nAudio\n", font=(font + " " +header_size))]]

for i in range(num_audio):

    image_col = [[sg.Image(speaker_image)], [sg.Text("\n", font=(font + " " + "2"))],
                 [sg.Text("Speaker\n", font=(font + " " + body_size))]]
    settings_col = [[sg.Text("\n", font=(font + " 6"))],
                [sg.Slider(range=(0, 100), default_value=volume.GetMasterVolumeLevelScalar() * 100, orientation='h', key='audio' + str(i), disabled=True)],
                [sg.Checkbox("Enable !surprised", font=(font + " " + small_body_size), size=(20, 1.25))],
                [sg.Checkbox("Headphones", font=(font + " " + small_body_size))]]
    device_unit = [[sg.Column(image_col, element_justification='c'), sg.Column(settings_col)]]

    right_col.append([sg.Column(device_unit)])


calibrate_button = [sg.Button('Calibrate', font=(font + " " + body_size), size=(160, 70), button_color=("#bac6d4", "#3f618a"))]


button_container = [calibrate_button]

padding = [[sg.Stretch()]]

layout = [[sg.Stretch(), sg.Column(left_col, element_justification='c'),  sg.Stretch(), sg.Stretch(), sg.Column(right_col, element_justification='c'), sg.Stretch()],
          [sg.Column(button_container, element_justification='r')]]
scrollable = [[sg.Column(layout, size=full_size, scrollable=True)]]
window = sg.Window("!surprised", scrollable, size=full_size, resizable=False)




while True:
    event, values  = window.read()
    # End program if user closes window or
    # presses the OK button
    last_brightness = 10
    current_brightness = 50
    if event == "Calibrate":
        for i in range(num_displays):
            slider = window["display" + str(i)]
            slider.update(sbc.get_brightness())
        for i in range(num_audio):
            slider = window["audio" + str(i)]
            slider.update(volume.GetMasterVolumeLevelScalar() * 100)

    if event == sg.WIN_CLOSED:
        break



