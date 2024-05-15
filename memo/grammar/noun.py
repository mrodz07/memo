from .declension import Declension, DeclensionType
from .gender import Gender

class Noun(Declension):
    # sing for singular, plur for plural and dec for declensions
    # sing_trans and plur_trans are translations of the word
    def __init__(self, dec_type: DeclensionType, gender: Gender,
                 sing_trans: str, sing_dec: dict[str, str],
                 plur_trans: str, plur_dec: dict[str, str]
                 ):

        super().__init__(dec_type, sing_dec, plur_dec)

        self.gender = gender
        self.sing_word = sing_trans
        self.plur_trans = plur_trans
