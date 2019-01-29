import os
import json
from watson_developer_cloud import AssistantV1


def getAPIkey(path):
	absolutepath = os.path.join(os.path.dirname(__file__), path)
	with open(absolutepath) as fp:
		return fp.read()

def writeToFile(data, path):
	with open(path, 'w') as f:
		f.write(data)


assistant = AssistantV1(
	version='2018-11-08',
	iam_apikey=getAPIkey('../secret/watson_assistant.apikey'),
	url='https://gateway-fra.watsonplatform.net/assistant/api'
)

response = assistant.list_logs(
	workspace_id='03ca4790-466c-45a3-a556-f54b7bbb9b81',
	sort='-request_timestamp',
	page_limit=1000
).get_result()

#print(json.dumps(response, indent=2))

filepath = "../data/chatbot/users_conversations_logs/" \
           + "log_from_" \
           + response["logs"][-1]["request_timestamp"] \
           + "_to_" \
           + response["logs"][0]["request_timestamp"] \
           + ".json"

writeToFile(json.dumps(response, indent=2)+"\n", filepath)