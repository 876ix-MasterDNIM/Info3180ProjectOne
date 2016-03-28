from bs4 import BeautifulSoup

def temp(url):
    html = BeautifulSoup(url, 'html_parser')
    return html.prettify()