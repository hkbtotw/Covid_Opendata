import requests
import pandas as pd
import json

response = requests.get("https://covid19.th-stat.com/api/open/cases/sum")

#print(response.status_code)

#print(response.json())
result=response.json()

print(result,' == ',type(result))

headerColumn=list(result.keys())
print(headerColumn)
#print(result.values())

dfData=pd.DataFrame(columns=['Category','Attribute','Value'])

header1=list(result['Province'])
print(header1)
for n in header1:
    #print(n)
    newrow={'Category':'Province', 'Attribute':n, 'Value':result['Province'][n]}
    dfData=dfData.append(newrow, ignore_index=True)

header1=list(result['Nation'])
print(header1)
for n in header1:
    #print(n)
    newrow={'Category':'Nation', 'Attribute':n, 'Value':result['Nation'][n]}
    dfData=dfData.append(newrow, ignore_index=True)

header1=list(result['Gender'])
print(header1)
for n in header1:
    #print(n)
    newrow={'Category':'Gender', 'Attribute':n, 'Value':result['Gender'][n]}
    dfData=dfData.append(newrow, ignore_index=True)

print(dfData)
