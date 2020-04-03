import requests
import pandas as pd
import json

response = requests.get("https://covid19.th-stat.com/api/open/area")

#print(response.status_code)

#print(response.json())
result=response.json()

print(result,' == ',type(result))

headerColumn=list(result.keys())
print(headerColumn)
#print(result.values())

header1=list(result['Data'][0].keys())
print(header1)


dfData=pd.DataFrame(columns=['Date', 'Time', 'Detail', 'Location', 'Recommend', 'AnnounceBy', 'Province', 'ProvinceEn', 'Update'])

for n in range(len(result['Data'])):
    #print(n)
    newrow={'Date':result['Data'][n][header1[0]], 'Time':result['Data'][n][header1[1]], 'Detail':result['Data'][n][header1[2]], 
    'Location':result['Data'][n][header1[3]], 'Recommend':result['Data'][n][header1[4]], 'AnnounceBy':result['Data'][n][header1[5]], 
    'Province':result['Data'][n][header1[6]], 'ProvinceEn':result['Data'][n][header1[7]], 'Update':result['Data'][n][header1[8]]}
    dfData=dfData.append(newrow, ignore_index=True)

print(dfData)