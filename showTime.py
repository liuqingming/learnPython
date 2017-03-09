from datetime import datetime
from os import system
import threading

now = datetime.today()
print now.year,now.month,now.day,now.hour,now.minute,now.second
str="%s:%s:%s"%(now.hour,now.minute,now.second)
print str