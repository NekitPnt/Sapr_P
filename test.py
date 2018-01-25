"""
file = open('input.txt', 'r')
words, country1, user_id1 = [], [], []
for line in file:
    word = line.rstrip('\n').split(';')
    try:
        country1.append(word[2])
        words.append(word)
    except IndexError:
        continue

file = open('1.sapr', 'r')
with file:
    data = file.read().split(',')
    for i in range(len(data)):
        data[i] = int(data[i])
    print(data)

class lol:
    #def __init__(self, parent = None):
    left_zd = 1
    right_zd = 0
        
    def kek(self):
        print (self.left_zd, self.right_zd)

if __name__ == '__main__':
    mySappR = lol()
    mySappR.kek()

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QBrush
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.setGeometry(300, 300, 355, 280)
        self.setWindowTitle('Brushes')
        self.show()


    def paintEvent(self, e):

        qp = QPainter()
        qp.begin(self)
        self.drawBrushes(qp)
        qp.end()


    def drawBrushes(self, qp):

        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 15, 90, 60)

        brush.setStyle(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 15, 90, 60)

        brush.setStyle(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 15, 90, 60)

        brush.setStyle(Qt.Dense3Pattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush.setStyle(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 105, 90, 60)

        brush.setStyle(Qt.Dense5Pattern)
        qp.setBrush(brush)
        qp.drawRect(130, 105, 90, 60)

        brush.setStyle(Qt.Dense6Pattern)
        qp.setBrush(brush)
        qp.drawRect(250, 105, 90, 60)

        brush.setStyle(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(10, 195, 90, 60)

        brush.setStyle(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(130, 195, 90, 60)

        brush.setStyle(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(250, 195, 90, 60)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

import sys, time
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.targetBtn = QPushButton('target', self)
        self.targetBtn.move(100, 100)
        self.targetBtn.clicked.connect(self.sleep5sec)

        self.setGeometry(100, 100, 300, 300)
        self.show()

    def sleep5sec(self):
        self.targetBtn.setEnabled(False)
        #time.sleep(5)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())    

data = '0 50 150 -200'
def converter(data):
    data = data.split(' ')
    for i in range(len(data)):
        data[i] = int(data[i])
    sum(data)
    return data
print(converter(data))

data = '0 50 150 200'.split(' ')
for i in range(len(data)):
    print(data[i])
    #data[i] = int(data[i])
print(data)

class a:
    uzli_arr = []
    def open():
        #name = 'C:\Python36\PROJECTS\Sapr\1.sapr'
        #file = open(name, 'r')
        #with file:
        data = '0 1 2 3'
        print(data)
            #self.uzli_arr = self.conv(data)

    def conv(data):
        data = data.split(' ')
        for i in range(len(data)):
            data[i] = int(data[i])
        return data
if __name__ == '__main__':
    b = a.open()

sili_SU = [1, 2, 3, 4]
sili_type = [1, 2, 1, 1]
for j in range(len(sili_SU)):
    i = (sili_SU[j]-1)
    if sili_type[i] == 1:
        print('1', i)
    else:
        print('2', i)
        
text = '1, 2 3'
def conv(data):
    data = data.split(' ')
    for i in range(len(data)):
        if data[i].isdigit():
            data[i] = int(data[i])
        else: return al()
    return data

def al():
    mes = 'allert'
    return mes

print(conv(text))

a = []
if len(a) == 0 or len(a) == 1:print('0')
else:print('1')

a = [1, 2, 3]
b = []
b = a.copy()
print(b)
"""


"""
import numpy as np


a = [2, 3, 1, 1]
b = [1, 3, 1, 6]
c = [1, 4, 1, 1]
e = [1, 1, 1, 5]

A = [a, b, c, e]

d = [1, 2, 3, 4]

m = np.array(A)
v = np.array(d)
delta = list(np.linalg.solve(m, v))
for i in delta: round(i, 2)
print(delta)

k = np.linalg.det(A)
"""
#print(k)

#E - ster_upr
#A - ster_hei
#L - len_arr
#F - sili_value(sili_type = 1)
#Q - sili_value(sili_type = 2)
#K - E[i]*A[i]/L[i]
import numpy as np

#e = [1, 9, 1, 1]
#a = [1, 1, 2, 1]
#l = [2, 1, 2, 3]
#l=[2,4]
#a=[2,1]
#e=[1,1]
l=[2,1]
a=[2,1]
e=[1,1]
u = len(l)+1#len(self.uzli_mas)
k = []

for i in range(len(l)):
    k.append(a[i]*e[i]/l[i])

#print(k)
#k = [1, 2, 3]
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

m[0][1] = 0
#m[-1][-2] = 0
M = np.array(m)

#--------------------------
s = [2, 2]
t = [1, 2]
z = [-2,1]
f = [0] * u
q = [0] * len(l)

for i in range(len(t)):
    if t[i] == 1:
        f[s[i]-1] = (z[i])
    elif t[i] == 2:
        q[s[i]-1] = (z[i]/2)
print(f)
print(q)

b = [q[0] + f[0]]
for i in range(1, u-1):
    b.append(q[i-1]+q[i]+f[i])
b.append(q[-1]+f[-1])

#print(f)
#print(q)
print(b)
    

"""

v = [0,-1.5,0.5]#np.array([1,2,2,4,1])
#delta = []
det = np.linalg.det(M)
if det != 0:
    delta = list(np.linalg.solve(M, v)) 
    print(delta)

for i in m:
    print(i)
"""
























