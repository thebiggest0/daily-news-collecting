"""
ADD A DOCSTRING
"""
import json


def write_json(json_file_path, data):
    # Write to JSON file
    with open(json_file_path, 'w') as file:
        json.dump(data, file, indent=4)


def read_json(json_file_path):
    # Read the JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    return data


def main():
    path = '../data/weather.json'
    read_json(path)
    write_json(path)


if __name__ == "__main__":
    main()
