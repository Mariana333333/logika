import json

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel,
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout,
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)

app = QApplication([])
window = QWidget()

field_text = QTextEdit()

lb_notes = QLabel('Список заміток')

lst_notes = QListWidget()
btn_note_create = QPushButton('Створити замітку')
btn_note_del = QPushButton('Видалити замітку')
btn_note_save = QPushButton('Зберегти замітку')

lb_tags = QLabel('Список заміток')

lst_tag = QListWidget()

field_tag = QLineEdit()
btn_tag_add = QPushButton('Додати тег')
btn_tag_unpin = QPushButton('Відкріпити тег')
btn_tag_search = QPushButton('Шукати за тегом')

layout_notes = QHBoxLayout()
col1 = QHBoxLayout()
col2 = QHBoxLayout()

layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2, stretch=2)

col2.addWidget(lb_notes)
col2.addWidget(lst_notes)

row1 = QHBoxLayout()
row1.addWidget(btn_note_create)
row1.addWidget(btn_note_del)

col2.addLayout(row1)
col2.addWidget(btn_note_save)

with open('notes.json', 'r', encoding='utf8') as file:
    notes = json.load(file)

lst_notes.addItems(notes)


def show_notes():
    key = lst_notes.selectedItems()[0].text()
    field_text.setText(notes[key]['текст'])


lst_notes.itemClicked.connect(show_notes())

window.setLayout((layout_notes))
window.show()
app.exec_()
