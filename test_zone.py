from math import pi, sin, cos, atan2
import matplotlib as plt


print(sin(pi))


class Vector:
    def __new__(cls, *args):
        if len(args) == 2:
            return Vector2(*args)
        elif len(args) == 3:
            return Vector3(*args)
        else:
            raise ValueError("Vector must be 2D or 3D")
        
    def magnitude(self):
        return (self.x**2 + self.y**2)**0.5
    
    def direction(self):
        for args in self.__dict__.values():
            print(args)

class Vector2(Vector):
    def __init__(self, *args):
        if args and len(args) == 2:
            self.x = args[0]
            self.y = args[1]
    
    
class Vector3(Vector):
    def __init__(self, *args):
        if args and len(args) == 3:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
    
    def magnitude(self):
        return (self.x**2 + self.y**2 + self.z**2)**0.5
    
    def direction(self):
        return (atan2(self.y, self.x), atan2(self.z, (self.x**2 + self.y**2)**0.5))
    
    
print(Vector(3, 4).magnitude(), Vector(3, 4).direction())


class Shapes:
    def __init__(self, size: int, type):
        pass
        