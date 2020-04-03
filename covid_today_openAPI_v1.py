import requests
import pandas as pd
import json
import deepcut

response = requests.get("https://covid19.th-stat.com/api/open/today")

#print(response.status_code)

#print(response.json())
result=response.json()

print(result,' == ',type(result))

headerColumn=list(result.keys())
print(headerColumn)
#print(result.values())

dfData=pd.DataFrame(columns=headerColumn)

newrow={'Confirmed':result[headerColumn[0]], 'Recovered':result[headerColumn[1]], 'Hospitalized':result[headerColumn[2]], 'Deaths':result[headerColumn[3]],
       'NewConfirmed':result[headerColumn[4]], 'NewRecovered':result[headerColumn[5]], 'NewHospitalized':result[headerColumn[6]],
        'NewDeaths':result[headerColumn[7]], 'UpdateDate':result[headerColumn[8]], 'Source':result[headerColumn[9]],
         'DevBy':result[headerColumn[10]], 'SeverBy':result[headerColumn[11]]}
dfData=dfData.append(newrow, ignore_index=True)

print(dfData)
#data=pd.DataFrame.from_dict(result)
#print(data.columns)