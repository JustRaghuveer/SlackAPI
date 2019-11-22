import requests
import json


def CreateAPI():
    url = "	https://slack.com/api/channels.create"

    # Namespace = TY_Register_API.cell_value(1, 2)
    Flag = ""

    headers = {'content-type': 'application/json', 'Authorization': 'Bearer xoxp-847258608774-832268085666-844593558948-9ec0ff5ccf5f7d7b716d4a233f7ac8af'}

    payload = {'name': 'slack59'}

    # response = requests.post(url, cert=cert, data=json.dumps(body), headers=headers)
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        result = json.loads(response.text)
        return result
    except:
        print("error in create api call")




def JoinAPI():
    url = "https://slack.com/api/channels.join"

    headers = {'content-type': 'application/json', 'Authorization': 'Bearer xoxp-847258608774-832268085666-844593558948-9ec0ff5ccf5f7d7b716d4a233f7ac8af'}

    payload = {'name': 'slack59', 'validate': True}

    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        result = json.loads(response.text)
        return result
    except:
        print("error in join api call")



def RenameAPI():
    url = "https://slack.com/api/channels.rename"

    headers = {'content-type': 'application/json', 'Authorization': 'Bearer xoxp-847258608774-832268085666-844593558948-9ec0ff5ccf5f7d7b716d4a233f7ac8af'}

    payload = {'channel': 'CQX889YQ6', 'name': 'slack49',  'validate': True}

    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers)
        result = json.loads(response.text)
        return result
    except:
        print("error in RenameAPI api call")



def ListChannelandValidateAPI():
    url = "https://slack.com/api/conversations.list"

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    payload = {'token': 'xoxp-847258608774-832268085666-844593558948-9ec0ff5ccf5f7d7b716d4a233f7ac8af'}

    response = requests.get(url, params=payload, headers=headers)
    result = json.loads(response.text)

    print(result['channels'])

    searchslack = (list(filter(lambda slacname: slacname['name'] == 'slack49', result['channels'])))

    previous_name = searchslack[0]['previous_names']

    if previous_name[0] == "slack59":
        return "Previous name validates as true: ", previous_name
    else:
        return "Previous name validates as false, found name as: ", previous_name

def ArchieveAPI():
    url = "	https://slack.com/api/channels.archive"

    headers = {'content-type': 'application/json', 'Authorization': 'Bearer xoxp-847258608774-832268085666-844593558948-9ec0ff5ccf5f7d7b716d4a233f7ac8af'}

    payload = {'channel': 'CQX889YQ6'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    result = json.loads(response.text)

    return result

def ValidateArchieveAPI():
    url = "https://slack.com/api/conversations.list"

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    payload = {'token': 'xoxp-847258608774-832268085666-844593558948-9ec0ff5ccf5f7d7b716d4a233f7ac8af', 'exclude_archived':True}

    response = requests.get(url, params=payload, headers=headers)
    result = json.loads(response.text)

    print(result['channels'])

    searchslack = (list(filter(lambda slacname: slacname['name'] == 'slack49', result['channels'])))

    if len(searchslack) == 0:
        return "Slack name is archieved successfully"
    else:
        return "Slack name is not archieved sucessfully"


if __name__ == "__main__":
    # print(CreateAPI())
    print(JoinAPI())
    # print(RenameAPI())
    # print(ListChannelandValidateAPI())
    # print(ArchieveAPI())
    # print(ValidateArchieveAPI())