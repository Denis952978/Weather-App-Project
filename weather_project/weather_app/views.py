import requests
from django.shortcuts import render

def weather_view(request):
    api_key = "81a4a9575b96ec1a213c539dcd63cc69" 
    city = request.GET.get('city', 'London')  # Default city is London
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        weather = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'icon': data['weather'][0]['icon'],
        }
    else:
        weather = {
            'error': data.get('message', 'Unable to fetch weather data.')
        }

    return render(request, 'weather_app/weather.html', {'weather': weather})
