from turtle import Turtle, Screen
import math

class ECircuit_Draw():

    def __init__(self):
        try:
            self.matrix = []

            self.textSize = 1
            self.fontSize = 30
            self.itemWidth = 100    # размер в пикселях
            self.itemHeight = self.fontSize * 4   # размер в пикселях

            self.matrixWidth = 0
            self.matrixHeight = 0

            self.circuit = Turtle()
            self.circuit.speed(0)
            self.circuit.pensize(2)
            self.circuit.screen.colormode(255)
            self.circuit.pencolor(0, 0, 0)
            self.circuit.fillcolor(255,255,255)
            #self.circuit.pencolor(112, 109, 83)
            #self.circuit.fillcolor(212,208,176)
            self.circuit.hideturtle()
        except Exception as e:
            print(e.args)


    def setMatrix(self, matrix):
        self.matrixWidth = len(max([a for a in matrix]))
        self.matrixHeight = len(matrix)
        self.matrix = matrix

    def setTextSetting(self, textSize, fontSize):
        self.fontSize = fontSize
        self.textSize = textSize
        self.itemHeight = self.fontSize * 3
        self.itemWidth = self.textSize*self.fontSize
        if self.itemWidth < self.itemHeight:
            self.itemWidth = self.itemHeight


    def _drowText(self, text, indent=False):
        self.circuit.up()
        if indent:
            self.circuit.forward(self.itemWidth / 2 - self.itemHeight / 2)
        else:
            self.circuit.forward(self.itemWidth / 2)
        self.circuit.right(90)
        self.circuit.forward(self.itemHeight / 2 + self.fontSize / 2)
        self.circuit.write(text, True, align="center", font=("Arial", self.fontSize, 'bold'))
        self.circuit.right(270)
        self.circuit.down()


    def _drawFunctionalItem(self, text, x, y):
        x = x * self.itemWidth
        x += self.itemWidth
        y*=-self.itemHeight

        self.circuit.up()
        self.circuit.goto(x, y)
        self.circuit.down()

        self.circuit.begin_fill()
        for _ in range(2):
            for size in [self.itemWidth, self.itemHeight]:
                self.circuit.forward(size)
                self.circuit.right(90)
        self.circuit.end_fill()

        self._drowText(text, indent=False)


    def _drawPredicateItem(self, text, x, y):
        x = x * self.itemWidth
        x += self.itemWidth
        y*=-self.itemHeight

        self.circuit.up()
        self.circuit.goto(x, y)
        self.circuit.forward(self.itemHeight / 2)
        self.circuit.down()

        line = math.sqrt(math.pow(self.itemHeight / 2, 2) + math.pow(self.itemHeight / 2, 2))
        self.circuit.begin_fill()
        for _ in range(2):
            self.circuit.forward(self.itemWidth - self.itemHeight)
            self.circuit.right(45)
            self.circuit.forward(line)
            self.circuit.right(90)
            self.circuit.forward(line)
            self.circuit.right(45)
        self.circuit.end_fill()

        self._drowText(text, indent=True)


    def _drawStartEnd(self, type, x, y):
        x = x * self.itemWidth
        x += self.itemWidth
        y*=-self.itemHeight

        self.circuit.up()
        self.circuit.goto(x, y)
        self.circuit.forward(self.itemHeight / 2)
        self.circuit.down()

        self.circuit.begin_fill()
        self.circuit.right(180)
        self.circuit.circle(self.itemHeight / 2, 180)
        self.circuit.forward(self.itemWidth - self.itemHeight)
        self.circuit.circle(self.itemHeight / 2, 180)
        self.circuit.forward(self.itemWidth - self.itemHeight)
        self.circuit.right(180)
        self.circuit.end_fill()

        if type.upper() not in ['START', 'END']:
            type = "START"

        self._drowText(type, indent=True)


    def _drawAngle(self, type, x, y):
        x = x * self.itemWidth
        x += self.itemWidth
        y*=-self.itemHeight

        self.circuit.up()
        self.circuit.goto(x + self.itemWidth, y)
        self.circuit.right(90)
        self.circuit.forward(self.itemHeight / 2)
        self.circuit.right(90)
        self.circuit.down()

        angle = 90
        if type.upper() == "UP":
            angle = 270

        self.circuit.forward(self.itemWidth / 2)
        self.circuit.right(angle)
        self.circuit.forward(self.itemHeight / 2)
        self.circuit.right(angle)


    def _drawLine(self, type, x, y):
        x = x * self.itemWidth
        x += self.itemWidth
        y*=-self.itemHeight


        self.circuit.up()
        self.circuit.goto(x, y)
        self.circuit.down()

        if type.upper() == "HORIZONTAL":
            self.circuit.up()
            self.circuit.right(90)
            self.circuit.forward(self.itemHeight / 2)
            self.circuit.right(270)
            self.circuit.down()
            self.circuit.forward(self.itemWidth)
        else:
            self.circuit.up()
            self.circuit.forward(self.itemWidth / 2)
            self.circuit.right(90)
            self.circuit.down()
            self.circuit.forward(self.itemHeight)
            self.circuit.right(270)


    def draw(self):
        # задаем размер сцены
        self.circuit.screen.screensize(self.matrixHeight * self.itemWidth * 10, self.matrixHeight * self.itemHeight * 15)
        for i in range(self.matrixHeight):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == "│":
                    self._drawLine("vertical", j, i)
                elif self.matrix[i][j] == "─":
                    self._drawLine("horizontal", j, i)
                elif self.matrix[i][j] == "└":
                    self._drawAngle("down", j, i)
                elif self.matrix[i][j]  == "┌":
                    self._drawAngle("up", j, i)
                elif len(self.matrix[i][j]) > 0 and list(self.matrix[i][j])[-1] == "┤":
                    temp = list(self.matrix[i][j])
                    temp.remove("┤")
                    temp = ''.join(temp)
                    self._drawPredicateItem(temp, j, i)
                elif str(self.matrix[i][j]).upper() == 'START':
                    self._drawStartEnd(self.matrix[i][j], j, i)
                elif str(self.matrix[i][j]).upper() == 'END':
                    self._drawStartEnd(self.matrix[i][j], j, i)
                elif self.matrix[i][j] != '':
                    self._drawFunctionalItem(self.matrix[i][j], j, i)
        self.circuit.screen.exitonclick()
        del self.circuit
        # self.circuit.screen.mainloop()



if __name__ == "__main__":

    while True:
        wn = Screen()
        wn.bgcolor("black")
        wn.title("Space invaders")

        border_pen = Turtle()
        border_pen.speed("fastest")
        border_pen.color("white")
        border_pen.pensize(3)

        border_pen.penup()
        border_pen.setposition(-300, -300)
        border_pen.pendown()

        for side in range(4):
            border_pen.forward(600)
            border_pen.left(90)

        border_pen.hideturtle()


        wn.exitonclick()
        input("121232231")