import requests
import json

brand_names = open('data/brandnames.txt')
json_file = open('data/med_base.json', 'w')

root = 'https://api.fda.gov/drug/ndc.json/?search=brand_name:'

line_num = 0
med_base = []

for line in brand_names:

    resp = requests.get(root + line)

    if resp.ok:
        
       json_data = json.loads(resp.content)

       med_info = json_data['results'][0]

       med_base.append(med_info)

       print("\033[A                             \033[A")
       print(str(line_num) + '/ 1009')

    else:

       json_file.close()
       brand_names.close()
       resp.raise_for_status()

    line_num += 1

d = {'data': med_base}
json.dump(d, json_file, indent=4)

json_file.close()
brand_names.close()

