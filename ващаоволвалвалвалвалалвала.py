from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QGroupBox, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Калькулятор')
main_win.resize(400, 500)

exp = QLabel('выражение')
opers_group = QGroupBox()
zero = QPushButton('0')
one = QPushButton('1')
two = QPushButton('2')
three = QPushButton('3')
four = QPushButton('4')
five = QPushButton('5')
six = QPushButton('6')
seven = QPushButton('7')
eight = QPushButton('8')
nine = QPushButton('9')
equal = QPushButton('=')
plus = QPushButton('+')
minus = QPushButton('-')
divide = QPushButton('/')
multiply = QPushButton('*')
clear = QPushButton('AC')


hline1 = QHBoxLayout()
hline2 = QHBoxLayout()
#тут были еще 3 линии

vline1 = QVBoxLayout()
vline2 = QVBoxLayout()
vline3 = QVBoxLayout()
vline4 = QVBoxLayout()

hline1.addWidget(exp, alignment=Qt.AlignRight)

#создаю первый столбик операторов
vline1.addWidget(clear, alignment=Qt.AlignCenter)
vline1.addWidget(two, alignment=Qt.AlignCenter)
vline1.addWidget(five, alignment=Qt.AlignCenter)
vline1.addWidget(eight, alignment=Qt.AlignCenter)

#создаю второй столбик операторов
vline2.addWidget(zero, alignment=Qt.AlignCenter)
vline2.addWidget(three, alignment=Qt.AlignCenter)
vline2.addWidget(six, alignment=Qt.AlignCenter)
vline2.addWidget(nine, alignment=Qt.AlignCenter)

#создаю третий столбик операторов
vline3.addWidget(one, alignment=Qt.AlignCenter)
vline3.addWidget(four, alignment=Qt.AlignCenter)
vline3.addWidget(seven, alignment=Qt.AlignCenter)
vline3.addWidget(equal, alignment=Qt.AlignCenter)

#создаю четвертый стоблбик операторов
vline4.addWidget(plus, alignment=Qt.AlignCenter) 
vline4.addWidget(minus, alignment=Qt.AlignCenter) 
vline4.addWidget(multiply, alignment=Qt.AlignCenter) 
vline4.addWidget(divide, alignment=Qt.AlignCenter) 

#добавляю на горизонталь
hline2.addLayout(vline1)
hline2.addLayout(vline2)
hline2.addLayout(vline3)
hline2.addLayout(vline4)

#добавляю это всё в группу кнопок
opers_group.setLayout(hline2)

main_line = QVBoxLayout()
main_line.addLayout(hline1)
main_line.addWidget(opers_group)

main_win.setLayout(main_line)

main_win.show()
app.exec_()