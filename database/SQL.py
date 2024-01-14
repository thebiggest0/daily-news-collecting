import mysql.connector
from data_manage import save
import json


def sql_access_cloud():
    config = {
        'user': 'your_username',  # Replace with your RDS username, often 'admin'
        'password': 'your_password',  # Replace with your RDS password
        'host': 'your_rds_instance_endpoint',  # Replace with your RDS instance endpoint
        'database': 'your_database_name',  # Replace with your database name
        'port': 3306  # Replace with your RDS instance port, default is 3306 for MySQL
    }


def sql_access_local():
    config = {
        'user': 'local_user',  # Replace with your local database username
        'password': 'local_password',  # Replace with your local database password
        'host': 'localhost',  # Typically 'localhost' for a local database
        'database': 'local_database_name',  # Replace with the name of your local database
        'port': 3306  # Replace with the port your local database is using (3306 is common for MySQL)
    }
    return config


def sql_write_data(config, data):
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


def sql_read_data(config):
    connect = mysql.connector.connect(**config)
    cursor = connect.cursor(dictionary=True)

    cursor.execute(f"SELECT * FROM news")

    rows = cursor.fetchall()
    with open('../data/sql_data.json', 'w') as file:
        json.dump(rows, file, indent=4)

    cursor.close()
    connect.close()


def main():
    # create/read data from relational table
    configuration = sql_access_local()
    data_news = save.read_json('../data/news.json')
    sql_write_data(configuration, data_news)
    # sql_read_data(configuration)


if __name__ == '__main__':
    main()
