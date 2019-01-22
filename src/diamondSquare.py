import random

def diamondSquare(size):
    matrix = [[0.0 for i in range(size)] for j in range(size)]

    matrix[0][0] = round(random.random(),2)
    matrix[0][size-1] = round(random.random(),2)
    matrix[size-1][0] = round(random.random(),2)
    matrix[size-1][size-1] = round(random.random(),2)

    stepSize = size - 1
    rate = 0.25
    bound = 1

    while stepSize > 1:

        # Diamond step
        for x in range(0,size-1,stepSize):
            for y in range(0,size-1,stepSize):
                matrix[x + stepSize//2][y + stepSize//2] = diamondStep(matrix,x,y,stepSize,rate * random.uniform(-1,1))

        # Square step
        for x in range(stepSize//2,size,stepSize):
            for y in range(stepSize//2,size,stepSize):
                # Upper diamond
                matrix[x][y-stepSize//2] = squareStep(matrix,x-stepSize//2,y-stepSize//2,x+stepSize//2,y-stepSize//2,x,y,stepSize,rate * random.uniform(-bound,bound))
                # Lower diamond
                matrix[x][y+stepSize//2] = squareStep(matrix,x-stepSize//2,y+stepSize//2,x+stepSize//2,y+stepSize//2,x,y,stepSize,rate * random.uniform(-bound,bound))
                # Left diamond
                matrix[x-stepSize//2][y] = squareStep(matrix,x-stepSize//2,y-stepSize//2,x-stepSize//2,y+stepSize//2,x,y,stepSize,rate * random.uniform(-bound,bound))
                # Right diamond
                matrix[x+stepSize//2][y] = squareStep(matrix,x+stepSize//2,y-stepSize//2,x+stepSize//2,y+stepSize//2,x,y,stepSize,rate * random.uniform(-bound,bound))

        stepSize //= 2
        rate -= 0.03
        bound -= 0.15

    return matrix

def diamondStep(matrix,x,y,stepSize,r):
    value = sum([matrix[x][y],matrix[x][y+stepSize],matrix[x+stepSize][y],matrix[x+stepSize][y+stepSize]]) / 4
    return max(min(round(value,2) + r,1.0),0.0)

def squareStep(matrix,x1,y1,x2,y2,x3,y3,stepSize,r):
    value = sum([matrix[x1][y1],matrix[x2][y2],matrix[x3][y3]]) / 3
    return max(min(round(value,2) + r,1.0),0.0)
