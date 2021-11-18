import PySimpleGUIQt as sg
import screen_brightness_control as sbc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))


monitors = sbc.list_monitors()
num_displays = len(monitors)
num_audio = 2


def make_window():
    font = 'Verdana'
    header_font = font + ' 24'
    body_font = font + ' 14'
    small_body_font = font + ' 10'

    sg.theme("Dark")

    full_size = (800, 600)  # width, height

    monitor_image = "monitor_image.png"
    speaker_image = "speaker_image.png"

    left_col = [[sg.Image(monitor_image)], [sg.Text("\nDisplays\n", font=header_font)]]

    for i in range(num_displays):
        image_col = [[sg.Text("\n", font=(font + " " + "2"))],
                     [sg.Text("Display\n", font=body_font)]]
        settings_col = [[sg.Text("\n", font=(font + " 6"))],
                        [sg.Slider(range=(0, 100), orientation='h',
                                   key='display' + str(i), disabled=True)],
                        [sg.Checkbox("Enable !surprised", font=small_body_font, size=(20, 1.75))]]
        device_unit = [[sg.Column(image_col, element_justification='c'), sg.Column(settings_col)]]
        left_col.append([sg.Column(device_unit)])

    right_col = [[sg.Image(speaker_image)], [sg.Text("\nAudio\n", font=header_font)]]

    for i in range(num_audio):
        image_col = [[sg.Text("\n", font=(font + " " + "2"))],
                     [sg.Text("Speaker\n", font=body_font)]]
        settings_col = [[sg.Text("\n", font=(font + " 6"))],
                        [sg.Slider(range=(0, 100),
                                   orientation='h', key='audio' + str(i), disabled=True)],
                        [sg.Checkbox("Enable !surprised", font=small_body_font, size=(20, 1.25))],
                        [sg.Checkbox("Is speaker", font=small_body_font)]]
        device_unit = [[sg.Column(image_col, element_justification='c'), sg.Column(settings_col)]]
        right_col.append([sg.Column(device_unit)])

    calibrate_button = [sg.Button('Calibrate', font=body_font, size=(160, 70), button_color=("#bac6d4", "#3f618a"))]

    button_container = [calibrate_button]

    layout = [[sg.Stretch(),
               sg.Column(left_col, element_justification='c'),
               sg.Stretch(),
               sg.Stretch(),
               sg.Column(right_col, element_justification='c'),
               sg.Stretch()],
              [sg.Column(button_container, element_justification='c')]]
    scrollable = [[sg.Column(layout, size=full_size, scrollable=True)]]
    window = sg.Window("!surprised", scrollable, size=full_size, resizable=False, disable_minimize=True)
    return window


def make_tray():
    menu = ['', ['&Configure', '---', 'E&xit']]
    tooltip = '!surprised'
    tray = sg.SystemTray(menu, tooltip=tooltip, data_base64=sg.DEFAULT_BASE64_ICON)
    return tray


def read(window, tray, timeout=100):
    if window is not None:
        event, values = window.read(timeout / 2)
        if event != sg.TIMEOUT_EVENT:
            return event, values
    event = tray.read(timeout / 2)
    return event, None


def refresh_values(window):
    if window is None:
        return
    for i in range(num_displays):
        slider = window["display" + str(i)]
        slider.update(sbc.get_brightness()[i])
    for i in range(num_audio):
        slider = window["audio" + str(i)]
        slider.update(volume.GetMasterVolumeLevelScalar() * 100)


def run():
    window = make_window()
    tray = make_tray()
    while True:
        event, values = read(window, tray, 50)
        refresh_values(window)
        if event != sg.TIMEOUT_EVENT:
            print(event, values)
            if window is not None:
                if event in [sg.WIN_CLOSED]:
                    window.close()
                    window = None
                if event in ["Calibrate"]:
                    pass
            else:
                if event in ["Configure", sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED]:
                    window = make_window()
            if event in ["Exit"]:
                break

    tray.close()
    if window is not None:
        window.close()


if __name__ == "__main__":
    run()
