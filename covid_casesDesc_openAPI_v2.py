import requests
import pandas as pd
from googlemaps import Client as GoogleMaps
import pandas as pd 
#import json
gmaps = GoogleMaps('AIzaSyCYA0c5qppFhpcGeWK-e1QIT6EBS3LoMx4')  # my account API, replace with yours

response = requests.get("https://covid19.th-stat.com/api/open/cases")

#print(response.status_code)

#print(response.json())
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
      'ProvinceEn':result['Data'][n][header1[9]]}
    dfData=dfData.append(newrow, ignore_index=True)

#print(dfData)

#dfData['ProvinceEn']=dfData['ProvinceEn']+' Thailand'
 
dfData['lat'] = ""
dfData['long'] = ""


for x in range(len(dfData)):
    print('1 :  ',dfData['Province'][x])
    if(dfData['Province'][x]=='ไม่พบข้อมูล'):
        dfData['Province'][x]='Thailand'
    print(' 2   : ',dfData['Province'][x])
    geocode_result = gmaps.geocode(dfData['Province'][x])

    print(dfData['Province'][x], '  :::    ',geocode_result[0]['geometry'])
    print(dfData['Province'][x],'  ===>    ',geocode_result[0]['geometry']['location'])
    dfData['lat'][x] = geocode_result[0]['geometry']['location'] ['lat']
    dfData['long'][x] = geocode_result[0]['geometry']['location']['lng']

#latList=dfIn['lat'].values.tolist()
#longList=dfIn['long'].values.tolist()
#pairList=list(zip(latList,longList))

print(dfData)
fileout=r'C:/Users/kira/Documents/advanalysis/OutComment.csv'
dfData.to_csv(fileout)