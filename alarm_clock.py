# Project 14 : Python Alarm Clock

import time 
import datetime
import pygame  # type: ignore

def set_alarm(alarm):
    print(f"Alarm time has been set at {alarm}")
    sound_file = "Powerhouse-Vibe-MassTamilan.dev.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time : {current_time}")

        if current_time == alarm:
            print("Wake up!!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)
                pass

            is_running = False

        time.sleep(1)
        # is_running = False

def main():
    alarm_time = input("Enter the alarm time (HH:MM:SS) : ")
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()