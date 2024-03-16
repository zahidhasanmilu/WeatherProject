import datetime
import requests
from django.shortcuts import render

def index(request):
    if request.method == "GET":
        city = request.GET.get('city')
        if not city:  # If the city is blank, use default location (Dhaka)
            city = 'Dhaka'

    appid = "c82f708fd3aa6ea0a49c877fa1cc01bd"
    url = "https://api.openweathermap.org/data/2.5/weather"

    parameters = {
        'q': city,
        'appid': appid,
        'units': 'metric'  # Corrected typo
    }

    try:
        response = requests.get(url=url, params=parameters)
        response.raise_for_status()  # Raise exception for unsuccessful responses
        data = response.json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
    except requests.exceptions.RequestException as e:
        # Handle API request errors gracefully
        description = "Error fetching data: " + str("city Not Found")
        icon = ""
        temp = ""

    day = datetime.date.today()

    context = {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city
    }

    return render(request, 'weatherapp/index.html', context)
