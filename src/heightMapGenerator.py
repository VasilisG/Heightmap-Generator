import math
from random import random
from midpointDisplacement import midpointDisplacement
from diamondSquare import diamondSquare
from rule import ColorRule
from PIL import Image

class HeightMapGenerator:

    MIDPOINT_DISPLACEMENT = 1
    DIAMOND_SQUARE = 2

    def __init__(self):
        self.ruleList = []
        self.heightMap = None
        self.size = 0

    def addRule(self, rule):
        self.ruleList.append(rule)

    def addRules(self, rules):
        if not rules is None:
            rules = list(rules)
            self.ruleList.extend(rules)

    def createHeightMapPixels(self):
        size = len(self.heightMap)
        pixels = []
        for x in range(size):
            for y in range(size):
                for rule in self.ruleList:
                    if rule.contains(self.heightMap[x][y]):
                        pixels.append(rule.getColor())
                        break
        return pixels

    def createMap(self,size,method):
        img = Image.new("RGB", (size,size))
        self.createHeightMap(size,method)
        pixels = self.createHeightMapPixels()
        img.putdata(pixels)
        return img

    def createHeightMap(self, size, method):
        self.size = size
        if method == self.MIDPOINT_DISPLACEMENT:
            self.heightMap = midpointDisplacement(size)
        elif method == self.DIAMOND_SQUARE:
            self.heightMap = diamondSquare(size)
        else:
            return None
        return self.heightMap

    def saveImage(self, img, name):
        if not img is None:
            img.save(name + ".png")

    def printHeightMap(self):
        for i in range(len(self.heightMap)):
            for j in range(len(self.heightMap)):
                print("%.2f" % self.heightMap[i][j], end=" ")
            print()