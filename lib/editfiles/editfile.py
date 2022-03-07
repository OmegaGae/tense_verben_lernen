"""
 # @ Author: OmegaGae
 # @ Create Time: 2022-03-03 13:41:10
 # @ Modified by: OmegaGae
 # @ Modified time: 2022-03-07 16:18:02
 # @ Description: Ready for work !!
 """

#!/usr/bin/env python3
from cmath import inf
import os
from typing import List


ERRORS_EDITFILE = {
    0: "Data length is incorrect",
    1: "This verb and his tenses are already known by the VerbenLernen App",
    2: "First element in the list is not a german infinitive verb",
    3: "The auxiliary enter is incorrect",
    4: "The level enter is incorrect",
}


class Editfile:
    def __init__(self, filename: str):
        """
        To read and write file with .txt extension

        filename: Name of the file you want to read/write
        """

        self.filename = filename
        print(self.filename)
        self.data_dir = os.path.join(os.path.dirname(__file__), "files")
        self.data_path = os.path.join(self.data_dir, filename)

    def readtxt(self):
        """
        Only txt extension are readable by this function.
        It will use the filename given during object creation.
        """

        if self.filename.split(".")[1] == "txt":
            with open(self.data_path, "r") as txt_file:
                self.textfile = txt_file.readlines()
            return self.textfile

    @classmethod
    def find_infinitive_verbs(cls, tense_verbs: list) -> List:

        infinitive = []

        for row_tense_verbs in tense_verbs:
            infinitive.append(row_tense_verbs.split()[0])

        return infinitive

    @classmethod
    def _check_data_format(cls, tense_verbs: list, data_to_check: list):

        if len(data_to_check) != 5:
            raise ValueError(ERRORS_EDITFILE.get(0))

        len_infinitive_verb = len(data_to_check[0])
        infinive = [
            v for i, v in enumerate(data_to_check[0]) if i >= len_infinitive_verb - 2
        ]
        if (infinive == ["e", "n"]) is False:
            if (infinive == ["r", "n"]) is False:
                raise ValueError(ERRORS_EDITFILE.get(2))

        infinive_verbs = Editfile.find_infinitive_verbs(tense_verbs)
        if data_to_check[0] in infinive_verbs:
            raise ValueError(ERRORS_EDITFILE.get(1))

        perfect = data_to_check[3].split()
        if (perfect[0] in ["hat", "ist"]) is False:
            raise ValueError(ERRORS_EDITFILE.get(3))

        if (data_to_check[4] in ["A1", "A2", "B1", "B2", "C1", "C2"]) is False:
            raise ValueError(ERRORS_EDITFILE.get(4))

    def writetxt(self, data_to_write: list) -> None:
        """
        Only txt extension are writable by this function.
        It will use the filename given during object creation.

        data_to_write: Data you want to write in the txt file. Language data must be german.
                       Waiting format: ["infinitive verb","conjugate verb to 3rd singular form","preterite verb in 3rd singular form","perfect with auxiliary in 3rd singular form","level:A1-C2"]
                       example: ["fahren","Fährt", "Fuhr","ist gefahren", "A2"]
        """
        txt = Editfile(self.filename)
        lecture_txt = txt.readtxt()
        Editfile._check_data_format(
            lecture_txt, data_to_write
        )  # If nothing is raise, format is good, data can be written
        str_data_to_write = "\n" + " ".join(list(map(str, data_to_write)))

        if self.filename.split(".")[1] == "txt":
            with open(self.data_path, "a") as txt_writable:
                txt_writable.write(str_data_to_write)


if __name__ == "__main__":
    input_vb = Editfile("starke_unregelmäßie.txt")
    input_vb.writetxt(["erinnern", "erinnert", "erinnerte", "hat erinnert", "A2"])
