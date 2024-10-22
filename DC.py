import pygame
import sys
import numpy as np
import random

mapwidth = 700
mapheight = 700
chunksize = 7
rows = int(mapwidth / chunksize)
collums = int(mapheight / chunksize)

size = mapwidth, mapheight

pygame.init()

screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))

shapepos = (mapwidth / 2, mapheight / 2)
nextpos = ((mapwidth / 2) + 14, (mapheight / 2))
#print(nextpos)
shape_size = (chunksize, chunksize)
shape_color = (255, 255, 255)

# make a pygame.Rect variable for the shape:
shape_rect = pygame.Rect(shapepos, shape_size)
shape_rect2 = pygame.Rect(nextpos, shape_size)

#clock = pygame.time.Clock()
#Set up an array of the map
DM = np.zeros((rows, collums))

def cardinal_check(DM, check_pos, cur_cell):
    nbrs_empty = True
    #Check North
    pos = (check_pos[0], check_pos[1] +1)
    if pos != cur_cell:
        if DM[pos[0]][pos[1]] != 0:
            return False
#Check East
    pos = (check_pos[0] + 1, check_pos[1])
    if pos != cur_cell:
        if DM[pos[0]][pos[1]] != 0:
            return False
#Check South
    pos = (check_pos[0], check_pos[1] - 1)
    if pos != cur_cell:
        if DM[pos[0]][pos[1]] != 0:
            return False
#Check West
    pos = (check_pos[0] - 1, check_pos[1])
    if pos != cur_cell:
        if DM[pos[0]][pos[1]] != 0:
            return False
    return True

#Create a randomly size room
def makeroom(DM, start_pos):
    roomsize = random.randrange(4, 36)
    cur_size = 1
    #fill in start pos chunk
    #print(start_pos)
    DM[start_pos[0]][start_pos[1]] = 1
    cur_cell = start_pos
    while cur_size < roomsize:
        for i in range (-1, 1):
            for j in range(-1, 1):
                if i != 0 and j != 0:
                    checkpos = (cur_cell[0] + i, cur_cell[1] + j)
                    if cardinal_check(DM, checkpos, cur_cell) == True:
                        #print("adding cell")
                        DM[checkpos[0]][checkpos[1]] = 1
                        cur_size += 1

makeroom(DM, (50, 50))
#print(DM)
rownum = 0
for row in DM:
        print(row)
        colnum = 0
        for element in row:
            if element == 1:
                posX = colnum * 7
                posY = rownum * 7
                position = (posX, posY)
                #print(position)
                room_fill = pygame.Rect(position, shape_size)
                screen.fill(shape_color, rect=room_fill)
            colnum += 1
        rownum += 1

while True:
    
    for event in pygame.event.get():
        # The pygame.QUIT event happens when someone tries to close the game window.
        if event.type == pygame.QUIT:
            sys.exit()
    
    #screen.fill(shape_color, rect=shape_rect)
    #screen.fill(shape_color, rect=shape_rect2)
    #pause = input(">>")
    pygame.display.flip()