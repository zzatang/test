import os
import csv

__version__ = '0.0.1'

HTML_PATH = '.\\programs\\graphic-design.htm'
CSV_FILES = ('.\\_assets\\first_semester.csv',
             '.\\_assets\\second_semester.csv')
SP_INC = 2

def create_row(row_data, **kwargs):
    sp = '  ' * kwargs.get('line_space', 0)
    output = sp + '<tr>\n'
    sp += SP_INC * ' '
    
    if kwargs.get('is_header', False):
        for item in row_data:
            output += sp + '<th>' + item + '</th>\n'
    else:
        first_col = row_data[0].split(' ', 1)
        output += sp + '<td><strong>' + first_col[0] + ' </strong>' + first_col[1] + '</td>'
        for item in row_data[1:]:
            output += '<td>' + item + '</td>\n'

    sp = sp[:-SP_INC]
    output += sp + '</tr>\n'
    return output       

def create_table(table_data, **kwargs):
    border = str(kwargs.get('border', 0))
    cellspacing = str(kwargs.get('cellspacing', 0))
    cellpadding = str(kwargs.get('cellpadding', 0))
    sp = ' ' * kwargs.get('line_space', 0)
    output = sp + '<table border="' + border + '" cellspacing="' + cellspacing + '" cellpadding="' + cellpadding + '">\n'
    sp += ' ' * SP_INC
    output += create_row(table_data[0], line_space = len(sp), is_header = True)
    for item in table_data[1:]:
        output += create_row(item, line_space = len(sp))

    sp = sp[:-SP_INC]
    output += sp + '</table>\n'
    return output
    

def insert_table(html_path, csv_files):
    html_orig = open(html_path)
    html_halves = html_orig.read().split('</article')
    sp = (len(html_halves[0]) - len(html_halves[0].rstrip(' ')))

    new_table = ''
    for path in csv_files:
        print('Building table from ' + path)
        file = open(path, 'r')
        csv_data = list(csv.reader(file, delimiter = ','))
        new_table += create_table(csv_data, line_space = sp + 2)

    print('Inserting new table to copy of ' + html_path)
    output_html = html_halves[0].rstrip(' ') + new_table + (sp * ' ') + '</article>' + html_halves[1]
    output_path = os.path.dirname(html_path) + '\\output1.html'
    print('Saving result to ' + output_path)
    output_file = open(output_path, 'w')
    output_file.write(output_html)

if __name__ == '__main__':insert_table(HTML_PATH, CSV_FILES)