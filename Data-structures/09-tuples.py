#Tuples are imutable ordered listar that are recommended to be used with tightly connected pieces of data, luch as latitude and longitude or 3d coordinates

location = (13.4125, 103.866667)

print(type(location))
# <class 'tuple'="">

print("AngkorWat is at latitude: {}".format(location[0]))
# AngkorWat is at latitude: 13.4125

print("AngkorWat is at longitude: {}".format(location[1]))
# AngkorWat is at longitude: 103.866667