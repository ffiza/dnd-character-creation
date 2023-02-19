import unittest
import sys
import os
sys.path.append(os.path.abspath("./source"))
from system import System


class TestSystemMethods(unittest.TestCase):
    def test_mod_calc(self):
        system = System()
        self.assertEqual(-5, system.calc_modifier(1))
        self.assertEqual(-4, system.calc_modifier(2))
        self.assertEqual(-4, system.calc_modifier(3))
        self.assertEqual(-3, system.calc_modifier(4))
        self.assertEqual(-3, system.calc_modifier(5))
        self.assertEqual(-2, system.calc_modifier(6))
        self.assertEqual(-2, system.calc_modifier(7))
        self.assertEqual(-1, system.calc_modifier(8))
        self.assertEqual(-1, system.calc_modifier(9))
        self.assertEqual(0, system.calc_modifier(10))
        self.assertEqual(0, system.calc_modifier(11))
        self.assertEqual(1, system.calc_modifier(12))
        self.assertEqual(1, system.calc_modifier(13))
        self.assertEqual(2, system.calc_modifier(14))
        self.assertEqual(2, system.calc_modifier(15))
        self.assertEqual(3, system.calc_modifier(16))
        self.assertEqual(3, system.calc_modifier(17))
        self.assertEqual(4, system.calc_modifier(18))
        self.assertEqual(4, system.calc_modifier(19))
        self.assertEqual(5, system.calc_modifier(20))

    def test_prof_bonus_calc(self):
        system = System()
        self.assertEqual(2, system.calc_prof_bonus(3))
        self.assertEqual(3, system.calc_prof_bonus(6))
        self.assertEqual(4, system.calc_prof_bonus(10))
        self.assertEqual(5, system.calc_prof_bonus(14))
        self.assertEqual(6, system.calc_prof_bonus(19))

    def test_ability_mod_calc(self):
        system = System()
        ability_scores = {"Strength": 10,
                          "Dexterity": 15,
                          "Constitution": 14,
                          "Intelligence": 13,
                          "Wisdom": 12,
                          "Charisma": 8}
        ability_modifiers = {"Strength": 0,
                             "Dexterity": 2,
                             "Constitution": 2,
                             "Intelligence": 1,
                             "Wisdom": 1,
                             "Charisma": -1}
        self.assertDictEqual(ability_modifiers,
                             system.calc_ability_modifiers(ability_scores))


if __name__ == '__main__':
    unittest.main()
