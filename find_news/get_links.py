"""
ADD A DOCSTRING
"""
from datetime import date, timedelta
from data import user_info
import requests


def get_newsapi_org(category, day):
    url = ('https://newsapi.org/v2/everything?'
           f'q={category}'
           f'&from={day}'
           '&sortBy=popularity'
           '&pageSize=20'
           f'&apiKey={user_info.NEWSAPI_KEY}')

    response = requests.get(url)
    data = response.json()
    news = data['articles']
    return news


def main():
    day = (date.today() - timedelta(days=1))
    for category in ["technology", "world+news", "vancouver+canada", "sports", "business"]:
        news = get_newsapi_org(category, day)
        print(news)

if __name__ == "__main__":
    main()
