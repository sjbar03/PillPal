import requests

# This script is for fetching a list of drug brand names that are consistent with the OpenFDA API I am using. Running this script will take
# a few minutes, and there is really no reason to run this script again unless the data on https://www.rxassist.org/pap-info/brand-drug-list-print
# changes.

root = 'https://www.rxassist.org/pap-info/brand-drug-list-print'
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

fetched_html = requests.get(root, headers=headers)

if fetched_html.ok:
    html = fetched_html.content
    file = open('web_response.txt', 'a')

    file.writelines([html.decode('utf-8')])
    file.close()
else:
    fetched_html.raise_for_status()

names = open('brandnames.txt', "w")
source = open('web_response.txt')
bad = open('bad.txt', 'w')

line_number = 1
until_next = 6

for line in source:
    if line_number < 33:
        line_number += 1
        continue

    if until_next == 0:
        until_next = 6
        try:
            start = line.index('">')
            end = start + line[start:].index("<")

            line = line[start+2:end]
            root = 'https://api.fda.gov/drug/ndc.json/?search=brand_name:'
            resp = requests.get(root + line)
            if resp.ok:
                names.write(line+ '\n')
                print('good' + str(line_number) + '/' + '10600')
            else:
                print('bad'+ str(line_number) + '/' + '10600')
                bad.write(line+'\n')
        except:
            break

    until_next -= 1
    line_number += 1

source.close()
names.close()
bad.close()
