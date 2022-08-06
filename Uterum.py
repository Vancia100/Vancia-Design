import time
import threading
import Thermometer

#GPIO.cleanupp()
#GPIO.setmode(GPIO.BCM)

#Sätter läget på GPIO pint till att räkna pin numer som BCM, Vilket man behöver googla upp.

#De variablar som vi kommer att behöva för att räkna ut temperaturerna och fläktarnas värde
FanAuto = True
FanOn = True
Utetemp = 21
Innetemp = 23
Toltemp = 20, 22
Agrev = 25
Dif = 20 
#Dif är skilnaden i temperatur mellan inne och ute som behövs för att fläktarna ska gå hälften så långsamt

#Sätt in Pin-number för de olika aplikationerna nedan!
FanPin = 21
UtePin = 420
InePin = 70
OnoffPin = 22
TruefalsePin = 20

#Temporära grejer som ska bytas ut med riktiga prompts:
ButtonPress = False
ButtonPress2 = False

#Detta är en funktion som faktiskt kontrollerar fläktarna
#Den krävar att man faktiskt  sätter upp de olika GPIO pinsen och PWM på denna pin!
def Fan(hastighet):
        if hastighet > 100:
                print (100)
        elif  hastighet < 20:
                print (20)
        else:
                print (hastighet)

#kör denna som en funktion av multithreading så att den alltid är på.
#Denna funktionen har hand om alla knapparna som man kan sätta till, kräver att man byter ut ButtonPress till faktiska prompts.
#Kan lägga till LEDs för att indikera vad den är på.
def Buttons():
        while True:
                if ButtonPress == True:
                        if FanAuto == True:
                                FanAuto = False
                                if FanOn == True:
                                        Fan(100)
                                else:
                                        Fan(0)
                        elif FanAuto == False:
                                FanAuto == True
                        while ButtonPress == True:
                                time.sleep(0.3)

                if ButtonPress2 == True and FanAuto == False:
                        if FanOn == False:
                                FanOn = True
                                Fan(100)
                        if FanOn == True:
                                FanOn = True
                                Fan(0)
                        while ButtonPress2 == True:
                                time.sleep(0.3)
                time.sleep(0.5)

#Detta är det huvudsakliga skriptet som ser till att fläktarna kör och att de gör det i rätt hastighet

def FanAutoSys():
        while True:
                if FanAuto == True and not(Toltemp[0] <= Innetemp <= Toltemp[1]) and ((Innetemp > Utetemp and Innetemp > Toltemp[1]) or (Innetemp > Utetemp and Innetemp < Toltemp[0])):
                        UteTemp = Thermometer.Readtemp()
                        IneTemp = Thermometer.Readtemp2()
                        Fan(round(Agrev*abs(Innetemp-(sum(Toltemp)/2))/(abs(Innetemp-Utetemp)*(1/Dif+1))))
                        time.sleep(1)

                else:
                        time.sleep(1)

#Denna del är det som faktiskt kommer att göra någonting:
#öppnar en thread på de olika funktionerna

T1 = threading.Thread(target=Buttons)
T2 = threading.Thread(target=FanAutoSys)

T1.start()
T2.start()