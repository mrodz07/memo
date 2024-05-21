import csv

from .grammar.noun import Noun
from .grammar.gender import Gender
from .grammar.declension import DeclensionType
from .grammar.number import GrammaticalNumber as GNum


# TODO: Implement singleton pattern???
class VocabularyUtils:
    """
    Utilities to read vocabulary from csv files
    """

    def read_nouns_csv(self, filePath: str):
        nouns = []

        if "noun" not in filePath:
            raise Exception("Your file must have noun as part of its name")

        with open(filePath, newline="") as file:
            reader = csv.DictReader(file)
            # Check that each file has each attribute

            for row in reader:
                # Setting example gender and declension, will be overwritten
                # TODO: Don't create new enums if they are arleady on these variables
                gender = Gender["MASCULINE"]
                declension = DeclensionType["FIRST"]

                # Saving the line num as we read two by two
                sing_line_num = reader.line_num
                sing_data = row
                sing_trans = sing_data["translation"]

                plur_data = next(reader)
                plur_line_num = reader.line_num
                plur_trans = plur_data["translation"]

                # Do checks on both lines to determine if they are valid
                if self.check_declension(
                    sing_data["declension"], sing_line_num
                ) and self.check_declension(plur_data["declension"], plur_line_num):
                    # Indeces in python start at 0
                    # Declension enum for noun
                    declension = DeclensionType(int(sing_data["declension"]) - 1)

                if self.check_gender(
                    sing_data["gender"], sing_line_num
                ) and self.check_gender(plur_data["gender"], plur_line_num):
                    # Gender enum for noun
                    gender = Gender[sing_data["gender"].lower().upper()]

                if self.check_number(
                    sing_data["number"], sing_line_num
                ) and self.check_number(plur_data["number"], plur_line_num):
                    # Gender enum for noun
                    # TODO: Add number to each declension object???
                    pass

                # Remove unnecessary dict keys, only the five declensions are left
                for k in ["translation", "number", "declension", "gender"]:
                    del sing_data[k]
                    del plur_data[k]

                nouns.append(
                    Noun(
                        declension,
                        gender,
                        sing_trans,
                        sing_data,
                        plur_trans,
                        plur_data,
                    )
                )

        return nouns

    def check_declension(self, dec_num: str, line_num: int) -> bool:
        if 1 <= int(dec_num) <= len(DeclensionType):
            return True
        else:
            raise Exception(f"Invalid declension on line {line_num}: {dec_num}")

    def check_gender(self, gender: str, line_num: int) -> bool:
        try:
            if Gender[gender.lower().upper()]:
                return True
        except (ValueError, KeyError):
            raise Exception(f"Invalid gender on line {line_num}: {gender}")

        return False

    def check_number(self, num: str, line_num: int) -> bool:
        try:
            if GNum[num.lower().upper()]:
                return True
        except (ValueError, KeyError):
            raise Exception(f"Invalid grammtical number on line {line_num}: {num}")

        return False
