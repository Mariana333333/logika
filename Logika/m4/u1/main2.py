from PIL import Image, ImageFilter

class ImageEditor:
        def __init__(self, filename):
            self.filename = filename
            self.original = None
            self.edited = []

        def open(self):
            try:
                self.original = Image.open(self.filename)
                self.original.show()
            except:
                print('Такого файлу не існує')

        def do_left(self):
            left = self.original.transpose(Image.ROTATE_90)
            self.edited.append(left)

            left.save('Left_' + self.filename)

        def bw(self):
            bw = self.original.convert('L')
            self.edited.append()

            bw.save('bw_' + self.filename)




img = ImageEditor('Sonor-Drums-Drumset.jpg')


img.open()
img.do_left()
img.bw()