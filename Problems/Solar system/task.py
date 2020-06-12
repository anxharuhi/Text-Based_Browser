# create the planets.txt
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
file = open('planets.txt', 'wt', encoding='utf-8')
for planet in planets:
    file.write(planet + '\n')
file.close()