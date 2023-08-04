from

app = QApplication([])
main_window = QWidget()
text = QLabel('Натисни щоб дізнатись переможця')
winner = QLabel('?')
button = QPushButton('Згенерувати')

line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(winner, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)


def win():
    ran = randint(1, 100)
    winner.set.Text(str(ran))


button.clicked.connect(win)

main_window.setLayout(line)
main_window.show()
app.exec_()

main_window.show()
app.exec_()
