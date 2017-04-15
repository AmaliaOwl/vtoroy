import re
import xlrd
import xlwt

workbook1 = xlrd.open_workbook('D:\\учеба\\УНИВЕР\\курсач\\Книга1.xlsx')
worksheet1 = workbook1.sheet_by_index(0)

workbook2 = xlrd.open_workbook('D:\\учеба\\УНИВЕР\\курсач\\Книга2.xlsx')
worksheet2 = workbook1.sheet_by_index(0)

wb = xlwt.Workbook('D:\\учеба\\УНИВЕР\\курсач\\КНИГА3.xlsx')
ws = wb.add_sheet('Test')

b = 0
p = 0
t = 1
print(worksheet.cell(0,b).value)
print(type(worksheet.cell(0,b).value))
s = str(worksheet.cell(0, b).value)
print(s)

row_number = worksheet.nrows
col_number = worksheet.ncols

while b < col_number: #ищем столбец с частицей
    s = str(worksheet.cell(0, b).value)
    a = re.search('part\|(.+)', s)
    i = re.search('v\|(.+)', s)
    if a:
        t = 0
        while t < col_number:#ищем столбец с таким же глаголом
            c = a.group(1)
            string = str(worksheet.cell(0,t).value)
            n = re.search('v\|'+c, string)
            if n: #если нашли, то перезаписываем столбец с глаголом
                value_0 = worksheet.cell(0,t).value
                ws.write(0,p,value_0) #записали заголовок ГЛАГОЛ
                d = 1
                while d < row_number: #идем по строчкам
                    value_0 = worksheet.cell(d,b).value
                    value_1 = worksheet.cell(d,t).value
                    value_2 = value_0 + value_1
                    ws.write(d,p,value_2)
                    print('записали ЗНАЧЕНИЕ')
                    d += 1   
                p += 1
                b += 1
                break
            else: 
                t += 1
        if t == col_number: #записываем столбец, меняя ПАРТ на В
            value_0 = 'v|'+c
            d = 1
            ws.write(0,p,value_0)
            while d < row_number:
                value_0 = worksheet.cell(d,b).value
                ws.write(d,p,value_0)
                d += 1
            p += 1
            b += 1
    elif i: #если столбец оказался с глаголом
        t = 0
        while t < col_number:#ищем столбец с такой же частицей
            c = i.group(1)
            string = str(worksheet.cell(0,t).value)
            n = re.search('part\|'+c, string)
            if n:
                b += 1#если нашли, то пропускаем
                break
            else: 
                t += 1
        if t == col_number: #записываем столбец с глаголом
            d = 0
            while d < row_number:
                value_0 = worksheet.cell(d,b).value
                ws.write(d,p,value_0)
                d += 1
            p += 1
            b += 1        
    else: #если столбец оказался с полом/возрастом
        d = 0
        while d < row_number:
            value_0 = worksheet.cell(d,b).value
            ws.write(d,p,value_0)
            d += 1
        p += 1
        print('записали ИНФО')
        b += 1

wb.save('D:\\учеба\\УНИВЕР\\курсач\\stat.CinderellaVerbs_3_000_TEST.xls')
