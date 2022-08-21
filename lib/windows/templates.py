# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys
from pathlib import Path
from turtle import width
from typing import Optional

path_test = Path(__file__).resolve().parents[2]
sys.path.append(str(path_test))

import tkinter as tk
from tkinter import ttk
from lib.edit.game_text import (
    presentation_text,
    start_text,
    game_title,
    infinitive_text,
    imperfect_tense_text,
    preterite_tense_text,
    next_text,
    remain_verbs_text,
    valide_text,
)
from tkinter.scrolledtext import ScrolledText
from tkinter.constants import END


class DisplayTextFrame:

    ...


class ButtonsFrame:
    ...


class InputFrame:
    ...


class PictureFrame:
    ...


class GamePresentationTemplate(ttk.Frame):
    """
    Template for game presentation
    """

    def __init__(self, parent):
        """
        Template game presentation.
        Find here the presentation and the rules of the game
        displayed as a scrowling text. After finishing reading,
        you can go to the next page by clicking onto the next button.

        :param parent: root widget
        """
        self.parent = parent
        super().__init__(parent)
        self.pack()  # pack frame completly in parent (size)

    def scrowling_text(self, width: Optional[int] = None, height: Optional[int] = None):
        """
        Print a text in a scrowling text box.

        :param width: define the scrowling text box width. Default set to None
        :param heigth: define the scrowling text box heigth. Default set to None

        """
        scrowling_text = ScrolledText(self, width=width, height=height)
        scrowling_text.insert(END, presentation_text)
        scrowling_text.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5)
        scrowling_text.configure(state=tk.DISABLED)
        scrowling_text.focus_set()

    def start_button(self):
        """
        create a start button for the frame
        """
        start_button = ttk.Button(self, text=start_text, command=lambda: self.quit())
        start_button.pack(side=tk.BOTTOM, ipadx=5, ipady=5, pady=35)
        start_button.focus_set()


class GamePageTemplate(ttk.Frame):
    """
    Scrowling game template
    """

    def __init__(self, parent: tk.Tk):
        """
        Template game presentation.
        Find here the presentation and the rules of the game
        displayed as a scrowling text. After finishing reading,
        you can go to the next page by clicking onto the next button.

        :param parent: root widget type Tk
        """
        self.parent = parent

        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)

        # define weigth of column cell
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        label_game = tk.Label(self, text=game_title)
        label_game.grid(column=1, row=0, pady=5, columnspan=2, sticky=tk.NS)

        label_infinitive = tk.Label(self, text=infinitive_text, anchor=tk.W)
        label_infinitive.grid(column=0, row=2, columnspan=2, sticky=tk.NS)

        label_imperfect = tk.Label(self, text=imperfect_tense_text, anchor=tk.W)
        label_imperfect.grid(column=0, row=4, columnspan=2, sticky=tk.NS)

        label_preterite = tk.Label(self, text=preterite_tense_text, anchor=tk.W)
        label_preterite.grid(column=3, row=4, columnspan=2, sticky=tk.W)


class GameSuccessTemplate:
    """
    Template for game success response
    """


class GameFailedTemplate:
    """
    Template for failed response
    """


class GameConclusionTemplate:
    """
    Template for game conclusion
    """


if __name__ == "__main__":
    root = tk.Tk()
    root.title("VerbenLernen")
    root.geometry("550x500")
    root.resizable(0, 0)  # make sure full screen is not availabe
    pr = GamePageTemplate(root)
    # pr.scrowling_text()
    # pr.start_button()
    root.mainloop()
