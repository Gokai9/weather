import requests

api_key = ""
with open("token.txt") as token:
    api_key = token.read()


def cityname(city: str, units='metric'):
    """metric = celcius \nimperial = farenhait
    """
    response = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&units={units}&appid={api_key}")

    return response.json()
