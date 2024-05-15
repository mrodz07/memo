from __future__ import annotations
from enum import Enum


class DeclensionType(Enum):
    FIRST, SECOND, THIRD, FOURTH, FIFTH = range(5)


# TODO: Add vocative and locative???
# TODO: Add irregular parameter for nouns that don't follow regular
# terminations or don't have singular/plural number
# TODO: Check if terminations are correct depending on DeclensionType
class Declension():
    cases = ["nominative", "genitive", "dative", "accusative", "ablative"]
    # sing for singular, plur for plural
    # dec for declensions
    def __init__(self,
                 dec_type: DeclensionType,
                 sing_dec: dict[str, str], plur_dec: dict[str, str],
                 ):
        if not all([case in sing_dec for case in self.cases]) or \
            not all([case in plur_dec for case in self.cases]):
            raise Exception("Dictionary with incorrect keys passed to Declension")
        else:
            if all(sing_dec.values()) and all(plur_dec.values()):
                self.sing_dec = sing_dec
                self.plur_dec = plur_dec
                self.dec_type = dec_type
            else:
                raise Exception("Emtpy value on dict passed to Declension")
