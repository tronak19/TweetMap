import json
from pprint import pprint

with open('tweets_english.json', encoding='utf-8') as data_file:
	jsondata = json.loads(json.dumps(data_file.read()))[0]
pprint(jsondata)
# print(type(jsondata))
