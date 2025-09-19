# testweightcovert
initial_weight = x
moon_ratio = 0.165
earth_weight = initial_weight
for year in range（1, 11）:
    moon_weight = earth_weight * moon_ratio
    print（"第{}年\t{:.2f}\t\t{:.2f}".format（year,earth_weight, moon_weight））
    earth_weight += 0.5
