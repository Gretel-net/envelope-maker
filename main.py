#!/usr/bin/env python

import os
import sys
import json
import argparse

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from paper_layout import PaperLayout
from template_to import TemplateTo
import metric

FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts/")

FONT_GOTHIC = os.path.join(FONT_DIR, "ipaexg.ttf")
FONT_MINCHO = os.path.join(FONT_DIR, "ipaexm.ttf")

DPI = 72


class Main():
    def __init__(self):
        args = self.argp()
        self._template_path = args.template_path
        self._layout_path = args.layout_path
        self._output = args.output
        self._a4_compatible_mode = args.a4_native

        if self._output in (self._template_path, self._layout_path):
            raise ValueError(
                "You cannot specify the same output as the input file")

        self.layout = PaperLayout(self._layout_path)
        self.to = TemplateTo(self._template_path)

        pass

    def argp(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", dest="template_path", required=True)
        parser.add_argument("-p", dest="layout_path", required=True)
        parser.add_argument("-o", dest="output", required=True)
        parser.add_argument("--a4", dest="a4_native", action="store_true")

        return parser.parse_args()

    def main(self):
        pdfmetrics.registerFont(TTFont("GOTHIC", FONT_GOTHIC))
        pdfmetrics.registerFont(TTFont("MINCHO", FONT_MINCHO))

        output_path = self._output

        m = metric.Metric(DPI)

        if self._a4_compatible_mode:
            # A4
            print_size = A4
            width_px, height_px = print_size
            x_offset = (m.px2mm(width_px) - self.layout.width) / 2
            y_offset = (m.px2mm(height_px) - self.layout.height) / 2
        else:
            # Native
            print_size = (m.mm2px(self.layout.width),
                          m.mm2px(self.layout.height))
            width_px, height_px = print_size
            x_offset = 0
            y_offset = 0

        page = canvas.Canvas(
            output_path, pagesize=portrait(print_size), bottomup=False)

        width = m.px2mm(width_px)
        height = m.px2mm(height_px)

        # layout debug
        self.draw_layout_line(page, m, width, height, x_offset, y_offset)

        # zip-code
        page.setFont("GOTHIC", 22)
        page.drawRightString(m.mm2px(x_offset + self.layout.width - 10),
                             m.mm2px(y_offset + 35),
                             self.to.zip_code
                             )

        # name
        font_size = 26
        lines = len(self.to.name)
        page.setFont("MINCHO", font_size)

        for x_cursor, line in enumerate(self.to.name):
            for y_cursor, char in enumerate(line):
                page.drawCentredString(m.mm2px(x_offset + self.layout.width / 2) + (font_size - font_size / 2) - (font_size * x_cursor),
                                       m.mm2px(y_offset + 65) +
                                       font_size * y_cursor,
                                       char
                                       )

        # address
        font_size = 20
        lines = len(self.to.address)
        page.setFont("MINCHO", font_size)

        for x_cursor, line in enumerate(self.to.address):
            for y_cursor, char in enumerate(line):
                page.drawCentredString(m.mm2px(x_offset + self.layout.width) - (font_size / lines) - 50 + (font_size - font_size / 2) - (font_size * x_cursor),
                                       m.mm2px(y_offset + 120) +
                                       font_size * y_cursor,
                                       char
                                       )

        # contets
        if self.to.contents is not None:
            font_size = 16
            lines = len(self.to.contents)
            page.setFont("MINCHO", font_size)

            page.setStrokeColorCMYK(0.0, 1.0, 0.8, 0.1)
            page.setLineWidth(m.mm2px(0.5))

            page.rect(m.mm2px(x_offset) + 50 - font_size / 2 - m.mm2px(3),
                      m.mm2px(y_offset + 160) - font_size - m.mm2px(3),
                      font_size + m.mm2px(6),
                      font_size * lines + m.mm2px(7),
                      1,
                      False
                      )

            page.setFillColorCMYK(0.0, 1.0, 0.8, 0.1)
            for y_cursor, char in enumerate(self.to.contents):
                page.drawCentredString(m.mm2px(x_offset) + 50,
                                       m.mm2px(y_offset + 160) +
                                       font_size * y_cursor,
                                       char
                                       )

        page.save()

        print("complite")

    def draw_layout_line(self, page, m, width, height, x_offset, y_offset):
        page.setStrokeColorRGB(0.0, 1.0, 1.0)
        page.setLineWidth(m.mm2px(0.5))

        page.line(m.mm2px(x_offset + 0),
                  m.mm2px(0),
                  m.mm2px(x_offset + 0),
                  m.mm2px(height)
                  )

        page.line(m.mm2px(x_offset + self.layout.width),
                  m.mm2px(0),
                  m.mm2px(x_offset + self.layout.width),
                  m.mm2px(height)
                  )

        page.line(m.mm2px(0),
                  m.mm2px(y_offset + 0),
                  m.mm2px(width),
                  m.mm2px(y_offset + 0)
                  )

        page.line(m.mm2px(0),
                  m.mm2px(y_offset + self.layout.height),
                  m.mm2px(width),
                  m.mm2px(y_offset + self.layout.height)
                  )


if __name__ == "__main__":
    main = Main()
    exit_cd = main.main()

    exit(exit_cd)
