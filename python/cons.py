class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")
Point1=Point()
Point1.x=10
Point1.y=20
print(Point1.x,Point1.y)
Point1.draw()