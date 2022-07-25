# import plotly.express as px
# import plotly.graph_objects as go
# import pyrebase
# import json
# import pandas as pd
import requests

config={  
"apiKey": "AIzaSyCn7bN52E2v3ELIEWx1Fy3OeZE6ertQiuk",
  "authDomain": "esp32-fb-61701.firebaseapp.com",
  "databaseURL": "https://esp32-fb-61701-default-rtdb.firebaseio.com",
  "projectId": "esp32-fb-61701",
  "storageBucket": "esp32-fb-61701.appspot.com",
  "messagingSenderId": "355330542241",
  "appId": "1:355330542241:web:6ab97bc2f70ed7f826bee0",
  "measurementId": "G-JFR16DHHN0"
}

# firebase=pyrebase.initialize_app(config)
# db = firebase.database()
# raw = json.loads(json.dumps(db.child('data').get().val()))
# dates_data = raw['dates']
# print(dates_data)
# dates_keys = dates_data.keys()
# temp = []
# for i in dates_keys:
#   d = {"date":i, "temp":dates_data[i]['Temp'], "turbidity":dates_data[i]['Turbidity'], 'water_lvl':dates_data[i]['Water level']  }
#   temp.append(d)
# df = pd.DataFrame(temp)
# print(df)


# # Line Chart of water temperature 
# fig = px.line(df, x="date", y="temp", title='Water Temperature')
# fig.write_image('static/img/temp.png')

# # water level bar graph
# fig = px.bar(df, x='date',y='water_lvl')
# fig.write_image('static/img/water_lvl.png')

# #line chart for turbidity
# fig = px.line(df, x='date',y='turbidity')
# fig.write_image('static/img/tur.png')

# #PH gauge 
# fig = go.Figure(go.Indicator(
# mode = "gauge+number",
# value = raw['ph'],
# domain = {'x': [0, 1], 'y': [0, 1]},
# title = {'text': "Ph Value"}))
# fig.write_image('static/img/ph.png')


# fig.show()
# firebase=pyrebase.initialize_app(config)
# db = firebase.database()
# raw = json.loads(json.dumps(db.child('data').get().val()))
# dates_data = raw['dates']

# dates_keys = dates_data.keys()
# temp = []
# for i in dates_keys:
#   d = {"date":i, "temp":dates_data[i]['Temp'], "turbidity":dates_data[i]['Turbidity'], 'water_lvl':dates_data[i]['Water level'] }
#   temp.append(d)
# df = pd.DataFrame(temp)
# print(df)
# # Line Chart of water temperature 
# fig = px.line(df, x="date", y="temp", title='Water Temperature')
# fig.write_image('static/img/temp.png')

# # water level bar graph
# fig = px.bar(df, x='date',y='water_lvl')
# fig.write_image('static/img/water_lvl.png')

# #line chart for turbidity
# fig = px.line(df, x='date',y='turbidity')
# fig.write_image('static/img/tur.png')

# #PH gauge 
# fig = go.Figure(go.Indicator(
# mode = "gauge+number",
# value = raw['ph'],
# domain = {'x': [0, 1], 'y': [0, 1]},
# title = {'text': "Ph Value"}))
# fig.write_image('static/img/ph.png')
url = 'https://aquamajorproject.herokuapp.com/update/1:2:3:4'
resp = requests.get(url)
print(resp)