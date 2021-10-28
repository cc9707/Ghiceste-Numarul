import random
import time

numar = random.randint(1, 50)

print('\033[93m' + "-> Crezi ca poti sa ghicesti numarul?" + '\033[91m')
raspuns1 = input()
if raspuns1 == 'nu':
    exit(1)

print('\033[93m' + "-> Cum te numesti?" + '\033[91m')
nume = input()
print('\033[93m' + "-> " + nume.upper() + ", gandeste-te la un numar !" + '\033[0m')
time.sleep(0.25)

alegeriDeFolositRamase = 10
alegeriDeFolosit = 10
alegeriFolosite = 0
while alegeriFolosite < alegeriDeFolosit:
    time.sleep(.25)
    enter = int(input('\033[91m' + "-> Numarul ales este: " + '\033[0m'))
    try:
        ghicire = int(enter)

        if ghicire <= 50 and ghicire >= 1:
            alegeriFolosite = alegeriFolosite + 1
            alegeriDeFolositRamase = alegeriDeFolositRamase - 1

            if alegeriFolosite < alegeriDeFolosit:
                if ghicire < numar:
                    print('\033[93m' + "->> Numarul este prea mic, mai incearca.")
                    time.sleep(0.65)
                    print("->>> Mai ai " + str(alegeriDeFolositRamase) + " sanse ramase.")
                if ghicire > numar:
                    print('\033[93m' + "->> Numarul este prea mare, mai incearca.")
                    time.sleep(0.65)
                    print("->>> Mai ai " + str(alegeriDeFolositRamase) + " sanse ramase." + '\033[0m')
            if ghicire == numar:
                break
        if ghicire > 50 and ghicire < 1:
            print("Nu sunt in interval!")
            time.sleep(.25)
            print("Alege un numar de la 1 la 50.")
    except:
        print("")

if ghicire == numar:
    alegeriFolosite = str(alegeriFolosite)
    print('\033[92m' + "-> Ai ghicit numarul din " + alegeriFolosite + " incercari." + '\033[0m')
elif ghicire == numar:
    alegeriFolosite = 1
    print("Felicitari, ai ghicit din prima!")
if ghicire != numar:
    alegeriFolosite = str(alegeriFolosite)
    print('\033[91m' + '\033[1m' + "-> Ai depasit numarul de incercari.")
    time.sleep(.8)
    print("-> Numarul era: " + str(numar))
    time.sleep(1.4)
    print('\33[6m' + "> GAME OVER! <")
