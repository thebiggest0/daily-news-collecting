import mysql.connector
from data_manage import save
from data import user_info
import json
import re


def sql_access_cloud():
    config = {
        'user': user_info.CLOUD_USER,  # Replace with your RDS username, often 'admin'
        'password': user_info.CLOUD_PASSWORD,  # Replace with your RDS password
        'host': user_info.CLOUD_HOST,  # Replace with your RDS instance endpoint
        'database': user_info.CLOUD_DATABASE,  # Replace with your database name
        'port': user_info.CLOUD_PORT  # Replace with your RDS instance port, default is 3306 for MySQL
    }
    return config


def sql_access_local():
    config = {
        'user': user_info.LOCAL_USER,
        'password': user_info.LOCAL_PASSWORD,
        'host': user_info.LOCAL_HOST,
        'database': user_info.LOCAL_DATABASE,
        'port': user_info.LOCAL_PORT
    }
    return config


def sql_write_data_old(config, data):
    # Connect to the MySQL database
    connect = mysql.connector.connect(**config)
    cursor = connect.cursor()

    # Insert data into the table
    for entry in data:
        cursor.execute('''
            INSERT INTO news (news_id, title, category, length, summary, url)
            VALUES (DEFAULT, %s, %s, %s, %s, %s)
        ''', (data[entry]['title'], data[entry]['category'], data[entry]['length'], data[entry]['summary'], data[entry]['url']))

    # # Commit the transactions
    connect.commit()

    # Close the connection
    cursor.close()
    connect.close()


def sql_write_data_new(config, entry, category, popular):
    # Connect to the MySQL database
    connect = mysql.connector.connect(**config)
    cursor = connect.cursor()

    # Insert data into the table
    def strip_non_numbers(input_string):
        return re.sub(r'\D', '', input_string)

    length = ''
    for i in range(len(entry['content']) - 1, -1, -1):
        if entry['content'][i] == ']':
            for j in range(i - 1, -1, -1):
                if entry['content'][j] == '[':
                    break
                length += entry['content'][j]
            length = strip_non_numbers(length)
            length = int(length[::-1])
            break

    try:
        cursor.execute('''
            INSERT INTO api_news (news_id, title, category, author, length, description, publishDate, url, popular, source)
            VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ''', (entry['title'], category, entry['author'], length, entry['description'], entry['publishedAt'][:10], entry['url'], popular, entry['source']['name']))
    except mysql.connector.Error:
        pass

    if popular:
        try:
            cursor.execute('''
                INSERT INTO popular_news (news_id, title, category, author, length, description, publishDate, url, popular, source)
                VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (entry['title'], category, entry['author'], length, entry['description'], entry['publishedAt'][:10],
                  entry['url'], popular, entry['source']['name']))
        except mysql.connector.Error as e:
            print(e)

    # # Commit the transactions
    connect.commit()

    # Close the connection
    cursor.close()
    connect.close()


def sql_read_data_general(config):
    connect = mysql.connector.connect(**config)
    cursor = connect.cursor(dictionary=True)

    cursor.execute(f"SELECT * FROM popular_news")

    rows = cursor.fetchall()
    for row in rows:
        print_info(row)

    cursor.close()
    connect.close()


def sql_read_data_specific(config):
    connect = mysql.connector.connect(**config)
    cursor = connect.cursor(dictionary=True)

    attributes = {"title", "category", "description", "source", "url", "all"}

    category = {"technology", "world", "sports", "business"}
    date = {}
    source = {}

    user_input_category = input("Category: ").lower()
    user_input_date = input("Date: ")
    user_input_source = input("Source: ").title()


    # Define your variable
    category = '%'
    publish_date = "2024-01-29"
    source = "%"

    # Use a parameter placeholder (%s) in the query
    # query = "SELECT * FROM popular_news WHERE category = %s"
    # cursor.execute(query, (category,))

    query = "SELECT * FROM popular_news WHERE category LIKE %s AND source LIKE %s AND publishDate LIKE %s"
    # cursor.execute(query, (category, source, publish_date,))
    cursor.execute(query, (user_input_category, user_input_source, user_input_date,))

    rows = cursor.fetchall()
    for row in rows:
        print_info(row)

    cursor.close()
    connect.close()


def print_info(row):
    try:
        print(f"Title: {row['title']}")
    except Exception:
        print("Title: Null")

    try:
        print(f"Date: {row['publishDate']}")
    except Exception:
        print("Date: Null")

    try:
        print(f"Category: {row['category']}")
    except Exception:
        print("Category: Null")

    try:
        print(f"Description: {row['description']}")
    except Exception:
        print("Description: Null")

    try:
        print(f"Source: {row['source']}")
    except Exception:
        print("Source: Null")

    try:
        print(f"URL: {row['url']}")
    except Exception:
        print("URL: Null")

    print()


def main():
    # create/read data from relational table
    configuration = sql_access_local()
    data_news = save.read_json('../data/news.json')
    sql_write_data_new(configuration, data_news)
    # sql_read_data(configuration)


if __name__ == '__main__':
    main()
