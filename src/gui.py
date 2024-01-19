# Import modules
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu
import math
from collections import Counter

class StatsCalculatorGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Setup the GUI layout, menus, etc.
        pass

    # Define methods for each calculator input
    # Example:
    def combinations(n, r):
        return math.comb(n, r)

    def permutations(n, r):
        return math.perm(n, r)

    def variance(data):
        mean = sum(data) / len(data)
        return sum((x - mean) ** 2 for x in data) / len(data)

    def standard_deviation(data):
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        return math.sqrt(variance)

    def mean(data):
        return sum(data) / len(data)

    def median(data):
        data_sorted = sorted(data)
        n = len(data_sorted)
        mid = n // 2

        if n % 2 == 0:
            return (data_sorted[mid - 1] + data_sorted[mid]) / 2
        else:
            return data_sorted[mid]

    def mode(data):
        count = Counter(data)
        max_count = max(count.values())
        return [k for k, v in count.items() if v == max_count]