import random
import time

numar = random.randint(1, 50)                                               #It gets a random number between 1 and 50

print('\033[93m' + "-> Crezi că poți să ghicești numărul?" + '\033[91m')    #"Do you think that you can guess the number?"
raspuns1 = input()                                                          #raspuns = answer

if raspuns1 == 'nu' or raspuns1 == 'Nu' or raspuns1 == 'NU':                #"no", "No", "NO"
    exit(1)                                                                 #If your answer is "no" the process will end with the exit code 1.

strin = 'da'                                                                #"yes"
str1 = 'Da'                                                                 #"Yes"
str2 = 'DA'                                                                 #"YES"
#while answer is different than 'yes or 'no', it will print "Invalid answer, answer with 'yes' or 'no'."
while raspuns1 != 'nu' and raspuns1 != 'Nu' and raspuns1 != 'NU' and raspuns1 != strin and raspuns1 != str1 and raspuns1 != str2:
    print("Răspuns invalid. Răspunde cu 'Da' sau 'Nu'.")
    exit(1)
    break


while raspuns1 == strin or raspuns1 == str1 or raspuns1 == str2:            #while answer == 'yes':
    print('\033[93m' + "-> Cum te numești?" + '\033[91m')                   #"What's your name?"
    nume = input()                                                          #String input for your name.
    print('\033[93m' + "-> " + nume[0].upper() + nume[1:].lower() + ", gândește-te la un număr între 1 și 50 !" + '\033[0m')    #"Pick a number between 1 and 50!"
    time.sleep(0.25)                                                        #It'll be a 0.25 seconds delay.

    #You will have 10 chances to guess the number
    alegeriDeFolositRamase = 10     # ~= leftGuessesToUse
    alegeriDeFolosit = 10           # ~= guessesToUse
    alegeriFolosite = 0             # ~= usedGuesses
    while alegeriFolosite < alegeriDeFolosit:                               #You can use every True sentence to make the loop
        time.sleep(.25)                                                     #Delay
        enter = int(input('\033[91m' + "-> Numărul ales este: " + '\033[0m'))   #"The chosen number is:" // This is the input for the number you choose


        try:
            ghicire = int(enter)    #"guess" // Variable used to make comparisons between the chosen number and the interval (1, 50)
            if ghicire <= 50 and ghicire >= 1:                              #if the chosen number it's in the interval, do:
                alegeriFolosite = alegeriFolosite + 1                       #Add up the usedGuesses by 1 with each wrong guess
                                                                            #This tells the program when you used all your guesses
                alegeriDeFolositRamase = alegeriDeFolositRamase - 1         #Down your leftGuessesToUse by 1 with each wrong guess
                                                                            #This will be used to inform you how many chances you got left


                if alegeriFolosite < alegeriDeFolosit:                      #If usedGuesses < guessesToUse

                    if ghicire < numar:                                     #If your number < the random number, then:
                        print('\033[93m' + "->> Numărul este prea mic, mai încearcă.") #"Number is too small, try again"
                        time.sleep(0.4)
                        print("->>> Mai ai " + '\033[40m' + '\033[36m' + str(alegeriDeFolositRamase) + '\033[0m' + '\033[93m' + " șanse rămase.")
                        #"You got "X" guesses left"

                    if ghicire > numar:                                     #If your number > the random number, then:
                        print('\033[93m' + "->> Numărul este prea mare, mai încearcă.") #"Number is too big, try again"
                        time.sleep(0.4)
                        print("->>> Mai ai " + '\033[40m' + '\033[36m' + str(alegeriDeFolositRamase) + '\033[0m' + '\033[93m' + " șanse rămase.")
                        #"You got "X" guesses left"

                    if ghicire == numar:
                        break

            else:                                                            #Else, the chosen number is not between 1 and 50, then:
                print('\033[91m' + '\033[1m' + "Nu este în interval!")       #"It's not in the interval"
                time.sleep(.25)                                              #Delay
                print("Alege un număr de la 1 la 50.")                       #"Choose a number from 1 to 50"
        except:
            print("")

    if ghicire == numar:                                                     #If your number = the random number, then:
        alegeriFolosite = str(alegeriFolosite)                               #The program gets the number of your tries
        print('\033[92m' + "->> Ai ghicit numărul din " + alegeriFolosite + " încercări." + '\033[0m')  # "You've guessed the number in 'X' tries"
        while ghicire == numar and alegeriFolosite == 1:                     #If usedGuesses = 1, then:
            print('\033[92m' + "> Felicitări, ai ghicit din prima! <")       #"Congrulations, you've guessed from the first try"
        break

    if ghicire != numar:                                                     #If your number is not equal to the random number, then:
        alegeriFolosite = str(alegeriFolosite)                               #Get number of tries
        print('\033[91m' + '\033[1m' + "-> Ai depașit numărul de încercări :(")            #"You've ran out of guesses"
        time.sleep(.8)
        print("-> Numărul era: " + '\033[40m' + '\033[36m' + str(numar) + '\033[0m' "\n")  #"The random number was: 'X'"
        time.sleep(1.4)
        print('\33[1m' + '\033[91m' + " > GAME OVER! <")
        break