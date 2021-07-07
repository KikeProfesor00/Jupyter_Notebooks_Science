#DIGITAL CLOCK IN PYTHON
#clcoding  telegram
from datetime import datetime
from time import sleep
while 1:
    n=datetime.now()
    print(datetime.strftime(n,"%H:%M:%S"), end='\r')
    sleep(1)