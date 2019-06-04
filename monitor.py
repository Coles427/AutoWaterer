import os
import time
from readAIN import readAIN
os.environ.setdefault("DJANGO_SETTINGS_MODULE","AutoWaterer.settings")
import django

django.setup()

from catalog.models import WaterDat
loop = False
read1 = readAIN.read_AIN0()
read2 = readAIN.read_AIN1()

while (loop == False):
    new1 = WaterDat()
    new2 = WaterDat()

    new1.plant_num = 1
    new1.current_level = read1
    print(new1.current_level)
    # new2.plant_num = 2
    # new2.current_level = read2

    new1.save()
    #new2.save()

    time.sleep(900)

    
