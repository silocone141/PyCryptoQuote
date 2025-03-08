import requests
import yaml


def get_random_quote():
    url = "https://zenquotes.io/api/random"
    api_call = requests.get(url)
    data = api_call.json()

    return [data[0]['q'], data[0]['a']]


def store_quote(quote):
    try:
        with open("solutions.yaml", "r") as file:
            data = yaml.safe_load(file)

        new_data = {
            "q_1": quote,
            "q_2": data["q_1"],
            "q_3": data["q_2"],
            "q_4": data["q_3"],
            "q_5": data["q_4"]
        }

    except FileNotFoundError:
        new_data = {
            "q_1": quote,
            "q_2": "",
            "q_3": "",
            "q_4": "",
            "q_5": ""
        }

    with open("solutions.yaml", "w") as file:
        yaml.safe_dump(new_data, file)


def get_stored_quotes():
    try:
        with open("solutions.yaml", "r") as file:
            data = yaml.safe_load(file)

        solutions = [
            data["q_1"],
            data["q_2"],
            data["q_3"],
            data["q_4"],
            data["q_5"]
        ]

        return solutions

    except FileNotFoundError:
        return ["", "", "", "", ""]
