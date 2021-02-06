import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic
import sqlite3

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)  # Загружаем дизайн
        # Обратите внимание: имя элемента такое же как в QTDesigner
        self.get_coffee()
    def get_coffee(self):
        con = sqlite3.connect("coffee.sqlite")
        col_name = ['id', 'название', "степень обжарки", "молотый/в зернах", "описание вкуса", "цена", "объем упаковки"]
        cur = con.cursor()
        result = cur.execute("""SELECT * FROM coffee """).fetchall()
        result.insert(0, col_name)
        self.table.setRowCount(len(result))
        self.table.setColumnCount(len(result[0]))
        print(result)
        for i in range(len(result)):
            for j in range(len(result[i])):
                print(result[i][j])
                self.table.setItem(i,j,QTableWidgetItem(str(result[i][j])))

        # Имя элемента совпадает с objectName в QTDesigner


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())