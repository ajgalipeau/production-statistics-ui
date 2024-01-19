from PyQt5.QtWidgets import QApplication
import sys
from gui import StatsCalculatorGUI

def main():
    app = QApplication(sys.argv)
    ex = StatsCalculatorGUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
