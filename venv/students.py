import sys

from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QGridLayout, \
    QLineEdit, QPushButton, QComboBox

import sys
from datetime import datetime

class DistanceCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()
        distance_label = QLabel("Distance")
        self.distance_line_edit = QLineEdit()

        #create widgets
        time_label = QLabel("Time (hours)")
        self.time_line_edit = QLineEdit()

        self.combo = QComboBox()
        self.combo.addItems(['Metric(km)', 'Imperial(miles)'])


        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_distance)
        self.output_label = QLabel("")

        #adds Widgets to grid
        grid.addWidget(distance_label, 0,0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1, 1, 1)
        grid.addWidget(self.output_label, 3, 0, 2, 2)

        self.setLayout(grid)

    def calculate_distance(self):
        if self.combo.currentText() == 'Metric(km)':
            distance = self.distance_line_edit.text()
            time = self.time_line_edit.text()
            average_speed = int(distance) / int(time)
            self.output_label.setText(f"Average Speed: {average_speed}km/h ")
        if self.combo.currentText() == 'Imperial(miles)':
            distance = 0.621371 * int(self.distance_line_edit.text())
            time = self.time_line_edit.text()
            average_speed = distance / int(time)
            self.output_label.setText(f"Average Speed: {average_speed:.2f}mph")





app = QApplication(sys.argv)
distance_calculator = DistanceCalculator()
distance_calculator.show()
sys.exit(app.exec())