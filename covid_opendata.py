import requests
import json
import pandas as pd

# Use URL from opendata website
url = 'https://opend.data.go.th/get-ckan/datastore_search?resource_id=93f74e67-6f76-4b25-8f5d-b485083100b6'  

# Use your API key
headers = {'api-key': 'KF9wQF4TgHcnbYPsWHx8PQtl1R5nR9Pw'}

response = requests.get(url, headers=headers)

result=response.json()

data=pd.DataFrame.from_dict(result)

print(data)

# Print Header to put in the creating table
#for n in result["result"]["fields"]:
#    print(' ==> ',type(n),' :: ',n)

# each component in this column's header comes from the "fields" in the read-in data
df_Data=pd.DataFrame(columns = ['id','no', 'age','sex','nation','occ_new', 'Province', 'Risk','District','Notification_date','Announce_Date'])

# Create new table containing data of interest
for n in result["result"]["records"]:
    #print(' ==> ',type(n),' :: ',n["age"])
    newrow= {'id':n['_id'],'no':n['no'], 'age':n['age'],'sex':n['sex'],'nation':n['nation'],'occ_new':n['occ_new'], 'Province':n['Province'], 'Risk':n['Risk'],'District':n['District'],'Notification_date':n['Notification date'],'Announce_Date':n['Announce Date']}
    df_Data = df_Data.append(newrow, ignore_index=True)
    print(' ==> ', df_Data)

print(' result : ',df_Data)

# Save data for further processing
filepath="C:/Users/70018928/Documents/Project2020/Opendata/out.csv"
df_Data.to_csv(filepath)

