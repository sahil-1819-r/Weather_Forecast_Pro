const locationBtn = document.getElementById("location-btn");

locationBtn.addEventListener("click", () => {

    navigator.geolocation.getCurrentPosition(

        (position) => {

            console.log(position.coords.latitude);
            console.log(position.coords.longitude);

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

            .then(respose => response.json())
            .then(data =>{
                console.log (data);
            })

        },

        () => {

            alert("Unable to fetch your location");

        }

    );

});