import json
import random
import webbrowser
with open('nycsubwaystops.json','r') as thefile:
    data=thefile.read()
obj=json.loads(data)
Stop_list=[]
service_list=[]
C_longlat=[]
Distances=["0-10",'10-20','20-30']
Direction=["North","East","South","West"]
Activity=["Restaurant for Dinner","Lunch/Brunch Spot","Cafe","Museum or Historical Landmark","Bar","Park","Cool Store","Place with Live Music","Something Cool!"]
information=obj['data']
for stops in information:
    Stop_list.append(stops[10])
    service_list.append(stops[12])
    
C_stop=random.choice(Stop_list)

for x in information:
    if C_stop==x[10]:
        longlat=x[11]
longlat=longlat.split(" ")
longlat=longlat[1:]
for lat in longlat:
    if "(" in lat:
        lat=lat.replace("(","")
    if ")" in lat:
        lat=lat.replace(")","")
    C_longlat.append(lat)

C_service=random.choice(service_list)
C_distances=random.choice(Distances)
C_direction=random.choice(Direction)
C_activity=random.choice(Activity)
url="https://www.google.com/maps/@"+str(C_longlat[1])+","+str(C_longlat[0])+",15z"
print(url)
webbrowser.open(url)
print("Take the subway to",C_stop, "with service on lines",C_service,".", "You should walk",C_distances, "minutes", C_direction, "to a", C_activity)



