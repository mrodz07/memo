import csv

from ..grammar.noun import Noun
from ..grammar.gender import Gender
from ..grammar.declension import DeclensionType, cases as dec_cases_lst
from .vocabulary import (
    check_substr_in_file_name,
    check_dict_fields_not_none,
    check_gender,
    check_number,
    check_declension,
    create_decl_dict,
)


def read_nouns_csv(file_path: str):
    file_name_substr = "noun"
    sing_data, sing_decl = ({}, {})
    plur_data, plur_decl = ({}, {})
    nouns = []

    check_substr_in_file_name(file_path, file_name_substr)

    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)

        for i, row in enumerate(reader):
            if (
                check_dict_fields_not_none(row, reader.line_num)
                and check_declension(row["declension"], reader.line_num)
                and check_gender(row["gender"], reader.line_num)
                and check_number(row["number"], reader.line_num)
                and check_no_empty_dec_cases(row, reader.line_num)
                # We need to save the declensions of the singular number, as we need both plural
                # and singular data to create a Noun object
                and i % 2 == 0
            ):
                sing_data = row
                sing_decl = create_decl_dict(row)
            else:
                plur_data = row
                plur_decl = create_decl_dict(row)

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
