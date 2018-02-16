from datetime import datetime
import time
import pygame

alarm_h = 6
alarm_m = 0
alarm_time = input()
while 1:
    time.sleep(0.2)
    print(str(datetime.strftime(datetime.now(), "%A, %b %d %Y %H:%M:%S.%f ")))
    print(alarm_time + "=" + str(datetime.strftime(datetime.now(), "%H:%M")))
    if datetime.strftime(datetime.now(), "%H:%M") == alarm_time:
        break

print("ALARM")
pygame.mixer.init()
pygame.mixer.music.load("alarm.wav")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue
