import requests
import json
import os
import xlrd
import xlwt


Slack_workbook = xlrd.open_workbook("Slack_Input.xlsx")  # input file path goes here
#
slack_wbk = xlwt.Workbook()
slack_createAPI = slack_wbk.add_sheet("CreateAPI_Result", cell_overwrite_ok=True)
slack_joinAPI = slack_wbk.add_sheet("JoinAPI_Result", cell_overwrite_ok=True)
slack_RenameAPI = slack_wbk.add_sheet("RenameAPI_Result", cell_overwrite_ok=True)


style_header = "font: bold on, color black; borders: left thin, right thin, top thin, bottom thin; \
pattern: pattern solid, fore_color teal; align: horiz center, wrap yes,vert centre;"
StyleHeader = xlwt.easyxf(style_header)

slack_keysheet = Slack_workbook.sheet_by_name("Certificate")
slack_Test_Suite = Slack_workbook.sheet_by_name("TestSuite")
slack_create_API = Slack_workbook.sheet_by_name("CreateAPI-Input")
slack_Join_API = Slack_workbook.sheet_by_name("JoinAPI-Input")


colour_style = xlwt.easyxf('align: wrap yes;')

passed_color = "font: bold on, color black; borders: left thin, right thin, top thin, bottom thin; \
pattern: pattern solid, fore_color green; align: horiz center, wrap yes,vert centre;"
Passed = xlwt.easyxf(passed_color)

rowstyle = xlwt.easyxf("align: horiz center, wrap yes,vert centre;")

failed_color = "font: bold on, color black; borders: left thin, right thin, top thin, bottom thin; \
pattern: pattern solid, fore_color red; align: horiz center, wrap yes,vert centre;"
Failed = xlwt.easyxf(failed_color)

slack_createAPI.write(0,0,"API Name", style=StyleHeader)
slack_createAPI.write(0,1,"Result",  style=StyleHeader)
slack_createAPI.write(0,2,"TestCase Description",  style=StyleHeader)

slack_joinAPI.write(0,0,"API Name", style=StyleHeader)
slack_joinAPI.write(0,1,"Result",  style=StyleHeader)
slack_joinAPI.write(0,2,"TestCase Description",  style=StyleHeader)


def CreateAPI():
    url = slack_create_API.cell_value(1, 1)

    # Namespace = TY_Register_API.cell_value(1, 2)
    Flag = ""

    headers = {'content-type': 'application/json', 'Authorization': 'Bearer {}'.format(slack_keysheet.cell_value(1, 0))}

    for value in range(4, slack_create_API.nrows):
        if slack_create_API.cell_value(value, 0).casefold() == "Yes".casefold():
            payload = {'name': slack_create_API.cell_value(value, 1)}

            response = requests.post(url, data=json.dumps(payload), headers=headers)
            result = json.loads(response.text)

            slack_createAPI.write(value - 3, 0, slack_create_API.cell_value(1, 0), style=rowstyle)
            slack_createAPI.write(value - 3, 2, slack_create_API.cell_value(value, 2), style=rowstyle)
            slack_createAPI.write(value - 3, 1, str(result), style=rowstyle)
            print(result)
        else:
            print("Test step is set to No")
            pass

    slack_wbk.save("slackAPI_Results.xls")

def JoinAPI():
    url = slack_Join_API.cell_value(1, 1)

    headers = {'content-type': 'application/json', 'Authorization': 'Bearer {}'.format(slack_keysheet.cell_value(1, 0))}

    for value in range(4, slack_Join_API.nrows):
        if slack_Join_API.cell_value(value, 0).casefold() == "Yes".casefold():
            payload = {'name': slack_Join_API.cell_value(value, 1), 'validate': True}

            response = requests.post(url, data=json.dumps(payload), headers=headers)

            result = json.loads(response.text)

            slack_joinAPI.write(value - 3, 0, slack_Join_API.cell_value(1, 0), style=rowstyle)
            slack_joinAPI.write(value - 3, 2, slack_Join_API.cell_value(value, 2), style=rowstyle)
            slack_joinAPI.write(value - 3, 1, str(result), style=rowstyle)

            print(result)

    slack_wbk.save("slackAPI_Results.xls")


def RenameAPI():
    url = "https://slack.com/api/channels.rename"

    headers = {'content-type': 'application/json', 'Authorization': 'Bearer xoxp-847258608774-832268085666-844593558948-9ec0ff5ccf5f7d7b716d4a233f7ac8af'}

    payload = {'channel': 'CQX889YQ6', 'name': 'slack49',  'validate': True}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    result = json.loads(response.text)

    print(result)

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
        print("Previous name validates as true: ", previous_name)
    else:
        print("Previous name validates as false, found name as: ", previous_name)

def ArchieveAPI():
    url = "	https://slack.com/api/channels.archive"

    headers = {'content-type': 'application/json', 'Authorization': 'Bearer xoxp-847258608774-832268085666-844593558948-9ec0ff5ccf5f7d7b716d4a233f7ac8af'}

    payload = {'channel': 'CQX889YQ6'}

    response = requests.post(url, data=json.dumps(payload), headers=headers)
    result = json.loads(response.text)

    print(result)

def ValidateArchieveAPI():
    url = "https://slack.com/api/conversations.list"

    headers = {'content-type': 'application/x-www-form-urlencoded'}

    payload = {'token': 'xoxp-847258608774-832268085666-844593558948-9ec0ff5ccf5f7d7b716d4a233f7ac8af', 'exclude_archived':True}

    response = requests.get(url, params=payload, headers=headers)
    result = json.loads(response.text)

    print(result['channels'])

    searchslack = (list(filter(lambda slacname: slacname['name'] == 'slack49', result['channels'])))

    if len(searchslack) == 0:
        print("Slack name is archieved successfully")
    else:
        print("Slack name is not archieved sucessfully")


if __name__ == "__main__":
    for value in range(1, slack_Test_Suite.nrows):
        if "SLACK_CREATE_API" == slack_Test_Suite.cell_value(value, 0) and "Yes" == slack_Test_Suite.cell_value(value, 2):
            print(slack_Test_Suite.cell_value(value, 0), slack_Test_Suite.cell_value(value, 1))
            CreateAPI()
        if "SLACK_JOIN_API" == slack_Test_Suite.cell_value(value, 0) and "Yes" == slack_Test_Suite.cell_value(value, 2):
            print(slack_Test_Suite.cell_value(value, 0), slack_Test_Suite.cell_value(value, 1))
            JoinAPI()
        else:
            print("Test Case Execution is set to No")

    # CreateAPI()
    # JoinAPI()
    # RenameAPI()
    # ListChannelandValidateAPI()
    # ArchieveAPI()
    # ValidateArchieveAPI()
