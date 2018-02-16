import time
from datetime import datetime

import pygame

while 1:
    alarm_file = open("/var/www/html/alarm.txt")
    alarm_time = alarm_file.read()
    alarm_file.close()
    time.sleep(0.2)
    print(str(datetime.strftime(datetime.now(), "%A, %b %d %Y %H:%M:%S.%f ")))
    print(alarm_time + "=" + str(datetime.strftime(datetime.now(), "%H:%M")))
    if datetime.strftime(datetime.now(), "%H:%M") == alarm_time:
        print("ALARM")
        pygame.mixer.init()
        pygame.mixer.music.load("alarm.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        print("ALARM ENDED")
