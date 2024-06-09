"""
ADD A DOCSTRING
"""
from database import SQL


# reads entire db and puts each news data into data.jsonl
def read_news():
    config = SQL.sql_access_local()
    SQL.sql_all_data_to_json(config)
    # SQL.sql_read_data_general(config)


def main():
    read_news()



if __name__ == "__main__":
    main()
