import pytest
from memo.grammar import declension
from memo.grammar.declension import DeclensionType
from memo.grammar.declension import Declension

correct_declension_data = [
    DeclensionType(1),
    {
        "nominative": "porta",
        "genitive": "portae",
        "dative": "portae",
        "accusative": "portam",
        "ablative": "porta",
    },
    {
        "nominative": "portae",
        "genitive": "portarum",
        "dative": "portis",
        "accusative": "portas",
        "ablative": "portis",
    },
]


def test_init_passess_correct_dict():
    assert Declension(*correct_declension_data)


class TestSingularDeclensions:
    def test_init_fails_dict_missing_key(self):
        bad_declension_data = correct_declension_data
        del bad_declension_data[1]["nominative"]  # Key removed

        with pytest.raises(Exception):
            Declension(*bad_declension_data)

    def test_init_fails_dict_wrong_key(self):
        bad_declension_data = correct_declension_data
        del bad_declension_data[1]["genitive"]  # Key removed
        bad_declension_data[1]["not_valid"] = "not valid"

        with pytest.raises(Exception):
            Declension(*bad_declension_data)

    def test_init_fails_dict_empty_values(self):
        bad_declension_data = correct_declension_data
        bad_declension_data[1]["genitive"] = ""  # Value is empty

        with pytest.raises(Exception):
            Declension(*bad_declension_data)


class TestPlurarDeclensions:
    def test_init_fails_dict_missing_key(self):
        bad_declension_data = correct_declension_data
        del bad_declension_data[2]["nominative"]  # Key removed

        with pytest.raises(Exception):
            Declension(*bad_declension_data)

    def test_init_fails_dict_wrong_key(self):
        bad_declension_data = correct_declension_data
        del bad_declension_data[2]["genitive"]  # Key removed
        bad_declension_data[2]["not_valid"] = "not valid"

        with pytest.raises(Exception):
            Declension(*bad_declension_data)

    def test_init_fails_dict_empty_values(self):
        bad_declension_data = correct_declension_data
        bad_declension_data[2]["genitive"] = ""  # Value is empty

        with pytest.raises(Exception):
            Declension(*bad_declension_data)
