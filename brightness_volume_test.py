import screen_brightness_control as sbc
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def set_screen_brighness(new):
    sbc.set_brightness(new)

def change_screen_brightness(change):
    set_screen_brighness(sbc.get_brightness() + change)

def set_system_volume(volume, new):
    volume.SetMasterVolumeLevelScalar(new / 100.0, None)
    print(str(int(volume.GetMasterVolumeLevelScalar()*100)) + "%")

def change_system_volume(volume, change):
    new_volume = volume.GetMasterVolumeLevelScalar() * 100 + change
    set_system_volume(volume, new_volume)


if __name__ == '__main__':
    change_choice = input("Would you like to change your brightness (b) or your volume (v)? ")
    if (change_choice == "b"):
        screen_choice = input("Would you like to set a brightness (s) or change it by a certain amount (c)? ")
        if(screen_choice == "s"):
            screen_input = int(input("What would you like to set your brightness to? "))
            set_screen_brighness(screen_input)
        elif(screen_choice == "c"):
            screen_input = int(input("How much would you like to change your brightness by? If you would like to decrease it, enter a negative number: "))
            change_screen_brightness(screen_input)

    elif (change_choice == "v"):
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(
            IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))


        volume_choice = input("Would you like to set a volume (s) or change it by a certain amount (c)? ")

        if (volume_choice == "s"):
            volume_input = int(input("What would you like to set your volume to? "))
            set_system_volume(volume, volume_input)
        elif (volume_choice == "c"):
            volume_input = int(input("How much would you like to change your volume by? If you would like to decrease it, enter a negative number: "))
            change_system_volume(volume, volume_input)



