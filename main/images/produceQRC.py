import os
def file_name(file_dir):
    with open('qqexpression.qrc', 'w') as f:
        temp = '<!DOCTYPE RCC>\n<RCC version="1.0">\n<qresource>'
        f.write(temp)
        for item in os.walk(file_dir):
            for item in item[2]:
                temp = "<file>" + file_dir +"/" + item + "</file>\n"
                f.write(temp)
        temp = '</qresource>\n</RCC>'
        f.write(temp)
file_name('./qqexpression')