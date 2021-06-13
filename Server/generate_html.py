from dominate import document
from dominate.tags import *

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

    def removeSigns(text):
        for x in range(len(text)):
            if ',' in text[x]:
                text[x] = text[x].replace(',','')
            if '.' in text[x]:
                text[x] = text[x].replace('.','')
            if '\n' in text[x]:
                text[x] = text[x].replace('\n','')
            if '!' in text[x]:
                text[x] = text[x].replace('!','')
            if '?' in text[x]:
                text[x] = text[x].replace('?','')
            if ':' in text[x]:
                text[x] = text[x].replace(':','')

            x += 1
        return text

    def errorsReplace(tekst, errors):
        for i in range(len(tekst)):
            for k in range(len(errors)):
                if errors[k] == tekst[i]:
                    tekst[i] = "<u>"+tekst[i]+"</u>"
        return tekst


    text, author = getString(text_path)

    split_text = text.split(' ')
    txt = removeSigns(split_text)
    txt_u = errorsReplace(txt, mistakes)

    counter = count(text, mistakes)

    doc = document(title="Wyniki")

    with doc.head:
        link(rel="stylesheet", href="style.css")


    with doc:
        with div(id="main_txt"):
            h2('Treść dyktanda')
            div(p(txt_u), _class='tekst')
            div(p(author), _class='author')

        with div(cls="mistakes").add(ol()):
            p('Popełnione błędy')
            for i in mistakes:
                li(i)

        with div(cls="percent"):
            p('%s procent błędnych wyrazów względem całego tekstu.'% counter)



    with open('result.html','w') as f:
        f.write(doc.render())
