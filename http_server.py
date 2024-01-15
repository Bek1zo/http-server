import sys, re, os, subprocess
from PyQt5 import QtWidgets, QtCore, QtGui
from http_server_ui import Ui_MainWindow


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # Инициализация UI
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()

        # Центровка
        qtRectangle = self.frameGeometry()
        centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.ui.setupUi(self)

        # Инициализация иконки трея
        self.icon = QtGui.QIcon('favicon.png')
        self.tray_icon = QtWidgets.QSystemTrayIcon()
        self.tray_icon.setIcon(self.icon)
        self.tray_icon.setVisible(True)

        # Изначальные значения
        self.log = []
        self.dir = "~"
        self.httpServerThread = None
        self.ui.stopButton.setEnabled(False)
        self.ui.serverAdress.setText(os.popen("hostname -I | awk '{print $1}'").read().strip())
        self.ui.serverPort.setText('8000')

        # Кнопки (Старт/Стоп/Каталог)
        self.ui.startButton.clicked.connect(self.start_server_thread)
        self.ui.stopButton.clicked.connect(self.stop_server_thread)
        self.ui.chooseDirButton.clicked.connect(self.choose_dir_menu)

        # Меню трея
        show_tray_action = QtWidgets.QAction("Развернуть", self)
        quit_tray_action = QtWidgets.QAction("Закрыть приложение", self)

        show_tray_action.triggered.connect(self.show)
        quit_tray_action.triggered.connect(self.closeEvent)

        tray_menu = QtWidgets.QMenu()
        tray_menu.addAction(show_tray_action)
        tray_menu.addAction(quit_tray_action)

        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        # Меню. (Инфо, трей, выход)
        self.ui.actionInfo.triggered.connect(self.show_info_box)
        self.ui.actionExit.triggered.connect(self.closeEvent)
        self.ui.actionTray.triggered.connect(self.hide)

    def choose_dir_menu(self):
        """ Открытие дополнительного окна с выбором каталога для расшаривания """
        self.dir = QtWidgets.QFileDialog.getExistingDirectory(self)

    def closeEvent(self, event):
        """ Переопределение метода выхода из приложения. """
        close = QtWidgets.QMessageBox.question(self,
                                               "Выход",
                                               "Вы действительно хотите завершить работу приложения?",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if close == QtWidgets.QMessageBox.Yes:
            if self.httpServerThread is not None:
                self.stop_server_thread()

            if not type(event) == bool:
                event.accept()
            else:
                sys.exit()
        else:
            event.ignore()

    def show_info_box(self):
        """ Отображение справки """
        popup_window = QtWidgets.QMessageBox.question(self, 'Справка',
                                                      'HTTP файловый сервер, который после запуска позволяет вам обмениваться файлами в локальной достаточно быстро и легко.\n\nДля запуска файлового сервера необходимо кликнуть "Запустить сервер", после чего открыть полученную ссылку в браузере, по умолчанию будет предоставлен доступ к вашему домашнему каталогу.',
                                                      QtWidgets.QMessageBox.Close)

    def start_server_thread(self):
        """ Создание нового треда и запуск сервера """
        self.kill_server()
        self.httpServerThread = QtCore.QThread(parent=self)
        self.httpServer = HttpServer()
        self.httpServer.dir = self.dir
        self.httpServer.port = self.ui.serverPort.toPlainText()
        self.httpServer.address = self.ui.serverAdress.toPlainText()
        self.httpServer.moveToThread(self.httpServerThread)
        self.httpServer.newLog.connect(self.add_log)
        self.httpServerThread.started.connect(self.httpServer.start_server)
        self.httpServerThread.start()

        self.ui.startButton.setEnabled(False)
        self.ui.stopButton.setEnabled(True)

    def stop_server_thread(self):
        """ Остановка треда сервера """
        self.kill_server()
        self.httpServerThread.exit()

        self.ui.startButton.setEnabled(True)
        self.ui.stopButton.setEnabled(False)

    def kill_server(self):
        """ Завершение процесса файлового сервера """
        shell_command = os.popen('lsof -i :{port} | grep python3'.format(port=self.ui.serverPort.toPlainText())).read()
        pid = (re.search(r'\s[0-9]*\s', shell_command))
        if pid is not None:
            pid = pid.group(0).strip()
            os.system('kill ' + pid)

    @QtCore.pyqtSlot(str)
    def add_log(self, logs):
        """ Запись логов """
        if logs == 'Terminated': logs = 'Сервер остановлен.'
        self.log.insert(0, logs)
        self.ui.history.setText('\n'.join(self.log))


class HttpServer(QtCore.QObject):
    newLog = QtCore.pyqtSignal(str)
    dir = None
    port = None
    address = None

    def start_server(self):
        """ Запуск файлового сервера """
        os.chdir(os.path.expanduser(self.dir))
        process = subprocess.Popen('python3 -m http.server --b ' + self.address + ' ' + self.port, stderr=subprocess.PIPE, bufsize=1, shell=True)
        self.newLog.emit("Сервер запущен по адресу: http://{address}:{port}/.\nДиректория: {dir}".format(address=self.address, port=self.port, dir=self.dir))

        while True:
            connections = process.stderr.readline()
            if connections == '' and process.poll() is not None:
                break

            if connections:
                self.newLog.emit(connections.strip().decode('utf-8'))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = MyWindow()
    application.show()
    sys.exit(app.exec())