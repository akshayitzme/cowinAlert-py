from time import time, sleep
from Functions.alert import alert

print('Alerter Running..')
while True:
    sleep(5)
    alert()