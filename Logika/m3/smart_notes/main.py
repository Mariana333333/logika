import json
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QTextEdit, QLabel,
    QListWidget, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QInputDialog,
    QTableWidget, QListWidgetItem, QFormLayout,
    QGroupBox, QButtonGroup, QRadioButton, QSpinBox)


def WriteToFile():
    with open('notes.json', 'w', 'encoding=utf8') as file:
        json.dump(notes, file, ensure_ascii=False, sort_keys=True, indent=4)


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




btn_note_add = QPushButton('Додати до замітки')

layout_notes = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

layout_notes.addLayout(col1, stretch=2)
layout_notes.addLayout(col2, stretch=1)

col1.addWidget(field_text)

col2.addWidget(lb_notes)
col2.addWidget(lst_notes)

row1 = QHBoxLayout()
row1.addWidget(btn_note_create)
row1.addWidget(btn_note_del)

col2.addLayout(row1)
col2.addWidget(btn_note_save)

col2.addWidget(lb_tags)
col2.addWidget(lst_tag)
col2.addWidget(field_tag)


row2 = QHBoxLayout()
row2.addWidget(btn_tag_add)
row2.addWidget(btn_tag_unpin)

col2.addLayout(row2)
col2.addWidget(btn_tag_search)


with open('notes.json', 'r', encoding='utf8') as file:
    notes = json.load(file)

lst_notes.addItems(notes)


def show_notes():
    key = lst_notes.currentItem().text()
    field_text.setText(notes[key]['текст'])

    lst_tag.clear()
    lst_tag.addItems(notes[key]['теги'])



def add_note():
    note_name, ok = QInputDialog.getText(window, 'Додати замітку', 'Назва замітки')
    if note_name and ok:
        lst_notes.addItem(note_name)
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
    key = lst_notes.currentItem().text()
    notes[key]['текст'] = field_text.toPlainText()

    WriteToFile()

def add_tag():
    key = lst_notes.currentItem().text()
    tag = field_tag.text()

    print(notes[key]['теги'])
    notes[key]['теги'].append(tag)

    lst_tag.addItem(tag)

    WriteToFile()

def del_tag():
    key = lst_notes.currentItem().text()
    tag = lst_tag.currentItem().text()

    notes[key]['теги'].remove(tag)

    lst_tag.clear()
    lst_tag.addItems(notes[key]['теги'])


    WriteToFile()

def search_tag():
    tag = field_tag.text()

    if 'Шукати за тегом' == btn_tag_search.text():
        filtered_notes = {}

        for key in notes:
            if tag in notes[key]['теги']:
                filtered_notes[key] = notes[key]

        btn_tag_search.setText('Скинути пошук')

        lst_notes.clear()
        lst_notes.addItems(filtered_notes)
        lst_tag.clear()
        field_text.clear()
    elif 'Скинути пошук' == btn_tag_search.text():
        btn_tag_search.setText('Шукати за тегом')

        lst_notes.clear()
        lst_notes.addItems(notes)
        lst_tag.clear()
        field_text.clear()
        field_tag.clear()


with open('notes.json', 'r', encoding='utf8') as file:
    notes = json.load(file)


btn_tag_add.clicked.connect(add_tag)
btn_tag_unpin.clicked.connect(del_tag)
btn_tag_search.clicked.connect(search_tag)

btn_note_save.clicked.connect(save_note)
btn_note_del.clicked.connect(del_note)
btn_note_create.clicked.connect(add_note)

lst_notes.itemClicked.connect(show_notes)

window.setLayout((layout_notes))
window.show()
app.exec_()
