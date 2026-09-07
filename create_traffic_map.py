import folium

m = folium.Map(
    location=[41.8057, 123.4315],
    zoom_start=12
)

m.save("shenyang_traffic_map.html")

print("Traffic map created successfully!")