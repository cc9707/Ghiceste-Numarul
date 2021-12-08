import random
import time

red = '\033[31m'
warning_yellow = '\033[93m'
green = '\033[32m'
cyan = '\033[36m'
endline = '\033[0m'
blackbg = '\033[40m'

numar = random.randint(1, 50)                                               #It gets a random number between 1 and 50
print(f"{warning_yellow}-> Crezi că poți să ghicești numărul?")             #"Do you think that you can guess the number?"
raspuns = input()                                                           #raspuns = answer
if raspuns == 'nu' or raspuns == 'Nu' or raspuns == 'NU':                   #"no", "No", "NO"
    exit(1)                                                                 #If your answer is "no" the process will end with the exit code 1.

strin = 'da'                                                                #"yes"
str1 = 'Da'                                                                 #"Yes"
str2 = 'DA'                                                                 #"YES"
#while answer is different than 'yes or 'no', it will print "Invalid answer, answer with 'yes' or 'no'."
while raspuns != 'nu' and raspuns != 'Nu' and raspuns != 'NU' and raspuns != strin and raspuns != str1 and raspuns != str2:
    print(f"{red} Răspuns invalid. Răspunde cu 'Da' sau 'Nu'.")
    exit(1)
    break

while raspuns == strin or raspuns == str1 or raspuns == str2:               #while answer == 'yes':
    print(f"{warning_yellow} -> Cum te numești?")                           #"What's your name?"
    nume = input()                                                          #String input for your name.
    print(f"{warning_yellow} {nume[0].upper()}{nume[1:].lower()} gândește-te la un număr între 1 și 50 !")    #"Pick a number between 1 and 50!"
    time.sleep(.25)                                                         #It'll be a 0.25 seconds delay.
    #You will have 10 chances to guess the number
    alegeriDeFolositRamase = 10     # ~= leftGuessesToUse
    alegeriDeFolosit = 10           # ~= guessesToUse
    alegeriFolosite = 0             # ~= usedGuesses
    while alegeriFolosite < alegeriDeFolosit:                                #You can use every True sentence to make the loop
        time.sleep(.25)                                                      #Delay
        enter = int(input(f"{red} -> Numărul ales este: "))                  #"The chosen number is:" // This is the input for the number you choose
        try:
            ghicire = int(enter)    #"guess" // Variable used to make comparisons between the chosen number and the interval (1, 50)
            if ghicire <= 50 and ghicire >= 1:                              #if the chosen number it's in the interval, do:
                alegeriFolosite = alegeriFolosite + 1                       #Add up the usedGuesses by 1 with each wrong guess
                                                                            #This tells the program when you used all your guesses
                alegeriDeFolositRamase = alegeriDeFolositRamase - 1         #Down your leftGuessesToUse by 1 with each wrong guess
                                                                            #This will be used to inform you how many chances you got left
                if alegeriFolosite < alegeriDeFolosit:                      #If usedGuesses < guessesToUse
                    if ghicire < numar:                                     #If your number < the random number, then:
                        print(f"{red} ->> Numărul este prea mic, mai încearcă.") #"Number is too small, try again"
                        time.sleep(.4)
                        print(f"{warning_yellow}->>> Mai ai {blackbg}{cyan}{str(alegeriDeFolositRamase)}{endline} {warning_yellow}șanse rămase.")
                        #"You got "X" guesses left"
                    if ghicire > numar:                                     #If your number > the random number, then:
                        print(f"{red} ->> Numărul este prea mare, mai încearcă.") #"Number is too big, try again"
                        time.sleep(.4)
                        print(f"{warning_yellow} ->>> Mai ai {blackbg}{cyan}{str(alegeriDeFolositRamase)}{endline} {warning_yellow}șanse rămase.")
                        #"You got "X" guesses left"
                    if ghicire == numar:                                     #If your number = the random number, then:
                        break                                                #Stop the loop
            else:                                                            #Else, the chosen number is not between 1 and 50, then:
                print(f"{red} Nu este în interval!")                         #"It's not in the interval"
                time.sleep(.25)                                              #Delay
                print("Alege un număr de la 1 la 50.")                       #"Choose a number from 1 to 50"
        except:
            print("")
    if ghicire == numar:                                                     #If your number = the random number, then:
        alegeriFolosite = str(alegeriFolosite)                               #The program gets the number of your tries
        print(f"{green} ->> Ai ghicit numărul din {alegeriFolosite} încercări.")  # "You've guessed the number in 'X' tries"
        if alegeriFolosite == 1:                        #If usedGuesses = 1, then:
            print(f"{green} > Felicitări, ai ghicit din prima! <")           #"Congrulations, you've guessed from the first try"
        break
    if ghicire != numar:                                                     #If your number is not equal to the random number, then:
        alegeriFolosite = str(alegeriFolosite)                               #Get number of tries
        print(f"{red} -> Ai depașit numărul de încercări :(")                #"You've ran out of guesses"
        time.sleep(.8)
        print(f"-> Numărul era: {blackbg}{cyan}{str(numar)} \n {endline}")   #"The random number was: 'X'"
        time.sleep(1.4)
        print(f"{red} > GAME OVER! <")
        break