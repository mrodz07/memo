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
    dec = {}

    # sing for singular, plur for plural
    # dec for declensions
    def __init__(
        self,
        dec_type: DeclensionType,
        sing_dec: dict[str, str],
        plur_dec: dict[str, str],
    ):
        if (
            self.check_dec_keys("Singular", sing_dec)
            and self.check_dec_keys("Plural", plur_dec)
            and self.check_no_empty_vals("Singular", sing_dec)
            and self.check_no_empty_vals("Plural", plur_dec)
        ):
            self.sing_dec = sing_dec
            self.plur_dec = plur_dec
            self.dec_type = dec_type

    # Check if the dec keys (cases) are correct.
    # case_num refers to case number
    def check_dec_keys(self, case_num, dec_dic):
        if self.cases == len(dec_dic):
            for case in dec_dic:
                if case not in dec_dic.values():
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
