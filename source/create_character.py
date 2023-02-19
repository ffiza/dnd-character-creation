from player import Character
from system import System
import logging
logging.basicConfig(format="%(levelname)s:%(message)s",
                    level=logging.DEBUG)


def create_character() -> Character:
    """
    This method uses user input to create a character with given
    characteristics and returns an instance of the Player class.

    Returns
    -------
    Character
        The character.
    """
    system = System()

    name = input("\nEnter character name: ")
    logging.debug(f"Character is named {name}.")

    class_prompt = "\nSelect character class:\n"
    for i in range(len(system.classes)):
        class_prompt += f"\t[{i}] {system.classes[i]}\n"
    char_class_input = int(input(class_prompt))
    char_class = system.classes[char_class_input]
    logging.debug(f"{name} is now a {char_class}!")

    level = int(input("\nEnter character level: "))
    logging.debug(f"{name} is now level {level}!")

    background_prompt = "\nSelect character background:\n"
    for i in range(len(system.backgrounds)):
        background_prompt += f"\t[{i}] {system.backgrounds[i]}\n"
    background_input = int(input(background_prompt))
    background = system.backgrounds[background_input]
    logging.debug(f"{name} is now a {background}!")

    race_prompt = "\nSelect your character's race:\n"
    for i in range(len(system.races)):
        race_prompt += f"\t[{i}] {system.races[i]}\n"
    race_input = int(input(race_prompt))
    race = system.races[race_input]
    logging.debug(f"{name} is now a {race}!")

    # TODO: Add functionality for the user to change any option at the end.

    return Character(name, char_class, level, background, race, )


if __name__ == '__main__':
    create_character()
