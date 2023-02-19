from math import floor


class System:
    def __init__(self):
        self.abilities: list = ["Strength",
                                "Dexterity",
                                "Constitution",
                                "Intelligence",
                                "Wisdom",
                                "Charisma"]
        self.skills: list = ["Acrobatics",
                             "Animal Handling",
                             "Arcana",
                             "Athletics",
                             "Deception",
                             "History",
                             "Insight",
                             "Intimidation",
                             "Investigation",
                             "Medicine",
                             "Nature",
                             "Perception",
                             "Performance",
                             "Presuasion",
                             "Religion",
                             "Sleight of Hand",
                             "Stealth",
                             "Survival"]
        self.skill_parents: dict = {"Acrobatics": "Dexterity",
                                    "Animal Handling": "Wisdom",
                                    "Arcana": "Intelligence",
                                    "Athletics": "Strength",
                                    "Deception": "Charisma",
                                    "History": "Intelligence",
                                    "Insight": "Wisdom",
                                    "Intimidation": "Charisma",
                                    "Investigation": "Intelligence",
                                    "Medicine": "Wisdom",
                                    "Nature": "Intelligence",
                                    "Perception": "Wisdom",
                                    "Performance": "Charisma",
                                    "Presuasion": "Charisma",
                                    "Religion": "Intelligence",
                                    "Sleight of Hand": "Dexterity",
                                    "Stealth": "Dexterity",
                                    "Survival": "Wisdom"}
        self.classes: list = ["Barbarian",
                              "Bard",
                              "Cleric",
                              "Druid",
                              "Fighter",
                              "Monk",
                              "Paladin",
                              "Ranger",
                              "Rogue",
                              "Sorcerer",
                              "Warlock",
                              "Wizard"]
        self.races: list = ["Dwarf",
                            "Elf",
                            "Halfling",
                            "Human",
                            "Dragonborn",
                            "Gnome",
                            "Half-Elf",
                            "Half-Orc",
                            "Tiefling"]
        self.backgrounds: list = ["Acolyte",
                                  "Charlatan",
                                  "Criminal/Spy",
                                  "Entertainer",
                                  "Folk Hero",
                                  "Gladiator",
                                  "Guild Artisan",
                                  "Hermit",
                                  "Knight",
                                  "Noble",
                                  "Outlander",
                                  "Pirate",
                                  "Sage",
                                  "Soldier",
                                  "Urchin"]

    @staticmethod
    def calc_modifier(score: int) -> int:
        """
        This method calculated the modifier of a given ability score.

        Parameters
        ----------
        score : int
            The ability score.

        Returns
        -------
        int
            The modifier.
        """
        mod = int(floor((score - 10) / 2))
        return mod

    @staticmethod
    def calc_prof_bonus(level: int) -> int:
        """
        This method calculates the proficiency bonus for a given level.

        Parameters
        ----------
        level : int
            The character level.

        Returns
        -------
        int
            The proficiency bonus.

        Raises
        ------
        ValueError
            If input level is below 1.
        """
        if level >= 17:
            prof_bonus = 6
        elif level >= 13:
            prof_bonus = 5
        elif level >= 9:
            prof_bonus = 4
        elif level >= 4:
            prof_bonus = 3
        elif level >= 1:
            prof_bonus = 2
        else:
            raise ValueError("Level cannot be below 1.")
        return prof_bonus

    def calc_ability_modifiers(self, ability_scores: dict) -> dict:
        """
        This method calculates the ability modifiers for a given dictionary
        of ability scores.

        Parameters
        ----------
        ability_scores : dict
            A dictionary where each key is an ability and each value an
            ability score.

        Returns
        -------
        dict
            A dictionary where each key is an ability and each value an
            ability modifier.
        """
        ability_modifiers: dict = dict()
        for ability in self.abilities:
            ability_modifiers[ability] = self.calc_modifier(
                ability_scores[ability])
        return ability_modifiers
