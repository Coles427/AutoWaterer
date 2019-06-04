import os
from os.path import expanduser
import time
from readAIN import readAIN
import csv

inrange1 = False
inrange2 = False
home = expanduser('~')
path = home + "/Autowater2/water.csv"
data = []
with open(path) as watCSV:
    data = list(csv.reader(watCSV))

watCSV.close()
min1 = int(data[1][1])
max1 = int(data[1][2])
waterTo1 = (min1 + max1)/2

while(inrange1 == False):
    #Turn on water GPIO
    #water to will be  adjusted
    level = readAIN.read_AIN0()
    if (level > waterTo1):
        inrange1 = True
    print(level)
print(inrage)
