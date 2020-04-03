import requests
import pandas as pd
import json
from googlemaps import Client as GoogleMaps
from Covid_CommentCut_v1 import CommentCut as CC

gmaps = GoogleMaps('AIzaSyCYA0c5qppFhpcGeWK-e1QIT6EBS3LoMx4')  # my account API, replace with yours

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

print(' ==> ', len(dfData))

dfData['Map']=dfData['Location']+' '+dfData['Detail']+' '+dfData['Province']

outList=dfData['Map'].values.tolist()

inList=CC(outList)

#print(inList)

dfinList=pd.DataFrame(inList)
dfinList.columns=['MapSearch']

dfData=pd.concat([dfData,dfinList],axis=1)
print(len(dfData), ' ==== ', dfData.columns)

dfData['lat'] = ""
dfData['long'] = ""


for x in range(len(dfData)):
    geocode_result = gmaps.geocode(dfData['MapSearch'][x])
    dfData['lat'][x] = geocode_result[0]['geometry']['location'] ['lat']
    dfData['long'][x] = geocode_result[0]['geometry']['location']['lng']

#latList=dfIn['lat'].values.tolist()
#longList=dfIn['long'].values.tolist()
#pairList=list(zip(latList,longList))

print(dfData)