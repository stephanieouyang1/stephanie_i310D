import math
def calculate_volume_of_sphere(radius):
  volume = 4/3 * (math.pi)*(radius**3)
  return volume
radi30 = calculate_volume_of_sphere(30)
radi40 = calculate_volume_of_sphere(40)
print(f"The area of a sphere with a radius of 30 is: {radi30}")
print(f"The area of a sphere with a radius of 40 is: {radi40}")
