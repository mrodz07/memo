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


def test_init_correct_dict():
    assert Declension(*correct_declension_data)


def test_init_dicts_missing_key():
    bad_declension_data = correct_declension_data
    bad_declension_data[1].pop("nominative")  # Key removed

    with pytest.raises(Exception):
        Declension(*bad_declension_data)
