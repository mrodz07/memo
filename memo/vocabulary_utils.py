import csv

from .grammar.noun import Noun
from .grammar.gender import Gender
from .grammar.declension import Declension, DeclensionType


class VocabularyUtils():
    """
    Utilities to read vocabulary from csv files
    """
    def __init__(self):
        pass


    def read_nouns(self, filePath):
        nouns = []

        with open(filePath, newline='') as file:
            reader = csv.DictReader(file)
            # We need to have the genders in lower case
            genders = [gen.name.lower() for gen in Gender]

            for row in reader:
                sing_data = row
                plur_data = next(reader)
                sing_trans = sing_data["translation"]
                plur_trans = plur_data["translation"]

                if 1 <= int(sing_data["declension"]) <= len(DeclensionType):
                    # Indeces in python start at 0
                    declension = DeclensionType(int(sing_data["declension"]) - 1)
                else:
                    raise Exception("Incorrect value found reading declension type")

                if sing_data["gender"] in genders:
                    # Enum has to be initialized with upper case str
                    gender = Gender[sing_data["gender"].upper()]
                else:
                    raise Exception("Incorrect value found reading gender")

                # Remove unnecessary dict keys, only the five declensions are left
                for k in ["translation", "declension", "number", "gender"]:
                    del sing_data[k]
                    del plur_data[k]

                nouns.append(Noun(declension, gender, sing_trans, sing_data, \
                                  plur_trans, plur_data))
