import os
import json
import datetime
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

response = assistant.get_workspace('03ca4790-466c-45a3-a556-f54b7bbb9b81', True).get_result()

#print(json.dumps(response, indent=2))

filepath = "../data/chatbot/workspace_logic_saves/" \
           + "chatbot_logic_from_" \
           + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") \
           + ".json"

writeToFile(json.dumps(response, indent=2)+"\n", filepath)