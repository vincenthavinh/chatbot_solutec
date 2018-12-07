import requests
import os
import json
from watson_developer_cloud import AssistantV1


def send():
	url = 'http://api.cortical.io:80/rest/expressions/similar_terms?'

	params = {
		"retina_name":"en_associative",
		"start_index":0,
		"max_results":1,
		"sparsity":1.0,
		"get_fingerprint":False
	}

	data = {"positions":[0,6,7,29]}

	r = requests.post(url, params=params, json=data)

	print(r.status_code)
	print(r.json())

#send()


def getAPIkey(path):
	absolutepath = os.path.join(os.path.dirname(__file__), path)
	with open(absolutepath) as fp:
		return fp.read()


version = '2018-11-08'
apikey = getAPIkey('../APIkeys/watson_assistant.apikey')
url = 'https://gateway-fra.watsonplatform.net/assistant/api'


assistant = AssistantV1(
	version=version,
	iam_apikey=apikey,
	url=url
)

print(getAPIkey('../APIkeys/watson_assistant.apikey'))

response = assistant.get_workspace('cc705c7e-b5f8-40ef-ba42-3df071661b29', True).get_result()

print(json.dumps(response, indent=2))
