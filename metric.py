
INCH = 25.4


def inch2mm(inch):
    return inch * INCH


def px2mm(px, dpi):
    mm = (px * INCH) / dpi
    return mm


def mm2px(mm, dpi):
    px = (mm / INCH) * dpi
    return px


class Metric(object):
    def __init__(self, dpi):
        self.dpi = dpi

    def px2mm(self, px):
        return px2mm(px, self.dpi)

    def mm2px(self, mm):
        return mm2px(mm, self.dpi)
