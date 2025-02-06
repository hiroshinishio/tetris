 # -*- coding: utf-8 -*-
 
 import sys
-from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QHBoxLayout, QLabel
-from PyQt5.QtCore import Qt, QBasicTimer, pyqtSignal
-from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt6.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication, QHBoxLayout, QLabel
from PyQt6.QtCore import Qt, QBasicTimer, pyqtSignal
from PyQt6.QtGui import QPainter, QColor, QFont
 
 from board_manager import BOARD_DATA, Shape
 from block_controller import BLOCK_CONTROLLER