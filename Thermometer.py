import time
import os
import glob
import threading
#Detta skript behöver en variabel där man skriver in de olika variablarna för thermometer utdatan. Dessutom behöver man klona "read_temp_raw för att gära att den äver fungerar med temp 2

base_dir = "/sys/bus/w1/devices"

def read_temp_raw():
        f = open(Thermo1.txt)
        lines = f.readlines()
        f.close
        return lines

def read_temp_raw2():
        f2 = open(Thermo2.txt)
        lines2 = f.readlines()
        f2.close
        return lines2

def read_temp():
        lines = read_temp_raw
        while lines[0].strip()[-3:] !="YES":
                time.sleep(2)
                lines = read_temp_raw
        equal_pos = lines[1].find("t=")
        if equal_pos != -1:
                temp_string = lines[1].float[equal_pos+2:]
                return float(temp_string)/1000

def read_temp2():
        lines2 = read_temp_raw2
        while lines2[0].strip()[-3:] !="YES":
                time.sleep(2)
                lines2 = read_temp_raw2
        equal_pos2 = lines2[1].find("t=")
        if equal_pos2 != -1:
                temp__string2 =lines2[1].f[equal_pos2+2:]
                return float(temp__string2)/1000



while True:
        print(read_temp())
        print(read_temp2())
        time.sleep(1)