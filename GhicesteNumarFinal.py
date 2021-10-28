import random
import time

numar = random.randint(1, 50)       #It gets a random number between 1 and 50

print('\033[93m' + "-> Crezi ca poti sa ghicesti numarul?" + '\033[91m')    #"Do you think that you can guess the number?"
raspuns1 = input()     #raspuns = answer
if raspuns1 == 'nu':   #"no"
    exit(1)            # If your answer is "no" the process will end with the exit code 1
                       # The process will continue if your answer is "yes" //but anythings else works

print('\033[93m' + "-> Cum te numesti?" + '\033[91m')       #"What's your name?"
nume = input()         #String input for your name
print('\033[93m' + "-> " + nume.upper() + ", gândește-te la un număr între 1 și 50 !" + '\033[0m')    #"Pick a number between 1 and 50"
time.sleep(0.25)       #It'll be a 0.25 seconds delay

#You will have 10 chances to guess the number
alegeriDeFolositRamase = 10     # ~ leftGuessesToUse
alegeriDeFolosit = 10           # ~ guessesToUse
alegeriFolosite = 0             # ~ usedGuesses
while alegeriFolosite < alegeriDeFolosit:   #You can use every True sentence to make the loop
    time.sleep(.25)             #Another delay
    enter = int(input('\033[91m' + "-> Ai ales: " + '\033[0m'))   #"The chosen number is:" // This is the input for the number you choose


    try:
        ghicire = int(enter)    #"guess" // Variable used to make comparisons between the chosen number and the interval (1, 50)
        if ghicire <= 50 and ghicire >= 1:                          #if the chosen number it's in the interval, do:
            alegeriFolosite = alegeriFolosite + 1                   #Add up the usedGuesses by 1 with each wrong guess
                                                                        #This tells the program when you used all your guesses
            alegeriDeFolositRamase = alegeriDeFolositRamase - 1     #Down your leftGuessesToUse by 1 with each wrong guess
                                                                        #This will be used to inform you how many chances you got left


            if alegeriFolosite < alegeriDeFolosit:   #If usedGuesses < guessesToUse

                if ghicire < numar:     #If your number < the random number, then:
                    print('\033[93m' + "->> Numarul este prea mic, mai incearca.")                        #"Number is too small, try again"
                    time.sleep(0.4)
                    print("->>> Mai ai " + str(alegeriDeFolositRamase) + " sanse ramase.")                #"You got "X" guesses left"

                if ghicire > numar:     #If your number > the random number, then:
                    print('\033[93m' + "->> Numarul este prea mare, mai incearca.")                       #"Number is too big, try again"
                    time.sleep(0.4)
                    print("->>> Mai ai " + str(alegeriDeFolositRamase) + " sanse ramase." + '\033[0m')    #"You got "X" guesses left"

            if ghicire == numar:        #If your number = the random number, then:
                break                   #Stop the loop


        if ghicire > 50 and ghicire < 1:            #If your number is not in the (1, 50) interval, then:
            print("Nu sunt in interval!")           #"It's not in the interval"
            time.sleep(.25)                         #Delay
            print("Alege un numar de la 1 la 50.")  #"Choose a number from 1 to 50"
    except:
        print("")

# ghicire = guess
# numar = number
if ghicire == numar:                                                                                #If your number = the random number, then:
    alegeriFolosite = str(alegeriFolosite)                                                          #The program gets the number of your tries
    print('\033[92m' + "-> Ai ghicit numarul din " + alegeriFolosite + " incercari." + '\033[0m')   #"You've guessed the number in 'X' tries"
elif ghicire == numar and alegeriFolosite == 1:                                           #If usedGuesses = 1, then:
    print('\033[92m' + "> Felicitari, ai ghicit din prima! <")     #"Congrulations, you've guessed from the first try"


if ghicire != numar:                                                            #If your number is not equal to the random number, then:
    alegeriFolosite = str(alegeriFolosite)                                      #Get number of tries
    print('\033[91m' + '\033[1m' + "-> Ai depasit numarul de incercari.")       #"You've ran out of guesses"
    time.sleep(.8)
    print("-> Numarul era: " + str(numar))                                      #"The random number was: 'X'"
    time.sleep(1.4)
    print('\33[6m' + "   > GAME OVER! <")
