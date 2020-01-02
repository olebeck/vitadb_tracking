import requests
import datetime
import json
r = requests.get('https://rinnegatamante.it/vitadb/list_hbs_json.php')
j = json.reads(r.content)
for entry in j:
  dlcount = entry["downloads"]
  name = entry["name"]
  id = entry["titleid"]
  f = open("files/" + id + ".json")
  jsonbefore = json.reads(f.read())
  f.close()
  x = datetime.datetime.now()
  tosave = {"downloads":dlcount,"name":name,"titleid":id,"time":x}
  jsonbefore += tosave
  print(jsonbefore)
