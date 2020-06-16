import requests
import json
import urllib3
import pandas as pd

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_data():
    # Get data from Strava API
    auth_url = "https://www.strava.com/oauth/token"
    activites_url = "https://www.strava.com/api/v3/clubs/688777/activities?page=1&per_page=100"

    payload = {
        'client_id': "49683",
        'client_secret': 'e397a0231101556dc067779f90a0641b5be36703',
        'refresh_token': '175b3ba25868c060a3e219784675b705f8e88569',
        'grant_type': "refresh_token",
        'f': 'json'
    }

    # print("Requesting Token...\n")
    res = requests.post(auth_url, data=payload, verify=False)
    access_token = res.json()['access_token']
    # print("Access Token = {}\n".format(access_token))

    header = {'Authorization': 'Bearer ' + access_token}
    param = {'per_page': 20, 'page': 1}
    my_dataset = requests.get(activites_url, headers=header, params=param).json()

    # Create df of the data set
    df_club = pd.read_json(json.dumps(my_dataset))

    who_list = []
    for index, row in df_club.iterrows():
        who_list.append(row["athlete"]["firstname"])

    df_club.insert(0, 'who', who_list, True)

    # for i in range(0, 11, 1):
    #     print(df_club["who"][i])
    #     print(df_club["type"][i])
    #     print("Moving time : {}".format(df_club["moving_time"][i]))
    #     print('\n')

    return(df_club)

