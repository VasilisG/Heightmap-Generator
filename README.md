# Heightmap-Generator
A heightmap generator used for terrain generation made in Python.

The algorithms used for terrain generation are:

- [Diamond Square](https://en.wikipedia.org/wiki/Diamond-square_algorithm)
- [Midpoint Displacement](http://stevelosh.com/blog/2016/02/midpoint-displacement/#midpoint-displacement)

We can add color rules to our heightmap generator so that every pixel will get the color of the rule that satisfies.

Results can be saved in a `png` image format.

Below there are two use cases of that heightmap generator:

**Classic landscape**

```
from heightMapGenerator import *

heightMapGenerator = HeightMapGenerator()
heightMapGenerator.addRule(ColorRule(0.0, 0.05, (10,109,159)))
heightMapGenerator.addRule(ColorRule(0.05, 0.30, (13,141,205)))
heightMapGenerator.addRule(ColorRule(0.30, 0.40, (255,255,199)))
heightMapGenerator.addRule(ColorRule(0.40, 0.70, (0,150,0)))
heightMapGenerator.addRule(ColorRule(0.70, 0.90, (0,130,0)))
heightMapGenerator.addRule(ColorRule(0.90, 0.98, (139,69,19)))
heightMapGenerator.addRule(ColorRule(0.98, 1.0, (110,49,9)))

img = heightMapGenerator.createMap(1025,HeightMapGenerator.DIAMOND_SQUARE)
heightMapGenerator.saveImage(img, "terrain_6")
```

Result:

![alt text](https://github.com/VasilisG/Heightmap-Generator/blob/master/images/terrain_2.png)

**Desert landscape**

```
from heightMapGenerator import *

heightMapGenerator = HeightMapGenerator()
heightMapGenerator.addRule(ColorRule(0.0, 0.5, (230, 166, 68)))
heightMapGenerator.addRule(ColorRule(0.5, 0.65, (225, 131, 57)))
heightMapGenerator.addRule(ColorRule(0.65, 0.8, (182, 87, 29)))
heightMapGenerator.addRule(ColorRule(0.8, 0.95, (140, 51, 19)))
heightMapGenerator.addRule(ColorRule(0.95, 1.0, (133, 98, 42)))

img = heightMapGenerator.createMap(1025,HeightMapGenerator.DIAMOND_SQUARE)
heightMapGenerator.saveImage(img, "terrain_6")
```

Result:

![alt text](https://github.com/VasilisG/Heightmap-Generator/blob/master/images/terrain_4.png)
