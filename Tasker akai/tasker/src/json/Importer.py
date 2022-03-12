# -*- coding: utf-8 -*-
import json


class Importer:

    def __init__(self):
        pass
#komenda load
    def read_tasks(self):
        # TODO odczytaj plik i zdekoduj treść tutaj
        with open("taski.json") as file:
            data = json.load(file)

    def get_tasks(self):
        # TODO zwróć zdekodowane taski tutaj
        with open("taski.json") as file:
            data = json.load(file)
        return data

