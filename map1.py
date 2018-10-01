import folium
map = folium.Map(location = [27.672480,85.378214],zoom_start=100)


fg = folium.FeatureGroup(name="My map")
fg.add_child(folium.Marker(location = [26.669453,87.382813], popup ="This is home", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("myMap.html")
