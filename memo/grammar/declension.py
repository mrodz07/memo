from __future__ import annotations
from enum import Enum


class DeclensionType(Enum):
    FIRST, SECOND, THIRD, FOURTH, FIFTH = range(5)


# TODO: Add vocative and locative???
# TODO: Add irregular parameter for nouns that don't follow regular
# terminations or don't have singular/plural number
# TODO: Check if terminations are correct depending on DeclensionType
class Declension:
    cases = ["nominative", "genitive", "dative", "accusative", "ablative"]

    # sing for singular, plur for plural
    # dec for declensions
    def __init__(
        self,
        dec_type: DeclensionType,
        sing: dict[str, str],
        plur: dict[str, str],
    ):
        if (
            self.check_dec_keys("Singular", sing)
            and self.check_dec_keys("Plural", plur)
            and self.check_no_empty_vals("Singular", sing)
            and self.check_no_empty_vals("Plural", plur)
        ):
            self.sing = sing
            self.plur = plur
            self.dec_type = dec_type

    # Check if the dec keys (cases) are correct.
    # case_num refers to case number
    def check_dec_keys(self, case_num, dec_dic):
        if len(self.cases) == len(dec_dic):
            for case in dec_dic:
                if case not in self.cases:
                    raise Exception(f"Invalid case on {case_num}: {case}")

            return True
        else:  # There are only 5 latin cases
            raise Exception(
                f"Incorrect dict length on {case_num}: Expected length 5 got {len(dec_dic)}"
            )

    # case_num refers to case number
    def check_no_empty_vals(self, case_num, dec_dic):
        for key, val in dec_dic.values():
            if val is None:
                raise Exception(f"Empty value found on: {case_num}, {key}")

        return True
