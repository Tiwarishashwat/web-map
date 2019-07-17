import folium
import pandas
data=pandas.read_excel("maps.xlsx",sheet_name=0)
lt=list(data["Lat"])
ln=list(data["Lon"])
col=list(data["Color"])
name=list(data["Loc"])
map=folium.Map(location=[20.5,78.9],zoom_start=5)
fgv=folium.FeatureGroup(name="Cities of india")
for i,j,k,l in zip(lt,ln,col,name):
    fgv.add_child(folium.Marker(location=[i,j],popup=l,icon=folium.Icon(color=k)))
fg=folium.FeatureGroup(name="Population chart")
fg.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 10000000 <=x['properties']['POP2005']<20000000 else 'red'}))
map.add_child(fg)
map.add_child(fgv)
map.add_child(folium.LayerControl())
map.save("India.html")
