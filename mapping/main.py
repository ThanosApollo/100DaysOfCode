import folium 

map = folium.Map(location=[38.5, 99.09], zoom_start=6, tiles="Stamen Terrain")
map.save("mapping/Map1.html")