import requests
import pandas as pd
import json

response = requests.get("https://covid19.th-stat.com/api/open/timeline")

#print(response.status_code)

#print(response.json())
result=response.json()

#print(result,' == ',type(result))

headerColumn=list(result.keys())
print(headerColumn)
#print(result.values())

updateDate=result['UpdateDate']
headerData=list(result['Data'][0].keys())
print(headerData, ' === ',len(result['Data']))

print(result['Data'][90])

dfData=pd.DataFrame(columns=['Date', 'NewConfirmed', 'NewRecovered', 'NewHospitalized', 'NewDeaths', 'Confirmed', 'Recovered', 'Hospitalized', 'Deaths','UpdateDate'])

for n in range(len(result['Data'])):
    #print(n)
    newrow={'Date':result['Data'][n][headerData[0]], 'NewConfirmed':result['Data'][n][headerData[1]], 'NewRecovered':result['Data'][n][headerData[2]], 
       'NewHospitalized':result['Data'][n][headerData[3]], 'NewDeaths':result['Data'][n][headerData[4]], 'Confirmed':result['Data'][n][headerData[5]],
        'Recovered':result['Data'][n][headerData[6]], 'Hospitalized':result['Data'][n][headerData[7]], 'Deaths':result['Data'][n][headerData[8]],'UpdateDate':updateDate}
    dfData=dfData.append(newrow, ignore_index=True)

print(dfData)
