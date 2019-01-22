import random
from PIL import Image

def midpointDisplacement(size):
    matrix = [[0.0 for i in range(size)] for j in range(size)]

    matrix[0][0] = random.random()
    matrix[0][size-1] = random.random()
    matrix[size-1][0] = random.random()
    matrix[size-1][size-1] = random.random()

    stepSize = size-1
    rate = 0.25
    bound = 1

    while stepSize > 1:
        for x in range(0,size-1,stepSize):
            for y in range(0,size-1,stepSize):
                # Upper midpoint
                matrix[x+stepSize//2][y] = max(min((matrix[x][y] + matrix[x+stepSize][y]) / 2 + (rate * random.uniform(-bound,bound)),1.0),0.0)
                # Lower midpoint
                matrix[x+stepSize//2][y+stepSize] = max(min((matrix[x][y+stepSize] + matrix[x+stepSize][y+stepSize]) / 2 + (rate * random.uniform(-bound,bound)),1.0),0.0)
                # Left midpoint
                matrix[x][y+stepSize//2] = max(min((matrix[x][y] + matrix[x][y+stepSize]) / 2 + (rate * random.uniform(-bound,bound)),1.0),0.0)
                # Right midpoint
                matrix[x+stepSize][y+stepSize//2] = max(min((matrix[x+stepSize][y] + matrix[x+stepSize][y+stepSize]) / 2 + (rate * random.uniform(-bound,bound)),1.0),0.0)
                # Center
                matrix[x+stepSize//2][y+stepSize//2] = max(min((matrix[x+stepSize//2][y] + matrix[x+stepSize//2][y+stepSize] + matrix[x][y+stepSize//2] + matrix[x+stepSize][y+stepSize//2]) / 4 +  (rate * random.uniform(-bound,bound)),1.0),0.0)

        stepSize //= 2   
        rate -= 0.03    
    return matrix