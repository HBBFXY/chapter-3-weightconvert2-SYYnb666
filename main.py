initial_weight = float(input())
annual_gain = 0.5
moon_ratio = 0.165
for year in range(1, 11):
    earth_weight = initial_weight + annual_gain * year
    moon_weight = earth_weight * moon_ratio
    print("{}\t{:.2f}\t\t{:.2f}".format(year, earth_weight, moon_weigh))
