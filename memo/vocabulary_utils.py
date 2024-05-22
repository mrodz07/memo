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

    def read_nouns_csv(self, file_path: str):
        file_name_substr = "noun"
        sing_data, sing_decl = ({}, {})
        plur_data, plur_decl = ({}, {})
        nouns = []

        self.check_substr_in_file_name(file_path, file_name_substr)

        with open(file_path, newline="") as file:
            reader = csv.DictReader(file)

            for i, row in enumerate(reader):
                if (
                    self.check_fields_not_none(row, reader.line_num)
                    and self.check_declension(row["declension"], reader.line_num)
                    and self.check_gender(row["gender"], reader.line_num)
                    and self.check_number(row["number"], reader.line_num)
                    # We need to save the declensions of the singular number, as we need both plural
                    # and singular data to create a Noun object
                    and i % 2 == 0
                ):
                    sing_data = row
                    sing_decl = self.create_decl_dict(row)
                else:
                    plur_data = row
                    plur_decl = self.create_decl_dict(row)

                    nouns.append(
                        Noun(
                            # Indeces in python start with 0
                            DeclensionType(int(sing_data["declension"]) - 1),
                            Gender[sing_data["gender"].upper()],
                            sing_data["translation"],
                            sing_decl,
                            plur_data["translation"],
                            plur_decl,
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

    def check_substr_in_file_name(self, file_path: str, substr: str) -> bool:
        if substr not in file_path:
            raise Exception(f"Your file must have '{substr}' as part of its name")

        return True

    def check_fields_not_none(self, fields: dict, line_num: int) -> bool:
        for _, val in fields.items():
            if val is None:
                raise Exception(f"Line {line_num} lacks all values")

        return True

    # decl as declention
    def create_decl_dict(self, row_data: dict[str, str]) -> dict[str, str]:
        new_row_data = row_data.copy()
        for key in ["translation", "number", "declension", "gender"]:
            del new_row_data[key]
        return new_row_data
