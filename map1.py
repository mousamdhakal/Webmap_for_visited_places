import folium
import pandas
map = folium.Map(location = [27.672480,85.378214],zoom_start=100)
pop = []
data = pandas.read_csv("places.csv")
lat = list(data["LAT"])
lon = list(data["LON"])
pop = list(data["PLACE"])

fg = folium.FeatureGroup(name="My map")
for i,j,k in zip(lat,lon,pop):
    fg.add_child(folium.Marker(location = [i,j], popup = k , icon=folium.Icon(color='green')))


map.add_child(fg)

map.save("myMap.html")
