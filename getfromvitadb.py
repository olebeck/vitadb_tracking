import requests
import datetime
import json
r = requests.get('https://rinnegatamante.it/vitadb/list_hbs_json.php')
j = json.loads(r.content)
for entry in j:
  f = open("files/" + entry["titleid"] + ".json")
  fi = f.read()

  jsonbefore = json.loads(fi)

  x = datetime.datetime.now()
  dlcount = entry["downloads"]
  name = entry["name"]
  id = entry["titleid"]
  tosave = {"downloads":dlcount,"name":name,"titleid":id,"time":x.strftime("%m/%d/%Y, %H:%M:%S")}
  jsonbefore.append(tosave)
  f.close()
  f = open("files/" + entry["titleid"] + ".json","w")
  f.write(json.dumps(jsonbefore))
