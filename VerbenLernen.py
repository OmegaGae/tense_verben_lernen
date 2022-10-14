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
        _split_tense_verb = _tense_verb.split()
        self._used_verbs.append(_tense_verb)

        return {
            TenseKey.INFINITIVE: _split_tense_verb[0],
            TenseKey.THIRD_FORM: _split_tense_verb[1],
            TenseKey.PRETERITE: _split_tense_verb[2],
            TenseKey.PERFECT: _split_tense_verb[3] + " " + _split_tense_verb[4],
            TenseKey.LEVEL: _split_tense_verb[5],
        }


class PlayerScore:
    def __init__(self, score: int) -> None:
        """:param score: player score"""
        self._current_score = score

    @property
    def current_score(self):
        return self._current_score

    @current_score.setter
    def current_score(self, score):
        if not isinstance(score, int):
            # add log warning -> wrong score type set
            self._current_score = self._current_score
        if score < 0 or score > 20:
            # add log warning -> wrong range
            self._current_score = self._current_score
        self._current_score = score


class VerbenLernenApp(tk.Tk):
    """Game class."""

    def __init__(
        self, file_name: str = STARKE_UNREGELMEASSIE, max_game: int = 20
    ) -> None:

        check_input([(file_name, str), (max_game, int)])

        super().__init__()

        self.title("VerbenLernenApp")
        self.geometry("550x500")
        self.resizable(0, 0)  # make sure full screen is not availabe
        self.file_name = file_name
        self.max_game = max_game
        self.reset_trigger = False
        self._reset()

    def start(self):
        self.presentation_page.template_launcher()

    def _reset(self):
        """Set object or attributes to their default state"""
        self.reset_trigger = True
        self.verbs_handler = HandlerTenseVerbs(self.file_name, self.max_game)
        self._verb_to_find = self.verbs_handler.select_verb()

        self.player_score = PlayerScore(score=0)
        self.conclusion_page = GameConclusionTemplate(self, self.quit)

        self.game_pages = GamePageTemplate(self, self.choose_failed_or_success_page())
        self.fail_page = GameFailedTemplate(self, self.choose_game_or_conclusion_page())
        self.success_page = GameSuccessTemplate(
            self, self.choose_game_or_conclusion_page()
        )
        self.presentation_page = GamePresentationTemplate(
            self,
            func=self.game_pages.template_launcher(
                self._verb_to_find[TenseKey.INFINITIVE],
                len(self.verbs_handler._not_used_verbs),
                self.player_score.current_score,
            ),
        )
        self.reset_trigger = False

    def choose_failed_or_success_page(self):
        """Choose either to launch failure page or success page"""
        # init: if reset trigger
        if self.reset_trigger:
            # do nothing if called from reset
            return

        if self.validate_user_input():
            self.player_score.current_score = self.player_score.current_score + 1
            self.success_page.tkraise()  # switch to success frame
            return self.success_page.template_launcher()

        self.player_score.current_score = self.player_score.current_score
        self.fail_page.tkraise()  # switch to failed frame
        return self.fail_page.template_launcher()

    def choose_game_or_conclusion_page(self):
        """Choose either to go to game page or conclusion page"""

        # init: if reset trigger
        if self.reset_trigger:
            # do nothing if call from reset
            return

        self._verb_to_find = self.verbs_handler.select_verb()

        if len(self.verbs_handler._used_verbs) == self.max_game:
            self.conclusion_page.tkraise()  # switch to conclusion frame
            return self.conclusion_page.template_launcher(
                self.player_score.current_score
            )

        self.game_pages.reset()
        self.game_pages.tkraise()  # switch to game frame
        return self.game_pages.template_launcher(
            self._verb_to_find[TenseKey.INFINITIVE],
            len(self.verbs_handler._not_used_verbs),
            self.player_score.current_score,
        )

    def validate_user_input(self) -> bool:
        """Check user entries, and return True if all entries are correct"""

        # init: if reset trigger
        if self.reset_trigger:
            # do nothing if called from reset
            return

        if (
            self.game_pages.imperfect_entried == self._verb_to_find[TenseKey.PERFECT]
            and self.game_pages.preterite_entried
            == self._verb_to_find[TenseKey.PRETERITE]
        ):
            return True
        return False


if __name__ == "__main__":
    game_app = VerbenLernenApp()
    game_app.start()
    game_app.mainloop()
