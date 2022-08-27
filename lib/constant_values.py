"""
Find here all Enum values for Verben Lernen application

"""
from enum import Enum, unique


@unique
class GradePlayer(Enum):
    """
    Get the grade of the player
    """

    CREATOR = (
        "GERMAN TENSE HAS NO SECRET FOR YOU ! YOU ARE THE PERFECTION IN HIS EYES !",
    )
    MASTER = (
        'GERMAN TENSE IS AS SIMPLE AS SAYING "HELLO" FOR YOU ! YOU CAN STOP HERE BUT REMEMBER: PERFECTION IS THE NEXT DOOR !',
    )
    EXPERT = "GERMAN TENSE RECOGNISES YOU AS A SKILLFULL PERSON ! YOU ARE NOT FAR FROM PERFECTION !"
    ELITE = "GERMAN TENSE HAS ALREADY RECOGNISED YOU AS A GENIUS ! BUT THE ROAD IS STILL LONG TO REACH PERFECTION"
    DISCIPLE = "GERMAN TENSE HAS RECOGNISED YOUR POTENTIAL ! A LONG ROAD HIS WATING FOR YOU TO REACH THE PERFECTION !"
    OUTSIDER = "GERMAN TENSE HAS RECOGNISED YOU AS A POTENTIAL TALENT ! A LONG ROAD HIS WATING FOR YOU TO REACH THE PERFECTION !"
    ALIEN = "ERROR ERROR ERROR GERMAN TENSE DOES NOT RECOGNISE YOU ! PLEASE UPGRADE YOURSELF IF YOU WANT HIS RECOGNITION !"


class TkBooleans(Enum):
    """Symbolic constants for Tk"""

    NO = FALSE = OFF = 0
    YES = TRUE = ON = 1


@unique
class TkAnchorNSticky(Enum):
    """anchor and sticky"""

    N = "n"
    S = "s"
    W = "w"
    E = "e"
    NW = "nw"
    SW = "sw"
    NE = "ne"
    SE = "se"
    NS = "ns"
    EW = "ew"
    NSEW = "nsew"
    CENTER = "center"


class TkFilling(Enum):
    """fill"""

    NONE = "none"
    X = "x"
    Y = "y"
    BOTH = "both"


@unique
class TKSide(Enum):
    """side"""

    LEFT = "left"
    TOP = "top"
    RIGHT = "right"
    BOTTOM = "bottom"


@unique
class TKRelief(Enum):
    """relief"""

    RAISED = "raised"
    SUNKEN = "sunken"
    FLAT = "flat"
    RIDGE = "ridge"
    GROOVE = "groove"
    SOLID = "solid"


class TkOrientation(Enum):
    """orient"""

    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"
