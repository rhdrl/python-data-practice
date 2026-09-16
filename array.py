temp = [21.5, 22.3, 19.8, 23.1,]

print(temp)
print(temp[0])
print(temp[1])
print(temp[2])
print(temp[3])


print(temp[:2])
print(temp[2:])

temp.append(24.5)
temp[0] = 20.0
print(temp)

year = 2026
city = "Incheon"
value = [10, 20, 30, 40]

print(type(year))
print(type(city))
print(type(value))
print(len(value))

weather = { "city": "Incheon", "temp":27.5, }

print(type(weather))
print(len(weather))

print(weather.keys())
for key in weather.keys():
    print(key)

print(weather.values())
for value in weather.values():
    print(value)

print(weather.items())
for key, value in weather.items():
    print(key, value)

