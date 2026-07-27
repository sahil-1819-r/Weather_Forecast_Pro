    const locationBtn = document.getElementById("location-btn");

    locationBtn.addEventListener("click", () => {

        navigator.geolocation.getCurrentPosition(

            (position) => {

                console.log(position.coords.latitude);
                console.log(position.coords.longitude);

                document.getElementById("loading").style.display= "block";

                fetch("/location",{
                    method: "POST",
                    headers:{
                        "content-Type": "application/json"
                    },

                    body:JSON.stringify({
                        latitude: position.coords.latitude,
                        longitude: position.coords.longitude
                    })
                })

                .then(response => response.json())
                .then(data =>{
                    console.log (data);

                    document.getElementById("loading").style.display = "none"; 
                    document.getElementById("weather-result").innerHTML= `
                    
                    <div class= "weather-card">
                        
                    <h2>📍 ${data.city}, ${data.region}, ${data.country} </h2>
                        <img src= "https:${data.icon}" alt= "weather icon">
                        <h1>${data.temperature}°C</h1>
                        <h3>${data.condition}</h3>

                        <div class="weather-info">

                            <p>💧 Humidity : ${data.humidity}%</p>
                            <p>🌬 Wind Speed : ${data.wind_kph} km/h</p>

                        </div>

                    </div>`;
                })

            },

            () => {

                alert("Unable to fetch your location");

            }

        );

    });