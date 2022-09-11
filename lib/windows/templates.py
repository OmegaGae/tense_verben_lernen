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
    remain_verbs_text,
    submit_text,
    success_text,
    failed_text,
)
from lib.constant_values import (
    PackErrors,
    TkMode,
    TkOrientation,
    TkRelief,
    TkAnchorNSticky,
    TkSide,
    TkStates,
)

from tkinter.scrolledtext import ScrolledText
from lib.img import PATH_TO_POSITIVE_SMILEY, PATH_TO_SAD_SMILEY, PATH_TO_THUM_UP_SMILEY


from PIL import ImageTk, Image


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

    if not (isinstance(tk_relief, TkRelief) or isinstance(tk_relief, str)):
        raise TypeError(
            f"Your Input type:{type(tk_relief)}, is different from expected input type"
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
    **pack_options,
) -> ttk.Label:
    """Create a label that will be contained in an already existing parent frame

    :param frame: Parent frame
    :param text: Label text
    :param tk_relief: Tkinter constant for label relief. Default set to flat
    :param tk_anchor: Tkinter constant for label anchor. Default set to center
    :param tk_width: (optional) Width of the label widget
    :param pack_options: Configuration options to pack the created label.
    Only pack options are expected.

    :return: tk_label (ttk.Label)

    :raise TypeError: Error raised when input type is different from expected type"""

    # check input
    inputs_to_check = [(frame, ttk.Frame), (text, str)]
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
    :param pack_options: Configuration options to pack the created label.
    Only pack options are expected.

    :return: tk_label (ttk.Label)

    :raise TypeError: Error raised when input type is different from expected type"""

    # check input
    inputs_to_check = [(frame, ttk.Frame), (tk_photo, ImageTk.PhotoImage)]
    check_input(inputs_to_check)

    if not (isinstance(tk_anchor, TkAnchorNSticky) or isinstance(tk_anchor, str)):
        raise TypeError(
            f"Your Input type:{type(tk_anchor)}, is different from expected input type"
        )

    if not (isinstance(tk_compound, TkSide) or isinstance(tk_compound, str)):
        raise TypeError(
            f"Your Input type:{type(tk_compound)}, is different from expected input type"
        )

    if not (isinstance(tk_relief, TkRelief) or isinstance(tk_relief, str)):
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
    tk_width: int,
    tk_height: int = 1,
    tk_state: Union[TkStates, str] = TkStates.DISABLED,
    **pack_options,
) -> tk.Text:
    """Create a tkinter text that will be contained in an already existing parent frame

    :param frame: Parent frame
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
        (frame, ttk.Frame),
        (text, str),
        (tk_width, int),
        (tk_height, int),
    ]
    check_input(inputs_to_check)

    if not (isinstance(tk_state, TkStates) or isinstance(tk_state, str)):
        raise TypeError(
            f"Your Input type:{type(tk_state)}, is different from expected input type"
        )

    tk_text = tk.Text(frame, height=tk_height, width=tk_width, state=tk_state)
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
    frame: ttk.Frame,
    tk_textvariable: tk.StringVar,
    tk_width: int,
    **pack_options,
) -> tk.Entry:
    """Create a tkinter entry that will be contained in an already existing parent frame

    :param frame: Parent frame
    :param tk_textvariable: Catch user input text into this parameter
    :param tk_width: Width of the entry widget
    :param pack_options: Configuration options to pack the created entry.
    Only pack options are expected.

    :return: tk_entry (tk.Entry)

    :raise TypeError: Error raised when input type is different from expected type"""

    # check input
    inputs_to_check = [
        (frame, ttk.Frame),
        (tk_textvariable, tk.StringVar),
        (tk_width, int),
    ]
    check_input(inputs_to_check)

    tk_entry = tk.Entry(frame, textvariable=tk_textvariable, width=tk_width)
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
    callable_function=None,
    **pack_options,
) -> ttk.Button:
    """Create a tkinter button that will be contained in an already existing parent frame

    :param frame: Parent frame
    :param text: Text to insert into tkinter Button widget
    :param callable_function: Function to call when clicking on the button
    :param pack_options: Configuration options to pack the created button.
    Only pack options are expected.

    :return: tk_button (ttk.Button)

    :raise TypeError: Error raised when input type is different from expected type"""

    # check input
    inputs_to_check = [
        (frame, ttk.Frame),
        (text, str),
    ]
    check_input(inputs_to_check)

    if not callable_function:
        callable_function = frame.quit

    tk_button = ttk.Button(frame, text=text, command=callable_function)

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

    def __init__(self, parent, presentation_text):
        """
        Template game presentation.
        Find here the presentation and the rules of the game
        displayed as a scrowling text. After finishing reading,
        you can go to the next page by clicking onto the next button.

        :param parent: root widget
        :param presentation_text: game presentation
        """
        self.parent = parent
        self.presentation_text = presentation_text
        super().__init__(parent)

        self.pack(fill=tk.X, expand=True)

        self.frames = []
        self.config_frames = {
            0: {"fill": tk.X, "side": tk.TOP, "pady": 10},
            1: {"fill": tk.X, "side": tk.BOTTOM, "pady": 10},
        }
        self._nber_frames = len(self.config_frames)

    def template_launcher(self):
        """Default function to call to call the template window"""
        # create frames
        for nber in range(self._nber_frames):
            frame = create_frame(
                self,
                fill=self.config_frames[nber]["fill"],
                side=self.config_frames[nber]["side"],
                pady=self.config_frames[nber]["pady"],
            )
            self.frames.append(frame)

        self.scrowling_text(self.frames[0])
        self.start_button(self.frames[1])

    def scrowling_text(
        self,
        frame: ttk.Frame,
        width: Optional[int] = None,
        height: Optional[int] = None,
    ):
        """
        Print a text in a scrowling text box.

        :param frame: Parent frame
        :param width: (Optional) define the scrowling text box width. Default set to None
        :param heigth: (Optional) define the scrowling text box heigth. Default set to None

        """
        scrowling_text = ScrolledText(frame, width=width, height=height)
        scrowling_text.insert(tk.END, self.presentation_text)
        scrowling_text.pack(fill=tk.BOTH, side=tk.TOP, expand=True, padx=5)
        scrowling_text.configure(state=tk.DISABLED)

    def start_button(self, frame: ttk.Frame):
        """
        create a start button for the frame

        :param frame: Parent frame
        """
        start_button = ttk.Button(frame, text=start_text, command=frame.quit)
        start_button.pack(side=tk.BOTTOM, ipadx=5, ipady=5)
        start_button.focus_get()


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

        # define variable
        self.imperfect_entried = tk.StringVar()
        self.preterite_entried = tk.StringVar()

        self.frames = []
        self._nber_frames = 7
        self.config_frames = {
            0: {"fill": tk.X, "side": tk.TOP, "pady": 10},
            1: {"fill": tk.X, "side": None, "pady": 40},
            2: {"fill": tk.X, "side": None, "pady": None},
            3: {"fill": tk.X, "side": None, "pady": 15},
            4: {"fill": tk.X, "side": tk.BOTTOM, "pady": 10},
            5: {"fill": tk.X, "side": tk.BOTTOM, "pady": 10},
            6: {"fill": tk.X, "side": tk.BOTTOM, "pady": 75},
        }

    def template_launcher(self):
        """Default function to call to call the template window"""

        # create frames
        for nber in range(self._nber_frames):
            frame = create_frame(
                self,
                fill=self.config_frames[nber]["fill"],
                side=self.config_frames[nber]["side"],
                pady=self.config_frames[nber]["pady"],
            )
            self.frames.append(frame)

        # create widgets

        self.label_game = create_label(
            self.frames[0], text=game_title, tk_height=1, fill=tk.X, pady=5
        )
        self.label_infinitive = create_label(
            self.frames[1],
            text=infinitive_text,
            tk_width=30,
            tk_anchor=tk.E,
            side=tk.LEFT,
            padx=10,
        )

        self.text_infinitive = create_text(
            self.frames[1], text="infinitive verb", tk_width=35, side=tk.LEFT, padx=10
        )
        self.text_infinitive.focus_get()

        self.label_imperfect = create_label(
            self.frames[2],
            text=imperfect_tense_text,
            tk_width=35,
            tk_anchor=tk.CENTER,
            side=tk.LEFT,
            padx=10,
            ipadx=5,
        )
        self.label_preterite = create_label(
            self.frames[2],
            text=preterite_tense_text,
            tk_width=35,
            tk_anchor=tk.CENTER,
            side=tk.RIGHT,
            padx=10,
            ipadx=5,
        )

        self.entry_imperfect = create_entry(
            self.frames[3],
            tk_textvariable=self.imperfect_entried,
            tk_width=35,
            side=tk.LEFT,
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
            self.frames[4], fill=tk.X, padx=10, pady=5
        )
        self.label_remain_verbs = create_label(
            self.frames[5],
            text=remain_verbs_text,
            tk_width=35,
            tk_anchor=TkAnchorNSticky.W,
            side=tk.LEFT,
            padx=25,
            ipadx=5,
        )
        self.submit_button = create_button(
            self.frames[6], text=submit_text, anchor=tk.CENTER
        )


class GameStateTemplate(ttk.Frame):
    """
    Default template for game state
    """

    def __init__(
        self,
        parent: tk.Tk,
        img_path: str = PATH_TO_THUM_UP_SMILEY,
        resize_values: tuple = (400, 350),
        type_resize: Image.Resampling = Image.Resampling.LANCZOS,
        text_to_display: str = success_text,
    ):
        """
        Template game presentation.
        Find here the presentation and the rules of the game
        displayed as a scrowling text. After finishing reading,
        you can go to the next page by clicking onto the next button.

        :param parent: root widget type Tk
        :param img_path: Path to image. Default set to PATH_TO_POSITIVE_SMILEY
        :param resize_values: Reshape image size as (x,y). Default set to (400,350)
        :param type_resize: See Image.Resampling. Default set to Resampling.LANCZOS
        :param text_to_display: Text to display alongside the image. Default set to success_text
        """
        self.parent = parent

        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)

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

    def template_launcher(self):
        """Default function to call to call the template window"""

        for nber in range(self._nber_frames):
            frame = create_frame(
                self,
                fill=self.config_frames[nber].get("fill"),
                side=self.config_frames[nber].get("side"),
                pady=self.config_frames[nber].get("pady"),
                expand=self.config_frames[nber].get("expand"),
            )
            self.frames.append(frame)

        self.photo_label = create_photo_label(
            self.frames[0],
            tk_photo=self._tk_photo,
            tk_compound=TkSide.TOP,
            text=self._text_to_display,
            pady=10,
        )

        self.submit_button = create_button(
            self.frames[1], text=submit_text, anchor=tk.NE
        )


class GameFailedTemplate(GameStateTemplate):
    """
    Template for failed response
    """

    def __init__(
        self,
        parent: tk.Tk,
        img_path: str = PATH_TO_SAD_SMILEY,
        resize_values: tuple = (400, 350),
        type_resize: Image.Resampling = Image.Resampling.LANCZOS,
        text_to_display: str = failed_text,
    ):
        """
        Template game presentation.
        Find here the presentation and the rules of the game
        displayed as a scrowling text. After finishing reading,
        you can go to the next page by clicking onto the next button.

        :param parent: root widget type Tk
        :param img_path: Path to image. Default set to PATH_TO_SAD_SMILEY
        :param resize_values: Reshape image size as (x,y). Default set to (400,350)
        :param type_resize: See Image.Resampling. Default set to Resampling.LANCZOS
        :param text_to_display: Text to display alongside the image.
        Default set to failed_text
        """

        super().__init__(parent, img_path, resize_values, type_resize, failed_text)


class GameSuccessTemplate(GameStateTemplate):
    """
    Template for success response
    """

    def __init__(
        self,
        parent: tk.Tk,
        img_path: str = PATH_TO_POSITIVE_SMILEY,
        resize_values: tuple = (400, 350),
        type_resize: Image.Resampling = Image.Resampling.LANCZOS,
        text_to_display: str = success_text,
    ):
        """
        Template game presentation.
        Find here the presentation and the rules of the game
        displayed as a scrowling text. After finishing reading,
        you can go to the next page by clicking onto the next button.

        :param parent: root widget type Tk
        :param img_path: Path to image. Default set to PATH_TO_SAD_SMILEY
        :param resize_values: Reshape image size as (x,y). Default set to (400,350)
        :param type_resize: See Image.Resampling. Default set to Resampling.LANCZOS
        :param text_to_display: Text to display alongside the image. Default set to success_text
        """

        super().__init__(parent, img_path, resize_values, type_resize, failed_text)


class GameConclusionTemplate:
    """
    Template for game conclusion
    """


if __name__ == "__main__":
    root = tk.Tk()
    root.title("VerbenLernen")
    root.geometry("550x500")
    root.resizable(0, 0)  # make sure full screen is not availabe
    pr = GameFailedTemplate(root)
    pr.template_launcher()
    root.mainloop()
