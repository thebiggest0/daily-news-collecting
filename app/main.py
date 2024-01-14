"""
ADD A DOCSTRING
"""
from search import search
from search import match_image
from data_manage import save
from database import SQL


def main():
    # # get data from links
    links = search.acquire_links()
    for link in links:
        search.acquire_data(link)
        match_image.transfer_data()

    # process text file into json
    data = save.process_textfile()
    save.textfile_to_json(data)
    save.clear_textfile()

    # writing to database
    config = SQL.sql_access_local()
    data_news = save.read_json('../data/news.json')
    SQL.sql_write_data(config, data_news)


if __name__ == "__main__":
    main()
