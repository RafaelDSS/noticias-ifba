import requests as r
from bs4 import BeautifulSoup


def news_all():
    data_news = {'data': []}

    res = r.get("https://portal.ifba.edu.br/irece/noticias-2/noticias-campus-irece", verify=False)
    soup = BeautifulSoup(res.text, 'html.parser')
    news_school = soup.findAll('article', 'entry')
    
    for news in news_school:
        json_news = {}
        news = news.select('.summary a')[0]
        json_news['title'] = news.string
        json_news['link'] = news['href']
        data_news['data'].append(json_news)

    return data_news

print(news_all())

