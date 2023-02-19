from system import System


class Character:
    def __init__(self, name: str,
                 char_class: str,
                 level: int,
                 background: str,
                 race: str,
                 alignment: str,
                 stats: dict,
                 ability_scores: dict,
                 proficiencies: dict):

        self.name: str = name
        self.char_class: str = char_class
        self.level: int = level
        self.background: str = background
        self.race: str = race
        self.alignment: str = alignment

        system = System()
        self.prof_bonus: int = system.calc_prof_bonus(self.level)

        self.ability_scores: dict = ability_scores
        self.ability_modifiers: dict = system.calc_ability_modifiers(
            self.ability_scores)

        self.proficiencies: dict = proficiencies

        # Determine saving throws
        self.saving_throws: dict = dict()
        for ability in system.abilities:
            bonus: int = 0
            if ability in self.proficiencies["Saving Throws"]:
                bonus = self.prof_bonus
            self.saving_throws[ability] = self.ability_modifiers[ability] \
                + bonus

        # Determine skills
