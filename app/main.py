"""
ADD A DOCSTRING
"""
from search import search
from search import match_image
from data_manage import save
from database import SQL
from find_news import get_links
from datetime import date, timedelta


def main():

    write_to_new = True
    config = SQL.sql_access_local()

    if not write_to_new:

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
        # config = SQL.sql_access_local()
        data_news = save.read_json('../data/news.json')
        SQL.sql_write_data_old(config, data_news)

    else:
        day = (date.today() - timedelta(days=7))
        # for category in ["technology", "world", "vancouver+canada", "sports", "business"]:
        for category in ["business", "technology", "world", "sports"]:
            data_news = get_links.get_newsapi_org(category, day)
            for i in range(len(data_news)):
                if i < 10:
                    popular = True
                    SQL.sql_write_data_new(config, data_news[i], category, popular)
                else:
                    popular = False
                    SQL.sql_write_data_new(config, data_news[i], category, popular)


if __name__ == "__main__":
    main()
