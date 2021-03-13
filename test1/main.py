#   У меня есть 2 файла ui_t and ui, различия между ними только в том, как набирается время сообщения
#   в ui_t установлено поле со временем, а во втором просто поле для текста
#   это было сделано, чтобы проверить что эффективнее использовать

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui_t import Ui_MainWindow              # Для работы с графическим интерфейсом
import time                                 # Для работы с временем
from plyer import notification        # Для работы с уведомлениями


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
        self.ui.pushButton.clicked.connect(self.alert_func)

    def alert_func(self):                    # Функция для обработки сообщений и вывода уведомления
        input_message = self.ui.plainTextEdit.toPlainText()
        input_time = self.ui.timeEdit.text()

        notification.notify(                 # Устанавливаем заголовок, текст и картинку уведомлению
            title='NotifyMe',                # Название уведомления
            message=input_message,           # Текст
            app_icon='C:\\Users\\guttl\\Desktop\\curs\\загружено1.ico',     # Картинка в формате ico
            timeout=10,                      # Время закрепления уведомления
        )


app = QtWidgets.QApplication([])            # Создаем экземпляр класса QApplication
application = Notifier()
application.show()


sys.exit(app.exec_())                       # вызываем цикл обработки событий и возможность выхода из него
