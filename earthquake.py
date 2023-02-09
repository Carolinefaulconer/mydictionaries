
import json
infile = open("eq_data.json", "r")
data = json.load(infile) 


print("number of earthquakes:", len(data["features"]))
print()

eq_dict = {}
i = 0
for earthquake in data["features"]:
    if earthquake["properties"]["mag"] > 6:
        eq_dict[i] = {
            "location": earthquake["properties"]["place"],
            "magnitude": earthquake["properties"]["mag"],
            "longitude": earthquake["geometry"]["coordinates"][0],
            "latitude": earthquake["geometry"]["coordinates"][1],
        }
        i += 1

print("new dictionary of earthquakes with magnitude > 6:", eq_dict) 
print()

for i, earthquake in eq_dict.items():
    print("Location:", earthquake["location"])
    print("Magnitude:", earthquake["magnitude"])
    print("Longitude:", earthquake["longitude"])
    print("Latitude:", earthquake["latitude"])
    print()







