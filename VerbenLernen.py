# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
 # @ Author: OmegaGae
 # @ Create Time: 2022-03-03 11:20:51
 # @ Modified by: OmegaGae
 # @ Modified time: 2022-03-03 12:11:31
 # @ Description: Ready for work !!
 """

import random

from typing import Dict, List
from lib.edit.editfile import Editfile
from lib.edit import STARKE_UNREGELMEASSIE
from lib.constant_values import TenseKey


class HandlerTenseVerbs:
    def __init__(
        self, file_name: str = STARKE_UNREGELMEASSIE, max_game: int = 20
    ) -> None:
        """
        :param file_name: Name of the file to import
        :param max_game: Maximum game possible to play"""

        self.file_name = file_name
        self.max_game = max_game
        self._file_to_edit = Editfile(self.file_name)
        # think about switch from list to numpy array (1.22.4) for perform in the future...
        # python: 3.7 -> 3.8.10 or 3.8.14 (3.8 lowest python sw vs supported by numpy)
        self._verbs_list = self._file_to_edit.read_txt()
        self._length_verbs_list = len(self._verbs_list)
        self._random_numbers = self.get_random_numbers()
        self._not_use_verbs = self._get_game_verbs()
        self._used_verbs = []

    def get_random_numbers(self) -> List[int]:
        """Generate a list of number which represents the tense verbs to play with"""
        return random.sample(range(self._length_verbs_list), self.max_game)

    def _get_game_verbs(self) -> List[str]:
        """Get the tense verbs to be used during the game.
        Only generated one time, for each HandlerTenseVerbs object instanciation"""

        return [self._verbs_list[ind] for ind in self._random_numbers]

    def select_verb(self) -> Dict:
        """Select random tense verbs in a list of tense verbs and order it in
        a dictionary with the corresponding key.
        "Fahren","Fährt", "Fuhr","ist gefahren", "A2"
        e.g:
            dict =
                {
                    "infinitive": "Fahren"
                    "verb singular third form": "Fährt"
                    "preterite": "Fuhr"
                    "perfect": "ist gefahren"
                    "level": "A2"
                }
        return tense_verb (dict)"""

        if not self._not_use_verbs:  # check if list empty
            return dict()  # empty dict

        tense_verb = self._not_use_verbs.pop()
        split_tense_verb = tense_verb.split()
        self._used_verbs.append(tense_verb)

        return {
            TenseKey.INFINITIVE: split_tense_verb[0],
            TenseKey.THIRD_FORM: split_tense_verb[1],
            TenseKey.PRETERITE: split_tense_verb[2],
            TenseKey.PERFECT: split_tense_verb[3] + " " + split_tense_verb[4],
            TenseKey.LEVEL: split_tense_verb[5],
        }


class VerbenLernenApp:
    """Game class."""

    def __init__(self) -> None:
        pass

    def start(self):
        pass

    def reset(self):
        pass


if __name__ == "__main__":
    verbs = HandlerTenseVerbs()
    print(verbs.select_verb())
