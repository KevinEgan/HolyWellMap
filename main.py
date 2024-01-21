
import folium
import pandas as pd

data = pd.read_csv("NMS_OpenData_20230420_HolyWell_csv.csv")

mappy = folium.Map(location=(53.199787, -8.738516), zoom_start=6, tiles="cartodb positron")
fg = folium.FeatureGroup(name="MyMap")

lat = list(data["LATITUDE"])
long = list(data["LONGITUDE"])
name = ['Name not found' if name == ' ' else name for name in data["LATEST_EDI"]]
location = list(data["TOWNLAND"])
desc = list(data["WEB_NOTES"])

html = """<h4>Holy well:</h4>
Location: %s 
\nName: %s
"""

for i, j, k, l in zip(lat, long, name, location):
    iframe = folium.IFrame(html=html % (str(l), str(k)), width=200, height=100)
    fg.add_child(folium.Marker(location=(i, j), popup=folium.Popup(iframe), icon=folium.Icon(color='green')))

mappy.add_child(fg)

mappy.save("Map1.html")
