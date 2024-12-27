while True:
    try:
        numberOfWrestlers = int(
            input("How many wrestlers are at Sacrifice?\n"))

        if numberOfWrestlers < 2:
            print(
                "Error: Not enough wrestlers for Scott Steiner and Samoa Joe to be at Sacrifice."
            )
            continue
        break
    except ValueError:
        print("Error: Please enter a valid number.")

while True:
    userInput = input(
        "Are you a genetic freak and not normal? (y/n)\n").strip().lower()

    if userInput == "y":
        geneticFreak = True
        break
    elif userInput == "n":
        geneticFreak = False
        break
    else:
        print("Error: Invalid input. Please enter 'yes' or 'no'.")

while True:
    userInput = input(
        "Is Samoa Joe a genetic freak and not normal? (y/n)\n").strip(
        ).lower()

    if userInput == "y":
        samoaJoeGeneticFreak = True
        break
    elif userInput == "n":
        samoaJoeGeneticFreak = False
        break
    else:
        print("Error: Invalid input. Please enter 'y' or 'n'.")

kurtAngleInTheMix = False

while numberOfWrestlers > 2:
    userInput = input("Is Kurt Angle in the mix? (y/n)\n").strip().lower()

    if userInput == "y":
        kurtAngleInTheMix = True
        break
    elif userInput == "n":
        kurtAngleInTheMix = False
        break
    else:
        print("Error: Invalid input. Please enter 'y' or 'n'.")

kurtAngleIsGonnaTry = False
if kurtAngleInTheMix:
    while True:

        userInput = input(
            "Is Kurt Angle even gonna try? (y/n)\n").strip().lower()
        if userInput == "y":
            kurtAngleIsGonnaTry = True
            break
        elif userInput == "n":
            kurtAngleIsGonnaTry = False
            break
        else:
            print("Error: Invalid input. Please enter 'y' or 'n'.")

chancesOfWinning = 100 / numberOfWrestlers
samoaJoeChancesOfWinning = chancesOfWinning

if geneticFreak:
    chancesOfWinning += 25
    samoaJoeChancesOfWinning -= 25

if samoaJoeGeneticFreak:
    chancesOfWinning -= 25
    samoaJoeChancesOfWinning += 25

if kurtAngleInTheMix and not kurtAngleIsGonnaTry:
    chancesOfWinning += 100 / numberOfWrestlers

chanceToAdd = 100 / numberOfWrestlers

if geneticFreak and not samoaJoeGeneticFreak:
    chanceToAdd += 0.5 * chanceToAdd

if samoaJoeGeneticFreak and not geneticFreak:
    chanceToAdd -= 0.5 * chanceToAdd

chancesOfWinning += chanceToAdd
print(f"\nChances of winning at Sacrifice: {chancesOfWinning:.2f}%")
print(f"Samoa Joe's chances of winning at Sacrifice: {samoaJoeChancesOfWinning:.2f}%")
if kurtAngleInTheMix:
    print(f"Kurt Angle's chances of winning at Sacrifice: {(100 - chancesOfWinning - samoaJoeChancesOfWinning):.2f}%")

if chancesOfWinning > 100:
    print("\nThe numbers don’t lie, and they spell disaster for you at Sacrifice!")
  
