"""
ADD A DOCSTRING
"""
import json
import re


def write_json(json_file_path, data):
    # Write to JSON file
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)


def read_json(json_file_path):
    # Read the JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    return data


def process_textfile():
    location = '../data/textfile.txt'
    with open(location, 'r') as files:
        data = files.read().replace('\n}\n{', ',')
    count = [0]

    def add_id(match):
        count[0] += 1
        return '"' + str(count[0]) + '"'

    # change format to dictionary style
    data = re.sub(r'"#"', add_id, data)
    data = data.replace("\n", '')
    return data


def clear_textfile():
    location = '../data/textfile.txt'
    with open(location, 'w'):
        pass


def textfile_to_json(data):
    dictionary = json.loads(data)
    with open('../data/news.json', 'w') as file:
        json.dump(dictionary, file, indent=4)


def main():
    # path = '../data/weather.json'
    # read_json(path)
    # write_json(path)
    data = process_textfile()
    textfile_to_json(data)


if __name__ == "__main__":
    main()
