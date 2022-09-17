#!/usr/bin/env python3
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
    """Basic class to read and add verbs in the specific filename

    method read_txt: to read the specific filename
    method add_txt_in_file: to add a line in the specific filename"""
    
    def __init__(self, filename: str):
        """
        To read and write file with .txt extension

        filename: Name of the file you want to read/write
        """

        self.filename = filename
        #print(self.filename)
        self.data_path = os.path.join(os.path.dirname(__file__), self.filename)

        self._textfile = []

    def read_txt(self):
        """
        Only txt extension are readable by this function.
        It will use the filename given during object creation.
        """

        if self.filename.split(".")[1] == "txt":
            with open(self.data_path, "r") as txt_file:
                self._textfile = txt_file.readlines()
            return self._textfile

    @classmethod
    def __find_infinitive_verbs(cls, tense_verbs: list) -> List:
        """
        Find in the list, all infinitive verbs

        :param tense_verbs: list of all tense verbs

        :return: all infinitive verbs (list)
        """

        infinitive = []

        for row_tense_verbs in tense_verbs:
            infinitive.append(row_tense_verbs.split()[0])

        return infinitive

    @classmethod
    def __check_data_format(cls, tense_verbs: list, data_to_check: list) -> int:
        """
        Check if the entry data respects the verben_lernen format.

        :param tense_verbs: list of all tense verbs
        :param data_to_check: list of data to check, data should respect tense verben format:
            - Waiting format:
                [
                    "infinitive verb",
                    "conjugate verb to 3rd singular form",
                    "preterite verb in 3rd singular form",
                    "perfect with auxiliary in 3rd singular form",
                    "level:A1-C2"
                ]

        :return: 0 for success (int)

        :raise ValueError: Error raised when these following mistakes are made:
            - Data length is incorrect,
            - This verb and his tenses are already known by the VerbenLernen App,
            - First element in the list is not consider as german infinitive verb,
            - The auxiliary enter is incorrect,
            - The level enter is incorrect.
        """

        if len(data_to_check) != 5:
            raise ValueError(ERRORS_EDITFILE.get(0))

        len_infinitive_verb = len(data_to_check[0])
        infinive = [
            v for i, v in enumerate(data_to_check[0]) if i >= len_infinitive_verb - 2
        ]
        if not (infinive == ["e", "n"]):
            if not (infinive == ["r", "n"]):
                raise ValueError(ERRORS_EDITFILE.get(2))

        infinive_verbs = Editfile.__find_infinitive_verbs(tense_verbs)
        if data_to_check[0] in infinive_verbs:
            raise ValueError(ERRORS_EDITFILE.get(1))

        perfect = data_to_check[3].split()
        if not (perfect[0] in ["hat", "ist"]):
            raise ValueError(ERRORS_EDITFILE.get(3))

        if not (data_to_check[4] in ["A1", "A2", "B1", "B2", "C1", "C2"]):
            raise ValueError(ERRORS_EDITFILE.get(4))

        return 0

    def add_txt_in_file(self, data_to_write: list) -> None:
        """
        Only txt extension are writable by this function.
        It will use the filename given during object creation.

        :param data_to_write: Data you want to write in the txt file. Language data must be german.
            - Waiting format:
                [
                    "infinitive verb",
                    "conjugate verb to 3rd singular form",
                    "preterite verb in 3rd singular form",
                    "perfect with auxiliary in 3rd singular form",
                    "level:A1-C2"
                ]
            - example: ["fahren","Fährt", "Fuhr","ist gefahren", "A2"]
        """
        if not self._textfile:
            self._textfile = self.read_txt()

        Editfile.__check_data_format(
            self._textfile, data_to_write
        )  # If nothing is raised, format is good, data can be written

        # map:convert each element from list, to str -> list object
        str_data_to_write = "\n" + " ".join(list(map(str, data_to_write)))

        if self.filename.split(".")[1] == "txt":
            with open(self.data_path, "a") as txt_writable:
                txt_writable.write(str_data_to_write)


if __name__ == "__main__":
    input_vb = Editfile("starke_unregelmäßie.txt")
    text = input_vb.read_txt()
    input_vb.add_txt_in_file(["erinnern", "erinnert", "erinnerte", "hat erinnert", "A2"])
