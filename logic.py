from time import sleep as delay
from win32api import GetSystemMetrics
import pygame as pg

pg.init()

FPS = 60
clock = pg.time.Clock()

screen_width = GetSystemMetrics(0)
screen_height = GetSystemMetrics(1) - 64

map = 0
default = screen_width

g = 64*2
line = [[g*2,g*1],
        [g*2,g*2],
        [g*2,g*3],
        [g*2,g*4],
        [g*2,g*5],
        
        [g*3,g*1],
        [g*3,g*2],
        [g*3,g*3],
        [g*3,g*4],
        [g*3,g*5],

        [g*4,g*1],
        [g*4,g*2],
        [g*4,g*3],
        [g*4,g*4],
        [g*4,g*5],

        [g*5,g*1],
        [g*5,g*2],
        [g*5,g*3],
        [g*5,g*4],
        [g*5,g*5],

        [g*6,g*1],
        [g*6,g*2],
        [g*6,g*3],
        [g*6,g*4],
        [g*6,g*5],

        [g*7,g*1],
        [g*7,g*2],
        [g*7,g*3],
        [g*7,g*4],
        [g*7,g*5],

        [g*8,g*1],
        [g*8,g*2],
        [g*8,g*3],
        [g*8,g*4],
        [g*8,g*5],

        [g*9,g*1],
        [g*9,g*2],
        [g*9,g*3],
        [g*9,g*4],
        [g*9,g*5],

        [g*10,g*1],
        [g*10,g*2],
        [g*10,g*3],
        [g*10,g*4],
        [g*10,g*5],
        ]
g_c = ['#6db53b','#4f8828']
m_c = '#a6c690'

class map0:
    # HEALTH | INDEX
    health_data = [[120, 0],[120,0],[120,0],[120,0],[120,0]]
    # *** #
    # TYPE | LINE | X
    position_data = [['line1',default],
                     ['line2',default],
                     ['line3',default],
                     ['line4',default],
                     ['line5',default]]
    # *** #
    # LIST | INDEX | IMAGE
    sprite_data = [['Normal', None, 0, None],
                   ['Normal', None, 0, None],
                   ['Normal', None, 0, None],
                   ['Normal', None, 0, None],
                   ['Normal', None, 0, None]]
    # *** #