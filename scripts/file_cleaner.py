""" Cleaner for starke_unregelmäßie
Delete from file: (,),*"""

import sys
from pathlib import Path
from typing import Union

path_test = Path(__file__).resolve().parents[1]
sys.path.append(str(path_test))

from lib.edit import PATH_TO_STARKE_UNREGELMEASSIE


def clean_file(
    path_to_file: str = PATH_TO_STARKE_UNREGELMEASSIE,
    unwanted_char: Union[str, list] = ["(", ")", "*"],
):
    """Delete unwanted characters from file

    :param path_to_file: path to filename
    :param unwanted_char: character(s) to delete"""

    clean_text = []

    with open(path_to_file, "r") as txt_file:
        text = txt_file.readlines()

    for line in text:
        # replace all (, ), and *
        new_line = (
            line.replace(unwanted_char[0], "")
            .replace(unwanted_char[1], "")
            .replace(unwanted_char[2], "")
        )
        clean_text.append(new_line)

    with open(path_to_file, "w") as txt_file:
        for text in clean_text:
            txt_file.write(text)


if __name__ == "__main__":
    clean_file()
