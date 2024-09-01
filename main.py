import pygame as pg
from image_treater import *
from logic import *

pg.init()

screen = pg.display.set_mode((screen_width, screen_height), pg.RESIZABLE)
pg.display.set_caption('Pvz - Remake')

run = [True]

def draw_grass(screen):
	#row0
	pg.draw.rect(screen, g_c[0], (line[0][0],line[0][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[1][0],line[1][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[2][0],line[2][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[3][0],line[3][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[4][0],line[4][1],g,g))
	#row1
	pg.draw.rect(screen, g_c[1], (line[5][0],line[0][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[6][0],line[1][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[7][0],line[2][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[8][0],line[3][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[9][0],line[4][1],g,g))
	#row2
	pg.draw.rect(screen, g_c[0], (line[10][0],line[0][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[11][0],line[1][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[12][0],line[2][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[13][0],line[3][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[14][0],line[4][1],g,g))
	#row3
	pg.draw.rect(screen, g_c[1], (line[15][0],line[0][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[16][0],line[1][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[17][0],line[2][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[18][0],line[3][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[19][0],line[4][1],g,g))
	#row4
	pg.draw.rect(screen, g_c[0], (line[20][0],line[0][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[21][0],line[1][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[22][0],line[2][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[23][0],line[3][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[24][0],line[4][1],g,g))
	#row5
	pg.draw.rect(screen, g_c[1], (line[25][0],line[0][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[26][0],line[1][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[27][0],line[2][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[28][0],line[3][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[29][0],line[4][1],g,g))
	#row6
	pg.draw.rect(screen, g_c[0], (line[30][0],line[0][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[31][0],line[1][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[32][0],line[2][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[33][0],line[3][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[34][0],line[4][1],g,g))
	#row7
	pg.draw.rect(screen, g_c[1], (line[35][0],line[0][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[36][0],line[1][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[37][0],line[2][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[38][0],line[3][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[39][0],line[4][1],g,g))
	#row8
	pg.draw.rect(screen, g_c[0], (line[40][0],line[0][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[41][0],line[1][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[42][0],line[2][1],g,g))
	pg.draw.rect(screen, g_c[1], (line[43][0],line[3][1],g,g))
	pg.draw.rect(screen, g_c[0], (line[44][0],line[4][1],g,g))

while run[0]:
	screen.fill('#84c15a')
	clock.tick(FPS)
	mouse = pg.mouse.get_pos()

	draw_grass(screen)

	for j in range(45):
		if (line[j][0]<mouse[0]<line[j][0]+g) and (line[j][1]<mouse[1]<line[j][1]+g):
			pg.draw.rect(screen, m_c, (line[j][0],line[j][1],g,g))

	if map0.health_data[0][0] == 120:
		if map0.sprite_data[0][0] == 'Normal':
			if map0.position_data[0][0] == 'line1':
				map0.sprite_data[0][1] = Zombies.Normal.idle.list
	
	map0.sprite_data[0][3] = map0.sprite_data[0][1][map0.sprite_data[0][2]]

	screen.blit(map0.sprite_data[0][3], (default, g*1))

	for event in pg.event.get():
		if event.type == pg.QUIT:
			run[0] = False
	
	pg.display.flip()

pg.quit()