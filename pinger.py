import os
import time

os.system('start .\server.jar')

time.sleep(10)

os.system('Stop-Process -Name "javaw" ')
