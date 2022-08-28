"""
Find here all Enum values for Verben Lernen application

"""
from enum import Enum, IntEnum, unique


@unique
class GradePlayer(str, Enum):
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


class TkErrors(Exception):
    """Raised for any Tkinter error"""

    def __init__(
        self, msg: str = "An error occured when using tkinter package"
    ) -> None:
        """Print error message
        :param msg: Error message to print"""
        super().__init__(msg)


class PackErrors(TkErrors):
    """Raised for any Tkinter error during pack method usage"""

    def __init__(self, msg: str = "pack input values are incorrects") -> None:
        """Print pack error message
        :param msg: Error message to print"""
        super().__init__(msg)


class TkBooleans(IntEnum):
    """Symbolic constants for Tk"""

    NO = FALSE = OFF = 0
    YES = TRUE = ON = 1


@unique
class TkAnchorNSticky(str, Enum):
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


class TkFilling(str, Enum):
    """fill"""

    NONE = "none"
    X = "x"
    Y = "y"
    BOTH = "both"


@unique
class TkSide(str, Enum):
    """side"""

    LEFT = "left"
    TOP = "top"
    RIGHT = "right"
    BOTTOM = "bottom"


@unique
class TkRelief(str, Enum):
    """relief"""

    RAISED = "raised"
    SUNKEN = "sunken"
    FLAT = "flat"
    RIDGE = "ridge"
    GROOVE = "groove"
    SOLID = "solid"


class TkOrientation(str, Enum):
    """orient"""

    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"


class TkStates(str, Enum):
    """Possible states with tkinter"""

    # Text widget and button states
    NORMAL = "normal"
    DISABLED = "disabled"
    ACTIVE = "active"
    # Canvas state
    HIDDEN = "hidden"


class TkMode(str, Enum):
    """Mode"""

    DETERMINATE = "determinate"
    INDETERMINATE = "indeterminate"
