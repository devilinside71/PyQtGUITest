# -*- coding: utf-8 -*-

"""Module implementing MainWindow."""

import logging
from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from .Ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, arguments, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.class_name = self.__class__.__name__
        log_name = 'program.' + self.class_name
        self.module_logger = logging.getLogger(log_name)
        self.module_logger.setLevel(logging.DEBUG)
        logger_fh = logging.FileHandler('program.log')
        logger_ch = logging.StreamHandler()
        logger_ch.setLevel(logging.INFO)
        self.args = arguments

        # create formatter and add it to the handlers

        formatter = \
            logging.Formatter(
                    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                              )
        logger_fh.setFormatter(formatter)
        logger_ch.setFormatter(formatter)

        # add the handlers to the logger

        self.module_logger.addHandler(logger_fh)
        self.module_logger.addHandler(logger_ch)
        self.setupUi(self)

    @pyqtSlot()
    def closeEvent(self, event):
        """
        Override original event.

        @param event original close event

        """
        _translate = QCoreApplication.translate
        quit_title = _translate('MainWindow', 'Confirmation')
        quit_msg = _translate('MainWindow',
                              'Are you sure you want to exit the program?')
        reply = QMessageBox.question(self, quit_title, quit_msg,
                                     QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.module_logger.debug('Confirmed to exit program')
            event.accept()
        else:
            event.ignore()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError

#     @pyqtSlot()
#     def on_pushButton_pressed(self):
#         """
#         Slot documentation goes here.
#         """
#         # TODO: not implemented yet
#         raise NotImplementedError

#     @pyqtSlot()
#     def on_pushButton_released(self):
#         """
#         Slot documentation goes here.
#         """
#         # TODO: not implemented yet
#         raise NotImplementedError
    
    @pyqtSlot()
    def on_actionQuit_triggered(self):
        """
        Slot documentation goes here.
        """
        self.close()
    
    @pyqtSlot()
    def on_actionSettings_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot()
    def on_actionAbout_triggered(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        raise NotImplementedError
