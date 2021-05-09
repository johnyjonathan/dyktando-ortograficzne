from dominate import document
from dominate.tags import *
def generateTemplate(file, mistakes):

    text_path = file

    def getString(path_txt_file):
        file = open(path_txt_file,'r',encoding='utf8')
        lines = file.readlines()
        author = lines[len(lines)-1]
        lines = lines[:-1]
        string = ''
        for line in lines:
            string += line

        return string, author

    text, author = getString(text_path)

    with doc.head:
        link(rel='stylesheet',href='style.css')

    with document(title='Wyniki') as doc:
        h2('Treść dyktanda')
        div(p(text), _class='tekst')
        div(p('Autor'), _class='author')



    with open('result.html','w') as f:
        f.write(doc.render())


generateTemplate('dyktando.txt','elo')
