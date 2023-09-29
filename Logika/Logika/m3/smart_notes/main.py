import json
def WriteToFile():
    with open('notes.json', 'w', 'encoding=utf8') as file:
        json.dump(notes, file, ensure_ascii=False, sort_keys=True, indent=4)




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

lb_tags = QLabel('Список тегів')

lst_tag = QListWidget()

field_tag = QLineEdit()
btn_tag_add = QPushButton('Додати тег')
btn_tag_unpin = QPushButton('Відкріпити тег')
btn_tag_search = QPushButton('Шукати за тегом')

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2, stretch=1)

col1.addWidget(field_text)


0

col2.addWidget(lb_notes)
col2.addWidget(lst_notes)

row1 = QHBoxLayout()
row1.addWidget(btn_note_create)
row1.addWidget(btn_note_del)

col2.addLayout(row1)
col2.addWidget(btn_note_save)

col2.addWidget(lb_tags)


with open('notes.json', 'r', encoding='utf8') as file:
    notes = json.load(file)

lst_notes.addItems(notes)


def show_notes():
    key = lst_notes.currentItem().text()
    field_text.setText(notes[key]['текст'])

    lst_tag.addItems(notes[key]['тег'])
    lst_tag.clear()

def add_note():
    note_name, ok = QInputDialog.getText(window, 'Додати замітку', 'Назва замітки')
    if note_name and ok:
        lst_notes.addItems(note_name)
        notes[note_name] = {"текст": "", "теги": []}


def del_note():
    if lst_notes.currentItem():
        key = lst_notes.currentItem().text()
        del notes[key]

        field_text.clear()
        field_tag.clear()
        lst_notes.clear()
        lst_notes.addItems(notes)

        WriteToFile()
    def save_note():
        if lst_notes.currentItem():
            key = lst_notes.currentItem().text()


            print(notes[key]['текс'])



btn_note_save.clicked.connect(save_note())
btn_note_del.clicked.connect(del_note)



btn_note_create.clicked.connect(add_note())

lst_notes.itemClicked.connect(show_notes)

window.setLayout((layout_notes))
window.show()
app.exec_()
