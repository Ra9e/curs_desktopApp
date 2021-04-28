#   У меня есть 2 файла ui_t and ui, различия между ними только в том, как набирается время сообщения
#   в ui_t установлено поле со временем, а во втором просто поле для текста
#   это было сделано, чтобы проверить что эффективнее использовать

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtCore import QTimer
from ui1 import Ui_MainWindow  # Для работы с графическим интерфейсом
from PyQt5.QtWidgets import  QSystemTrayIcon, QMenu, QAction

from plyer import notification  # Для работы с уведомлениями

import time  # Для работы с временем
import datetime


class Notifier(QtWidgets.QMainWindow):
    def __init__(self):
        super(Notifier, self).__init__()  # Возвращает объект родителя notifier и возвращает его конструктор
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)  # Вызываем функцию setupUi чтобы отрисовать интерфейс
        self.init_UI()

    def init_UI(self):  # Функция для работы с графическим интерфейсом
        self.setWindowTitle('NotifyME')     # Устанавливаем название приложения
        self.setWindowIcon(QIcon('../загружено.png'))       # Картинку приложения
        self.ui.plainTextEdit.setPlaceholderText('for example: take your pills')    # Указываем пример текста
        self.ui.line_edit.setPlaceholderText('H')       # Указываем что здесь будут часы
        self.ui.line_edit_2.setPlaceholderText('M')     # Указываем что здесь будут минуты
        self.ui.pushButton.clicked.connect(self.alert_func)     # Подключаем кнопку к функции
        self.setFixedSize(449, 629)     # Устанавливаем неизменяемый размер окна

        # Делаем валидатор для времени, чтобы принимались только числа в определенном промежутке
        int_validator_hours = QIntValidator(self)
        int_validator_minutes = QIntValidator(self)
        int_validator_hours.setRange(0, 23)
        int_validator_minutes.setRange(0, 60)
        self.ui.line_edit.setValidator(int_validator_hours)
        self.ui.line_edit_2.setValidator(int_validator_minutes)

        # Создаём работу с треем (свернутым приложением)
        self.tray_icon = QSystemTrayIcon(self)                  # устанавливаем иконку
        self.tray_icon.setIcon(QIcon('C:\\Users\\guttl\\Desktop\\curs\\загружено1.ico'))
        # Делаем три действия (показать, скрыть и закрыть приложение)
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        # Подключаем их
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(app.quit)
        # Создаём само меню трея и показываем его
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

    # Функция проверки времени и вывода сообщения
    def timer_loop(self, time_obj, input_message):
        application.hide()
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

    # Функция для обработки сообщений и вывода уведомления
    def alert_func(self):

        if self.ui.plainTextEdit.toPlainText():  # Проверка, если строка пустая
            input_message = self.ui.plainTextEdit.toPlainText()
        else:
            input_message = 'Default Reminder'  # то выводим соообщение по умолчанию

        try:
            # Запоминаем введенное время пользователем
            input_time = self.ui.line_edit.text() + ':' + self.ui.line_edit_2.text()
            # Преобразовываем полученное число в объект времени
            time_obj = datetime.datetime.strptime(input_time, '%H:%M')
            # Подключаем таймер
            self.timer = QTimer()
            self.timer.timeout.connect(lambda: self.timer_loop(time_obj, input_message))
            self.timer.start(1000)
        except:
            pass


app = QtWidgets.QApplication([])  # Создаем экземпляр класса QApplication
application = Notifier()
application.show()

sys.exit(app.exec_())  # вызываем цикл обработки событий и возможность выхода из него
