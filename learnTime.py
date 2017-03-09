import threading
from os import system
from datetime import datetime

def func():
 print 'hi'
 system('shutdown -r -t 6')
 now = datetime.today()
 print now.year,now.month,now.day,now.hours,now.minutes,now.seconds

timer = threading.Timer(1,func)
timer.start()
