# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys
from pathlib import Path
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
    submit_text,
)
from tkinter.scrolledtext import ScrolledText


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

        self.pack(fill=tk.X, pady=50)  # pack frame completly in parent (size)

    def scrowling_text(self, width: Optional[int] = None, height: Optional[int] = None):
        """
        Print a text in a scrowling text box.

        :param width: define the scrowling text box width. Default set to None
        :param heigth: define the scrowling text box heigth. Default set to None

        """
        scrowling_text = ScrolledText(self, width=width, height=height)
        scrowling_text.insert(tk.END, presentation_text)
        scrowling_text.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5)
        scrowling_text.configure(state=tk.DISABLED)

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

        # frames creation
        frame_one = ttk.Frame(self, relief=tk.RIDGE)
        frame_one.pack(fill=tk.X, side=tk.TOP, pady=10)
        frame_two = ttk.Frame(self, relief=tk.RIDGE)
        frame_two.pack(fill=tk.X, pady=40)
        frame_three = ttk.Frame(self, relief=tk.RIDGE)
        frame_three.pack(fill=tk.X)
        frame_four = ttk.Frame(self, relief=tk.RIDGE)
        frame_four.pack(fill=tk.X, pady=15)
        frame_four = ttk.Frame(self, relief=tk.RIDGE)
        frame_four.pack(fill=tk.X)
        frame_five = ttk.Frame(self, relief=tk.RIDGE)
        frame_five.pack(fill=tk.X, pady=10, side=tk.BOTTOM)
        frame_seven = ttk.Frame(self, relief=tk.RIDGE)
        frame_seven.pack(fill=tk.X, side=tk.BOTTOM, pady=10)
        frame_eight = ttk.Frame(self, relief=tk.RIDGE)
        frame_eight.pack(fill=tk.X, side=tk.BOTTOM, pady=75)

        # define variable
        imperfect_entried = tk.StringVar()
        preterite_entried = tk.StringVar()

        label_game = tk.Label(frame_one, text=game_title, height=1, relief=tk.RIDGE)
        label_game.pack(fill=tk.X, pady=5)

        label_infinitive = ttk.Label(
            frame_two, text=infinitive_text, width=40, relief=tk.RIDGE, anchor=tk.E
        )
        label_infinitive.pack(side=tk.LEFT, padx=10)

        text_infinite = tk.Text(frame_two, height=1, width=30)
        text_infinite.insert(tk.END, "infinitve verb")
        text_infinite.config(state=tk.DISABLED)
        text_infinite.pack(side=tk.RIGHT, padx=10)
        text_infinite.focus()

        label_imperfect = ttk.Label(
            frame_three,
            text=imperfect_tense_text,
            width=35,
            anchor=tk.CENTER,
            relief=tk.RIDGE,
        )
        label_imperfect.pack(side=tk.LEFT, padx=10, ipadx=5)

        label_preterite = ttk.Label(
            frame_three,
            text=preterite_tense_text,
            anchor=tk.CENTER,
            width=35,
            relief=tk.RIDGE,
        )
        label_preterite.pack(side=tk.RIGHT, padx=10, ipadx=5)

        entry_imperfect = ttk.Entry(
            frame_four,
            textvariable=imperfect_entried,
            width=35,
        )
        entry_imperfect.pack(side=tk.LEFT, padx=10, ipadx=5)
        entry_imperfect.focus_get()

        entry_preterite = ttk.Entry(
            frame_four,
            text=preterite_entried,
            width=35,
        )
        entry_preterite.pack(side=tk.RIGHT, padx=10, ipadx=5)
        entry_preterite.focus_get()

        left_time = ttk.Progressbar(
            frame_five, orient=tk.HORIZONTAL, mode="determinate"
        )
        left_time.start(395)  # 0,395 s
        left_time.step(1000.0)
        left_time.pack(fill=tk.X, padx=10, pady=5)

        left_time.after(40000, left_time.stop)  # 40 s == normal mode

        label_preterite = ttk.Label(
            frame_seven,
            text=remain_verbs_text,
            anchor=tk.CENTER,
            width=35,
            relief=tk.RIDGE,
        )
        label_preterite.pack(side=tk.LEFT, padx=10, ipadx=5)

        submit_button = ttk.Button(frame_eight, text=submit_text, command=root.quit)
        submit_button.pack(anchor=tk.CENTER)


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
