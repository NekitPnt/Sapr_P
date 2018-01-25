import sys, os
import numpy as np
from interface import *
from PyQt5 import QtWidgets, QtCore, QtGui

class mySapr(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setupUi(self)

        #image button
        self.refresh.clicked.connect(self.refresh_plot)      

        #zadelka
        self.left_zadel.clicked.connect(self.left_zadelka)
        self.right_zadel.clicked.connect(self.right_zadelka)
        self.dual_zadel.clicked.connect(self.dual_zadelka)
        
        #menu
        self.menu_open.triggered.connect(self.file_open)
        self.menu_save.triggered.connect(self.file_save)
        self.menu_rasschet.triggered.connect(self.raschet)
        #TODO       
        self.menu_help.triggered.connect(self.help)        
        self.menu_about.triggered.connect(self.info)

    #----------------------------------------------------------------
    uzli_mas = []    
    ster_hei = []
    ster_upr = []
    ster_napr = []
    sili_SU = []
    sili_type = []
    sili_value = []
    
    left_zd = True
    right_zd = False

    def raschet(self):
        if self.check_arrays():
            l = []
            for i in range(len(self.uzli_mas)-1):
                l.append(self.uzli_mas[i+1] - self.uzli_mas[i])
            e = self.ster_upr
            a = self.ster_hei
            u = len(l)+1 #размер массива узлов
            k = []

            for i in range(len(l)):
                k.append(e[i]*a[i]/l[i])

            m = [0] * u
            for i in range(u):
                m[i] = [0] * u
            m[0][0] = k[0]
            m[-1][-1] = k[-1]
    
            if len(m) > 2:   
                for i in range(len(m)-1):
                    for j in range(len(m)-1):
                        if i == j:
                            m[i][j+1] = -k[i]
                            m[i+1][j] = -k[i]

                for i in range(1, len(m)-1):
                    m[i][i] = k[i] + k[i-1]
                    
            #---------vector b---------------
            f = [0] * u
            q = [0] * len(l)

            for i in range(len(self.sili_type)):
                if self.sili_type[i] == 1:
                    f[self.sili_SU[i]-1] = (self.sili_value[i])
                elif self.sili_type[i] == 2:
                    q[self.sili_SU[i]-1] = (self.sili_value[i]*l[self.sili_SU[i]-1]/2)

            #print(q)
            #print(f)
            #print(k)
            b = [q[0] + f[0]]
            for i in range(1, u-1):
                b.append(q[i-1] + q[i] + f[i])
            b.append(q[-1] + f[-1])            

            if self.left_zd:
                m[0][0] = 1
                m[0][1] = 0
                b[0] = 0
            if self.right_zd:
                m[-1][-1] = 1
                m[-1][-2] = 0
                b[-1] = 0

            M = np.array(m)
            det = np.linalg.det(M)
            if det != 0:
                delta = list(np.linalg.solve(M, b))
                del_mes = 'deltas = ['
                for i in delta:
                    del_mes += str(i)+', '
                del_mes += ']'
                QtWidgets.QMessageBox.information(self,
                    "Результаты расчета", del_mes,
                    buttons = QtWidgets.QMessageBox.Close)
                
            else:
                self.det_error()
                
        else: self.allert_NAN()

    def refresh_plot(self):
        if self.check_text():
            #узлы--------------------------------------
            self.uzli_mas = self.conv(self.Uzli_table.toPlainText())            
            self.uzli_mas.sort()
            #стержни-----------------------------------
            self.ster_hei = self.conv(self.Ster_table_3.toPlainText())
            self.ster_upr = self.conv(self.Ster_table_4.toPlainText())
            self.ster_napr = self.conv(self.Ster_table_5.toPlainText())
            #силы--------------------------------------
            self.sili_SU = self.conv(self.Sili_table_1.toPlainText())
            self.sili_type = self.conv(self.Sili_table_2.toPlainText())
            self.sili_value = self.conv(self.Sili_table_3.toPlainText())

            if self.check_arrays():
                self.draw()
            else: self.allert_NAN()
        else: self.allert()
            
    
    def check_arrays(self):
        flag = True
        if len(self.uzli_mas) < 2: flag = False 
        if len(self.ster_hei) != len(self.uzli_mas)-1: flag = False
        if len(self.ster_upr) != len(self.uzli_mas)-1: flag = False 
        if len(self.ster_napr) != len(self.uzli_mas)-1: flag = False
        for i in self.ster_upr:
            if i < 0: flag = False
        for i in self.ster_napr:
            if i < 0: flag = False

        for i in self.sili_SU:
            if i > len(self.uzli_mas): flag = False
            if self.sili_type == 2 and self.sili_SU > len(self.sili_SU):
                flag = False
        if len(self.sili_type) != len(self.sili_SU): flag = False
        if len(self.sili_value) != len(self.sili_SU): flag = False
        return flag
    
    def check_text(self):
        flag = True
        if self.Uzli_table.toPlainText() == '': flag = False
        if self.Ster_table_3.toPlainText() == '': flag = False
        if self.Ster_table_4.toPlainText() == '': flag = False
        if self.Ster_table_5.toPlainText() == '': flag = False
        if self.Sili_table_1.toPlainText() == '': flag = False
        if self.Sili_table_2.toPlainText() == '': flag = False
        if self.Sili_table_3.toPlainText() == '': flag = False
        return flag
    
    def file_save(self):
        name = QtWidgets.QFileDialog.getSaveFileName(self,
            'Сохранить файл', 'C:\Python36\PROJECTS\Sapr', 'Sapr (*.sapr)')[0]
        if not name:
            self.name_allert()
        elif self.check_text() and self.check_arrays():
            file = open(name, 'w')
            file.write(self.Uzli_table.toPlainText()+'\n')
            file.write(self.Ster_table_3.toPlainText()+'\n')
            file.write(self.Ster_table_4.toPlainText()+'\n')
            file.write(self.Ster_table_5.toPlainText()+'\n')
            file.write(self.Sili_table_1.toPlainText()+'\n')
            file.write(self.Sili_table_2.toPlainText()+'\n')
            file.write(self.Sili_table_3.toPlainText())
            file.close()
        else: self.allert()
    
    def file_open(self):
        text_arr = []
        name = QtWidgets.QFileDialog.getOpenFileName(self,
            'Открыть файл', 'C:\Python36\PROJECTS\Sapr', 'Sapr (*.sapr)')[0]
        if name:
            file = open(name, 'r')
            with file:
                for line in file:
                    data = line.rstrip('\n')
                    text_arr.append(data)
            #узлы--------------------------------------
            self.Uzli_table.setText(text_arr[0])
            #стержни-----------------------------------
            self.Ster_table_3.setText(text_arr[1])
            self.Ster_table_4.setText(text_arr[2])
            self.Ster_table_5.setText(text_arr[3])
            #силы--------------------------------------
            self.Sili_table_1.setText(text_arr[4])
            self.Sili_table_2.setText(text_arr[5])
            self.Sili_table_3.setText(text_arr[6])
            
        if self.check_text():
            self.refresh_plot()

    def draw(self):
        scene = QtWidgets.QGraphicsScene()
        self.paint_widget.setScene(scene)
        pen = QtGui.QPen(QtCore.Qt.black)
        noPen = QtGui.QPen(QtCore.Qt.NoPen)
        osPen = QtGui.QPen(QtCore.Qt.DashDotLine)
        sPen = QtGui.QPen(QtCore.Qt.red)
        rPen = QtGui.QPen(QtCore.Qt.green)
        rrPen = QtGui.QPen(QtCore.Qt.green)
        sPen.setWidth(3)
        rrPen.setWidth(3)
        brush = QtGui.QBrush(QtCore.Qt.DiagCrossPattern)
        brush2 = QtGui.QBrush(QtGui.QColor(40, 250, 40),
                              QtCore.Qt.VerPattern)
        
        uzli_arr = self.uzli_mas.copy()
        ster_hei = self.ster_hei.copy()
        for i in range(len(uzli_arr)):
            uzli_arr[i] = uzli_arr[i] * 50
        for i in range(len(ster_hei)):
            ster_hei[i] = ster_hei[i] * 50

        middle = 140
        x0 = 615/2 - (uzli_arr[-1] - uzli_arr[0])/2
        sh = 10
        scene.addLine(0, middle, 615, middle, osPen)
        
        #отрисовка заделки
        for i in range(len(uzli_arr)-1):
            r = QtCore.QRectF(x0+uzli_arr[i]+sh, middle-ster_hei[i]/2,
                              uzli_arr[i+1]-uzli_arr[i], ster_hei[i])
            scene.addRect(r, pen)
        #----------------------------------------------------------------------
        #отрисовка сил
        for j in range(len(self.sili_SU)):
            i = self.sili_SU[j]-1
            if self.sili_type[j] == 1:
                if self.sili_value[j] > 0:
                    scene.addLine(x0+uzli_arr[i]+sh*2, middle-sh,
                              x0+uzli_arr[i]+sh*3, middle, sPen)
                    scene.addLine(x0+uzli_arr[i]+sh*2, middle+sh,
                              x0+uzli_arr[i]+sh*3, middle, sPen)
                    scene.addLine(x0+uzli_arr[i]+sh, middle,
                              x0+uzli_arr[i]+sh*3, middle, sPen)
                elif self.sili_value[j] < 0:
                    scene.addLine(x0+uzli_arr[i], middle-sh,
                              x0+uzli_arr[i]-sh, middle, sPen)
                    scene.addLine(x0+uzli_arr[i], middle+sh,
                              x0+uzli_arr[i]-sh, middle, sPen)
                    scene.addLine(x0+uzli_arr[i]+sh, middle,
                              x0+uzli_arr[i]-sh, middle, sPen)
                elif self.sili_value[j] == 0:
                    pass
            elif self.sili_type[j] == 2:
                if self.sili_value[j] > 0:
                    r = QtCore.QRectF(x0+uzli_arr[i]+sh, middle-sh,
                              uzli_arr[i+1]-uzli_arr[i], sh*2)
                    scene.addRect(r, rPen, brush2)
                    #стрелка вправо-----------------------------------
                    scene.addLine(x0+uzli_arr[i]+sh*3, middle-sh,
                              x0+uzli_arr[i]+sh*4, middle, rrPen)
                    scene.addLine(x0+uzli_arr[i]+sh*3, middle+sh,
                              x0+uzli_arr[i]+sh*4, middle, rrPen)
                    scene.addLine(x0+uzli_arr[i]+sh, middle,
                              x0+uzli_arr[i]+sh*4, middle, rrPen)
                elif self.sili_value[j] < 0:
                    r = QtCore.QRectF(x0+uzli_arr[i]+sh, middle-sh,
                              uzli_arr[i+1]-uzli_arr[i], sh*2)
                    scene.addRect(r, rPen, brush2)
                    #стрелка влево-------------------------------------
                    scene.addLine(x0+uzli_arr[i+1]-sh, middle-sh,
                              x0+uzli_arr[i+1]-sh*2, middle, rrPen)
                    scene.addLine(x0+uzli_arr[i+1]-sh, middle+sh,
                              x0+uzli_arr[i+1]-sh*2, middle, rrPen)
                    scene.addLine(x0+uzli_arr[i+1]+sh, middle,
                              x0+uzli_arr[i+1]-sh*2, middle, rrPen)
                elif self.sili_value[j] == 0:
                    pass
            else:
                QtWidgets.QMessageBox.critical(self, "Ахтунг!",
                    'Введены неверные данные в поле "Типы сил"!',
                    defaultButton = QtWidgets.QMessageBox.Ok)
                
        #--------------------------------------------------------------
        #отрисовка заделок
        if self.left_zd:
            rl = QtCore.QRectF(x0+uzli_arr[0], middle-ster_hei[0]/2-sh,
                               sh-1, ster_hei[0]+2*sh)
            scene.addRect(rl, noPen, brush)
            
        if self.right_zd:
            rr = QtCore.QRectF(x0+uzli_arr[-1]+sh+1, middle-ster_hei[-1]/2-sh,
                              sh+1, ster_hei[-1]+2*sh)
            scene.addRect(rr, noPen, brush)
                
    def left_zadelka(self):
        self.left_zd = True
        self.right_zd = False
        self.refresh_plot()
            
    def right_zadelka(self):
        self.left_zd = False
        self.right_zd = True
        self.refresh_plot()

    def dual_zadelka(self):
        self.right_zd = True
        self.left_zd = True
        self.refresh_plot()

    def conv(self, data):
        data = data.split(' ')
        for i in range(len(data)):
            data[i] = int(data[i])
        return data
    
    def allert(self):
        QtWidgets.QMessageBox.critical(self, "Ахтунг!",
            "Введены не все данные!", defaultButton = QtWidgets.QMessageBox.Ok)
            
    def name_allert(self):
         QtWidgets.QMessageBox.critical(self, "Ахтунг!",
            "Файл не был сохранен!", defaultButton = QtWidgets.QMessageBox.Ok)
    
    def allert_NAN(self):
        QtWidgets.QMessageBox.critical(self, "Ахтунг!",
            "Введены неверные данные!", defaultButton = QtWidgets.QMessageBox.Ok)

    def det_error(self):
        QtWidgets.QMessageBox.critical(self, "Ахтунг!",
            "Вырожденная матрица!", defaultButton = QtWidgets.QMessageBox.Ok)

    def info(self):
        QtWidgets.QMessageBox.about(self,
                    "О разработчике", 'Программа Sapr_P разработана Панариным Никитой специально для предмета "Компуктерная механика", 2017г.')
    def help(self):
        QtWidgets.QMessageBox.about(self,
                    "Пимощь", 'Вводите данные через пробел, координаты узлов начинаются с "0", расстояние между узлами считается в метрах, площадь считается в квадратных метрах, количество чисел во всех полях "Стержни" должно совпадать друг с другом, количество чисел во всех полях "Силы" должно совпадать друг с другом, в поле "Тип" группы "Силы" допустим ввод только "1" и "2", в полях "Упругость" и "Максимальное напряжение" отрицательные числа недопустимы, перед рассчетом конструкции убедитесь что все заделки выставленны.')
        
        
if __name__ == '__main__':
    SappR = QtWidgets.QApplication(sys.argv)
    mySappR = mySapr()
    mySappR.show()
    sys.exit(SappR.exec_())
