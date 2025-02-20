import requests
from django.shortcuts import render

def get_prayer_times(request):
    # API URL
    url = "http://api.aladhan.com/v1/timingsByCity"
    
    # API Parameters (City, Country, and Calculation Method)
    params = {
        "city": "Sheffield",
        "country": "United Kingdom",
        "method": 2  # Calculation method (2 for Islamic Society of North America)
    }
    
    # Send API request
    response = requests.get(url, params=params)
    data = response.json()
    
    # Check if the request was successful
    if response.status_code == 200:
        timings = data['data']['timings']
        return render(request, 'prayers/prayer_times.html', {'timings': timings})
    else:
        return render(request, 'prayers/error.html', {'error': 'Failed to fetch prayer times'})