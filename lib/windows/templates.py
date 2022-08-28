# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys
from pathlib import Path
from typing import Optional, Union, List

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
from lib.constant_values import (
    PackErrors,
    TkMode,
    TkOrientation,
    TkRelief,
    TkAnchorNSticky,
    TkStates,
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


def check_input(value_to_check: Union[tuple, List[tuple]]) -> Union[Exception, None]:
    """Check if inputs have the right instance type

    :param value_to_check: Inputs values to check their type.
    It should be a tuple, e.g (input, expected_type)

    :raise TypeError: Error raised when input type is different from expected type"""

    if isinstance(value_to_check, tuple):
        if not isinstance(value_to_check[0], value_to_check[1]):
            raise TypeError(
                f"Your Input type:{type(value_to_check[0])}, is different from expected input type"
            )

    elif isinstance(value_to_check, list):
        for value in value_to_check:  # value == tuple
            if not isinstance(value[0], value[1]):
                raise TypeError(
                    f"Your Input type:{type(value[0])}, is different from expected input type"
                )

    else:
        raise TypeError(
            f" parameter value_to_check type:{type(value_to_check[0])}, is different from tuple or list"
        )

    return


def create_frame(
    root: ttk.Frame,
    tk_relief: Union[TkRelief, str] = TkRelief.FLAT,
    **pack_options,
) -> ttk.Frame:
    """Create a frame that will be contained in an already existing parent frame
    :param root: Parent frame
    :param tk_relief: Tkinter constant for frame relief. Default set to flat
    :param pack_options: Configuration options to pack the created frame.
    Only pack options are expected.

    :return: frame (ttk.Frame)

    :raise TypeError: Error raised when input type is different from expected type"""

    # check input
    check_input((root, ttk.Frame))

    if not (isinstance(tk_relief, TkRelief) or isinstance(tk_relief, str)):
        raise TypeError(
            f"Your Input type:{type(tk_relief)}, is different from expected input type"
        )

    frame = ttk.Frame(root, relief=tk_relief)
    try:
        frame.pack(
            fill=pack_options.get("fill"),
            side=pack_options.get("side"),
            padx=pack_options.get("padx"),
            pady=pack_options.get("pady"),
            ipadx=pack_options.get("ipadx"),
            ipady=pack_options.get("ipady"),
            anchor=pack_options.get("anchor"),
        )
    except:  # to test
        raise PackErrors

    return frame


def create_label(
    root: ttk.Frame,
    text: str,
    tk_relief: Union[TkRelief, str] = TkRelief.FLAT,
    tk_anchor: Union[TkAnchorNSticky, str] = TkAnchorNSticky.CENTER,
    tk_height: Optional[int] = None,
    tk_width: Optional[int] = None,
    **pack_options,
) -> ttk.Label:
    """Create a label that will be contained in an already existing parent frame

    :param root: Parent frame
    :param text: Label text
    :param tk_relief: Tkinter constant for label relief. Default set to flat
    :param tk_anchor: Tkinter constant for label relief. Default set to center
    :param tk_height: (optional) Height of the label widget
    :param tk_width: (optional) Width of the label widget
    :param pack_options: Configuration options to pack the created label.
    Only pack options are expected.

    :return: tk_label (ttk.Label)

    :raise TypeError: Error raised when input type is different from expected type"""

    # check input
    inputs_to_check = [(root, ttk.Frame), (text, str)]
    check_input(inputs_to_check)

    # add check for size parameter ?

    if not (isinstance(tk_relief, TkRelief) or isinstance(tk_relief, str)):
        raise TypeError(
            f"Your Input type:{type(tk_relief)}, is different from expected input type"
        )

    if not (isinstance(tk_anchor, TkRelief) or isinstance(tk_anchor, str)):
        raise TypeError(
            f"Your Input type:{type(tk_relief)}, is different from expected input type"
        )

    tk_label = ttk.Label(
        root,
        text=text,
        height=tk_height,
        width=tk_width,
        relief=tk_relief,
        anchor=tk_anchor,
    )
    try:
        tk_label.pack(
            fill=pack_options.get("fill"),
            side=pack_options.get("side"),
            padx=pack_options.get("padx"),
            pady=pack_options.get("pady"),
            ipadx=pack_options.get("ipadx"),
            ipady=pack_options.get("ipady"),
        )
    except:  # to test
        raise PackErrors

    return tk_label


def create_text(
    root: ttk.Frame,
    text: str,
    tk_width: int,
    tk_height: int = 1,
    tk_state: Union[TkStates, str] = TkStates.DISABLED,
    **pack_options,
) -> tk.Text:
    """Create a tkinter text that will be contained in an already existing parent frame

    :param root: Parent frame
    :param text: Text to insert into tkinter text widget
    :param tk_width: Width of the text widget
    :param tk_height: Height of the text widget. Default set to 1
    :param tk_state: State of tkinter widget text. Default state set to disabled.
    Disabled for read only, Normal for edit mode.
    :param pack_options: Configuration options to pack the created text.
    Only pack options are expected.

    :return: tk_text (tk.Text)

    :raise TypeError: Error raised when input type is different from expected type"""

    # check input
    inputs_to_check = [
        (root, ttk.Frame),
        (text, str),
        (tk_width, int),
        (tk_height, int),
    ]
    check_input(inputs_to_check)

    if not (isinstance(tk_state, TkStates) or isinstance(tk_state, str)):
        raise TypeError(
            f"Your Input type:{type(tk_state)}, is different from expected input type"
        )

    tk_text = tk.Text(root, height=tk_height, width=tk_width, state=tk_state)
    tk_text.insert(tk.END, text)
    try:
        tk_text.pack(
            fill=pack_options.get("fill"),
            side=pack_options.get("side"),
            padx=pack_options.get("padx"),
            pady=pack_options.get("pady"),
            ipadx=pack_options.get("ipadx"),
            ipady=pack_options.get("ipady"),
            anchor=pack_options.get("anchor"),
        )
    except:  # to test
        raise PackErrors

    return tk_text


def create_entry(
    root: ttk.Frame,
    tk_textvariable: tk.StringVar,
    tk_width: int,
    tk_height: int = 1,
    **pack_options,
) -> tk.Entry:
    """Create a tkinter entry that will be contained in an already existing parent frame

    :param root: Parent frame
    :param tk_textvariable: Catch user input text into this parameter
    :param tk_width: Width of the entry widget
    :param tk_height: Height of the entry widget. Default set to 1
    :param pack_options: Configuration options to pack the created entry.
    Only pack options are expected.

    :return: tk_entry (tk.Entry)

    :raise TypeError: Error raised when input type is different from expected type"""

    # check input
    inputs_to_check = [
        (root, ttk.Frame),
        (tk_textvariable, tk.StringVar),
        (tk_width, int),
        (tk_height, int),
    ]
    check_input(inputs_to_check)

    tk_entry = tk.Entry(
        root, textvariable=tk_textvariable, height=tk_height, width=tk_width
    )
    try:
        tk_entry.pack(
            fill=pack_options.get("fill"),
            side=pack_options.get("side"),
            padx=pack_options.get("padx"),
            pady=pack_options.get("pady"),
            ipadx=pack_options.get("ipadx"),
            ipady=pack_options.get("ipady"),
            anchor=pack_options.get("anchor"),
        )
    except:  # to test
        raise PackErrors

    return tk_entry


def create_progress_bar(
    root: ttk.Frame,
    tk_orientation: Union[TkOrientation, str] = TkOrientation.HORIZONTAL,
    tk_mode: Union[TkMode, str] = TkMode.DETERMINATE,
    interval_time: int = 395,
    incrementation_time: float = 1000.0,
    stop_time: int = 40000,
    callable_function=None,
    tk_length: Optional[int] = None,
    **pack_options,
) -> ttk.Progressbar:
    """Create a tkinter progressbar that will be contained in an already existing parent frame

    :param root: Parent frame
    :param tk_orientation: Set progressbar orientation
    :param tk_mode: Set mode of the progressbar. Default mode set to determinate.
    :param interval_time: Recurrence time for the progressbar to move. Defalut set to 395 ms
    :param incrementation_time: Recurrence time to increment the timer. Default set to 1000.0 ms
    :param stop_time: Time needed to reach to stop the progressbar. Default set to 40000 ms
    :param callable_function: Function to call after reaching the end of the progressbar
    :param tk_length: (Optional) Set progressbar length.
    :param pack_options: Configuration options to pack the created progressbar.
    Only pack options are expected.

    :return: tk_progress_bar (ttk.Progressbar)

    :raise TypeError: Error raised when input type is different from expected type"""

    # check input
    inputs_to_check = [
        (root, ttk.Frame),
        (interval_time, int),
        (incrementation_time, float),
        (stop_time, int),
    ]
    check_input(inputs_to_check)

    if not (
        isinstance(tk_orientation, TkOrientation) or isinstance(tk_orientation, str)
    ):
        raise TypeError(
            f"Your Input type:{type(tk_orientation)}, is different from expected input type"
        )

    if not (isinstance(tk_mode, TkMode) or isinstance(tk_mode, str)):
        raise TypeError(
            f"Your Input type:{type(tk_mode)}, is different from expected input type"
        )

    tk_progress_bar = ttk.Progressbar(
        root, orient=tk_orientation, mode=tk_mode, length=tk_length
    )
    tk_progress_bar.start(interval_time)
    tk_progress_bar.step(incrementation_time)
    try:
        tk_progress_bar.pack(
            fill=pack_options.get("fill"),
            side=pack_options.get("side"),
            padx=pack_options.get("padx"),
            pady=pack_options.get("pady"),
            ipadx=pack_options.get("ipadx"),
            ipady=pack_options.get("ipady"),
            anchor=pack_options.get("anchor"),
        )
    except:  # to test
        raise PackErrors

    if callable_function:
        tk_progress_bar.after(stop_time, callable_function)
    else:
        tk_progress_bar.after(stop_time, tk_progress_bar.stop)

    return tk_progress_bar


def create_button(
    root: ttk.Frame,
    text: str,
    callable_function=None,
    **pack_options,
) -> ttk.Button:
    """Create a tkinter button that will be contained in an already existing parent frame

    :param root: Parent frame
    :param text: Text to insert into tkinter Button widget
    :param callable_function: Function to call when clicking on the button
    :param pack_options: Configuration options to pack the created button.
    Only pack options are expected.

    :return: tk_button (ttk.Button)

    :raise TypeError: Error raised when input type is different from expected type"""

    # check input
    inputs_to_check = [
        (root, ttk.Frame),
        (text, str),
    ]
    check_input(inputs_to_check)

    if not callable_function:
        callable_function = root.quit

    tk_button = ttk.Button(root, text=text, command=callable_function)

    try:
        tk_button.pack(
            fill=pack_options.get("fill"),
            side=pack_options.get("side"),
            padx=pack_options.get("padx"),
            pady=pack_options.get("pady"),
            ipadx=pack_options.get("ipadx"),
            ipady=pack_options.get("ipady"),
            anchor=pack_options.get("anchor"),
        )
    except:  # to test
        raise PackErrors

    return tk_button


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
    Game template
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
