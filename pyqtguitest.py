# -*- coding: utf-8 -*-
"""This module does blah blah."""
import argparse
import logging
import os
import sys
from pathlib import Path

from PyQt5 import QtCore,  QtWidgets

from ui.mainwindow import MainWindow


___copyright___ = 'Copyright (c) 2024 Laszlo Tamas'
___author___ = 'Laszlo Tamas'

# import locale

logger = logging.getLogger('pyqtguitest')
# set level for file handling (NOTSET>DEBUG>INFO>WARNING>ERROR>CRITICAL)

logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages

logger_fh = logging.FileHandler('pyqtguitest.log')

# create console handler with a higher log level

logger_ch = logging.StreamHandler()
logger_ch.setLevel(logging.INFO)

# create formatter and add it to the handlers

formatter = \
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                      )
logger_fh.setFormatter(formatter)
logger_ch.setFormatter(formatter)

# add the handlers to the logger

logger.addHandler(logger_fh)
logger.addHandler(logger_ch)


def parse_arguments():
    """
    Parse program arguments.

    @return arguments

    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-v', '--verbose',
                        help='increase output verbosity',
                        action='store_true')
    return parser.parse_args()


if __name__ == '__main__':

    args = parse_arguments()
    logger.debug('Start program')
    # Read loc_lang from settings file
    settings = QtCore.QSettings('settings.ini', QtCore.QSettings.IniFormat)
    settings.beginGroup('UserSettings')
    loc_lang = settings.value('Language')
    settings.endGroup()
    app = QtWidgets.QApplication(sys.argv)
    parent_path = os.path.join(__file__, os.path.pardir)
    dir_path = os.path.abspath(parent_path)
    file_path = os.path.join(dir_path, 'i18n',  loc_lang + '.qm')
    if Path(file_path).exists():
        translator = QtCore.QTranslator()
        translator.load(file_path)
        app.installTranslator(translator)
    ui = MainWindow(args)
    ui.show()
    sys.exit(app.exec_())
    logger.debug('Exit program')
