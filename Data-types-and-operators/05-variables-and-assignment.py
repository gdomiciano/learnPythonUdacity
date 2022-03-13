# variable in python should always be lowercase with underscores, rest of JS rules apply.

mv_population = 74728 # assignment
mv_population += 4000 # plus equal assignment
mv_population -= 600 # less equal assignment
print(mv_population)

# --- QUIZ --- #
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
print(reservoir_volume)
# The amount of rainfall from a storm (in cubic metres
rainfall = 5e6
print(rainfall)

# decrease the rainfall variable by 10% to account for runoff
# rainfall -= rainfall*0.1
rainfall *= .9
print(rainfall)

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall
print(reservoir_volume)
# increase reservoir_volume by 5% to account for stormwater that flows into the reservoir in the days following the storm
# reservoir_volume += reservoir_volume*0.05
reservoir_volume *= 1.05
print(reservoir_volume)
# decrease reservoir_volume by 5% to account for evaporation
# reservoir_volume -= reservoir_volume*0.05
reservoir_volume *= 0.95
print(reservoir_volume)
# subtract 2.5e5 cubic metres from reservoir_volume to account for water that's piped to arid regions.
print(2.2e5)
reservoir_volume -= 2.2e5
# print the new value of the reservoir_volume variable
print(reservoir_volume)