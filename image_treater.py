import pygame as pg

pg.init()

def get(url):
	return pg.image.load(url)

def zoom2x(image):
	return pg.transform.scale2x(image)

class Plants:
	class Peashooter:
		class idle:
			list = []
			# for i in range(7):
				# list.append(zoom2x(get(f"asset/")))

class Zombies:
	class Normal:
		class idle:
			list = []
			for i in range(4):
				list.append(zoom2x(get(f"asset/zombies/normal/idle/{i}.png")))
		class dying:
			list = []
			for i in range(7):
				list.append(zoom2x(get(f"asset/zombies/normal/dying/{i}.png")))