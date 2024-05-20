import pytest

from memo.grammar.declension import DeclensionType
from memo.grammar.declension import Declension

correct_dec_data = {
    "dec_type": DeclensionType["FIRST"],
    "sing": {
        "nominative": "porta",
        "genitive": "portae",
        "dative": "portae",
        "accusative": "portam",
        "ablative": "porta",
    },
    "plur": {
        "nominative": "portae",
        "genitive": "portarum",
        "dative": "portis",
        "accusative": "portas",
        "ablative": "portis",
    },
}


def test_init_passess_correct_dict():
    assert Declension(
        correct_dec_data["dec_type"], correct_dec_data["sing"], correct_dec_data["plur"]
    )


class TestSingularDeclensions:
    num = "sing"

    def test_init_fails_dict_missing_key(self):
        bad_dec_data = correct_dec_data
        del bad_dec_data[self.num]["nominative"]  # Key removed

        with pytest.raises(Exception):
            Declension(
                bad_dec_data["dec_type"], bad_dec_data["sing"], bad_dec_data["plur"]
            )

    def test_init_fails_dict_wrong_key(self):
        bad_dec_data = correct_dec_data
        del bad_dec_data[self.num]["genitive"]  # Key removed
        bad_dec_data[self.num]["not_valid"] = "not valid"

        with pytest.raises(Exception):
            Declension(
                bad_dec_data["dec_type"], bad_dec_data["sing"], bad_dec_data["plur"]
            )

    def test_init_fails_dict_empty_values(self):
        bad_dec_data = correct_dec_data
        bad_dec_data[self.num]["genitive"] = ""  # Value is empty

        with pytest.raises(Exception):
            Declension(
                bad_dec_data["dec_type"], bad_dec_data["sing"], bad_dec_data["plur"]
            )


class TestPlurarDeclensions:
    num = "plur"

    def test_init_fails_dict_missing_key(self):
        bad_dec_data = correct_dec_data
        del bad_dec_data[self.num]["nominative"]  # Key removed

        with pytest.raises(Exception):
            Declension(
                bad_dec_data["dec_type"], bad_dec_data["sing"], bad_dec_data["plur"]
            )

    def test_init_fails_dict_wrong_key(self):
        bad_dec_data = correct_dec_data
        del bad_dec_data[self.num]["genitive"]  # Key removed
        bad_dec_data[self.num]["not_valid"] = "not valid"

        with pytest.raises(Exception):
            Declension(
                bad_dec_data["dec_type"], bad_dec_data["sing"], bad_dec_data["plur"]
            )

    def test_init_fails_dict_empty_values(self):
        bad_dec_data = correct_dec_data
        bad_dec_data[self.num]["genitive"] = ""  # Value is empty

        with pytest.raises(Exception):
            Declension(
                bad_dec_data["dec_type"], bad_dec_data["sing"], bad_dec_data["plur"]
            )
