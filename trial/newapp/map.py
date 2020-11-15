import plotly.graph_objects as go
from geopy import Nominatim
import os

lat1 = []
lon1 = []


def coordlat(place):
    g = Nominatim(user_agent='myGeocoder')
    location = g.geocode(place)
    return location.latitude


def coordlon(place):
    g = Nominatim(user_agent='myGeocoder')
    location = g.geocode(place)
    return location.longitude


def get_map(Place):
    for i in Place:
        lat1.append(coordlat(i))
        lon1.append(coordlon(i))

    # print (lat1)
    # print(lon1)

    fig = go.Figure(go.Scattermapbox(
        mode="markers+lines",
        lat=lat1,
        lon=lon1,
        marker={'size': 10}))

    fig.update_layout(
        margin={'l': 0, 't': 0, 'b': 0, 'r': 0},
        mapbox={

            'style': "open-street-map",

            'zoom': 2})

    fig.write_html(
        'C:/Users/ripti/Documents/PycharmProjects/new/trial/newapp/templates/newapp/display_map.html', include_plotlyjs='cdn')

# Place=['chennai','seoul','tokyo','delhi','kolkata','chennai']
# get_map(Place)
