#!/usr/bin/env python3

import sys
from pathlib import Path

from typing import Optional, Union, List, Callable

path_test = Path(__file__).resolve().parents[2]
sys.path.append(str(path_test))

import tkinter as tk
from tkinter import ttk
from lib.edit.game_text import *
from lib.constant_values import (
    PackErrors,
    TkMode,
    TkOrientation,
    TkRelief,
    TkAnchorNSticky,
    TkSide,
    TkStates,
    GradePlayer,
    TenseKey,
    VlColors,
    StyleNamesCustomized,
)

from tkinter.scrolledtext import ScrolledText
from lib.img import (
    PATH_TO_POSITIVE_SMILEY,
    PATH_TO_SAD_SMILEY_2,
    PATH_TO_THUM_UP_SMILEY,
)

from PIL import ImageTk, Image


def get_player_grade(score: int) -> GradePlayer:
    """
    Get the grade according to the score
        :e.g:
            CREATOR:20,
            MASTER:>20-18>=,
            EXPERT:>18-16>=,
            ELITE:>16-14>=,
            DISCIPLE:>14-10>=,
            OUTSIDER:>10-5>=,
            ALIEN:>5-0>="""

    if score == 0 or (score > 0 and score < 5):
        return GradePlayer.ALIEN

    elif score == 5 or (score > 5 and score < 10):
        return GradePlayer.OUTSIDER

    elif score == 10 or (score > 10 and score < 14):
        return GradePlayer.DISCIPLE

    elif score == 14 or (score > 14 and score < 16):
        return GradePlayer.ELITE

    elif score == 16 or (score > 16 and score < 18):
        return GradePlayer.EXPERT

    elif score == 18 or (score > 18 and score < 20):
        return GradePlayer.MASTER

    else:
        return GradePlayer.CREATOR


def check_input(value_to_check: Union[tuple, List[tuple]]) -> Union[Exception, None]:
    """Check if inputs have the right instance type

    :param value_to_check: Inputs values to check their type.
    It should be a tuple, e.g (input, expected_type)

    :raise TypeError: Error raised when input type is different from expected type"""

    if isinstance(value_to_check, tuple):
        if not isinstance(value_to_check[0], value_to_check[1]):
            raise TypeError(
                f"Your Input has a type:{type(value_to_check[0])}, "
                + f"which is different from expected input type: {value[1]}"
            )

    elif isinstance(value_to_check, list):
        for index, value in enumerate(value_to_check):  # value == tuple
            if not isinstance(value[0], value[1]):
                raise TypeError(
                    f"Your Input in index: {index} has a type: {type(value[0])}, "
                    + f"which is different from expected input type: {value[1]}"
                )

    else:
        raise TypeError(
            f" parameter value_to_check type: {type(value_to_check[0])}, "
            + "is different from tuple or list"
        )

    return


def create_frame(
    frame: ttk.Frame,
    tk_relief: Union[TkRelief, str] = TkRelief.FLAT,
    **pack_options,
) -> ttk.Frame:
    """Create a frame that will be contained in an already existing parent frame
    :param frame: Parent frame
    :param tk_relief: Tkinter constant for frame relief. Default set to flat
    :param pack_options: Configuration options to pack the created frame.
    Only pack options are expected.

    :return: frame (ttk.Frame)

    :raise TypeError: Error raised when input type is different from expected type"""

    # check input
    check_input((frame, ttk.Frame))

    if not isinstance(tk_relief, (TkRelief, str)):
        raise TypeError(
            f"Your Input type:{type(tk_relief)}, is different from expected input type for tk_relief"
        )

    frame = ttk.Frame(frame, relief=tk_relief)
    try:
        frame.pack(
            fill=pack_options.get("fill"),
            side=pack_options.get("side"),
            padx=pack_options.get("padx"),
            pady=pack_options.get("pady"),
            ipadx=pack_options.get("ipadx"),
            ipady=pack_options.get("ipady"),
            anchor=pack_options.get("anchor"),
            expand=pack_options.get("expand"),
        )
    except:  # to test
        raise PackErrors

    return frame


def create_label(
    frame: ttk.Frame,
    text: str,
    tk_relief: Union[TkRelief, str] = TkRelief.FLAT,
    tk_anchor: Union[TkAnchorNSticky, str] = TkAnchorNSticky.CENTER,
    tk_width: Optional[int] = None,
    label_style: str = StyleNamesCustomized.tlabel,
    **pack_options,
) -> ttk.Label:
    """Create a label that will be contained in an already existing parent frame

    :param frame: Parent frame
    :param text: Label text
    :param tk_relief: Tkinter constant for label relief. Default set to flat
    :param tk_anchor: Tkinter constant for label anchor. Default set to center
    :param tk_width: (optional) Width of the label widget
    :param label_style: (optional) customized style of the label.
    :param pack_options: Configuration options to pack the created label.
    Only pack options are expected.

    :return: tk_label (ttk.Label)

    :raise TypeError: Error raised when input type is different from expected type"""

    # check input
    inputs_to_check = [(frame, ttk.Frame), (text, str), (label_style, str)]
    check_input(inputs_to_check)

    # add check for size parameter ?

    if not (isinstance(tk_relief, TkRelief) or isinstance(tk_relief, str)):
        raise TypeError(
            f"Your Input type:{type(tk_relief)}, is different from expected input type"
        )

    if not (isinstance(tk_anchor, TkAnchorNSticky) or isinstance(tk_anchor, str)):
        raise TypeError(
            f"Your Input type:{type(tk_anchor)}, is different from expected input type"
        )

    tk_label = ttk.Label(
        frame,
        text=text,
        width=tk_width,
        relief=tk_relief,
        anchor=tk_anchor,
        style=label_style,
    )
    try:
        tk_label.pack(
            fill=pack_options.get("fill"),
            side=pack_options.get("side"),
            padx=pack_options.get("padx"),
            pady=pack_options.get("pady"),
            ipadx=pack_options.get("ipadx"),
            ipady=pack_options.get("ipady"),
            expand=pack_options.get("expand"),
        )
    except:  # to test
        raise PackErrors

    return tk_label


def create_photo_label(
    frame: ttk.Frame,
    tk_photo: ImageTk.PhotoImage,
    tk_compound: Union[TkSide, str] = TkSide.TOP,
    tk_anchor: Union[TkAnchorNSticky, str] = TkAnchorNSticky.CENTER,
    tk_relief: Union[TkRelief, str] = TkRelief.FLAT,
    text: Optional[str] = None,
    tk_width: Optional[int] = None,
    label_style: str = StyleNamesCustomized.tlabel,
    **pack_options,
) -> ttk.Label:
    """Create a label that will be contained in an already existing parent frame

    :param frame: Parent frame
    :param tk_photo: Image to display
    :param tk_compound: Tkinter constant for label compound. Default set to TOP
    :param tk_anchor: Tkinter constant for label anchor. Default set to CENTER
    :param tk_relief: Tkinter constant for label relief. Default set to flat
    :param text: (optional) Label text
    :param tk_width: (optional) Width of the label widget
    :param label_style: (optional) customized style of the label
    :param pack_options: Configuration options to pack the created label.
    Only pack options are expected.

    :return: tk_label (ttk.Label)

    :raise TypeError: Error raised when input type is different from expected type"""

    # check input
    inputs_to_check = [
        (frame, ttk.Frame),
        (tk_photo, ImageTk.PhotoImage),
        (label_style, str),
    ]
    check_input(inputs_to_check)

    if not isinstance(tk_anchor, (TkAnchorNSticky, str)):
        raise TypeError(
            f"Your Input type:{type(tk_anchor)}, is different from expected input type"
        )

    if not isinstance(tk_compound, (TkSide, str)):
        raise TypeError(
            f"Your Input type:{type(tk_compound)}, is different from expected input type"
        )

    if not isinstance(tk_relief, (TkRelief, str)):
        raise TypeError(
            f"Your Input type:{type(tk_relief)}, is different from expected input type"
        )

    # add check for size parameter ?... missing checks see later

    # Put Tk photo as global so it won't be destroyed after getting out of the function
    # see garbage collection --> other solution trsf this function to a class...

    tk_photo_label = ttk.Label(
        frame,
        image=tk_photo,
        compound=tk_compound,
        anchor=tk_anchor,
        relief=tk_relief,
        text=text,
        width=tk_width,
        style=label_style,
    )
    try:
        tk_photo_label.pack(
            fill=pack_options.get("fill"),
            side=pack_options.get("side"),
            padx=pack_options.get("padx"),
            pady=pack_options.get("pady"),
            ipadx=pack_options.get("ipadx"),
            ipady=pack_options.get("ipady"),
            expand=pack_options.get("expand"),
        )
    except:
        raise PackErrors

    return tk_photo_label


def create_text(
    frame: ttk.Frame,
    text: str,
    tk_width: int = 30,
    tk_height: int = 1,
    tk_state: Union[TkStates, str] = TkStates.DISABLED,
    fg_color: str = VlColors.dark,
    bg_color: str = VlColors.dark_grey_2,
    **pack_options,
) -> tk.Text:
    """Create a tkinter text that will be contained in an already existing parent frame

    :param frame: Parent frame
    :param text: Text to insert into tkinter text widget
    :param tk_width: Width of the text widget. Default set to 30
    :param tk_height: Height of the text widget. Default set to 1
    :param tk_state: State of tkinter widget text. Default state set to disabled.
    Disabled for read only, Normal for edit mode.
    :param fg_color: (Optional) Customized foregroung text color
    :param bg_color: (Optional) Customized backgroung text color
    :param pack_options: Configuration options to pack the created text.
    Only pack options are expected.

    :return: tk_text (tk.Text)

    :raise TypeError: Error raised when input type is different from expected type"""

    # check input
    inputs_to_check = [
        (frame, ttk.Frame),
        (text, str),
        (tk_width, int),
        (tk_height, int),
        (fg_color, str),
        (bg_color, str),
    ]
    check_input(inputs_to_check)

    if not (isinstance(tk_state, TkStates) or isinstance(tk_state, str)):
        raise TypeError(
            f"Your Input type:{type(tk_state)}, is different from expected input type"
        )

    tk_text = tk.Text(
        frame, height=tk_height, width=tk_width, fg=fg_color, background=bg_color
    )
    tk_text.insert(tk.END, text)  # line.column == 1.0
    try:
        tk_text.pack(
            fill=pack_options.get("fill"),
            side=pack_options.get("side"),
            padx=pack_options.get("padx"),
            pady=pack_options.get("pady"),
            ipadx=pack_options.get("ipadx"),
            ipady=pack_options.get("ipady"),
            anchor=pack_options.get("anchor"),
            expand=pack_options.get("expand"),
        )
    except:  # to test
        raise PackErrors

    tk_text.configure(state=tk_state)

    return tk_text


def create_entry(
    frame: ttk.Frame,
    tk_textvariable: tk.StringVar,
    tk_width: int,
    fg_color: str = VlColors.dark_brown,
    bg_color: str = VlColors.light_grey,
    **pack_options,
) -> tk.Entry:
    """Create a tkinter entry that will be contained in an already existing parent frame

    :param frame: Parent frame
    :param tk_textvariable: Catch user input text into this parameter
    :param tk_width: Width of the entry widget
    :param fg_color: (Optional) Customized foregroung button color
    :param bg_color: (Optional) Customized backgroung button color
    :param pack_options: Configuration options to pack the created entry.
    Only pack options are expected.

    :return: tk_entry (tk.Entry)

    :raise TypeError: Error raised when input type is different from expected type"""

    # check input
    inputs_to_check = [
        (frame, ttk.Frame),
        (tk_textvariable, tk.StringVar),
        (tk_width, int),
        (fg_color, str),
        (bg_color, str),
    ]
    check_input(inputs_to_check)

    tk_entry = tk.Entry(
        frame, textvariable=tk_textvariable, width=tk_width, fg=fg_color, bg=bg_color
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
    frame: ttk.Frame,
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

    :param frame: Parent frame
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
        (frame, ttk.Frame),
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
        frame, orient=tk_orientation, mode=tk_mode, length=tk_length
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
    frame: ttk.Frame,
    text: str,
    callable_function: Optional[Callable] = None,
    fg_color: str = VlColors.dark,
    bg_color: str = VlColors.purple,
    **pack_options,
) -> ttk.Button:
    """Create a tkinter button that will be contained in an already existing parent frame

    :param frame: Parent frame
    :param text: Text to insert into tkinter Button widget
    :param callable_function: Function to call when clicking on the button.
    Default value set to None
    :param fg_color: (Optional) Customized foregroung button color
    :param bg_color: (Optional) Customized backgroung button color
    :param pack_options: Configuration options to pack the created button.
    Only pack options are expected.

    :return: tk_button (ttk.Button)

    :raise TypeError: Error raised when input type is different from expected type"""

    # check input
    inputs_to_check = [
        (frame, ttk.Frame),
        (text, str),
        (fg_color, str),
        (bg_color, str),
    ]
    check_input(inputs_to_check)

    if not callable_function:
        callable_function = frame.quit

    tk_button = tk.Button(
        frame, text=text, command=callable_function, fg=fg_color, bg=bg_color
    )

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
    Template for game presentation.
    Find here the presentation and the rules of the game
    displayed as a scrowling text. After finishing reading,
    you can go to the next page by clicking onto the next button.
    """

    template_colors = VlColors()

    def __init__(
        self,
        parent: ttk.Frame,
        func: Callable,
        game_presentation: str = presentation_text,
    ):
        """
        Init module for game presentation template class.

        :param parent: Root widget
        :param func: Callable function
        :param presentation_text: Game presentation. Default set to game_text.presentation_text
        """
        check_input([(parent, ttk.Frame), (game_presentation, str)])

        self.parent = parent
        self.presentation_text = game_presentation
        super().__init__(parent)

        self.pack(
            side=TkSide.TOP,
            fill=tk.BOTH,
            expand=True,
        )

        self.callable_func = func

        self.frames = []
        self.config_frames = {
            0: {"fill": tk.X, "side": tk.TOP, "pady": 10},
            1: {"fill": tk.X, "side": tk.BOTTOM, "pady": 10},
        }
        self._nber_frames = len(self.config_frames)

    def scrolling_text(
        self,
        frame: ttk.Frame,
        width: Optional[int] = None,
        height: Optional[int] = None,
        fg_color: str = VlColors.dark,
        bg_color: str = VlColors.lavande,
    ):
        """
        Display a text in a scrowling text box.

        :param frame: Parent frame
        :param width: (Optional) define the scrowling text box width. Default set to None
        :param heigth: (Optional) define the scrowling text box heigth. Default set to None
        :param fg_color: (Optiobal) Customized foregroung button color
        :param bg_color: (Optiobal) Customized backgroung button color"""
        scrolling_text = ScrolledText(frame, width=width, height=height)
        scrolling_text.insert(tk.END, self.presentation_text)
        scrolling_text.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5)
        scrolling_text.configure(state=tk.DISABLED)
        scrolling_text.configure(
            foreground=fg_color,
            background=bg_color,
        )

    def start_button(
        self,
        frame: ttk.Frame,
        func: Callable,
        button_position: str = TkSide.BOTTOM,
        fg_color: str = VlColors.dark,
        bg_color: str = VlColors.turquoise_2,
    ):
        """
        create a start button for the frame

        :param frame: Parent frame
        :param func: Callable function
        :param button_position: (Optiobal) Position to place the button. Default set to Bottom
        :param fg_color: (Optiobal) Customized foregroung button color
        :param bg_color: (Optiobal) Customized backgroung button color"""

        start_button = tk.Button(
            frame, text=start_text, command=func, fg=fg_color, bg=bg_color
        )
        start_button.pack(side=button_position, ipadx=15, ipady=5, pady=20)

    def template_launcher(self, frame_style: str = StyleNamesCustomized.tframe):
        """Default function to call to call the template window
        :param frame_style: (Optiobal) Customized style frame, see ttk.Style"""

        # create frames
        for nber in range(self._nber_frames):
            frame = create_frame(
                self,
                frame_style=frame_style,
                fill=self.config_frames[nber]["fill"],
                side=self.config_frames[nber]["side"],
                pady=self.config_frames[nber]["pady"],
            )
            self.frames.append(frame)

        self.scrolling_text(self.frames[0])
        self.start_button(self.frames[1], self.callable_func)


class GamePageTemplate(ttk.Frame):
    """
    Game page template.
    Page as each game window is a game page. Go to the next game page
    by clicking on the SUBMIT Button.
    """

    template_colors = VlColors()

    def __init__(self, parent: ttk.Frame, func: Callable):
        """
        Init module for game page template class.

        :param parent: root widget type Tk
        :param func: Callable funtion
        """
        check_input((parent, ttk.Frame))
        self.parent = parent

        super().__init__(parent)
        self.pack(
            side=TkSide.TOP,
            fill=tk.BOTH,
            expand=True,
        )

        self.callable_func = func

        # user input
        self.imperfect_entried = tk.StringVar()
        self.preterite_entried = tk.StringVar()

        self.frames = []
        self.config_frames = {
            0: {"fill": tk.X, "side": tk.TOP, "pady": 10},
            1: {"fill": tk.X, "side": None, "pady": 40},
            2: {"fill": tk.X, "side": None, "pady": None},
            3: {"fill": tk.X, "side": None, "pady": 10},
            4: {"fill": tk.X, "side": tk.BOTTOM, "pady": 10},
            5: {"fill": tk.X, "side": tk.BOTTOM, "pady": 10},
            6: {"fill": tk.X, "side": tk.BOTTOM, "pady": 70},
        }
        self._nber_frames = len(self.config_frames)

    def reset(self):
        """Reset frame modules"""
        self.entry_imperfect.delete(0, "end")
        self.entry_preterite.delete(0, "end")

    def template_launcher(self, infinitive_verb: str, left_verb_nb: int, score: int):
        """Default function to call to call the template window
        :param infinitive_verb: Infinitive verb
        :param left_verb_nb: Number of left verb to find
        :param score: current score"""

        # create frames
        for nber in range(self._nber_frames):
            frame = create_frame(
                self,
                fill=self.config_frames[nber]["fill"],
                side=self.config_frames[nber]["side"],
                pady=self.config_frames[nber]["pady"],
            )
            self.frames.append(frame)

        left_verbs = remain_verbs_text + str(left_verb_nb)
        current_score = score_text + str(score)
        # create widgets

        self.label_game = create_label(
            self.frames[0],
            text=game_title,
            tk_height=1,
            label_style=StyleNamesCustomized.tlabel_arial_black18,
            fill=tk.X,
            pady=5,
        )
        self.label_infinitive = create_label(
            self.frames[1],
            text=infinitive_text,
            tk_width=30,
            label_style=StyleNamesCustomized.tlabel_calibri10,
            tk_anchor=tk.E,
            side=TkSide.LEFT,
            padx=10,
        )

        self.text_infinitive = create_text(
            self.frames[1],
            text=infinitive_verb,
            tk_width=30,
            side=TkSide.LEFT,
            padx=10,
        )
        self.text_infinitive.focus_get()

        self.label_imperfect = create_label(
            self.frames[2],
            text=imperfect_tense_text,
            tk_width=35,
            label_style=StyleNamesCustomized.tlabel_calibri10,
            tk_anchor=tk.CENTER,
            side=TkSide.LEFT,
            padx=10,
            ipadx=5,
        )
        self.label_preterite = create_label(
            self.frames[2],
            text=preterite_tense_text,
            tk_width=35,
            label_style=StyleNamesCustomized.tlabel_calibri10,
            tk_anchor=tk.CENTER,
            side=tk.RIGHT,
            padx=10,
            ipadx=5,
        )

        self.entry_imperfect = create_entry(
            self.frames[3],
            tk_textvariable=self.imperfect_entried,
            tk_width=35,
            side=TkSide.LEFT,
            padx=10,
            ipadx=5,
        )
        self.entry_imperfect.focus_get()

        self.entry_preterite = create_entry(
            self.frames[3],
            tk_textvariable=self.preterite_entried,
            tk_width=35,
            side=tk.RIGHT,
            padx=10,
            ipadx=5,
        )
        self.entry_preterite.focus_get()

        self.progress_bar = create_progress_bar(
            self.frames[4],
            fill=tk.X,
            padx=10,
            pady=5,
            callable_function=self.callable_func,
        )
        self.label_remain_verbs = create_label(
            self.frames[5],
            text=left_verbs,
            tk_width=25,
            label_style=StyleNamesCustomized.tlabel_arial_black10,
            tk_anchor=TkAnchorNSticky.W,
            side=TkSide.LEFT,
            padx=25,
            ipadx=5,
        )

        self.label_remain_verbs = create_label(
            self.frames[5],
            text=current_score,
            tk_width=25,
            label_style=StyleNamesCustomized.tlabel_arial_black10,
            tk_anchor=TkAnchorNSticky.E,
            side=TkSide.RIGHT,
            padx=25,
            ipadx=5,
        )

        self.submit_button = create_button(
            self.frames[6],
            text=submit_text,
            anchor=tk.CENTER,
            callable_function=self.callable_func,
            ipadx=15,
            ipady=5,
        )


class GameStateTemplate(ttk.Frame):
    """
    Default template for game state
    """

    def __init__(
        self,
        parent: ttk.Frame,
        func: Callable,
        img_path: str = PATH_TO_POSITIVE_SMILEY,
        resize_values: tuple = (350, 300),
        type_resize: Image.Resampling = Image.Resampling.LANCZOS,
        text_to_display: str = success_text,
    ):
        """
        Init module for game state template.

        :param parent: root widget type Tk
        :param func: Callable function
        :param img_path: Path to image. Default set to PATH_TO_POSITIVE_SMILEY
        :param resize_values: Reshape image size as (x,y). Default set to (400,350)
        :param type_resize: See Image.Resampling. Default set to Resampling.LANCZOS
        :param text_to_display: Text to display alongside the image. Default set to success_text
        """

        check_input(
            [
                (parent, ttk.Frame),
                (img_path, str),
                (resize_values, tuple),
                (type_resize, Image.Resampling),
                (text_to_display, str),
            ]
        )

        self.parent = parent

        super().__init__(parent)
        self.pack(
            side=TkSide.TOP,
            fill=tk.BOTH,
            expand=True,
        )

        self.callable_func = func

        # prepare image to display
        path_to_file = Path(img_path).resolve()
        photo = Image.open(path_to_file)
        photo = photo.resize(resize_values, type_resize)
        self._tk_photo = ImageTk.PhotoImage(photo)

        self._text_to_display = text_to_display  # add property

        self.frames = []
        self.config_frames = {
            0: {
                "fill": tk.BOTH,
                "side": tk.TOP,
                "pady": 5,
                "expand": True,
            },
            1: {
                "fill": tk.X,
                "side": tk.BOTTOM,
                "pady": 5,
            },
        }
        self._nber_frames = len(self.config_frames)

    def set_tk_photo(self, photo: ImageTk.PhotoImage):
        """Set directly the tk photo to use for this frame
        :param photo: image to display on the frame"""

        check_input((photo, ImageTk.PhotoImage))
        self._tk_photo(photo)

    def get_tk_photo(self) -> ImageTk.PhotoImage:
        """Get the current tk photo to use for this frame"""
        return self._tk_photo

    def template_launcher(self, verb_to_find: dict):
        """Default function to call to call the template window

        :param verb_to_find: current tense verb used in the game"""

        for nber in range(self._nber_frames):
            frame = create_frame(
                self,
                fill=self.config_frames[nber].get("fill"),
                side=self.config_frames[nber].get("side"),
                pady=self.config_frames[nber].get("pady"),
                expand=self.config_frames[nber].get("expand"),
            )
            self.frames.append(frame)

        verb_to_find_ans = (
            f"Infinitive: {verb_to_find[TenseKey.INFINITIVE.value]},\n"
            + f"Verb singular third form: {verb_to_find[TenseKey.THIRD_FORM.value]},\n"
            + f"Preterite: {verb_to_find[TenseKey.PRETERITE.value]},\n"
            + f"Perfect: {verb_to_find[TenseKey.PERFECT.value]},\n"
            + f"Verb Level: {verb_to_find[TenseKey.LEVEL.value]}"
        )
        self.photo_label = create_photo_label(
            self.frames[0],
            tk_photo=self._tk_photo,
            tk_compound=TkSide.TOP,
            text=self._text_to_display,
            pady=10,
            label_style=StyleNamesCustomized.tlabel_calibri10,
        )

        self.submit_button = create_label(
            self.frames[1],
            text=verb_to_find_ans,
            anchor=TkAnchorNSticky.NW,
            label_style=StyleNamesCustomized.tlabel_arial_black10,
            side=TkSide.LEFT,
            padx=25,
            pady=10,
            ipadx=5,
        )

        self.submit_button = create_button(
            self.frames[1],
            text=next_text,
            anchor=TkAnchorNSticky.E,
            callable_function=self.callable_func,
            side=TkSide.RIGHT,
            padx=25,
            pady=5,
            ipadx=15,
            bg_color=VlColors.green_water,
        )


class GameFailedTemplate(GameStateTemplate):
    """
    Template for failed response.
    """

    def __init__(
        self,
        parent: ttk.Frame,
        func: Callable,
        img_path: str = PATH_TO_SAD_SMILEY_2,
        resize_values: tuple = (350, 300),
        type_resize: Image.Resampling = Image.Resampling.LANCZOS,
        text_to_display: str = failed_text,
    ):
        """
        Init module for game failed template.

        :param parent: root widget type Tk
        :param func: Callable function
        :param img_path: Path to image. Default set to PATH_TO_SAD_SMILEY
        :param resize_values: Reshape image size as (x,y). Default set to (400,350)
        :param type_resize: See Image.Resampling. Default set to Resampling.LANCZOS
        :param text_to_display: Text to display alongside the image.
        Default set to failed_text
        """

        super().__init__(
            parent, func, img_path, resize_values, type_resize, text_to_display
        )


class GameSuccessTemplate(GameStateTemplate):
    """
    Template for successful response
    """

    def __init__(
        self,
        parent: ttk.Frame,
        func: Callable,
        img_path: str = PATH_TO_THUM_UP_SMILEY,
        resize_values: tuple = (350, 300),
        type_resize: Image.Resampling = Image.Resampling.LANCZOS,
        text_to_display: str = success_text,
    ):
        """
        Init module for game success template.

        :param parent: root widget type Tk
        :param func: Callable function
        :param img_path: Path to image. Default set to PATH_TO_SAD_SMILEY
        :param resize_values: Reshape image size as (x,y). Default set to (400,350)
        :param type_resize: See Image.Resampling. Default set to Resampling.LANCZOS
        :param text_to_display: Text to display alongside the image. Default set to success_text
        """

        super().__init__(
            parent, func, img_path, resize_values, type_resize, text_to_display
        )


class GameConclusionTemplate(ttk.Frame):
    """
    Template for game conclusion.
    """

    def __init__(self, parent: ttk.Frame, func: Callable):
        """
        Init module for game conclusion template.

        :param parent: root widget type Tk
        :param func: Callable function
        """
        check_input((parent, ttk.Frame))
        self.parent = parent

        super().__init__(parent)
        self.pack(
            side=TkSide.TOP,
            fill=tk.BOTH,
            expand=True,
        )

        self.callable_func = func
        self.frames = []

        self.config_frames = {
            0: {"fill": tk.X, "side": tk.TOP, "pady": 10},
            1: {"fill": tk.X, "pady": 40},
            2: {"fill": tk.X},
            3: {"fill": tk.X, "pady": 75},
            4: {"fill": tk.X, "side": tk.BOTTOM, "pady": 20},
        }
        self._nber_frames = len(self.config_frames)

    def template_launcher(self, score: int):
        """Default function to call to call the template window
        :param score: player score"""

        _score = str(score) + "/20"
        # _end_score = score_text + _score # choice was to use label and text
        # but only label can be used, if yes should use _end_score

        # create frames
        for nber in range(self._nber_frames):
            frame = create_frame(
                self,
                fill=self.config_frames[nber].get("fill"),
                side=self.config_frames[nber].get("side"),
                pady=self.config_frames[nber].get("pady"),
            )
            self.frames.append(frame)

        # create widgets

        self.label_end_game = create_label(
            self.frames[0],
            text=end_text,
            tk_height=1,
            fill=tk.X,
            pady=5,
            label_style=StyleNamesCustomized.tlabel_arial_black18,
        )
        self.label_final_score = create_label(
            self.frames[1],
            text=score_text,
            tk_width=30,
            label_style=StyleNamesCustomized.tlabel_arial_black10,
            tk_anchor=TkAnchorNSticky.E,
            side=TkSide.LEFT,
            padx=10,
            ipadx=10,
        )

        self.text_final_score = create_text(
            self.frames[1],
            text=_score,
            tk_width=8,
            bg_color=VlColors.blue_green,
            side=TkSide.LEFT,
            padx=20,
            ipadx=4,
        )

        self.label_grade = create_label(
            self.frames[2],
            text=grade_text,
            tk_width=30,
            tk_anchor=TkAnchorNSticky.E,
            label_style=StyleNamesCustomized.tlabel_arial_black10,
            side=TkSide.LEFT,
            padx=10,
            ipadx=10,
        )

        self.text_grade = create_text(
            self.frames[2],
            text=get_player_grade(score).name,
            tk_width=12,
            side=TkSide.LEFT,
            tk_anchor=TkAnchorNSticky.CENTER,
            bg_color=VlColors.blue_green,
            padx=20,
            ipadx=5,
        )

        self.grade_message = create_text(
            self.frames[3],
            text=get_player_grade(score).value,
            fill=tk.BOTH,
            tk_height=3,
            tk_anchor=TkAnchorNSticky.W,
            bg_color=VlColors.lavande,
            padx=10,
        )

        self.label_game_conclusion = create_label(
            self.frames[4],
            text=conclusion_text,
            tk_anchor=TkAnchorNSticky.SW,
            label_style=StyleNamesCustomized.tlabel_arial_black10,
            side=TkSide.LEFT,
            padx=25,
            ipadx=5,
        )
        self.submit_button = create_button(
            self.frames[4],
            text=close_app_text,
            side=TkSide.RIGHT,
            anchor=TkAnchorNSticky.SE,
            bg_color=VlColors.turquoise_2,
            padx=10,
            ipadx=5,
            callable_function=self.callable_func,
        )


def change_frame():
    global frame_root, pr
    auc = GamePageTemplate(frame_root, frame_root.quit)
    pr.destroy()
    # auc.tkraise()
    auc.template_launcher("richie", 15, 5)


def configure_style(frame):
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


if __name__ == "__main__":
    from lib.constant_values import TkFilling

    # TO TEST PACKAGE
    default_dict = {
        TenseKey.INFINITIVE.value: "richie",
        TenseKey.THIRD_FORM.value: "richie1",
        TenseKey.PRETERITE.value: "richieee",
        TenseKey.PERFECT.value: "richii",
        TenseKey.LEVEL.value: "A2",
    }
    root = tk.Tk()
    root.title("VerbenLernen")
    root.geometry("550x500")
    root.resizable(0, 0)
    frame_root = ttk.Frame(root)
    frame_root.pack(side=TkSide.TOP, fill=TkFilling.BOTH, expand=True)
    configure_style(frame_root)

    pr = GameConclusionTemplate(
        frame_root, change_frame
    )  # when using buttom callable should be call without parenthesis
    pr.template_launcher(10)
    root.mainloop()
