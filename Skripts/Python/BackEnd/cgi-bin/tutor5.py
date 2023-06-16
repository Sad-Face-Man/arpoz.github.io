import cgi, sys, locale
# Set the content type to text/html with UTF-8 encoding
#content_type = 'text/html; charset=utf-8'
#cgi.header('Content-Type', content_type)
print("Content-Type: text/html; charset=UTF-8")    # HTML is following
#print()                             # blank line, end of headers

form = cgi.FieldStorage()
# Define the HTML code for the table
html1 = """
<TITLE>таблица с анкетой</TITLE>
<H1>Анкета пользователя</H1>
<table border =2> <tr>  <td>Имя поля</td><td>Значение</td>  </tr>
"""
# Write the HTML code to the standard output stream
sys.stdout.write(html1)
ll = ['имя','размер обуви','должность', 'Любимый язык программирования','комментарий']
data = ['','','','','']; i=0
for field in ('name', 'shoesize', 'job', 'language', 'comment'):
    if not field in form:
        data[i] = '(unknown)'
    else:
        if not isinstance(form[field], list):
            data[i] = form[field].value
        else:
            values = [x.value for x in form[field]]
            data[i] = ', '.join(values)
    i+=1
# Print the table rows
for i in range(5):
   print ('<tr><td> %s </td> <td> %s </td></tr>'% (ll[i], data[i]))
# Close the HTML table tag
print (' </table>')