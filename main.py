from flask import Flask,render_template,request
import requests
import os

apiKey="439d4b804bc8187953eb36d2a8c26a02";
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/weather', methods=["GET","POST"])
def getweather():
    if request.method == 'POST':
        city= request.form['cityName']
        url = "https://openweathermap.org/data/2.5/weather?q=" + city + "&appid=" + apiKey + "&units=metric";
        r=requests.get(url)
        weatherData=r.json()
        di={}
        di['city']=weatherData['name']
        di['temp'] = weatherData['main']['temp']
        di['weatherDesc'] = weatherData['weather'][0]['description']
        di['icon'] = " http://openweathermap.org/img/wn/" + weatherData['weather'][0]['icon'] + "@2x.png";
        return render_template('weather.html',value=di)



if __name__ == '__main__':
    app.run()
