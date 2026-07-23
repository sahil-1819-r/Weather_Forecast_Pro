from flask import Flask, render_template, request, jsonify
from services.weather_service import get_weather, get_weather_by_coordinates

app =   Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    
    city= "" 
    weather= None
    error= None
    
    if request.method == "POST":
               
            city= request.form.get("city")
            weather= get_weather(city)

            if weather is None:
                  error = "City not found!"
    return render_template("index.html", city=city, weather= weather, error= error)
                  
@app.route("/location", methods=["POST"])
def location_weather():

    data = request.get_json()

    latitude = data["latitude"]
    longitude = data["longitude"]
    
    weather = get_weather_by_coordinates(latitude, longitude)

    print(latitude, longitude)

    return jsonify({weather})
        
if  __name__== "__main__":
    app.run(debug=True) 