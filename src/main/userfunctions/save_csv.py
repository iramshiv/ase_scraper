import json


def save_json(jobs):
    with open('person.txt', 'w+') as json_file:
        json.dump(jobs, json_file)
