from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QTableWidget, QListWidget, QListWidgetItem,
        QLineEdit, QFormLayout,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QButtonGroup, QRadioButton,
        QPushButton, QLabel, QSpinBox)
from memo___data import*

radio_list = [r_btn1, r_btn2, r_btn3, r_btn4]


frm = Question('Яблуко', 'Apple', 'orange', 'Berry', 'Tomato')
frm_card = QuestionView(frm, lb_question, radio_list[0], radio_list[1], radio_list[2],radio_list[3])

def show_data():
    ''' показує на екрані аотрібну інформацію '''
    pass

def check_results():
    pass





app = QApplication([])
btn_menu = QPushButton('Меню')
btn_sleep = QPushButton('Відпочивати')
btn_OK = QPushButton('Відповісти')
lb_Question = QLabel('')

box_minutes = QSpinBox()
box_minutes.setValue(5)
frm_card.show()


RadioGroupBox = QGroupBox('Варіанти відповідей')
RadioGroup = QButtonGroup()


rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')


RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox("езультат тесту")
lb_Result = QLabel('')
lb_Correct = QLabel('')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

Layoutline1 = QHBoxLayout()
Layoutline2 = QHBoxLayout()
Layoutline3 = QHBoxLayout()
Layoutline4 = QHBoxLayout()

Layoutline1.addWidget(btn_menu)
Layoutline1.addStretch(1)
Layoutline1.addWidget(btn_sleep)
Layoutline1.addWidget(box_minutes)
Layoutline1.addWidget(QLabel('хвилин'))
Layoutline2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

Layoutline3.addWidget(RadioGroupBox)
Layoutline3.addWidget(AnsGroupBox)

Layoutline4.addStretch(1)
Layoutline4.addWidget(btn_OK)
Layoutline4.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(Layoutline1, stretch=1)
layout_card.addLayout(Layoutline2, stretch=2)
layout_card.addLayout(Layoutline3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(Layoutline4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)














# віджети, які треба буде розмістити:
# кнопка повернення в основне вікно
# кнопка прибирає вікно і повертає його після закінчення таймера
# введення кількості хвилин
# кнопка відповіді "Ок" / "Наступний"
# текст питання

# Опиши групу перемикачів

# Опиши панень з результатами

# Розмісти весь вміст в лейаути. Найбільшим лейаутом буде layout_card

# Результат роботи цього модуля: віджети поміщені всередину layout_card, який можна призначити вікну.
def show_result():
    ''' показати панель відповідей '''
    pass

def show_question():
    ''' показати панель запитань '''
    pass