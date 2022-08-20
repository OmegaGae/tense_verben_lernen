# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import sys
from pathlib import Path

path_test = Path(__file__).resolve().parents[2]
sys.path.append(str(path_test))

import tkinter as tk
from tkinter import ttk
from lib.edit.game_text import presentation_text
from tkinter.scrolledtext import ScrolledText
from tkinter.constants import END




class DisplayTextFrame():

    ...

class ButtonsFrame():
    ...

class InputFrame():
    ...

class PictureFrame():
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
        super().__init__(parent)
        self.parent = parent
    
    def scrowling_text(self, width: int= 50, height: int=10):
        """
        Print a text in a scrowling text box.

        :param width: define the scrowling text box width. Default set to 50
        :param heigth: define the scrowling text box heigth. Default set to 10

        """
        
        scrowling_text = ScrolledText(self.parent, width=width,height=height)
        scrowling_text.insert(END, presentation_text)
        scrowling_text.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        scrowling_text.focus_set()


class GamePageTemplate():
    """
    Scrowling game template
    """


class GameSuccessTemplate():
    """
    Template for game success response
    """


class GameFailedTemplate():
    """
    Template for failed response
    """


class GameConclusionTemplate():
    """
    Template for game conclusion
    """


if __name__ == "__main__":
    root = tk.Tk()
    pr = GamePresentationTemplate(root)
    pr.scrowling_text()
    root.mainloop()
    
