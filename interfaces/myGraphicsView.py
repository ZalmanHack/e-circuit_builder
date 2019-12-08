from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QGraphicsScene, QGraphicsView
from PyQt5.Qt import *

class MyGraphicView(QGraphicsView):
    class TypesLine:
        horizontal = 1
        vertical = 2
        upper = 3
        down = 4

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.initFunctions()

    def initUI(self):
        self.setFrameShape(QFrame.NoFrame)
        #self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.setAlignment(QtCore.Qt.AlignCenter)
        # сцена --------------------------------------------------------------------------------------------------------
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        # таймер отрисовки ---------------------------------------------------------------------------------------------
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout)
        self.timer.start(50)
        # шрифт --------------------------------------------------------------------------------------------------------
        self.font = QFont()
        self.font.setPixelSize(25)
        self.font.setBold(False)
        self.font.setFamily("Arial")
        # кисти --------------------------------------------------------------------------------------------------------
        self.pen = QPen(Qt.black)
        self.pen.setWidth(3)
        self.brush = QBrush(Qt.NoBrush)

    def initFunctions(self):
        self.matrix = []
        self.matrixWidth = 0
        self.matrixHeight = 0
        self.setTextSetting(textSize=7,fontSize=50)

    def timeout(self):
        """
        self._drawPredict("Шлюха",0,0)
        self._drawNode("2", 2, 0)
        self._drawLine(row=3,column=1)
        self._drawLine(self.TypesLine.down, 3, 0)
        width = 300
        height = 300
        self.scene.setSceneRect(0, 0, width, height)
        """
        self.timer.stop()

    @pyqtSlot(list)
    def setMatrix(self, matrix):
        self.matrixWidth = len(max([a for a in matrix]))
        self.matrixHeight = len(matrix)
        self.matrix = matrix

    @pyqtSlot(int, int)
    def setTextSetting(self, textSize: int = 0, fontSize: int = 0):
        self.font.setPixelSize(fontSize)
        self.textSize = textSize + 2
        self.itemHeight = self.font.pixelSize() * 2
        self.itemWidth = self.textSize * self.font.pixelSize()
        if self.itemWidth < self.itemHeight:
            self.itemWidth = self.itemHeight

    # отрисовка текста__________________________________________________________________________________________________
    def _drawText(self, text: str = "", row: int = 0, column: int = 0):
        global_pos = QPoint(self.itemWidth*column, self.itemHeight*row)
        g_text = QGraphicsTextItem(text)
        g_text.setDefaultTextColor(QColor(Qt.black))
        g_text.setFont(self.font)
        g_text.setScale(1)
        text_lenght = g_text.boundingRect().width()
        print(text_lenght)
        start = QPoint()  # начальная позиция для текущей отрисовки
        start.setY(self.itemHeight/5)
        start.setX(self.itemWidth/2 - text_lenght/2)
        self.scene.addItem(g_text)
        g_text.setPos(start.x() + global_pos.x(), start.y() + global_pos.y())

    def _drawPredict(self, text: str = "", row: int = 0, column: int = 0):
        global_pos = QPoint(self.itemWidth * column, self.itemHeight * row)
        indent = self.itemHeight/2  # отступ для задания ромбиков
        polygon = QPolygonF()
        polygon.append(QPoint(global_pos.x() + indent,
                              global_pos.y()))
        polygon.append(QPoint(global_pos.x() + self.itemWidth - indent,
                              global_pos.y()))
        polygon.append(QPoint(global_pos.x() + self.itemWidth,
                              global_pos.y() + indent))
        polygon.append(QPoint(global_pos.x() + self.itemWidth - indent,
                              global_pos.y() + self.itemHeight))
        polygon.append(QPoint(global_pos.x() + indent,
                              global_pos.y() + self.itemHeight))
        polygon.append(QPoint(global_pos.x(),
                              global_pos.y() + indent))
        self.scene.addPolygon(polygon, self.pen, self.brush)
        self._drawText(text,row,column)

    def _drawFunctional(self, text: str = "", row: int = 0, column: int = 0):
        global_pos = QPoint(self.itemWidth * column, self.itemHeight * row)
        polygon = QPolygonF()
        polygon.append(QPoint(global_pos.x(),
                              global_pos.y()))
        polygon.append(QPoint(global_pos.x() + self.itemWidth,
                              global_pos.y()))
        polygon.append(QPoint(global_pos.x() + self.itemWidth,
                              global_pos.y() + self.itemHeight))
        polygon.append(QPoint(global_pos.x(),
                              global_pos.y() + self.itemHeight))
        self.scene.addPolygon(polygon, self.pen, self.brush)
        self._drawText(text, row, column)

    def _drawNode(self, text: str = "", row: int = 0, column: int = 0):
        global_pos = QPoint(self.itemWidth * column, self.itemHeight * row)
        ellipse_pos = QPoint(global_pos.x() + self.itemWidth/2 - self.itemHeight/2,
                             global_pos.y())
        line1 = QLineF(global_pos.x(), global_pos.y() + self.itemHeight/2,
                       ellipse_pos.x(), global_pos.y() + self.itemHeight/2)
        line2 = QLineF(ellipse_pos.x() + self.itemHeight, global_pos.y() + self.itemHeight/2,
                       global_pos.x() + self.itemWidth, global_pos.y() + self.itemHeight/2)
        self.scene.addLine(line1, self.pen)
        self.scene.addEllipse(QRectF(ellipse_pos.x(), ellipse_pos.y(),
                                     self.itemHeight,self.itemHeight), self.pen, self.brush)
        self.scene.addLine(line2, self.pen)
        self._drawText(text, row, column)

    def _drawLine(self, type = TypesLine.horizontal, row: int = 0, column: int = 0):
        global_pos = QPoint(self.itemWidth * column, self.itemHeight * row)
        if type == self.TypesLine.horizontal:
            line = QLineF(global_pos.x(), global_pos.y() + self.itemHeight / 2,
                           global_pos.x() + self.itemWidth, global_pos.y() + self.itemHeight / 2)
            self.scene.addLine(line, self.pen)
        elif type == self.TypesLine.vertical:
            line = QLineF(global_pos.x() + self.itemWidth/2, global_pos.y(),
                           global_pos.x() + self.itemWidth/2, global_pos.y() + self.itemHeight)
            self.scene.addLine(line, self.pen)
        elif type == self.TypesLine.upper:
            line = QLineF(global_pos.x() + self.itemWidth/2, global_pos.y() + self.itemHeight/2,
                           global_pos.x() + self.itemWidth/2, global_pos.y() + self.itemHeight)
            self.scene.addLine(line, self.pen)
            line = QLineF(global_pos.x() + self.itemWidth/2, global_pos.y() + self.itemHeight/2,
                           global_pos.x() + self.itemWidth, global_pos.y() + self.itemHeight/2)
            self.scene.addLine(line, self.pen)
        elif type == self.TypesLine.down:
            line = QLineF(global_pos.x() + self.itemWidth/2, global_pos.y() + self.itemHeight/2,
                           global_pos.x() + self.itemWidth/2, global_pos.y())
            self.scene.addLine(line, self.pen)
            line = QLineF(global_pos.x() + self.itemWidth/2, global_pos.y() + self.itemHeight/2,
                           global_pos.x() + self.itemWidth, global_pos.y() + self.itemHeight/2)
            self.scene.addLine(line, self.pen)

    # проверка на то, является ли элемент узлом ________________________________________________________________________
    def _is_knot(self, searchingElement: str):
        if searchingElement[0] == "(" or searchingElement[-1] == ")":
            return True
        return False

    @pyqtSlot()
    def draw(self):
        self.scene.clear()
        self.scene.setSceneRect(0,0,0,0)
        for row in range(0, len(self.matrix)):
            for column in range(0, len(self.matrix[row])):
                item = self.matrix[row][column]
                if item is not None and item != "":
                    if item == "┌":
                        self._drawLine(self.TypesLine.upper, row, column)
                    elif item == "└":
                        self._drawLine(self.TypesLine.down, row, column)
                    elif item == "─":
                        self._drawLine(self.TypesLine.horizontal, row, column)
                    elif item == "│":
                        self._drawLine(self.TypesLine.vertical, row, column)
                    elif self._is_knot(item):
                        self._drawNode("".join(list(item)[1:-1]), row, column)
                    elif list(item)[-1] == "┤":
                        self._drawPredict("".join(list(item)[:-1]), row, column)
                    else:
                        self._drawFunctional(item, row, column)

    def wheelEvent(self, e: QWheelEvent):
        print(e.x(), e.y(), e.angleDelta())
        if e.angleDelta().y() > 0:
            self.scale(1.1, 1.1)
        else:
            self.scale(0.9, 0.9)