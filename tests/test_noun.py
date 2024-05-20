from memo.grammar.noun import Noun
from memo.grammar.gender import Gender
from memo.grammar.declension import Declension, DeclensionType

noun_male = {
    "dec": DeclensionType["SECOND"],
    "gen": Gender["MASCULINE"],
    "sing_trans": "Friend",
    "sing_dec": {
        "nominative": "amicus",
        "genitive": "amici",
        "dative": "amico",
        "accusative": "amicum",
        "ablative": "amico",
    },
    "plur_trans": "Friends",
    "plur_dec": {
        "nominative": "amici",
        "genitive": "amicorum",
        "dative": "amicis",
        "accusative": "amicos",
        "ablative": "amicis",
    },
}

noun_female = {
    "dec": DeclensionType["FIRST"],
    "gen": Gender["FEMININE"],
    "sing_trans": "Gate",
    "sing_dec": {
        "nominative": "puer",
        "genitive": "pueri",
        "dative": "puero",
        "accusative": "puerum",
        "ablative": "puero",
    },
    "plur_trans": "Gates",
    "plur_dec": {
        "nominative": "pueri",
        "genitive": "puerorum",
        "dative": "pueris",
        "accusative": "pueros",
        "ablative": "pueris",
    },
}

noun_neuter = {
    "dec": DeclensionType["SECOND"],
    "gen": Gender["NEUTER"],
    "sing_trans": "Gift",
    "sing_dec": {
        "nominative": "donum",
        "genitive": "doni",
        "dative": "dono",
        "accusative": "donum",
        "ablative": "dono",
    },
    "plur_trans": "Gifts",
    "plur_dec": {
        "nominative": "dona",
        "genitive": "donorum",
        "dative": "donis",
        "accusative": "dona",
        "ablative": "donis",
    },
}


def test_init_passess_masculine():
    assert Noun(
        noun_male["dec"],
        noun_male["gen"],
        noun_male["sing_trans"],
        noun_male["sing_dec"],
        noun_male["plur_trans"],
        noun_male["plur_dec"],
    )


def test_init_passess_feminine():
    assert Noun(
        noun_female["dec"],
        noun_female["gen"],
        noun_female["sing_trans"],
        noun_female["sing_dec"],
        noun_female["plur_trans"],
        noun_female["plur_dec"],
    )


def test_init_passess_neuter():
    assert Noun(
        noun_neuter["dec"],
        noun_neuter["gen"],
        noun_neuter["sing_trans"],
        noun_neuter["sing_dec"],
        noun_neuter["plur_trans"],
        noun_neuter["plur_dec"],
    )
