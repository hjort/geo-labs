import math

lat1 = 42.0095
lon1 = -122.3782

lat2 = 32.5288
lon2 = -117.2049

rLat1 = math.radians(lat1)
rLon1 = math.radians(lon1)
rLat2 = math.radians(lat2)
rLon2 = math.radians(lon2)

dLat = rLat2 - rLat1
dLon = rLon2 - rLon1

a = math.sin(dLat/2)**2 + math.cos(rLat1) * math.cos(rLat2) \
                        * math.sin(dLon/2)**2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
distance = 6371 * c

print("Great circle distance is {:0.0f} kilometers".format(distance))

