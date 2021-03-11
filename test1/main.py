#   У меня есть 2 файла ui_t and ui, различия между ними только в том, как набирается время сообщения
#   в ui_t установлено поле со временем, а во втором просто поле для текста
#   это было сделано, чтобы проверить что эффективнее использовать

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui_t import Ui_MainWindow              #   Для работы с графическим интерфейсом


class Notifier(QtWidgets.QMainWindow):
    def __init__(self):
        super(Notifier, self).__init__()    #   Возвращает объект родителя noptyfier и возвращает его конструктор
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)               #   Вызываем функцию setupUi чтобы отрисовать интерфейс
        self.init_UI()

    def init_UI(self):                      #   Функция для работы с графическим интерфейсом
        self.setWindowTitle('NotifyME')
        self.setWindowIcon(QIcon('../загружено.png'))


app = QtWidgets.QApplication([])            #   Создаем экземпляр класса QApplication
application = Notifier()
application.show()


sys.exit(app.exec_())                       # вызываем цикл обработки событий и возможность выхода из него