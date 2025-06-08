def get_integer_input(prompt, error_message):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print(error_message)


def get_yes_no_input(prompt, error_message):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == "y":
            return True
        elif user_input == "n":
            return False
        else:
            print(error_message)


def main():
    number_of_wrestlers = get_integer_input("How many wrestlers are at Sacrifice?\n", "Error: Please enter a valid number.")

    if number_of_wrestlers < 2:
        print("Error: Not enough wrestlers for Scott Steiner and Samoa Joe to be at Sacrifice.")
        return

    genetic_freak = get_yes_no_input("Are you a genetic freak and not normal? (y/n)\n", "Error: Invalid input. Please enter 'y' or 'n'.")

    samoa_joe_genetic_freak = get_yes_no_input("Is Samoa Joe a genetic freak and not normal? (y/n)\n", "Error: Invalid input. Please enter 'y' or 'n'.")

    kurt_angle_in_the_mix = number_of_wrestlers > 2 and get_yes_no_input("Is Kurt Angle in the mix? (y/n)\n", "Error: Invalid input. Please enter 'y' or 'n'.")

    kurt_angle_is_gonna_try = False
    if kurt_angle_in_the_mix:
        kurt_angle_is_gonna_try = get_yes_no_input("Is Kurt Angle even gonna try? (y/n)\n", "Error: Invalid input. Please enter 'y' or 'n'.")

    chances_of_winning = 100 / number_of_wrestlers
    samoa_joe_chances_of_winning = chances_of_winning

    if genetic_freak:
        chances_of_winning += 25
        samoa_joe_chances_of_winning -= 25

    if samoa_joe_genetic_freak:
        chances_of_winning -= 25
        samoa_joe_chances_of_winning += 25

    if kurt_angle_in_the_mix and not kurt_angle_is_gonna_try:
        chances_of_winning += 100 / number_of_wrestlers

    chance_to_add = 100 / number_of_wrestlers

    if genetic_freak and not samoa_joe_genetic_freak:
        chance_to_add += 0.5 * chance_to_add

    if samoa_joe_genetic_freak and not genetic_freak:
        chance_to_add -= 0.5 * chance_to_add

    chances_of_winning += chance_to_add

    print(f"\nChances of winning at Sacrifice: {chances_of_winning:.2f}%")
    print(f"Samoa Joe's chances of winning at Sacrifice: {samoa_joe_chances_of_winning:.2f}%")

    if kurt_angle_in_the_mix:
        kurt_angle_chances_of_winning = 100 - chances_of_winning - samoa_joe_chances_of_winning
        print(f"Kurt Angle's chances of winning at Sacrifice: {kurt_angle_chances_of_winning:.2f}%")

    if chances_of_winning > 100:
        print("\nThe numbers don’t lie, and they spell disaster for you at Sacrifice!")

if __name__ == "__main__":
    main()
