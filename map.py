import folium
from folium.plugins import MousePosition

m = folium.Map([31.86502, -116.60339], zoom_start=14)
# Posicion del Mouse
MousePosition().add_to(m)

Sauzal = [
    [31.8676, -116.62343],
    [31.86786, -116.62327],
    [31.8677, -116.62284],
    [31.86668, -116.62338],
    [31.8671, -116.62458],
    [31.8672, -116.62451],
    [31.86919, -116.62355]
]

folium.PolyLine(
    locations=Sauzal,
    color="#109DFA",
    weight=4,
    tooltip="Ruta Sauzal",
).add_to(m)

m.save("templates/Mapa.html")