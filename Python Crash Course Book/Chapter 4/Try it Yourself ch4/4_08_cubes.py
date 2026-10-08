# 4-8. Cubes
# Make a list of the first 10 cubes and use a for loop to print the value of each cube.

cubes = []

for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

for cube in cubes:
    print(cube)
