#   У меня есть 2 файла ui_t and ui, различия между ними только в том, как набирается время сообщения
#   в ui_t установлено поле со временем, а во втором просто поле для текста
#   это было сделано, чтобы проверить что эффективнее использовать

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QTimer
from ui1 import Ui_MainWindow                # Для работы с графическим интерфейсом
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QCheckBox, QSystemTrayIcon, \
    QSpacerItem, QSizePolicy, QMenu, QAction, QStyle, qApp

from plyer import notification              # Для работы с уведомлениями

import time                                 # Для работы с временем
import datetime

class Notifier(QtWidgets.QMainWindow):
    def __init__(self):
        super(Notifier, self).__init__()    # Возвращает объект родителя notifier и возвращает его конструктор
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)               # Вызываем функцию setupUi чтобы отрисовать интерфейс
        self.init_UI()

    def init_UI(self):                      # Функция для работы с графическим интерфейсом
        self.setWindowTitle('NotifyME')
        self.setWindowIcon(QIcon('../загружено.png'))
        self.ui.plainTextEdit.setPlaceholderText('for example: take your pills')
        self.ui.line_edit.setPlaceholderText('H')
        self.ui.line_edit_2.setPlaceholderText('M')
        self.ui.pushButton.clicked.connect(self.alert_func)
        pIntValidator = QIntValidator(self)
        pIntValidator.setRange(1, 99)
        self.ui.line_edit.setValidator(pIntValidator)
        self.ui.line_edit_2.setValidator(pIntValidator)
        self.setFixedSize(449, 629)

    def timer_loop(self, time_obj, input_message):
            current_time = time.strftime("%H:%M:%S")
            print(current_time)
            if current_time == str(time_obj.time()):  # совпало - выводим уведомление
                notification.notify(  # Устанавливаем заголовок, текст и картинку уведомлению
                    title='NotifyMe',  # Название уведомления
                    message=input_message,  # Текст
                    app_icon='C:\\Users\\guttl\\Desktop\\curs\\загружено1.ico',  # Картинка в формате ico
                    timeout=10,  # Время закрепления уведомления
                    app_name='NotifyMe',
                )
                self.timer.stop()

    def alert_func(self):                    # Функция для обработки сообщений и вывода уведомления

        if self.ui.plainTextEdit.toPlainText():                     # Проверка, если строка пустая
            input_message = self.ui.plainTextEdit.toPlainText()
        else:
            input_message = 'Default Reminder'                      # то выводим соообщение по умолчанию

        try:
            input_time = self.ui.line_edit.text()
            input_time += ':'
            input_time += self.ui.line_edit_2.text()
            time_obj = datetime.datetime.strptime(input_time, '%H:%M')  # Преобразовываем числа в объект времени
            # Подключаем таймер
            self.timer = QTimer()
            self.timer.timeout.connect(lambda:  self.timer_loop(time_obj, input_message))
            self.timer.start(1000)
        except:
            pass


app = QtWidgets.QApplication([])            # Создаем экземпляр класса QApplication
application = Notifier()
application.show()


sys.exit(app.exec_())                       # вызываем цикл обработки событий и возможность выхода из него
