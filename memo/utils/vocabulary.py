from ..grammar.gender import Gender
from ..grammar.declension import DeclensionType, cases as dec_cases_lst
from ..grammar.number import GrammaticalNumber as GNum

"""
Utilities to check the validity of arguments used through the program
"""


def check_declension(dec_num: str, line_num: int) -> bool:
    if 1 <= int(dec_num) <= len(DeclensionType):
        return True
    else:
        raise Exception(f"Invalid declension on line {line_num}: {dec_num}")


def check_gender(gender: str, line_num: int) -> bool:
    try:
        if Gender[gender.lower().upper()]:
            return True
    except (ValueError, KeyError):
        raise Exception(f"Invalid gender on line {line_num}: {gender}")

    return False


def check_number(num: str, line_num: int) -> bool:
    try:
        if GNum[num.lower().upper()]:
            return True
    except (ValueError, KeyError):
        raise Exception(f"Invalid grammtical number on line {line_num}: {num}")

    return False


def check_substr_in_file_name(file_path: str, substr: str) -> bool:
    if substr not in file_path:
        raise Exception(f"Your file must have '{substr}' as part of its name")

    return True


def check_dict_fields_not_none(fields: dict, line_num: int) -> bool:
    for _, val in fields.items():
        if val is None:
            raise Exception(f"Line {line_num} lacks all values")

    return True


# decl as declention
def create_decl_dict(row_data: dict[str, str]) -> dict[str, str]:
    new_row_data = row_data.copy()
    for key in ["translation", "number", "declension", "gender"]:
        del new_row_data[key]
    return new_row_data


def check_no_empty_strs_list(lst_str: list[str], line_num: int) -> bool:
    # dec_cases as in declension cases
    if all([True if lst_str != "" else False for dec_case in dec_cases_lst]):
        return True
    else:
        raise Exception(f"Empty value found in case on line {line_num}")
