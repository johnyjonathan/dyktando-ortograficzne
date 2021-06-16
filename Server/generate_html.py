from dominate import document
from dominate.tags import *
from dominate.util import text
def generateTemplate(fileToRead, mistakes):

    text_path = fileToRead

    def getString(path_txt_file):
        file = open(path_txt_file,'r',encoding='utf8')
        lines = file.readlines()
        author = lines[len(lines)-1]
        lines = lines[:-1]
        string = ''
        for line in lines:
            string += line

        return string, author

    def count(text, mistakes):
        a = len(text)
        b = len(mistakes)
        tmp = (b/a) * 100
        return tmp

    text, author = getString(text_path)

    #counter = count(text, mistakes)

    doc = document(title="Wyniki")

    with doc.head:
        link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css", integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO",crossorigin="anonymous")
        meta(charset="utf-8", name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no")
        link(rel="stylesheet", href="style.css")
    with doc:
        with div(id="main_txt"):
            h2('Dyktando ortograficzne')
            div(h5(author), _class='author')
            div(p(text), _class='tekst')
            hr()
            with div(cls="mistakes").add(ol()):
                h5('Popełnione błędy')
                for i in mistakes:
                    li(i)





    with open('result.html','w') as f:
        f.write(doc.render())
