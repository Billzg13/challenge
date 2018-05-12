import requests
import json


def find_gender_with_db(name):
    pass
    '# search for name in DB first, if name is not found in db' \
    'then return FALSE or if its found return TRUE'
    return False


def find_gender_with_api(name):

    url = "https://gender-api.com/get?name=" + name + "&key=mEScbrVxjTnApQcQYe"
    source = requests.get(url)

    j_son = json.loads(source.content)
    gender = j_son['gender']

    save_in_db(gender)

    return gender

    #save j_son in DB for further use


def save_in_db(json):
    pass

