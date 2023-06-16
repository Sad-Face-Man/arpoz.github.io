#вывод в таблицу
import cgi, sys
form = cgi.FieldStorage()         # извлечь данные из формы
print("Content-type: text/html; charset=utf-8")  # плюс пустая строка

html1 = """
<TITLE>таблица с анкетой</TITLE>
<H1>Анкета пользователя</H1>
<table border =2> <tr>
"""
print (html1)
# печать заголовка таблицы
ll = ['имя','размер обуви','работа', 'язык','комментарий']
for head in ll:
    ss = '<td>'+head+'</td>'
    print ( ss)
print ('</tr> <tr>')

data = ['','','','',''];    i=0
for field in ('name', 'shoesize', 'job', 'language', 'comment'):
    if not field in form:
        data[i] = '(unknown)'
    else:
        if not isinstance(form[field], list):
            data[i] = form[field].value
        else:
            values = [x.value for x in form[field]]
            data[i] = ' and '.join(values)
    i+=1
for el in data:
   print ('<td> %s </td>'% el)

print ('</tr> </table>')
