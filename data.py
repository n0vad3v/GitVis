import json
import requests
import sys

username = sys.argv[1]
url = "https://github-contributions-api.now.sh/v1/%s" %username

r = requests.get(url)
json_data = json.loads(r.text)

# Seperate data into lists containing json
washed_data_list = list()
t_washed_data_list = list()

# Exclude datas for unwanted years
substring_years = ["2017","2016"]
start_date = "2018-11-06"

# Iterate from the end to beginning, from end till the start_date
t_is_known = 1

for item in json_data['contributions']:
    if not any(x in item['date'] for x in substring_years):
        # from the end to the start_date
        if start_date in item['date']:
            t_is_known = 0
        washed_data = dict()
        washed_data['date'] = item['date']
        washed_data['count'] = item['intensity']
        washed_data_list.append(washed_data)

        t_washed_data = dict()
        t_washed_data['date'] = item['date']
        if t_is_known == 1:
            t_washed_data['count'] = 5
        else:
            t_washed_data['count'] = 0
        t_washed_data_list.append(t_washed_data)

with open('data.json','w') as f:
    f.write(json.dumps(washed_data_list))

with open('t_data.json','w') as f:
    f.write(json.dumps(t_washed_data_list))
