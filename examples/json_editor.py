"""
This is a very basic usage example of the JSONCodeEdit.

The interface is minimalist, it will open a test file. You can open other
documents by pressing Ctrl+O
"""
import logging
import os
import random
import sys
from pyqode.qt import QtWidgets
from pyqode.core import api, modes
from pyqode.json.widgets import JSONCodeEdit


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)
        self.editor = JSONCodeEdit(self)
        self.setCentralWidget(self.editor)
        self.editor.file.open(
            os.path.abspath(os.path.join(
                '..', 'test', 'files', 'example.json')))
        # pygment_style = random.choice(modes.PYGMENTS_STYLES)
        # logging.info('pygments style: %s', pygment_style)
        # self.editor.syntax_highlighter.color_scheme = api.ColorScheme(
        #     pygment_style)


logging.basicConfig(level=logging.INFO)
app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
app.exec_()
