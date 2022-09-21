length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume_of_the_aquarium = length * width * height
volume_in_litres = volume_of_the_aquarium / 1000
occupied_space = volume_in_litres * (percent / 100)
need_litres = volume_in_litres - occupied_space
print(need_litres)
