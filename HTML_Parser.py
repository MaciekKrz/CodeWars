"""
Parsing HTML tags
"""
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            if attr[1] is None:
                value = 'None'
            else:
                value = attr[1]
            print("->", attr[0] + " > " + value)

    def handle_endtag(self, tag):
        print(tag)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            if attr[1] is None:
                value = 'None'
            else:
                value = attr[1]
            print("->", attr[0] + " > " + value)


html = ""

for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()
