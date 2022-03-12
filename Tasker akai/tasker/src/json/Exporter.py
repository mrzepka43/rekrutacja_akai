# -*- coding: utf-8 -*-
import json


class Exporter:
#komenda save
    def __init__(self):
        pass

    def save_tasks(self, tasks):
        # TODO zapisz taski do pliku tutaj
        with open('taski.json') as file:
            data = tasks
        with open('taski.json', 'w') as file:
            json.dump(data, file, indent=2)
