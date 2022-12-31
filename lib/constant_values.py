"""
Find here all Enum values for Verben Lernen application

"""

from enum import Enum, IntEnum, unique
from dataclasses import dataclass, field


@dataclass
class VlColors:
    """App Colors for background and foreground"""

    turquoise_1: str = field(default="#00A2E8")
    turquoise_2: str = field(default="#99D9EA")
    blue_green: str = field(default="#409596")
    blue_grey: str = field(default="#7092BE")
    blue_indigo: str = field(default="#6D70A1")
    dark_bleu_indigo: str = field(default="#0B0B24")
    green: str = field(default="#54B337")
    green_water: str = field(default="#69F5F7")
    dark_green: str = field(default="#377D22")
    dark_red: str = field(default="#9E1008")
    red: str = field(default="#EB180C")
    brown: str = field(default="#B5653C")
    dark_brown: str = field(default="#A15A1C")
    yellow: str = field(default="#EBE745")
    dark_yellow: str = field(default="#817F26")
    brown_yellow: str = field(default="#818049")
    light_purple: str = field(default="#CD37D9")
    purple: str = field(default="#9B22A6")
    dark_purple: str = field(default="#7C1B85")
    lavande: str = field(default="#C8BFE7")
    gold: str = field(default="#B8B63D")
    light_grey: str = field(default="#B3B3B3")
    grey: str = field(default="#7F827F")
    grey_2: str = field(default="#737373")
    dark_grey: str = field(default="#373737")
    dark_grey_2: str = field(default="#7D7D7D")
    white: str = field(default="#FFFFFF")
    dark: str = field(default="#000000")


@dataclass
class StyleNamesCustomized:
    # style names defined in GamePresentationTemplate
    tframe: str = field(default="TFrame")
    tlabel: str = field(default="TLabel")
    tlabel_calibri10: str = field(default="Calibri10.TLabel")
    tlabel_arial_black10: str = field(default="ArialBlack10.TLabel")
    tlabel_arial_black18: str = field(default="ArialBlack18.TLabel")


@unique
class GradePlayer(str, Enum):
    """
    Get the grade of the player
    """

    CREATOR = (
        "GERMAN TENSE HAS NO SECRET FOR YOU ! YOU ARE THE PERFECTION IN HIS EYES !",
    )
    MASTER = (
        'GERMAN TENSE IS AS SIMPLE AS SAYING "HELLO" FOR YOU ! YOU CAN STOP HERE BUT REMEMBER: PERFECTION IS AT THE NEXT DOOR !',
    )
    EXPERT = "GERMAN TENSE RECOGNISES YOU AS A SKILLFULL PERSON ! YOU ARE NOT FAR FROM PERFECTION !"
    ELITE = "GERMAN TENSE HAS ALREADY RECOGNISED YOU AS A GENIUS ! BUT THE ROAD IS STILL LONG TO REACH PERFECTION"
    DISCIPLE = "GERMAN TENSE HAS RECOGNISED YOUR POTENTIAL ! A LONG ROAD IS WATING FOR YOU TO REACH THE PERFECTION !"
    OUTSIDER = "GERMAN TENSE HAS RECOGNISED YOU AS A POTENTIAL TALENT ! A LONG ROAD IS WATING FOR YOU TO REACH THE PERFECTION !"
    ALIEN = "ERROR ERROR ERROR GERMAN TENSE DOES NOT RECOGNISE YOU ! PLEASE UPGRADE YOURSELF IF YOU WANT HIS RECOGNITION !"


class VerbenLernenEnum(str, Enum):
    """TO DO"""

    END_PG = "conclusion_page"
    GAME_PG = "game_pages"
    FAIL_PG = "fail_page"
    SUCCESS_PG = "success_page"
    START_PG = "presentation_page"


@unique
class TenseKey(str, Enum):
    """
    Get the key for tense verbs
    """

    INFINITIVE = "infinitive"
    THIRD_FORM = "verb singular third form"
    PRETERITE = "preterite"
    PERFECT = "perfect"
    LEVEL = "level"


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
