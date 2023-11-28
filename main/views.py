from bs4 import BeautifulSoup
from django.shortcuts import render
import requests
import html


def fectdata(city):
    city = city.replace(" ", "+")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers["User-Agent"] = USER_AGENT
    session.headers["Accept-Language"] = LANGUAGE
    session.headers["Content-Language"] = LANGUAGE

    response = session.get(f"https://www.bing.com/search?q={city}+weather&FORM=AWRE")

    return response


def wetherapp(request):
    response = None
    if request.POST.get("city"):
        city = request.POST.get("city")
        response = fectdata(city).text

        op = BeautifulSoup(response, "html.parser")

        place = op.find("span", attrs={"class": "wtr_foreGround"}).text
        heat = op.find("div", attrs={"class": "wtr_currTemp b_focusTextLarge"}).text
        wind = op.find("div", attrs={"class": "wtr_currWind"}).text
        humidity = op.find("div", attrs={"class": "wtr_currHumi"}).text

        response = {
            "data": [place, heat, wind, humidity],
        }
    return render(request, "index.html", response)
