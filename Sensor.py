import os
from pythonping import ping
import time 
while(True):
   if(ping('IP')._responses[0].success):
      print('Ping sucessful!')
      os.system('sudo python3 /Notify.py Your Title & >> /dev/null 2>&1')
      time.sleep(60)
   else:
      print('Ping failed!')
