# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import random
import tkinter as tk
from tkinter import ttk

from typing import Dict, List
from edit.editfile import Editfile
from edit import STARKE_UNREGELMEASSIE
from constant_values import (
    TenseKey,
    TkFilling,
    TkRelief,
    TkSide,
    VerbenLernenEnum,
    VlColors,
    StyleNamesCustomized,
)
from windows import (
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
            TenseKey.INFINITIVE.value: _split_tense_verb[0],
            TenseKey.THIRD_FORM.value: _split_tense_verb[1],
            TenseKey.PRETERITE.value: _split_tense_verb[2],
            TenseKey.PERFECT.value: _split_tense_verb[3] + " " + _split_tense_verb[4],
            TenseKey.LEVEL.value: _split_tense_verb[5],
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
        """TO DO"""

        check_input([(file_name, str), (max_game, int)])

        tk.Tk.__init__(self)

        self.title("VerbenLernenApp")
        self.geometry("550x500")
        self.resizable(0, 0)  # make sure full screen is not availabe
        self.file_name = file_name
        self.max_game = max_game
        self._current_frame = None
        self._previous_frame_name = None
        self._is_first_switch = True

        self.frames_container = ttk.Frame(self)
        self.frames_container.config(relief=TkRelief.GROOVE)
        self.frames_container.pack(side=TkSide.TOP, fill=TkFilling.BOTH, expand=True)

        self.configure_style(self.frames_container)
        self._reset()

    def switch_frame(self, frame_class):
        """TO DO"""
        if self._current_frame is not None:
            # TO DO: log which frame was destroyed
            self._current_frame.destroy()
            self.page_creator()

        self._current_frame = frame_class
        # TO DO : log current frame
        if self._is_first_switch:  # to launch presentation page
            self._is_first_switch = False
            self._previous_frame_name = VerbenLernenEnum.START_PG.value
            self._current_frame.template_launcher()

    def switch_to_game_page(self):
        """TO DO"""
        self.switch_frame(self.game_pages)
        self._previous_frame_name = VerbenLernenEnum.GAME_PG.value
        self._current_frame.template_launcher(
            self._verb_to_find[TenseKey.INFINITIVE],
            len(self.verbs_handler._not_used_verbs),
            self.player_score.current_score,
        )

    def configure_style(self, frame):
        """Customized ttk widgets style
        :param frame: Reference frame which style will be applyed"""
        style = ttk.Style(frame)
        style.configure("TFrame", background=VlColors.blue_grey)

        style.configure(
            StyleNamesCustomized.tframe,
            background=VlColors.blue_grey,
        )
        style.configure(
            StyleNamesCustomized.tlabel,
            background=VlColors.blue_grey,
            foreground=VlColors.dark,
        )
        style.configure(
            StyleNamesCustomized.tlabel_calibri10,
            background=VlColors.blue_grey,
            foreground=VlColors.dark,
            font=("Calibri", "12", "bold"),
        )
        style.configure(
            StyleNamesCustomized.tlabel_arial_black10,
            background=VlColors.blue_grey,
            foreground=VlColors.dark,
            font=("Arial Black", "10"),
        )
        style.configure(
            StyleNamesCustomized.tlabel_arial_black18,
            background=VlColors.blue_grey,
            foreground=VlColors.dark,
            font=("Arial Black", "18"),
        )

    def page_creator(self):
        """Create object to their default state.
        Should be used after destroying a page"""

        if self._previous_frame_name == VerbenLernenEnum.END_PG.value:
            self.conclusion_page = GameConclusionTemplate(
                self.frames_container, self.quit
            )

        elif self._previous_frame_name == VerbenLernenEnum.GAME_PG.value:
            self.game_pages = GamePageTemplate(
                self.frames_container, self.choose_failed_or_success_page
            )

        elif self._previous_frame_name == VerbenLernenEnum.FAIL_PG.value:
            self.fail_page = GameFailedTemplate(
                self.frames_container, self.choose_game_or_conclusion_page
            )

        elif self._previous_frame_name == VerbenLernenEnum.SUCCESS_PG.value:
            self.success_page = GameSuccessTemplate(
                self.frames_container, self.choose_game_or_conclusion_page
            )

        elif self._previous_frame_name == VerbenLernenEnum.START_PG.value:
            self.presentation_page = GamePresentationTemplate(
                self.frames_container,
                func=self.switch_to_game_page,
            )
        else:
            pass

    def _reset(self):
        """Set object or attributes to their default state"""

        self.verbs_handler = HandlerTenseVerbs(self.file_name, self.max_game)
        self._verb_to_find = self.verbs_handler.select_verb()

        self.player_score = PlayerScore(score=0)

        self.conclusion_page = GameConclusionTemplate(self.frames_container, self.quit)

        self.game_pages = GamePageTemplate(
            self.frames_container, self.choose_failed_or_success_page
        )
        self.fail_page = GameFailedTemplate(
            self.frames_container, self.choose_game_or_conclusion_page
        )
        self.success_page = GameSuccessTemplate(
            self.frames_container, self.choose_game_or_conclusion_page
        )
        self.presentation_page = GamePresentationTemplate(
            self.frames_container,
            func=self.switch_to_game_page,
        )

        # start game
        self.switch_frame(self.presentation_page)

    def choose_failed_or_success_page(self):
        """Choose either to launch failure page or success page"""

        if self.validate_user_input():
            self.player_score.current_score = self.player_score.current_score + 1
            self.switch_frame(self.success_page)
            self._previous_frame_name = VerbenLernenEnum.SUCCESS_PG.value
            self.success_page.template_launcher(self._verb_to_find)
        else:
            self.player_score.current_score = self.player_score.current_score
            self.switch_frame(self.fail_page)
            self._previous_frame_name = VerbenLernenEnum.FAIL_PG.value
            self.fail_page.template_launcher(self._verb_to_find)

    def choose_game_or_conclusion_page(self):
        """Choose either to go to game page or conclusion page"""

        self._verb_to_find = self.verbs_handler.select_verb()

        if len(self.verbs_handler._used_verbs) == self.max_game:
            self.switch_frame(self.conclusion_page)
            self._previous_frame_name = VerbenLernenEnum.END_PG.value
            self.conclusion_page.template_launcher(self.player_score.current_score)
        else:
            self.switch_frame(self.game_pages)
            self._previous_frame_name = VerbenLernenEnum.GAME_PG.value
            self.game_pages.template_launcher(
                self._verb_to_find[TenseKey.INFINITIVE],
                len(self.verbs_handler._not_used_verbs),
                self.player_score.current_score,
            )

    def validate_user_input(self) -> bool:
        """Check user entries, and return True if all entries are correct"""

        if (
            self.game_pages.imperfect_entried.get()
            == self._verb_to_find[TenseKey.PERFECT.value]
            and self.game_pages.preterite_entried.get()
            == self._verb_to_find[TenseKey.PRETERITE.value]
        ):
            return True
        return False


if __name__ == "__main__":
    game_app = VerbenLernenApp()
    game_app.mainloop()
