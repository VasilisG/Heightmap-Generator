class ColorRule:

    MIN = 0.0
    MAX = 1.0
    MIN_VALUE = 0
    MAX_VALUE = 255
    COLORS = 3

    def __init__(self, lowerBound, upperBound, color):
        if not (self.MIN <= lowerBound <= self.MAX):
            raise RuleError("RuleError", "'lowerBound' must within " + str(self.MIN) + " and " + str(self.MAX))
        if not (self.MIN <= upperBound <= self.MAX):
            raise RuleError("RuleError", "'upperBound' must within " + str(self.MIN) + " and " + str(self.MAX))
        if lowerBound > upperBound:
            lowerBound, upperBound = upperBound, lowerBound
        if not isinstance(color, tuple) or not len(color)==self.COLORS:
            raise RuleError("RuleError", "'color' must be a tuple of len==" + str(self.COLORS) + ".")
        for c in color:
            if not (self.MIN_VALUE <= c <= self.MAX_VALUE):
                raise RuleError("RuleError", "RGB value must be between " + str(self.MIN_VALUE) + " and " + str(self.MAX_VALUE))

        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.color = color

    def getColor(self):
        return self.color

    def contains(self, value):
        return self.lowerBound <= value <= self.upperBound

class RuleError(Exception):

    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors