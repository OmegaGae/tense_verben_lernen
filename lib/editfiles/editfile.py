#!/usr/bin/env python3
import os


ERRORS_EDITFILE = {
    0: "Data length is incorrect",
    1: "This verb and his tenses is already known by the VerbenLernen App",
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

    def _check_data_format(self, data_to_check: list):

        if len(data_to_check) != 5:
            raise ValueError(ERRORS_EDITFILE.get(0))

        if data_to_check[0] in self.readtxt():  # add for to find infinitive verbs
            raise ValueError(ERRORS_EDITFILE.get(1))

        len_infinitive = len(data_to_check[0])
        if (
            [v for i, v in enumerate(data_to_check[0]) if i >= len_infinitive - 2]
            == ["e", "n"]
        ) is False:
            raise ValueError(ERRORS_EDITFILE.get(2))

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
                       example: ["fahren","Fährt", "Fuhr","ist gefahreeeeeeeeeen", "A2"]
        """
        self._check_data_format(
            data_to_write
        )  # If nothing is raise, format is good, data can be written
        str_data_to_write = "\n" + " ".join(list(map(str, data_to_write)))

        if self.filename.split(".")[1] == "txt":
            with open(self.data_path, "a") as txt_writable:
                txt_writable.write(str_data_to_write)


if __name__ == "__main__":
    input_vb = Editfile("starke_unregelmäßie.txt")
    print(input_vb.readtxt())
    input_vb.writetxt(["fahren", "Fährt", "Fuhr", "ist gefahren", "A2"])
