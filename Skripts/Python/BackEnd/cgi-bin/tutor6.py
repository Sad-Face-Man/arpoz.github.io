import cgi, sys
form = cgi.FieldStorage()         # извлечь данные из формы
print("Content-Type: text/html; charset=UTF-8")  # плюс пустая строка

html = """
<head> <style> body{background: rgba(255,100,0,0.8);}</style></head>
<TITLE>tutor5.py</TITLE>
<h1>Анкета пользователя</h1>    <HR>
<h4>Вас зовут: %(name)s</h4>
<h4>Вы играете %(playFrequency)s</h4>
<h4>Статус работы: %(job)s</h4>
<h4>Используемый(/е) лаунчер(ы): %(launcher)s</h4>
<h4>О себе:</h4>
<P>%(about)s</P>
<h4>%(hid)s</h4>
<HR>"""
data = {}
for field in ('name', 'playFrequency', 'job', 'launcher', 'about', 'hid'):
    if not field in form:
        data[field] = '(unknown)'
    else:
        if not isinstance(form[field], list):
            data[field] = form[field].value
        else:
            values = [x.value for x in form[field]]
            data[field] = ' и '.join(values)
print(html % data)