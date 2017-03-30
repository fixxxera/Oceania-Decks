import requests

session = requests.session()
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive"
}
final_count = {
    "deck1": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck2": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck3": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck4": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck5": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck6": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck7": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck8": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck9": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck10": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck11": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck12": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck13": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck14": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck15": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck16": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck17": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck18": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    },
    "deck19": {
        "inside": 0,
        "oceanview": 0,
        "balcony": 0,
        "suite": 0
    }
}
url = 'https://www.oceaniacruises.com/api/deckplan/getall'
resp = session.post(url=url, headers=headers).json()['deckPlans']
for vessel in resp:
    if vessel['shipName'] == "Sirena":
        decks = vessel['decks']
        for deck in decks:
            if deck['deckNumber'] == "1":
                if len(deck['stateroomCategories']) > 0:
                    for stateroom_type in deck['stateroomCategories']:
                        if stateroom_type['stateroomCategoryCode'] == 'D' or stateroom_type['stateroomCategoryCode'] == 'C1' or stateroom_type['stateroomCategoryCode'] == 'C2' or stateroom_type['stateroomCategoryCode'] == 'E':
                            final_count['deck1']['oceanview'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'G' or stateroom_type['stateroomCategoryCode'] == 'F':
                            final_count['deck1']['inside'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'A2' or stateroom_type['stateroomCategoryCode'] == 'B1' or stateroom_type['stateroomCategoryCode'] == 'B2' or stateroom_type['stateroomCategoryCode'] == 'A1' or stateroom_type['stateroomCategoryCode'] == 'A3':
                            final_count['deck1']['balcony'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'OS' or stateroom_type['stateroomCategoryCode'] == 'VS' or stateroom_type['stateroomCategoryCode'] == 'PH1' or stateroom_type['stateroomCategoryCode'] == 'PH2' or stateroom_type['stateroomCategoryCode'] == 'PH3':
                            final_count['deck1']['suite'] += len(stateroom_type['roomNumbers'])
            if deck['deckNumber'] == "2":
                if len(deck['stateroomCategories']) > 0:
                    for stateroom_type in deck['stateroomCategories']:
                        if stateroom_type['stateroomCategoryCode'] == 'D' or stateroom_type['stateroomCategoryCode'] == 'C1' or stateroom_type['stateroomCategoryCode'] == 'C2' or stateroom_type['stateroomCategoryCode'] == 'E':
                            final_count['deck2']['oceanview'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'G' or stateroom_type['stateroomCategoryCode'] == 'F':
                            final_count['deck2']['inside'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'A2' or stateroom_type['stateroomCategoryCode'] == 'B1' or stateroom_type['stateroomCategoryCode'] == 'B2' or stateroom_type['stateroomCategoryCode'] == 'A1' or stateroom_type['stateroomCategoryCode'] == 'A3':
                            final_count['deck2']['balcony'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'OS' or stateroom_type['stateroomCategoryCode'] == 'VS' or stateroom_type['stateroomCategoryCode'] == 'PH1' or stateroom_type['stateroomCategoryCode'] == 'PH2' or stateroom_type['stateroomCategoryCode'] == 'PH3':
                            final_count['deck2']['suite'] += len(stateroom_type['roomNumbers'])
            if deck['deckNumber'] == "3":
                if len(deck['stateroomCategories']) > 0:
                    for stateroom_type in deck['stateroomCategories']:
                        if stateroom_type['stateroomCategoryCode'] == 'D' or stateroom_type['stateroomCategoryCode'] == 'C1' or stateroom_type['stateroomCategoryCode'] == 'C2' or stateroom_type['stateroomCategoryCode'] == 'E':
                            final_count['deck3']['oceanview'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'G' or stateroom_type['stateroomCategoryCode'] == 'F':
                            final_count['deck3']['inside'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'A2' or stateroom_type['stateroomCategoryCode'] == 'B1' or stateroom_type['stateroomCategoryCode'] == 'B2' or stateroom_type['stateroomCategoryCode'] == 'A1' or stateroom_type['stateroomCategoryCode'] == 'A3':
                            final_count['deck3']['balcony'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'OS' or stateroom_type['stateroomCategoryCode'] == 'VS' or stateroom_type['stateroomCategoryCode'] == 'PH1' or stateroom_type['stateroomCategoryCode'] == 'PH2' or stateroom_type['stateroomCategoryCode'] == 'PH3':
                            final_count['deck3']['suite'] += len(stateroom_type['roomNumbers'])
            if deck['deckNumber'] == "4":
                if len(deck['stateroomCategories']) > 0:
                    for stateroom_type in deck['stateroomCategories']:
                        if stateroom_type['stateroomCategoryCode'] == 'D' or stateroom_type['stateroomCategoryCode'] == 'C1' or stateroom_type['stateroomCategoryCode'] == 'C2' or stateroom_type['stateroomCategoryCode'] == 'E':
                            final_count['deck4']['oceanview'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'G' or stateroom_type['stateroomCategoryCode'] == 'F':
                            final_count['deck4']['inside'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'A2' or stateroom_type['stateroomCategoryCode'] == 'B1' or stateroom_type['stateroomCategoryCode'] == 'B2' or stateroom_type['stateroomCategoryCode'] == 'A1' or stateroom_type['stateroomCategoryCode'] == 'A3':
                            final_count['deck4']['balcony'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'OS' or stateroom_type['stateroomCategoryCode'] == 'VS' or stateroom_type['stateroomCategoryCode'] == 'PH1' or stateroom_type['stateroomCategoryCode'] == 'PH2' or stateroom_type['stateroomCategoryCode'] == 'PH3':
                            final_count['deck4']['suite'] += len(stateroom_type['roomNumbers'])
            if deck['deckNumber'] == "5":
                if len(deck['stateroomCategories']) > 0:
                    for stateroom_type in deck['stateroomCategories']:
                        if stateroom_type['stateroomCategoryCode'] == 'D' or stateroom_type['stateroomCategoryCode'] == 'C1' or stateroom_type['stateroomCategoryCode'] == 'C2' or stateroom_type['stateroomCategoryCode'] == 'E':
                            final_count['deck5']['oceanview'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'G' or stateroom_type['stateroomCategoryCode'] == 'F':
                            final_count['deck5']['inside'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'A2' or stateroom_type['stateroomCategoryCode'] == 'B1' or stateroom_type['stateroomCategoryCode'] == 'B2' or stateroom_type['stateroomCategoryCode'] == 'A1' or stateroom_type['stateroomCategoryCode'] == 'A3':
                            final_count['deck5']['balcony'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'OS' or stateroom_type['stateroomCategoryCode'] == 'VS' or stateroom_type['stateroomCategoryCode'] == 'PH1' or stateroom_type['stateroomCategoryCode'] == 'PH2' or stateroom_type['stateroomCategoryCode'] == 'PH3':
                            final_count['deck5']['suite'] += len(stateroom_type['roomNumbers'])
            if deck['deckNumber'] == "6b":
                if len(deck['stateroomCategories']) > 0:
                    for stateroom_type in deck['stateroomCategories']:
                        if stateroom_type['stateroomCategoryCode'] == 'D' or stateroom_type['stateroomCategoryCode'] == 'C1' or stateroom_type['stateroomCategoryCode'] == 'C2' or stateroom_type['stateroomCategoryCode'] == 'E':
                            final_count['deck6']['oceanview'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'G' or stateroom_type['stateroomCategoryCode'] == 'F':
                            final_count['deck6']['inside'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'A2' or stateroom_type['stateroomCategoryCode'] == 'B1' or stateroom_type['stateroomCategoryCode'] == 'B2' or stateroom_type['stateroomCategoryCode'] == 'A1' or stateroom_type['stateroomCategoryCode'] == 'A3':
                            final_count['deck6']['balcony'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'OS' or stateroom_type['stateroomCategoryCode'] == 'VS' or stateroom_type['stateroomCategoryCode'] == 'PH1' or stateroom_type['stateroomCategoryCode'] == 'PH2' or stateroom_type['stateroomCategoryCode'] == 'PH3':
                            final_count['deck6']['suite'] += len(stateroom_type['roomNumbers'])
            if deck['deckNumber'] == "7b":
                if len(deck['stateroomCategories']) > 0:
                    for stateroom_type in deck['stateroomCategories']:
                        if stateroom_type['stateroomCategoryCode'] == 'D' or stateroom_type['stateroomCategoryCode'] == 'C1' or stateroom_type['stateroomCategoryCode'] == 'C2' or stateroom_type['stateroomCategoryCode'] == 'E':
                            final_count['deck7']['oceanview'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'G' or stateroom_type['stateroomCategoryCode'] == 'F':
                            final_count['deck7']['inside'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'A2' or stateroom_type['stateroomCategoryCode'] == 'B1' or stateroom_type['stateroomCategoryCode'] == 'B2' or stateroom_type['stateroomCategoryCode'] == 'A1' or stateroom_type['stateroomCategoryCode'] == 'A3':
                            final_count['deck7']['balcony'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'OS' or stateroom_type['stateroomCategoryCode'] == 'VS' or stateroom_type['stateroomCategoryCode'] == 'PH1' or stateroom_type['stateroomCategoryCode'] == 'PH2' or stateroom_type['stateroomCategoryCode'] == 'PH3':
                            final_count['deck7']['suite'] += len(stateroom_type['roomNumbers'])
            if deck['deckNumber'] == "8b":
                if len(deck['stateroomCategories']) > 0:
                    for stateroom_type in deck['stateroomCategories']:
                        if stateroom_type['stateroomCategoryCode'] == 'D' or stateroom_type['stateroomCategoryCode'] == 'C1' or stateroom_type['stateroomCategoryCode'] == 'C2' or stateroom_type['stateroomCategoryCode'] == 'E':
                            final_count['deck8']['oceanview'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'G' or stateroom_type['stateroomCategoryCode'] == 'F':
                            final_count['deck8']['inside'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'A2' or stateroom_type['stateroomCategoryCode'] == 'B1' or stateroom_type['stateroomCategoryCode'] == 'B2' or stateroom_type['stateroomCategoryCode'] == 'A1' or stateroom_type['stateroomCategoryCode'] == 'A3':
                            final_count['deck8']['balcony'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'OS' or stateroom_type['stateroomCategoryCode'] == 'VS' or stateroom_type['stateroomCategoryCode'] == 'PH1' or stateroom_type['stateroomCategoryCode'] == 'PH2' or stateroom_type['stateroomCategoryCode'] == 'PH3':
                            final_count['deck8']['suite'] += len(stateroom_type['roomNumbers'])
            if deck['deckNumber'] == "9":
                if len(deck['stateroomCategories']) > 0:
                    for stateroom_type in deck['stateroomCategories']:
                        if stateroom_type['stateroomCategoryCode'] == 'D' or stateroom_type['stateroomCategoryCode'] == 'C1' or stateroom_type['stateroomCategoryCode'] == 'C2' or stateroom_type['stateroomCategoryCode'] == 'E':
                            final_count['deck9']['oceanview'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'G' or stateroom_type['stateroomCategoryCode'] == 'F':
                            final_count['deck9']['inside'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'A2' or stateroom_type['stateroomCategoryCode'] == 'B1' or stateroom_type['stateroomCategoryCode'] == 'B2' or stateroom_type['stateroomCategoryCode'] == 'A1' or stateroom_type['stateroomCategoryCode'] == 'A3':
                            final_count['deck9']['balcony'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'OS' or stateroom_type['stateroomCategoryCode'] == 'VS' or stateroom_type['stateroomCategoryCode'] == 'PH1' or stateroom_type['stateroomCategoryCode'] == 'PH2' or stateroom_type['stateroomCategoryCode'] == 'PH3':
                            final_count['deck9']['suite'] += len(stateroom_type['roomNumbers'])
            if deck['deckNumber'] == "10":
                if len(deck['stateroomCategories']) > 0:
                    for stateroom_type in deck['stateroomCategories']:
                        if stateroom_type['stateroomCategoryCode'] == 'D' or stateroom_type['stateroomCategoryCode'] == 'C1' or stateroom_type['stateroomCategoryCode'] == 'C2' or stateroom_type['stateroomCategoryCode'] == 'E':
                            final_count['deck10']['oceanview'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'G' or stateroom_type['stateroomCategoryCode'] == 'F':
                            final_count['deck10']['inside'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'A2' or stateroom_type['stateroomCategoryCode'] == 'B1' or stateroom_type['stateroomCategoryCode'] == 'B2' or stateroom_type['stateroomCategoryCode'] == 'A1' or stateroom_type['stateroomCategoryCode'] == 'A3':
                            final_count['deck10']['balcony'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'OS' or stateroom_type['stateroomCategoryCode'] == 'VS' or stateroom_type['stateroomCategoryCode'] == 'PH1' or stateroom_type['stateroomCategoryCode'] == 'PH2' or stateroom_type['stateroomCategoryCode'] == 'PH3':
                            final_count['deck10']['suite'] += len(stateroom_type['roomNumbers'])
            if deck['deckNumber'] == "11":
                if len(deck['stateroomCategories']) > 0:
                    for stateroom_type in deck['stateroomCategories']:
                        if stateroom_type['stateroomCategoryCode'] == 'D' or stateroom_type['stateroomCategoryCode'] == 'C1' or stateroom_type['stateroomCategoryCode'] == 'C2' or stateroom_type['stateroomCategoryCode'] == 'E':
                            final_count['deck11']['oceanview'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'G' or stateroom_type['stateroomCategoryCode'] == 'F':
                            final_count['deck11']['inside'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'A2' or stateroom_type['stateroomCategoryCode'] == 'B1' or stateroom_type['stateroomCategoryCode'] == 'B2' or stateroom_type['stateroomCategoryCode'] == 'A1' or stateroom_type['stateroomCategoryCode'] == 'A3':
                            final_count['deck11']['balcony'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'OS' or stateroom_type['stateroomCategoryCode'] == 'VS' or stateroom_type['stateroomCategoryCode'] == 'PH1' or stateroom_type['stateroomCategoryCode'] == 'PH2' or stateroom_type['stateroomCategoryCode'] == 'PH3':
                            final_count['deck11']['suite'] += len(stateroom_type['roomNumbers'])
            if deck['deckNumber'] == "12":
                if len(deck['stateroomCategories']) > 0:
                    for stateroom_type in deck['stateroomCategories']:
                        if stateroom_type['stateroomCategoryCode'] == 'D' or stateroom_type['stateroomCategoryCode'] == 'C1' or stateroom_type['stateroomCategoryCode'] == 'C2' or stateroom_type['stateroomCategoryCode'] == 'E':
                            final_count['deck12']['oceanview'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'G' or stateroom_type['stateroomCategoryCode'] == 'F':
                            final_count['deck12']['inside'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'A2' or stateroom_type['stateroomCategoryCode'] == 'B1' or stateroom_type['stateroomCategoryCode'] == 'B2' or stateroom_type['stateroomCategoryCode'] == 'A1' or stateroom_type['stateroomCategoryCode'] == 'A3':
                            final_count['deck12']['balcony'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'OS' or stateroom_type['stateroomCategoryCode'] == 'VS' or stateroom_type['stateroomCategoryCode'] == 'PH1' or stateroom_type['stateroomCategoryCode'] == 'PH2' or stateroom_type['stateroomCategoryCode'] == 'PH3':
                            final_count['deck12']['suite'] += len(stateroom_type['roomNumbers'])
            if deck['deckNumber'] == "13":
                if len(deck['stateroomCategories']) > 0:
                    for stateroom_type in deck['stateroomCategories']:
                        if stateroom_type['stateroomCategoryCode'] == 'D' or stateroom_type['stateroomCategoryCode'] == 'C1' or stateroom_type['stateroomCategoryCode'] == 'C2' or stateroom_type['stateroomCategoryCode'] == 'E':
                            final_count['deck13']['oceanview'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'G' or stateroom_type['stateroomCategoryCode'] == 'F':
                            final_count['deck13']['inside'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'A2' or stateroom_type['stateroomCategoryCode'] == 'B1' or stateroom_type['stateroomCategoryCode'] == 'B2' or stateroom_type['stateroomCategoryCode'] == 'A1' or stateroom_type['stateroomCategoryCode'] == 'A3':
                            final_count['deck13']['balcony'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'OS' or stateroom_type['stateroomCategoryCode'] == 'VS' or stateroom_type['stateroomCategoryCode'] == 'PH1' or stateroom_type['stateroomCategoryCode'] == 'PH2' or stateroom_type['stateroomCategoryCode'] == 'PH3':
                            final_count['deck13']['suite'] += len(stateroom_type['roomNumbers'])
            if deck['deckNumber'] == "14":
                if len(deck['stateroomCategories']) > 0:
                    for stateroom_type in deck['stateroomCategories']:
                        if stateroom_type['stateroomCategoryCode'] == 'D' or stateroom_type['stateroomCategoryCode'] == 'C1' or stateroom_type['stateroomCategoryCode'] == 'C2' or stateroom_type['stateroomCategoryCode'] == 'E':
                            final_count['deck14']['oceanview'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'G' or stateroom_type['stateroomCategoryCode'] == 'F':
                            final_count['deck14']['inside'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'A2' or stateroom_type['stateroomCategoryCode'] == 'B1' or stateroom_type['stateroomCategoryCode'] == 'B2' or stateroom_type['stateroomCategoryCode'] == 'A1' or stateroom_type['stateroomCategoryCode'] == 'A3':
                            final_count['deck14']['balcony'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'OS' or stateroom_type['stateroomCategoryCode'] == 'VS' or stateroom_type['stateroomCategoryCode'] == 'PH1' or stateroom_type['stateroomCategoryCode'] == 'PH2' or stateroom_type['stateroomCategoryCode'] == 'PH3':
                            final_count['deck14']['suite'] += len(stateroom_type['roomNumbers'])
            if deck['deckNumber'] == "15":
                if len(deck['stateroomCategories']) > 0:
                    for stateroom_type in deck['stateroomCategories']:
                        if stateroom_type['stateroomCategoryCode'] == 'D' or stateroom_type['stateroomCategoryCode'] == 'C1' or stateroom_type['stateroomCategoryCode'] == 'C2' or stateroom_type['stateroomCategoryCode'] == 'E':
                            final_count['deck15']['oceanview'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'G' or stateroom_type['stateroomCategoryCode'] == 'F':
                            final_count['deck15']['inside'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'A2' or stateroom_type['stateroomCategoryCode'] == 'B1' or stateroom_type['stateroomCategoryCode'] == 'B2' or stateroom_type['stateroomCategoryCode'] == 'A1' or stateroom_type['stateroomCategoryCode'] == 'A3':
                            final_count['deck15']['balcony'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'OS' or stateroom_type['stateroomCategoryCode'] == 'VS' or stateroom_type['stateroomCategoryCode'] == 'PH1' or stateroom_type['stateroomCategoryCode'] == 'PH2' or stateroom_type['stateroomCategoryCode'] == 'PH3':
                            final_count['deck15']['suite'] += len(stateroom_type['roomNumbers'])
            if deck['deckNumber'] == "16":
                if len(deck['stateroomCategories']) > 0:
                    for stateroom_type in deck['stateroomCategories']:
                        if stateroom_type['stateroomCategoryCode'] == 'D' or stateroom_type['stateroomCategoryCode'] == 'C1' or stateroom_type['stateroomCategoryCode'] == 'C2' or stateroom_type['stateroomCategoryCode'] == 'E':
                            final_count['deck16']['oceanview'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'G' or stateroom_type['stateroomCategoryCode'] == 'F':
                            final_count['deck16']['inside'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'A2' or stateroom_type['stateroomCategoryCode'] == 'B1' or stateroom_type['stateroomCategoryCode'] == 'B2' or stateroom_type['stateroomCategoryCode'] == 'A1' or stateroom_type['stateroomCategoryCode'] == 'A3':
                            final_count['deck16']['balcony'] += len(stateroom_type['roomNumbers'])
                        elif stateroom_type['stateroomCategoryCode'] == 'OS' or stateroom_type['stateroomCategoryCode'] == 'VS' or stateroom_type['stateroomCategoryCode'] == 'PH1' or stateroom_type['stateroomCategoryCode'] == 'PH2' or stateroom_type['stateroomCategoryCode'] == 'PH3':
                            final_count['deck16']['suite'] += len(stateroom_type['roomNumbers'])
    else:
        pass
for k, v in final_count.items():
    if v['inside'] == 0 and v['oceanview'] == 0 and v['balcony'] == 0 and v['suite'] == 0:
        pass
    else:
        print(k, v)