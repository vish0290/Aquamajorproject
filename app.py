from flask import Flask, jsonify, request, render_template
import plotly.graph_objects as go
import plotly.express as px
import json,os
import requests
import pyrebase
import pandas as pd

# creating a Flask app
app = Flask(__name__)



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


@app.route('/', methods = ['GET'])
def fetch_data():
    firebase=pyrebase.initialize_app(config)
    db = firebase.database()
    raw = json.loads(json.dumps(db.child('data').get().val()))
    dates_data = raw['dates']
    dates_keys = dates_data.keys()
    temp = []
    for i in dates_keys:
      d = {"date":i, "temp":dates_data[i]['Temp'], "turbidity":dates_data[i]['Turbidity'], 'water_lvl':dates_data[i]['Water level'] }
      temp.append(d)
    df = pd.DataFrame(temp)
    
    #Line Chart of water temperature 
    fig = px.line(df, x="date", y="temp", title='Water Temperature')
    fig.write_image('static/img/temp.png')

    #water level bar graph
    fig = px.bar(df, x='date',y='water_lvl')
    fig.write_image('static/img/water_lvl.png')

    #Line chart for turbidity
    fig = px.line(df, x='date',y='turbidity')
    fig.write_image('static/img/tur.png')

    #PH gauge 
    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = raw['ph'],
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Ph Value"}))
    fig.write_image('static/img/ph.png')



    
    return render_template('index.html')





    
if __name__ == '__main__':
  
    app.run(debug=True)
    