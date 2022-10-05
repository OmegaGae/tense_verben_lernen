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
import tkinter as tk

from typing import Dict, List
from lib.edit.editfile import Editfile
from lib.edit import STARKE_UNREGELMEASSIE
from lib.constant_values import TenseKey
from lib.windows import (
    GamePresentationTemplate,
    GamePageTemplate,
    GameFailedTemplate,
    GameSuccessTemplate,
    GameConclusionTemplate,
    check_input,
)


class HandlerTenseVerbs:
    def __init__(
        self, file_name: str = STARKE_UNREGELMEASSIE, max_game: int = 20
    ) -> None:
        """
        :param file_name: Name of the file to import
        :param max_game: Maximum game possible to play"""

        check_input([(file_name, str), (max_game, int)])

        self.file_name = file_name
        self.max_game = max_game
        self._file_to_edit = Editfile(self.file_name)
        # think about switch from list to numpy array (1.22.4) for perform in the future...
        # python: 3.7 -> 3.8.10 or 3.8.14 (3.8 lowest python sw vs supported by numpy)
        self._verbs_list = self._file_to_edit.read_txt()
        self._length_verbs_list = len(self._verbs_list)
        self._random_numbers = self._get_random_numbers()
        self._not_used_verbs = self._get_game_verbs()
        self._used_verbs = []

    def _get_random_numbers(self) -> List[int]:
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

        if not self._not_used_verbs:  # check if list empty
            return dict()  # empty dict

        _tense_verb = self._not_used_verbs.pop()
        split_tense_verb = _tense_verb.split()
        self._used_verbs.append(_tense_verb)

        return {
            TenseKey.INFINITIVE: split_tense_verb[0],
            TenseKey.THIRD_FORM: split_tense_verb[1],
            TenseKey.PRETERITE: split_tense_verb[2],
            TenseKey.PERFECT: split_tense_verb[3] + " " + split_tense_verb[4],
            TenseKey.LEVEL: split_tense_verb[5],
        }


class PlayerScore:
    def __init__(self, score: int) -> None:
        """:param score: player score"""
        self._current_score = score

    @property
    def current_score(self):
        return self._current_score

    @property.setter
    def current_score(self, score):
        if not isinstance(score, int):
            # add log warning -> wrong score type set
            self._current_score = self._current_score
        if score < 0 or score > 20:
            # add log warning -> wrong range
            self._current_score = self._current_score
        self._current_score = score


class VerbenLernenApp:
    """Game class."""

    def __init__(
        self, file_name: str = STARKE_UNREGELMEASSIE, max_game: int = 20
    ) -> None:

        check_input([(file_name, str), (max_game, int)])
        self._root = tk.Tk()
        self._root.title("VerbenLernenApp")
        self._root.geometry("550x500")
        self._root.resizable(0, 0)  # make sure full screen is not availabe
        self.file_name = file_name
        self.max_game = max_game
        self._reset()

    def start(self):
        """Launch the game"""
        self.presentation_page.template_launcher()

    def _reset(self):
        """Set object or attributes to their default state"""

        self._verb_to_find = self.verbs_handler.select_verb()

        self.verbs_handler = HandlerTenseVerbs(self.file_name, self.max_game)
        self.player_score = PlayerScore(score=0)
        self.conclusion_page = GameConclusionTemplate(self._root, self._root.quit())
        self.game_pages = GamePageTemplate(
            self._root, self.choose_failed_or_success_page()
        )
        self.fail_page = GameFailedTemplate(
            self._root, self.choose_game_or_conclusion_page()
        )
        self.success_page = GameSuccessTemplate(
            self._root, self.choose_game_or_conclusion_page()
        )
        self.presentation_page = GamePresentationTemplate(
            self._root,
            self.game_pages.template_launcher(self._verb_to_find),
        )

    def choose_failed_or_success_page(self):
        """Choose either to launch failure page or success page"""
        if self.validate_user_input():
            self.player_score.current_score = self.player_score.current_score + 1
            return self.success_page.template_launcher()

        self.player_score.current_score = self.player_score.current_score
        return self.fail_page.template_launcher()

    def choose_game_or_conclusion_page(self):
        """Choose either to go to game page or conclusion page"""
        self._verb_to_find = self.verbs_handler.select_verb()

        if len(self.verbs_handler._used_verbs) == self.max_game:
            return self.conclusion_page.template_launcher(
                self.player_score.current_score
            )

        return self.game_pages.template_launcher(
            self._verb_to_find,
            len(self.verbs_handler._not_used_verbs),
            self.player_score.current_score,
        )  # missing frame for score

    def validate_user_input(self) -> bool:
        """Check user entries, and return True if all entries are correct"""

        if (
            self.game_pages.imperfect_entried == self._verb_to_find[TenseKey.PERFECT]
            and self.game_pages.preterite_entried
            == self._verb_to_find[TenseKey.PRETERITE]
        ):
            return True
        return False


if __name__ == "__main__":
    verbs = HandlerTenseVerbs()
    print(verbs.select_verb())
