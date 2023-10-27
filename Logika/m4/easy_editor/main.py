import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QWidget, QFileDialog, QLabel,
    QPushButton, QListWidget, QHBoxLayout, QVBoxLayout)
from PIL import Image, ImageFilter

#from PIL import Image, ImageFilter
#from PIL.ImageQt import ImageQt
#from PIL.ImageFilter import SHARPEN

app = QApplication([])
main_win = QWidget()


btn_folder = QPushButton('Папка')
btn_left = QPushButton('Ліво')
btn_right = QPushButton('Право')
btn_flip = QPushButton('Віддзеркалити')
btn_sharp = QPushButton('Різкість')
btn_bw = QPushButton('Ч/Б')


lst_files = QListWidget()
lb_pic = QLabel('Картинка')



Layout_editor = QHBoxLayout()
row = QHBoxLayout()


col1 = QVBoxLayout()
col2 = QVBoxLayout()


col1.addWidget(btn_folder)
col1.addWidget(lst_files)

row.addWidget(btn_left)
row.addWidget(btn_right)
row.addWidget(btn_flip)
row.addWidget(btn_sharp)
row.addWidget(btn_bw)


col2.addWidget(lb_pic)
col2.addLayout(row)

Layout_editor.addLayout(col1, 1)
Layout_editor.addLayout(col2, 4)


workdir = ""

def filter(files):
    result = []
    ext = ['jpg', 'jpeg', 'bmp', 'gif', 'jfif', 'svg', 'png']

    for file in files:
        if file.split('.')[-1] in ext:
            result.append(file)

    return result

def showFiles():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

    files_and_folders = os.listdir(workdir)

    filtered_img = filter(files_and_folders)

    lst_files.clear()
    lst_files.addItems((filtered_img))

class ImageProcessor():
    def __init__(self):
        self.filename = None
        self.original = None
        self.save_dir = 'Modified/'

    def loadImage(self, filename):
        self.filename = filename

        full_path = os.path.join(workdir, filename)

        self.original = Image.open(full_path)

    def show_image(self, path):
        lb_pic.hide()

        pixmapimage = QPixmap(path)
        w, h = lb_pic.width(), lb_pic.height()

        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)

        lb_pic.setPixmap(pixmapimage)
        lb_pic.show()

def showChosenImage():
    filename = lst_files.currentItem().text()
    workimage.loadImage(filename)
    full_path = os.path.join(workdir, filename)
    workimage.show_image(full_path)


workimage = ImageProcessor()



lst_files.itemClicked.connect(showChosenImage)

btn_folder.clicked.connect(showFiles)
main_win.setLayout(Layout_editor)
main_win.show()
app.exec_()