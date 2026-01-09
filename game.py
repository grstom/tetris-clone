import pygame
import random
from shapes import shape_options

class Tetris:
    def __init__(self, screen):
        self.blocks = []
        self.blockSize = 20
        self.screen = screen
        self.genTetriminos = True
        self.currentBlockPoints = []
        self.colors = [(220,20,60), (30,144,255), (255,255,0)]
        self.inactiveBlockPoints = []

        #timer
        self.speedlimit = 30
        self.speed = 1
        self.speedcounter = 0

    def CreateBlocks(self, screen_width, screen_height):
        for x in range(0, screen_width, self.blockSize):
            for y in range(0, screen_height, self.blockSize):
                rect = pygame.Rect(x, y, self.blockSize, self.blockSize)
                self.blocks.append(rect)


    # def showBlocks(self):
    #     for everything in self.blocks:
    #         pygame.draw.rect(self.screen, (255,255,255), everything, 1)

    def getBlockStart(self):
        rects = []

        #get all Y points at the top that start with 0
        for points in self.blocks:
            if points.y == 0:
                rects.append(points.x)

        dec = random.choice(rects)
        if dec >= 500:
            dec = random.choice(rects)
        else:
            return dec

    def createTetriminos(self):
        if self.genTetriminos:
            # print(self.getBlockStart())
            block = random.choice(shape_options)
            startingPoint = None        

            startingPoint = self.getBlockStart()
            if startingPoint == None:
                startingPoint = self.getBlockStart()

            if self.getBlockStart != None:
                row_count = 0
                for row in block:
                    col_count = startingPoint
                    for tile in row:
                        if tile == 1:
                            x = col_count
                            y = row_count
                            self.currentBlockPoints.append([x,y])
                        col_count += self.blockSize
                    row_count += self.blockSize


            #selected points

    def drawBlocks(self):
        #need to figure out a way to traverse the list and get the block points
        for everything_point in self.currentBlockPoints:
            # print(everything[0], everything[1])
            for everything_blocks in self.blocks:
                if everything_blocks.x == everything_point[0]:
                    if everything_blocks.y == everything_point[1]:
                        pygame.draw.rect(self.screen, (220,20,60), everything_blocks)
                else:
                    pygame.draw.rect(self.screen, (255,255,255), everything_blocks, 1)
                    print('drew block:', everything_point)

    def moveBlocks(self):
        keys = pygame.key.get_pressed()


        if keys[pygame.K_LEFT]:
            for points in self.currentBlockPoints:
                points[0] -= self.blockSize
        if keys[pygame.K_RIGHT]:
            for points in self.currentBlockPoints:
                points[0] += self.blockSize
        if keys[pygame.K_DOWN]:
            for points in self.currentBlockPoints:
                points[1] += self.blockSize


    # def checkBlocks(self):
    #     #make sure we don't go off screen: