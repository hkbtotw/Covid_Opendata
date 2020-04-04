import requests
import pandas as pd
import pandas as pd 
import json


response = requests.get("https://covid19.th-stat.com/api/open/cases")

print(response.status_code)

print(response.json())
result=response.json()

#print(result,' == ',type(result))

headerColumn=list(result.keys())
print(headerColumn)
#print(result.values())

#print(result['Data'][0])

header1=list(result['Data'][0].keys())
print(header1)

dfData=pd.DataFrame(columns=['ConfirmDate', 'No', 'Age', 'Gender', 'GenderEn', 'Nation', 'NationEn', 'Province', 'ProvinceId', 'ProvinceEn'])

for n in range(len(result['Data'])):
    #print(n)
    newrow={'ConfirmDate':result['Data'][n][header1[0]], 'No':result['Data'][n][header1[1]], 'Age':result['Data'][n][header1[2]], 
    'Gender':result['Data'][n][header1[3]], 'GenderEn':result['Data'][n][header1[4]], 'Nation':result['Data'][n][header1[5]],
     'NationEn':result['Data'][n][header1[6]], 'Province':result['Data'][n][header1[7]], 'ProvinceId':result['Data'][n][header1[8]],
      'ProvinceEn':result['Data'][n][header1[10]]}
    dfData=dfData.append(newrow, ignore_index=True)

#print(dfData)


# Create Dict of Province List to use in Location search in map api
provincethList=list(set(dfData['Province'].values.tolist()))
provinceEnList=[]
for n in provincethList:
    provinceEnList.append(list(set(list(dfData[dfData['Province']==n]['ProvinceEn'])))[0])

prvDict=zip(provinceEnList, provinceEnList)


    



