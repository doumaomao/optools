#!/bin/env python
# -*- encoding: utf-8 -*-

import sys
import xlwt
import codecs


def txt2xls(filename1, xlsname):
    print 'converting xls ... '
    f1 = codecs.open(filename1, 'r', 'utf-8')
    xls = xlwt.Workbook(encoding="utf-8")
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = 'SimSun'
    al = xlwt.Alignment()
    al.horz = xlwt.Alignment.HORZ_CENTER
    al.vert = xlwt.Alignment.VERT_CENTER
    al.wrap = xlwt.Alignment.WRAP_AT_RIGHT
    style.alignment = al
    style.font = font
    sheet1 = xls.add_sheet('all_data', cell_overwrite_ok=True)
    writexls(f1, sheet1, style)
    xls.save(xlsname+'.xls')


def writexls(f, sheet, style):
    x = 0
    y = 0
    while True:
        line = f.readline().encode("utf-8")
        if not line:
            break
        for i in line.split('|'):
            item = i.strip()
            sheet.write(x, y, item, style)
            y += 1
        x += 1
        y = 0
    f.close()

if __name__ == "__main__":
    filename1 = sys.argv[1]
    xlsname = sys.argv[2]
    txt2xls(filename1, xlsname)
