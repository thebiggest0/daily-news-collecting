import mysql.connector
from data_manage import save


def sql_access():
    config = {
        'user': 'your_username',
        'password': 'your_password',
        'host': 'host_address',
        'database': 'database_name',
        'port': 3306
    }
    return config


def sql_insert_data(config, data):
    # Connect to the MySQL database
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    # Insert data into the table
    for entry in data:
        cursor.execute('''
            INSERT INTO news (news_id, title, category, length)
            VALUES (DEFAULT, %s, %s, %s)
        ''', (data[entry]['title'], data[entry]['category'], data[entry]['length']))

    # # Commit the transactions
    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()


def main():
    configuration = sql_access()
    data_news = save.read_json('../data/news.json')
    sql_insert_data(configuration, data_news)
