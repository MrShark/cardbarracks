from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, Frame
from reportlab.lib.styles import getSampleStyleSheet


class pdffile:
    def __init__(self, filename, cardformat):
        self.width = cardformat.WIDTH * mm
        self.height = cardformat.HEIGHT * mm
        self.format = cardformat
        self.canvas = canvas.Canvas(filename, pagesize=(cardformat.WIDTH * mm, self.format.HEIGHT * mm))
        self.canvas.setFillColorRGB(*cardformat.BGCOLOR)
        self.canvas.rect(0, 0, self.width, self.height, stroke=0, fill=1)
        self.canvas.setFillColorRGB(0, 0, 0)

    def add_card(self, card):
        card.render(self)
        self.canvas.showPage()
        self.canvas.setFillColorRGB(*self.format.BGCOLOR)
        self.canvas.rect(0, 0, self.width, self.height, stroke=0, fill=1)
        self.canvas.setFillColorRGB(0, 0, 0)

    def close(self):
        self.canvas.save()

    def image(self, x, y, w, h, img):
        self.canvas.drawImage(img, x * mm, self.height - (y + h) * mm, width=w * mm, height=h * mm)

    def string(self, x, y, h, w, s, radius=2, label=""):
        px = x * mm
        py = self.height - (y + h) * mm
        th = h * .8 * mm
        pw = w * mm
        ph = h * mm
        m = h * .1 * mm
        self.canvas.setFillColorRGB(1, 1, 1)
        self.canvas.roundRect(px, py, pw, ph, radius, stroke=1, fill=1)
        self.canvas.setFillColorRGB(0, 0, 0)

        if not label:
            self.canvas.setFont("Helvetica", th)
            self.canvas.drawString(px + m, py + m * 2, s)
        else:
            self.canvas.setFont("Helvetica", th * .3)
            self.canvas.drawString(px + m, py + m * 7, label)
            self.canvas.setFont("Helvetica", th * .9)
            self.canvas.drawString(px + m * 5, py + m * 2, s)

    def text(self, x, y, w, h, lh, s, label=""):
        px = x * mm
        py = self.height - (y + h) * mm
        th = lh * .8 * mm
        m = lh * .1 * mm
        self.canvas.setFillColorRGB(1, 1, 1)
        self.canvas.roundRect(px, py, w * mm, h * mm, 2, stroke=1, fill=1)
        self.canvas.setFillColorRGB(0, 0, 0)
        start = py + h * mm - 2 * lh
        if label:
            self.canvas.setFont("Helvetica", th)
            self.canvas.drawString(px + m, start, label)
            start -= th * 1.2
        self.canvas.setFont("Helvetica", th)
        self.canvas.drawString(px + m, start, s)

    def box(self, x, y, h, w, s, count=1, radius=2):
        px = x * mm
        py = self.height - (y + h) * mm
        th = h * .8 * mm
        pw = w * mm
        ph = h * mm
        m = h * .1 * mm
        self.canvas.setFillColorRGB(1, 1, 1)
        self.canvas.roundRect(px, py, pw, ph, radius, stroke=1, fill=1)
        self.canvas.setFillColorRGB(0, 0, 0)

        for n in range(count):
            self.canvas.roundRect(px + 2 * m + ph * n, py + 2 * m, h * .6 * mm, h * .6 * mm, 1, stroke=1)

        self.canvas.setFont("Helvetica", th)
        self.canvas.drawString(px + ph * count, py + m * 2, s)
