"""
ADD A DOCSTRING
"""
import webbrowser
import pyautogui
import time
from search import match_image


def acquire_links():
    links = [
        'https://ca.news.yahoo.com/huge-ring-galaxies-challenges-thinking-023325122.html',
        'https://ca.news.yahoo.com/louisianas-special-session-kicks-off-050850728.html',
        'https://ca.news.yahoo.com/us-launches-second-strike-houthis-141810529.html',
        'https://ca.news.yahoo.com/uk-had-no-choice-strike-044635656.html',
        'https://ca.news.yahoo.com/nfl-play-offs-cj-stroud-010526208.html',
        'https://ca.news.yahoo.com/ruling-party-candidate-strongly-opposed-160257129.html',
        'https://ca.news.yahoo.com/iowa-caucuses-voters-thinking-ahead-025504809.html',
        'https://ca.news.yahoo.com/queen-margrethe-abdication-cause-ripple-011043849.html',
        'https://ca.news.yahoo.com/tom-walker-lost-way-music-024523063.html',
        'https://ca.news.yahoo.com/had-3-000-stolen-via-021315800.html'
    ]
    return links


def gpt_prompt(url):
    time.sleep(1)
    pyautogui.write(f'look at this {url} and provide answers to the following: - title:. - category: a word that '
                    f'is not "News" eg. business, politics, technology, etc. - length: short, medium, long. - '
                    f'summary: one sentence. - url: the link I gave you. In json format with key "#"\n')
    time.sleep(20)


def search_links():
    webbrowser.open('https://chat.openai.com/')
    time.sleep(3)

    news = {}
    count = 1
    for link in acquire_links():
        gpt_prompt(link)


def acquire_data(link):
    webbrowser.open('https://chat.openai.com/')
    time.sleep(5)
    gpt_prompt(link)


def main():

    links = acquire_links()
    for link in links:
        acquire_data(link)
        match_image.transfer_data()


if __name__ == "__main__":
    main()
