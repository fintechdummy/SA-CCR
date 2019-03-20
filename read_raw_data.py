import json

# load the json file from local
with open(f'/Users/.../Example_Data.json', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)

# store the data in a variable
netting_set = json_data['data']
