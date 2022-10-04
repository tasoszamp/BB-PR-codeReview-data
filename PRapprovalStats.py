import requests
import json

n = 0
i = 0
PR__DATA_LIST = []

while n < 1000:
    PR_ID = 35102-i
    url = "https://code.citrite.net/rest/api/1.0/projects/adc/repos/adc/pull-requests/{}/activities".format(PR_ID)
    #Change hardcoded creds
    resp = requests.get(url, auth=('***', '***'))

    if resp.status_code == 200:
        pullrequest = json.loads(resp.text)
        actions = pullrequest["values"]
        last_action_type = actions[0]["action"]
        creator = actions[len(actions)-1]["user"]["name"]
        
        if last_action_type == "MERGED": #and creator == "SergeyGol":

            APR_LIST = []
            for a in actions:
                if a["action"] == "APPROVED":
                    APR_LIST.insert(0, a["createdDate"])

            TIME_OPEN =  actions[len(actions)-1]["createdDate"]
            TIME_MERGED =  actions[0]["createdDate"]
            if len(APR_LIST) > 1:
                TIME_APPR = APR_LIST[1]
                DIFF_APPR = round(((TIME_APPR - TIME_OPEN)/3600000),1)
                DIFF_MERGE = round(((TIME_MERGED - TIME_OPEN)/3600000),1)
                n += 1
                print(n)

                dict = {"id": PR_ID, "Creator": creator, "Approved": DIFF_APPR, "Merged": DIFF_MERGE}
                PR__DATA_LIST.append(dict)
    
    i += 1

with open ("last1000.json", "w+") as file:
    json.dump(PR__DATA_LIST,file)
